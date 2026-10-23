#!/usr/bin/env python3
"""views.py — the views of cyberia/dev: queries over the pages, rendered as pages.

walks ~/cyber (canonical checkouts only), reads task pages, product maps,
audit receipts, the decisions log and the open pull requests, and writes
cyberia/views/*.md. generated, never edited by hand; a launchd job runs it
hourly and the graph serve re-renders. stdlib only.
"""
import datetime as dt, json, os, re, subprocess, sys

HOME = os.path.expanduser("~/cyber")
OUT = os.path.join(HOME, "cyberia", "views")
LADDER = [("1","nox","machine"),("2","trident","weapon"),("3","joy","warrior"),("4","cybergraph","brain"),("5","neural","language"),
          ("6","cy","agent"),("7","soft3","network"),("8","cyb","robot"),("9","cyber","superintelligence"),("10","cyberia","state")]
NOW = dt.datetime.now(dt.timezone.utc)
TODAY = NOW.date()

def sh(args, cwd=None):
    try: return subprocess.run(args, capture_output=True, text=True, cwd=cwd, timeout=120).stdout.strip()
    except Exception: return ""

def repos():
    for name in sorted(os.listdir(HOME)):
        p = os.path.join(HOME, name)
        if name.startswith(".") or not os.path.isdir(os.path.join(p, ".git")) and not os.path.isfile(os.path.join(p, ".git")): continue
        yield name, p

def frontmatter(path):
    try: text = open(path, encoding="utf-8").read()
    except Exception: return {}, ""
    if not text.startswith("---"): return {}, text
    end = text.find("\n---", 3)
    if end < 0: return {}, text
    fm = {}
    for line in text[3:end].split("\n"):
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if m: fm[m.group(1)] = m.group(2).strip()
    return fm, text[end+4:]

def days_since(datestr):
    try: return (TODAY - dt.date.fromisoformat(datestr[:10])).days
    except Exception: return None

# ---- products ---------------------------------------------------------------
def products():
    rows, alerts, nomap = [], [], []
    for rung, repo, role in LADDER:
        p = os.path.join(HOME, repo)
        maps = []
        if os.path.isdir(os.path.join(p, "audit")):
            for d in sorted(os.listdir(os.path.join(p, "audit"))):
                if os.path.isfile(os.path.join(p, "audit", d, "map.md")): maps.append(d)
        dots = "—"
        counter = os.path.join(p, "scripts", "requirements.py")
        if maps and os.path.isfile(counter):
            parts = []
            for m in maps:
                spec = os.path.join("specs", m + ".md")
                r = sh([sys.executable, counter, "--spec", spec, "--map", f"audit/{m}/map.md", "--dots"], cwd=p)
                parts.append(f"{m}: {r}" if r else f"{m}: counter failed")
            dots = "; ".join(parts)
        elif maps: dots = "map without a counter: " + ", ".join(maps)
        receipt = sh(["git", "log", "-1", "--format=%cs", "--", "audit"], cwd=p) if os.path.isdir(os.path.join(p, "audit")) else ""
        age = days_since(receipt) if receipt else None
        if age is None: alerts.append(f"{repo}: no receipt in `audit/`")
        elif age > 14: alerts.append(f"{repo}: last receipt {age} days ago")
        if not maps: nomap.append(repo)
        rows.append(f"| {rung} | [[{repo}]] · {role} | {dots} | {receipt or '—'}{'' if age is None else f' ({age} d)'} |")
    if nomap: alerts.append(f"{len(nomap)} of 10 products have no requirement map: " + ", ".join(nomap))
    body = "| rung | product | dots (open·stale 🔴 · simulated 🟡 · measured·proven 🟢) | last receipt |\n|---|---|---|---|\n" + "\n".join(rows)
    return body, alerts

# ---- flow -------------------------------------------------------------------
def tasks():
    out = []
    for name, p in repos():
        tdir = os.path.join(p, "tasks")
        if not os.path.isdir(tdir): continue
        for f in sorted(os.listdir(tdir)):
            if not f.endswith(".md") or f == "README.md": continue
            fm, _ = frontmatter(os.path.join(tdir, f))
            if "status" not in fm: continue
            out.append(dict(repo=name, page=f[:-3], kind=fm.get("kind","—"), status=fm.get("status","—"), owner=fm.get("owner","—"), serves=fm.get("serves","—")))
    return out

def prs():
    raw = sh(["gh", "search", "prs", "--owner", "cyberia-to", "--state", "open", "--limit", "500", "--json", "repository,number,title,createdAt,isDraft"])
    try: items = json.loads(raw) if raw else []
    except Exception: items = []
    for it in items:
        it["repo"] = it["repository"]["name"]; it["age"] = days_since(it["createdAt"]) or 0
    return items

def flow(task_rows, pr_rows):
    by_status = {}
    for t in task_rows: by_status[t["status"]] = by_status.get(t["status"], 0) + 1
    lines = ["## tasks", "", "| repo | page | kind | status | owner | serves |", "|---|---|---|---|---|---|"]
    for t in task_rows:
        if t["status"] in ("done", "closed", "abandoned"): continue
        lines.append(f"| {t['repo']} | [[{t['repo']}/tasks/{t['page']}|{t['page']}]] | {t['kind']} | {t['status']} | {t['owner']} | {t['serves']} |")
    lines.append("")
    lines.append("counts: " + ", ".join(f"{k} {v}" for k, v in sorted(by_status.items())) + f" — {len(task_rows)} task pages in {len({t['repo'] for t in task_rows})} repositories")
    per = {}
    for p in pr_rows: per.setdefault(p["repo"], []).append(p)
    lines += ["", "## pull requests, open", "", "| repo | open | oldest (days) | drafts |", "|---|---|---|---|"]
    for repo, ps in sorted(per.items(), key=lambda kv: -len(kv[1])):
        lines.append(f"| {repo} | {len(ps)} | {max(p['age'] for p in ps)} | {sum(1 for p in ps if p.get('isDraft'))} |")
    old = sorted(pr_rows, key=lambda p: -p["age"])[:8]
    lines += ["", f"total {len(pr_rows)} across {len(per)} repositories; older than 14 days: {sum(1 for p in pr_rows if p['age'] > 14)}", "", "oldest:", ""]
    for p in old: lines.append(f"- {p['repo']} [#{p['number']}](https://github.com/cyberia-to/{p['repo']}/pull/{p['number']}) · {p['age']} d · {p['title'][:90]}")
    return "\n".join(lines)

# ---- father -----------------------------------------------------------------
def father(task_rows):
    queue = [t for t in task_rows if t["kind"] == "review" and t["owner"] == "master" and t["status"] == "open"]
    lines = ["## verdicts waiting", "", f"{len(queue)} open decisions (the rule: fewer than five)", ""]
    for t in queue: lines.append(f"- [[{t['repo']}/tasks/{t['page']}|{t['page']}]] · serves {t['serves']}")
    lines += ["", "## the train", "", "| product | last candidate | age |", "|---|---|---|"]
    train_alerts = []
    for repo in ("cyb", "cyber", "soft3"):
        a = os.path.join(HOME, repo, "audit")
        cands = sorted(d for d in os.listdir(a)) if os.path.isdir(a) else []
        cands = [d for d in cands if d.startswith("release-")]
        if cands:
            last = cands[-1]; m = re.search(r"(\d{4})(\d{2})(\d{2})|(\d{4}-\d{2}-\d{2})", last)
            date = (f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m and m.group(1) else (m.group(4) if m else ""))
            age = days_since(date) if date else None
            lines.append(f"| {repo} | {last} | {'' if age is None else str(age)+' d'} |")
            if age is not None and age > 10: train_alerts.append(f"{repo}: last candidate {age} days ago")
        else:
            lines.append(f"| {repo} | — | — |"); train_alerts.append(f"{repo}: no candidate receipts in `audit/`")
    return "\n".join(lines), queue, train_alerts

# ---- experiments ------------------------------------------------------------
def experiments():
    path = os.path.join(HOME, "cyberia", "projects", "fathership.md")
    try: text = open(path, encoding="utf-8").read()
    except Exception: return "no decisions log"
    rows = []
    for line in text.split("\n"):
        if not line.startswith("- 20") or "expected effect" not in line: continue
        date = line[2:12]
        decision = line[15:line.find(". expected effect")].strip() if ". expected effect" in line else line[15:120]
        m = re.search(r"expected effect:\s*(.*?)\s*·\s*check:\s*(.*?)\s*·\s*outcome:\s*(.*)$", line)
        exp, chk, out = (m.group(1), m.group(2), m.group(3)) if m else ("", "", "")
        rows.append(f"| {date} | {decision[:110]} | {exp[:110]} | {chk[:80]} | {out or '—'} |")
    if not rows: return "no decision carries an expected effect yet"
    return "| date | decision | expected effect | check | outcome |\n|---|---|---|---|---|\n" + "\n".join(rows)

# ---- write ------------------------------------------------------------------
def page(name, title, body, aliases):
    fm = f"---\ntitle: {title}\ntags: cyber, cyberia, views, generated\nalias: {aliases}\ncrystal-type: measure\ncrystal-domain: cyberia\n---\n\n"
    note = f"generated by `cyberia/scripts/views.py` at {NOW.strftime('%Y-%m-%d %H:%M')} UTC; a query over the pages, never edited by hand. the questions are in [[dev]] § the views.\n\n"
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(fm + f"# {title}\n\n" + note + body + "\n")

def main():
    os.makedirs(OUT, exist_ok=True)
    prod_body, prod_alerts = products()
    task_rows, pr_rows = tasks(), prs()
    flow_body = flow(task_rows, pr_rows)
    father_body, queue, train_alerts = father(task_rows)
    exp_body = experiments()
    alerts = []
    if len(queue) >= 5: alerts.append(f"the father's queue holds {len(queue)} decisions (rule: fewer than five)")
    old = sum(1 for p in pr_rows if p["age"] > 14)
    if old: alerts.append(f"{old} pull requests older than 14 days")
    alerts += train_alerts + prod_alerts
    page("products.md", "views · products", prod_body, "views products, product dots, the ladder's dots")
    page("flow.md", "views · flow", flow_body, "views flow, open tasks, open pull requests")
    page("father.md", "views · father", father_body, "views father, verdicts waiting, the father's queue")
    page("experiments.md", "views · experiments", exp_body, "views experiments, experiment register, hypotheses of fathership")
    bridge = ["## alerts", ""] + ([f"- {a}" for a in alerts] or ["- none"]) + ["",
        "## the five numbers", "",
        "| what | now | page |", "|---|---|---|",
        f"| decisions waiting for the father | {len(queue)} | [[cyberia/views/father\\|father]] |",
        f"| open pull requests | {len(pr_rows)} ({old} older than 14 d) | [[cyberia/views/flow\\|flow]] |",
        f"| open task pages | {sum(1 for t in task_rows if t['status'] not in ('done','closed','abandoned'))} | [[cyberia/views/flow\\|flow]] |",
        f"| products with a requirement map | {sum(1 for r,_,_ in LADDER if any(os.path.isfile(os.path.join(HOME,r,'audit',d,'map.md')) for d in (os.listdir(os.path.join(HOME,r,'audit')) if os.path.isdir(os.path.join(HOME,r,'audit')) else [])))} of 10 | [[cyberia/views/products\\|products]] |",
        f"| experiments with an outcome | {exp_body.count('| worked') + exp_body.count('| did not')} of {max(exp_body.count(chr(10))-1,0)} | [[cyberia/views/experiments\\|experiments]] |",
        "", "## products", "", prod_body]
    page("README.md", "views", "\n".join(bridge), "views, the bridge, dashboard, the views of cyberia")
    print("views written:", OUT, "| alerts:", len(alerts), "| tasks:", len(task_rows), "| prs:", len(pr_rows))

if __name__ == "__main__":
    main()
