"""Apply explicitly queued SignalDesk approvals to an existing SS IPTV M3U."""
import argparse
import datetime
import json
import re
from pathlib import Path

ENTRY = re.compile(r'^#EXTINF:((?:"[^"]*"|[^",])*)[,](.+)$')
GROUP = re.compile(r'(?<![\w-])group-title="([^"]*)"')
DESC = re.compile(r'(?<![\w-])description="([^"]*)"')
TOKEN = re.compile(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}')
MARK = re.compile(r'^# Playback: user confirmed working on \d{4}-\d{2}-\d{2}\. SignalDesk approval ([a-f0-9-]+)\.$')
BAD_GROUP = re.compile(r'[\x00-\x1f"<>]')

def entries(lines):
    pending = None
    for i, line in enumerate(lines):
        if line.startswith('#EXTINF:'):
            match = ENTRY.fullmatch(line)
            if pending is not None or not match:
                raise ValueError('Incomplete EXTINF')
            pending = i, match
        elif line.startswith(('http://', 'https://')) and pending is not None:
            index, match = pending
            yield index, match, line
            pending = None
    if pending:
        raise ValueError('Missing stream URL')

def apply_approvals(text, queue):
    if not text.lstrip('\ufeff').startswith('#EXTM3U'):
        raise ValueError('Missing M3U header')
    newline = '\r\n' if '\r\n' in text else '\n'
    trailing = text.endswith('\n')
    lines = text.splitlines()
    original = [(m.group(2), u) for _, m, u in entries(lines)]
    report = {'applied': [], 'already_present': [], 'conflicts': []}
    for row in queue:
        token, target = row['token'], row['target_group']
        if not TOKEN.fullmatch(token) or not target.strip() or len(target)>180 or BAD_GROUP.search(target):
            raise ValueError('Invalid queued approval')
        date = datetime.date.fromisoformat(row['confirmed_at'][:10]).isoformat()
        matches = [(i,m) for i,m,u in entries(lines) if u == row['source_url'] and m.group(2).strip()==row['source_name']]
        if len(matches)!=1:
            report['conflicts'].append(token)
            continue
        i, match = matches[0]
        attrs, name = match.groups()
        group = GROUP.search(attrs)
        if not group or group.group(1) not in {row['source_group'],target}:
            report['conflicts'].append(token)
            continue
        marker = '# Playback: user confirmed working on '+date+'. SignalDesk approval '+token+'.'
        start=i
        while start and lines[start-1].startswith('# ') and not lines[start-1].startswith('#EXT'):
            start-=1
        if marker in lines[start:i] and group.group(1)==target:
            report['already_present'].append(token)
            continue
        attrs=GROUP.sub(lambda _: 'group-title="'+target+'"',attrs,count=1)
        stamp='בדיקת שידור אושרה '+date
        desc=DESC.search(attrs)
        if desc:
            old=re.sub(r'(?: · )?בדיקת שידור אושרה \d{4}-\d{2}-\d{2}$','',desc.group(1))
            attrs=DESC.sub(lambda _: 'description="'+(old+' · ' if old else '')+stamp+'"',attrs,count=1)
        else:
            attrs+=' description="'+stamp+'"'
        lines[i]='#EXTINF:'+attrs+','+name
        lines[start:i]=[l for l in lines[start:i] if not MARK.fullmatch(l)]+[marker]
        report['applied'].append(token)
    parsed=list(entries(lines))
    if [(m.group(2),u) for _,m,u in parsed]!=original:
        raise ValueError('Channels or stream URLs changed')
    if report['applied']:
        groups={g.group(1) for _,m,_ in parsed if (g:=GROUP.search(m.group(1)))}
        for i,line in enumerate(lines):
            if re.match(r'^# \d+ channel entries, \d+ groups\.',line):
                lines[i]=re.sub(r'^# \d+ channel entries, \d+ groups\.',f'# {len(parsed)} channel entries, {len(groups)} groups.',line)
                break
    return newline.join(lines)+(newline if trailing else ''),report

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    for arg in ('playlist','queue','output'):
        parser.add_argument(arg,type=Path)
    args=parser.parse_args()
    output,report=apply_approvals(args.playlist.read_bytes().decode('utf-8'),json.loads(args.queue.read_text()))
    args.output.write_bytes(output.encode('utf-8'))
    print(json.dumps(report))
