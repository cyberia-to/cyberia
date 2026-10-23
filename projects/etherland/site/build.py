#!/usr/bin/env python3
"""cyb.land — build the visitor site of etherland (cyberia/projects/etherland, markdown) into a build dir.

stdlib only. a small markdown subset is enough for the catalogue: headings, paragraphs,
lists, tables, links, wiki links, bold, italic, code. every page keeps its path:
visit.md → /visit/, visit/daypass.md → /visit/daypass/, "launch event.md" → /launch-event/.

    python3 site/build.py [--src ../etherland] [--out ~/.cache/cyber/etherland/build]
    rsync -az --delete ~/.cache/cyber/etherland/build/ cyberproxy:/var/www/html/cyb.land/
"""
import argparse, html, os, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXTERNAL = {  # wiki links to pages that live elsewhere
    "cyber valley": "https://cybervalley.io", "cv": "https://cybervalley.io", "cve": "https://cybervalley.io",
    "map": "https://cyberia.my/map", "cyber": "https://cyber.page", "cyberia": "https://cyberia.to",
    "$cyb": "https://cyb.money", "cyb.land": "/", "cv.land": "/",
}
SKIP = {"README.md", "cyb.land.md", "marketing.md"}  # README = index of the folder; welcome = the landing; marketing = internal
NAV = [("visit", "/visit/"), ("stay", "/stay/"), ("activities", "/activities/"), ("attractions", "/attractions/"),
       ("events", "/events/"), ("community", "/community/"), ("cart", "/cart/")]

def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "page"

def read_page(path, src):
    text = path.read_text(encoding="utf-8")
    meta = {}
    body = text
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if m:
        body = text[m.end():]
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
    rel = path.relative_to(src)
    parts = [slug(p) for p in rel.with_suffix("").parts]
    url = "/" + "/".join(parts) + "/"
    title = None
    mt = re.search(r"^# (.+)$", body, re.M)
    if mt:
        title = mt.group(1).strip()
        body = body[:mt.start()] + body[mt.end():]
    else:
        title = rel.stem
    names = {rel.stem.lower(), title.lower(), slug(rel.stem)}
    for a in meta.get("alias", "").split(","):
        if a.strip():
            names.add(a.strip().lower())
    return {"path": path, "rel": rel, "url": url, "title": title, "icon": meta.get("icon", ""), "names": names, "body": body, "parts": parts}

def build_index(pages):
    idx = {}
    for p in pages:
        for n in p["names"]:
            idx.setdefault(n, p["url"])
        # "visit/visas" style references
        idx.setdefault("/".join(p["rel"].with_suffix("").parts).lower(), p["url"])
    return idx

def resolve(name, idx):
    key = name.strip().lower()
    if key in idx:
        return idx[key]
    if key in EXTERNAL:
        return EXTERNAL[key]
    k2 = key.rstrip("s")
    if k2 in idx:
        return idx[k2]
    return None

def inline(s, idx):
    out = html.escape(s, quote=False)
    def wiki(m):
        target, _, label = m.group(1).partition("|")
        label = label or target
        href = resolve(target, idx)
        if href:
            ext = href.startswith("http")
            return f'<a href="{href}"{" target=_blank rel=noopener" if ext else ""}>{html.escape(label)}</a>'
        return f'<span class="dead">{html.escape(label)}</span>'
    out = re.sub(r"\[\[([^\]]+)\]\]", wiki, out)
    def link(m):
        label, href = m.group(1), m.group(2)
        href = href.replace("/cyberia/projects/etherland/", "/")
        if href.startswith("/") and not href.endswith("/") and "." not in href.rsplit("/", 1)[-1]:
            href += "/"
        cls = ' class="add"' if label.strip().startswith("+") else ""
        ext = href.startswith("http")
        return f'<a href="{href}"{cls}{" target=_blank rel=noopener" if ext else ""}>{label}</a>'
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, out)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", out)
    out = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<i>\1</i>", out)
    out = re.sub(r"\[illustration: ([^\]]+)\]", r'<span class="illus">illustration · \1</span>', out)
    return out

def render_body(body, idx):
    lines = body.splitlines()
    out, i = [], 0
    def flush_para(buf):
        if buf:
            out.append("<p>" + inline(" ".join(buf), idx) + "</p>")
    buf = []
    while i < len(lines):
        ln = lines[i]
        st = ln.strip()
        if not st or st.startswith("{{query") or st.startswith("<iframe"):
            flush_para(buf); buf = []; i += 1; continue
        hm = re.match(r"^(#{2,4}) (.+)$", st)
        if hm:
            flush_para(buf); buf = []
            lvl = len(hm.group(1)); t = hm.group(2)
            out.append(f'<h{lvl} id="{slug(t)}">{inline(t, idx)}</h{lvl}>'); i += 1; continue
        if st.startswith("|"):
            flush_para(buf); buf = []
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            rows = [r for r in rows if not all(re.fullmatch(r":?-+:?", c or "-") for c in r)]
            if rows:
                head, body_rows = rows[0], rows[1:]
                has_head = any(h for h in head) and not any(c.startswith("$") for c in head)
                t = ['<table>']
                if has_head:
                    t.append("<thead><tr>" + "".join(f"<th>{inline(c, idx)}</th>" for c in head) + "</tr></thead>")
                    rest = body_rows
                else:
                    rest = rows
                t.append("<tbody>" + "".join("<tr>" + "".join(f"<td>{inline(c, idx)}</td>" for c in r) + "</tr>" for r in rest) + "</tbody></table>")
                out.append("".join(t))
            continue
        lm = re.match(r"^(\s*)[-*] (.+)$", ln)
        if lm:
            flush_para(buf); buf = []
            items = []
            while i < len(lines):
                m2 = re.match(r"^(\s*)[-*] (.+)$", lines[i])
                if not m2: break
                items.append((len(m2.group(1)), m2.group(2))); i += 1
            out.append("<ul>")
            depth = 0
            for d, txt in items:
                lvl = 1 if d >= 2 else 0
                while depth < lvl: out.append("<ul>"); depth += 1
                while depth > lvl: out.append("</ul>"); depth -= 1
                out.append(f"<li>{inline(txt, idx)}</li>")
            while depth > 0: out.append("</ul>"); depth -= 1
            out.append("</ul>")
            continue
        if st.startswith("[illustration:") or st.startswith("<"):
            flush_para(buf); buf = []
            out.append(f"<p>{inline(st, idx)}</p>" if st.startswith("[") else st); i += 1; continue
        buf.append(st); i += 1
    flush_para(buf)
    return "\n".join(out)

def children_of(page, pages):
    base = page["rel"].with_suffix("")
    kids = [p for p in pages if p["rel"].parent == base]
    return sorted(kids, key=lambda p: p["title"].lower())

def page_html(page, pages, idx, tpl):
    crumbs = []
    for k in range(1, len(page["parts"])):
        url = "/" + "/".join(page["parts"][:k]) + "/"
        parent = next((p for p in pages if p["url"] == url), None)
        crumbs.append(f'<a href="{url}">{html.escape(parent["title"] if parent else page["parts"][k-1])}</a>')
    kids = children_of(page, pages)
    kids_html = ""
    if kids:
        kids_html = '<nav class="kids"><h2>inside</h2><ul>' + "".join(
            f'<li><a href="{k["url"]}">{html.escape(k["icon"] + " " if k["icon"] else "")}{html.escape(k["title"])}</a></li>' for k in kids) + "</ul></nav>"
    body = render_body(page["body"], idx)
    nav = "".join(f'<a href="{u}"{" class=on" if page["url"].startswith(u) else ""}>{n}</a>' for n, u in NAV)
    return (tpl.replace("{{title}}", html.escape(page["title"]))
               .replace("{{icon}}", html.escape(page["icon"]))
               .replace("{{crumbs}}", (" / " + " / ".join(crumbs)) if crumbs else "")
               .replace("{{nav}}", nav)
               .replace("{{body}}", body)
               .replace("{{kids}}", kids_html)
               .replace("{{url}}", page["url"]))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=str(ROOT.parent))  # the project folder: this file lives in its site/
    ap.add_argument("--out", default=os.path.expanduser("~/.cache/cyber/etherland/build"))  # never inside ~/cyber
    a = ap.parse_args()
    src, out = Path(a.src), Path(a.out)
    if not src.is_dir():
        sys.exit(f"source not found: {src}")
    pages = [read_page(p, src) for p in sorted(src.rglob("*.md")) if p.name not in SKIP]
    idx = build_index(pages)
    tpl = (ROOT / "page.html").read_text()
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(ROOT, out, ignore=shutil.ignore_patterns("page.html", "build.py", "__pycache__"))
    dead = set()
    for p in pages:
        d = out / p["url"].strip("/")
        d.mkdir(parents=True, exist_ok=True)
        h = page_html(p, pages, idx, tpl)
        for m in re.finditer(r'class="dead">([^<]+)<', h):
            dead.add(m.group(1))
        (d / "index.html").write_text(h, encoding="utf-8")
    (out / "sitemap.txt").write_text("\n".join("https://cyb.land" + p["url"] for p in pages) + "\n")
    print(f"{len(pages)} pages → {out}")
    if dead:
        print(f"unresolved wiki links ({len(dead)}): " + ", ".join(sorted(dead)[:40]))

if __name__ == "__main__":
    main()
