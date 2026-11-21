#!/usr/bin/env python3
"""Refresh a small, real XMLTV guide for the three Israeli channels missing SS IPTV EPG.

Never invent programme titles/times. Only use programme elements in public upstream feeds.
Missing channels are excluded. Retain last good output if both sources fail or no live
programmes are available.
"""
from __future__ import annotations

import datetime as dt
import gzip
import json
import pathlib
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "epg" / "idan-plus.xml"
STATUS = ROOT / "epg" / "status.json"
FEEDS = (
    "https://iptv-epg.org/files/epg-il.xml",
    "https://epgshare01.online/epgshare01/epg_ripper_IL1.xml.gz",
)
TARGETS = {
    "Now14.il@SD": {
        "display": "ערוץ 14",
        "aliases": (
            "Now14.il@SD", "Now14.il", "Channel14.il", "Channel14.il@SD",
            "ערוץ14.il", "ערוץ.14.HD.il", "ערוץ14", "עכשיו14",
            "ערוץ14שידורחי.il",
        ),
    },
    "EconomyChannel.il@SD": {
        "display": "ערוץ הכלכלה",
        "aliases": (
            "EconomyChannel.il@SD", "EconomyChannel.il", "הכלכלה", "הכלכלה.il",
            "כלכלה10", "ערוץהכלכלה", "ערוץהכלכלה.il", "ערוץ.הכלכלה.il",
        ),
    },
    "Channel16.il@SD": {
        "display": "ערוץ 16",
        "aliases": (
            "Channel16.il@SD", "Channel16.il", "ערוץ16", "ערוץ16.il",
            "ערוץ16ישראל", "ערוץ16ישראל.il",
        ),
    },
}

def norm(s: str | None) -> str:
    return re.sub(r"[^a-z0-9א-ת]+", "", (s or "").lower())

def download(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Israel-Live-TV-EPG/1.0"})
    with urllib.request.urlopen(req, timeout=90) as response:
        data = response.read(36_000_000)
    if len(data) >= 36_000_000:
        raise ValueError("EPG source too large")
    if data.startswith(b"\x1f\x8b"):
        data = gzip.decompress(data)
    if len(data) > 110_000_000:
        raise ValueError("Unpacked guide too large")
    return data

def start_time(s: str | None) -> dt.datetime | None:
    if not s:
        return None
    try:
        return dt.datetime.strptime(s.strip()[:20], "%Y%m%d%H%M%S %z").astimezone(dt.timezone.utc)
    except (ValueError, IndexError):
        return None

def collect(root: ET.Element, now: dt.datetime):
    channels = {}
    aliases = {
        wanted: {norm(x) for x in cfg["aliases"]} | {norm(cfg["display"])}
        for wanted, cfg in TARGETS.items()
    }
    for ch in root.findall("./channel"):
        keys = {norm(ch.get("id"))}
        keys.update(norm(el.text) for el in ch.findall("./display-name"))
        for wanted, acceptable in aliases.items():
            if keys & acceptable:
                channels.setdefault(ch.get("id"), set()).add(wanted)

    lo, hi = now - dt.timedelta(hours=2), now + dt.timedelta(hours=54)
    found = {k: [] for k in TARGETS}
    for programme in root.findall("./programme"):
        source_id = programme.get("channel")
        wanted_ids = channels.get(source_id, ())
        if not wanted_ids:
            continue
        st = start_time(programme.get("start"))
        end = start_time(programme.get("stop"))
        title = (programme.findtext("title") or "").strip()
        if not title or not st or not end or st >= hi or end <= lo or end <= st:
            continue
        for wanted in wanted_ids:
            found[wanted].append((st, end, programme))
    return found

def main() -> int:
    now = dt.datetime.now(dt.timezone.utc)
    gathered = {k: [] for k in TARGETS}
    failures = []
    for url in FEEDS:
        try:
            root = ET.fromstring(download(url))
            data = collect(root, now)
            for wanted, programmes in data.items():
                if not gathered[wanted] and programmes:
                    gathered[wanted] = programmes
        except Exception as exc:
            failures.append({"source": url, "error": str(exc)[:240]})

    counts = {k: len(v) for k, v in gathered.items()}
    if not any(counts.values()):
        print(json.dumps({"error": "No live programme listings found; keeping old guide", "counts": counts, "failures": failures}, ensure_ascii=False))
        return 1

    tv = ET.Element("tv", {"generator-info-name": "Israel Live TV - filtered public XMLTV"})
    for wanted, programmes in gathered.items():
        if not programmes:
            continue
        ch = ET.SubElement(tv, "channel", {"id": wanted})
        ET.SubElement(ch, "display-name", {"lang": "he"}).text = TARGETS[wanted]["display"]

    for wanted, programmes in gathered.items():
        seen = set()
        for st, end, upstream in sorted(programmes, key=lambda p: p[0]):
            title = (upstream.findtext("title") or "").strip()
            key = (st, end, title)
            if key in seen:
                continue
            seen.add(key)
            attrs = {
                "start": st.strftime("%Y%m%d%H%M%S +0000"),
                "stop": end.strftime("%Y%m%d%H%M%S +0000"),
                "channel": wanted,
            }
            p = ET.SubElement(tv, "programme", attrs)
            ET.SubElement(p, "title", {"lang": "he"}).text = title
            description = (upstream.findtext("desc") or "").strip()
            if description:
                ET.SubElement(p, "desc").text = description[:400]

    data = ET.tostring(tv, encoding="utf-8", xml_declaration=True)
    if len(data) > 2_000_000:
        raise ValueError("Filtered EPG exceeds 2 MB")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(data)
    STATUS.write_text(json.dumps({
        "generated_utc": now.isoformat(),
        "programme_counts": counts,
        "source_errors": failures,
        "source_urls": list(FEEDS),
        "no_data": [k for k in TARGETS if not gathered[k]],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"size_bytes": len(data), "counts": counts, "failures": failures}, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
