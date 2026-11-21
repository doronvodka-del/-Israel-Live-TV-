/**
 * SS IPTV-compatible XMLTV endpoint for a Vercel Node.js deployment.
 *
 * This is NOT a general-purpose CORS proxy. It fetches only the small,
 * filtered guide in this repository and sends SS IPTV's CORS/Range headers.
 *
 * Deployment is required. GitHub alone does not make this endpoint live.
 * After deployment and HTTP-header verification, point x-tvg-url at
 * the deployed /api/epg URL.
 */
const EPG_SOURCE = "https://raw.githubusercontent.com/doronvodka-del/-Israel-Live-TV-/main/epg/idan-plus.xml";
const MAX_BYTES = 4_000_000;
module.exports = async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS, HEAD");
  res.setHeader("Access-Control-Allow-Headers", "Range");
  res.setHeader("Access-Control-Expose-Headers",
    "Accept-Ranges, Content-Encoding, Content-Length, Content-Range");
  res.setHeader("Content-Type", "application/xml; charset=utf-8");
  res.setHeader("Content-Encoding", "identity");
  res.setHeader("Accept-Ranges", "bytes");
  res.setHeader("Cache-Control", "public, max-age=300, s-maxage=900");

  if (req.method === "OPTIONS") return res.status(204).end();
  if (!["GET", "HEAD", "POST"].includes(req.method)) return res.status(405).end();

  try {
    const upstream = await fetch(EPG_SOURCE, {
      signal: AbortSignal.timeout(12000),
      headers: { "User-Agent": "Israel-Live-TV-Guide/1.0" }
    });
    if (!upstream.ok) return res.status(502).end();

    const bytes = Buffer.from(await upstream.arrayBuffer());
    if (bytes.length === 0 || bytes.length > MAX_BYTES
        || !bytes.toString("utf8", 0, 100).includes("<?xml"))
      return res.status(502).end();

    const range = req.headers.range;
    const match = /^bytes=(\d*)-(\d*)$/.exec(range || "");
    let start = 0, end = bytes.length - 1;
    if (range) {
      if (!match) {
        res.setHeader("Content-Range", "bytes */" + bytes.length);
        return res.status(416).end();
      }
      if (match[1]) {
        start = Number(match[1]);
        end = match[2] ? Number(match[2]) : end;
      } else {
        const suffix = Number(match[2]);
        start = Math.max(0, bytes.length - suffix);
      }
      if (!Number.isSafeInteger(start) || !Number.isSafeInteger(end)
          || start < 0 || start > end || start >= bytes.length) {
        res.setHeader("Content-Range", "bytes */" + bytes.length);
        return res.status(416).end();
      }
      end = Math.min(end, bytes.length - 1);
      res.setHeader("Content-Range", "bytes " + start + "-" + end + "/" + bytes.length);
      res.status(206);
    } else res.status(200);

    const body = bytes.subarray(start, end + 1);
    res.setHeader("Content-Length", String(body.length));
    return req.method === "HEAD" ? res.end() : res.end(body);
  } catch (_) {
    return res.status(502).end();
  }
};
