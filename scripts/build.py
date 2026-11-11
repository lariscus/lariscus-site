#!/usr/bin/env python3
"""Generates the static pages (index, drey, dricket, 404). Run from anywhere: python3 scripts/build.py"""
import json, pathlib, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://lariscus.de"
GH = "https://github.com/HenrikPuls"
DREY_VER, DK_VER = "0.8.2", "0.6.2"

def esc(s): return html.escape(s, quote=True)

def ld(*objs):
    return "".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>\n' for o in objs)

def page(*, path, title, desc, og, body_class="", body, schema=(), robots="index,follow", nav=""):
    url = BASE + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}, max-image-preview:large">
<meta name="author" content="Lariscus">
<meta name="theme-color" content="#18191b">
<link rel="canonical" href="{url}">
<link rel="icon" href="/assets/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Lariscus">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{BASE}/assets/{og}">
<link rel="preload" as="style" href="/assets/site.css?v=3">
<link rel="stylesheet" href="/assets/site.css?v=3">
{ld(*schema)}</head>
<body class="{body_class}">
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap">
<a class="brand" href="/"><img src="/assets/icon-192.png" width="32" height="32" alt="">Lariscus</a>
<nav class="main" aria-label="Main">
<a href="/drey/"{' aria-current="page"' if nav=='drey' else ''}>Drey</a>
<a href="/dricket/"{' aria-current="page"' if nav=='dricket' else ''}>dricket</a>
<a href="{GH}">GitHub</a>
</nav></div></header>
<main id="main">
{body}
</main>
<footer class="site"><div class="wrap">
<div class="cols">
<div><h2>Lariscus</h2><p>Local-first software for work that people and AI agents share. Open source, plain files, no lock-in.</p></div>
<div><h2>Products</h2><ul><li><a href="/drey/">Drey – note vault</a></li><li><a href="/dricket/">dricket – Git tickets</a></li></ul></div>
<div><h2>Source</h2><ul><li><a href="{GH}/Drey">Drey on GitHub</a></li><li><a href="{GH}/dricket">dricket on GitHub</a></li><li><a href="{GH}/Drey/releases">Drey releases</a></li><li><a href="{GH}/dricket/releases">dricket releases</a></li></ul></div>
</div>
<p class="legal">Private, non-commercial open-source projects. Both are licensed GPL-3.0-or-later. This site sets no cookies, loads no third-party fonts or scripts, and does no tracking.</p>
</div></footer>
</body>
</html>
"""

def pic(name, alt, w, h, *, eager=False, sizes="(min-width: 900px) 60vw, 100vw"):
    return (f'<img src="/assets/{name}-1000.webp" srcset="/assets/{name}-1000.webp 1000w, /assets/{name}-1800.webp 1800w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt)}" '
            f'{"fetchpriority=\"high\"" if eager else "loading=\"lazy\" decoding=\"async\""}>')

TERM = """<pre class="term" aria-label="Example dricket session"><span class="p">$</span> dk add --prefix app -m "Login error" -l bug --unclaimed
app-1
<span class="p">$</span> dk next --claim --size M
<span class="ok">claimed app-1 (epoch 1, lease until …)</span>
<span class="p">$</span> dk sync &amp;&amp; $EDITOR tickets/app/0000/app-1/ticket.md
<span class="p">$</span> dk commit app-1
committed app-1 (rev 2, commit …)
<span class="p">$</span> dk release --stage review -m "Fix on dk/app-1" app-1
<span class="ok">released app-1 -&gt; review</span></pre>"""
TERM_SMALL = """<pre class="term" aria-hidden="true"><span class="p">$</span> dk next --claim --size M
<span class="ok">claimed app-1 (epoch 1)</span>
<span class="p">$</span> dk commit app-1
committed app-1 (rev 2)
<span class="p">$</span> dk release --stage review app-1
<span class="ok">released app-1 -&gt; review</span></pre>"""

# ---------------------------------------------------------------- home
home_body = f"""
<div class="wrap hero"><div class="grid two">
<div>
<p class="eyebrow">Lariscus</p>
<h1>Software for work that people and AI agents share.</h1>
<p class="lead">Two open-source tools built on the same idea: your data stays in plain files you own, agents do the legwork, and you stay in charge of what actually changes.</p>
<div class="cta"><a class="btn primary" href="/drey/">Explore Drey</a><a class="btn" href="/dricket/">Explore dricket</a></div>
<p class="note">Free and open source · Drey for Windows and Linux, dricket for Linux, macOS and Windows · GPL-3.0-or-later</p>
</div>
<figure><div class="shot">{pic('drey-overview','Drey showing a note with tasks, the calendar, the file tree and the AI assistant',1800,1125,eager=True,sizes='(min-width: 900px) 50vw, 100vw')}</div></figure>
</div></div>

<section><div class="wrap">
<h2>Two products, one principle</h2>
<p class="lead">Notes and tickets are the context. Agents are the hands. You are the gate.</p>
<div class="product">
<article class="card">
<div class="thumb">{pic('drey-editor','Drey editor with live Markdown preview in two panes',1000,625,sizes='(min-width: 700px) 40vw, 100vw')}</div>
<div class="body"><h3>Drey</h3>
<p>A private, local-first Markdown note vault with live preview, daily notes, tasks, tags and search, plus an optional AI assistant that works on your notes through permissioned tools.</p>
<a class="btn primary" href="/drey/">Discover Drey</a></div>
</article>
<article class="card">
<div class="thumb term">{TERM_SMALL}</div>
<div class="body"><h3>dricket</h3>
<p>A ticketing system with no server. Every ticket is a Markdown file in Git, and claiming one is a fast-forward push, so exactly one person or agent wins.</p>
<a class="btn primary" href="/dricket/">Discover dricket</a></div>
</article>
</div></div></section>

<section><div class="wrap">
<h2>What we believe</h2>
<div class="cards">
<div class="card"><span class="tag">Local-first</span><h3>Your files, your machine</h3><p>Notes are Markdown, tickets are Markdown. Open them in any editor, sync them any way you like, and leave whenever you want.</p></div>
<div class="card"><span class="tag">Agent-ready</span><h3>Built for AI to work alongside you</h3><p>Drey runs a local model or the provider you choose and speaks MCP. dricket gives agents a small, strict command line with exit codes they can rely on.</p></div>
<div class="card"><span class="tag">You decide</span><h3>Permissions, not promises</h3><p>Writes ask first unless you say otherwise, deletions are always confirmed, and everything that leaves your machine is opt-in.</p></div>
<div class="card"><span class="tag">Open</span><h3>Source you can read</h3><p>Both projects are published under the GPL. No accounts, no cloud service you have to trust.</p></div>
</div></div></section>

<section><div class="wrap">
<h2>About the name</h2>
<p class="lead" style="max-width:70ch"><em>Lariscus</em> is the genus of Asian ground squirrels. A <em>drey</em> is a squirrel's nest: a tidy place where a small animal keeps everything it will need. That is the idea behind the tools.</p>
</div></section>
"""
home_schema = [
 {"@context":"https://schema.org","@type":"Organization","name":"Lariscus","url":BASE+"/","logo":BASE+"/assets/drey-icon-512.png","sameAs":[GH]},
 {"@context":"https://schema.org","@type":"WebSite","name":"Lariscus","url":BASE+"/","inLanguage":"en"},
]
home = page(path="/", title="Lariscus – Drey note vault and dricket Git tickets",
  desc="Lariscus builds open-source, local-first tools for people who work with AI agents: Drey, a private Markdown note vault, and dricket, serverless Git tickets.",
  og="og-lariscus.png", body_class="home", body=home_body, schema=home_schema)

# ---------------------------------------------------------------- drey
dl = f"{GH}/Drey/releases/latest"
drey_body = f"""
<div class="wrap hero"><div class="grid">
<div>
<p class="eyebrow">Drey · Note vault</p>
<h1>Your private note vault that runs your work.</h1>
<p class="lead">Drey is a local-first Markdown note app. Your notes are plain files in a folder you own, with a true in-place live preview, daily notes, tasks, tags, search, diagrams, and an optional AI assistant that reads your vault and acts on it through permissioned tools.</p>
<div class="cta"><a class="btn primary" href="{dl}">Download Drey {DREY_VER}</a><a class="btn" href="{GH}/Drey">View source</a></div>
<p class="note">Windows installer and portable · Linux AppImage and .deb · GPL-3.0-or-later</p>
</div>
<figure><div class="shot">{pic('drey-overview','Drey main window: calendar, file tree, a note with open tasks and the assistant panel',1800,1125,eager=True,sizes='(min-width: 1120px) 1080px, 100vw')}</div></figure>
</div></div>

<section><div class="wrap">
<h2>Everything stays a file</h2>
<p class="lead">A vault is an ordinary folder, even one on OneDrive or a sync share. There is no database and no proprietary format: Markdown with optional YAML frontmatter.</p>
<dl class="facts">
<div><dt>Format</dt><dd>Markdown + YAML</dd></div>
<div><dt>Storage</dt><dd>Plain folders</dd></div>
<div><dt>AI</dt><dd>Local first, optional</dd></div>
<div><dt>Platforms</dt><dd>Windows, Linux</dd></div>
</dl>
</div></section>

<section><div class="wrap"><div class="split">
<div>
<h2>Write in a live preview</h2>
<p>Headings, tables and images render in place; syntax markers appear only around your cursor. Switch to source mode whenever you want the raw text.</p>
<ul class="ticks">
<li>Highlights, math, callouts, footnotes and emoji</li>
<li>Slash menu and a formatting strip for quick inserts</li>
<li>Split panes, tabs and movable docks</li>
<li>Wikilinks with link-safe rename and move</li>
<li>PDF export, spellcheck and per-note version history</li>
</ul>
</div>
<figure><div class="shot">{pic('drey-editor','Two Drey panes side by side with a Markdown cheatsheet rendered in live preview',1800,1125)}</div></figure>
</div></div></section>

<section><div class="wrap"><div class="split flip">
<div>
<h2>Find it, plan it, check it off</h2>
<p>Topics are free inline <code>#tags</code>, never folders. One search field covers tags and free text across the open note, the vault or all your vaults. Tasks carry due dates and priorities inside the note itself and show up in one panel.</p>
<ul class="ticks">
<li>Daily notes and quick capture</li>
<li>Case, whole-word and regex search with vault-wide replace</li>
<li>Tag rename and merge with prefix colours</li>
<li>Templates and snippets</li>
</ul>
</div>
<figure><div class="shot">{pic('drey-search-tasks','Drey search results and a task list next to the note they come from',1800,1125)}</div></figure>
</div></div></section>

<section><div class="wrap"><div class="split">
<div>
<h2>An assistant that asks before it acts</h2>
<p>Point Drey at a local OpenAI-compatible model such as LM Studio, llama.cpp, vLLM or Ollama, and ask questions about your notes. The assistant pulls in the sections that match your question and cites where they came from.</p>
<ul class="ticks">
<li>Hosted providers are opt-in and off by default</li>
<li>Edit access to notes is off, ask-first or automatic, your choice</li>
<li>Web search and external MCP servers only run when you allow them</li>
<li>Drey can also act as an MCP server for your other tools</li>
</ul>
</div>
<figure><div class="shot">{pic('drey-assistant','Drey assistant answering a question about a note with a task card and search results',1800,1125)}</div></figure>
</div></div></section>

<section><div class="wrap"><div class="split flip">
<div>
<h2>You hold the permissions</h2>
<p>Every tool the assistant may call has its own switch. Groups that write ask first, and anything that leaves your computer can ask before it runs. A deletion is always confirmed.</p>
</div>
<figure><div class="shot">{pic('drey-tools','Drey settings page for assistant tools with per-group permissions',1800,1125)}</div></figure>
</div></div></section>

<section><div class="wrap"><div class="split">
<div>
<h2>Built for real vaults</h2>
<p>Git-backed vaults get a Source control panel with commit, push, merge, stash and file history. Diagrams are draw.io files that embed like images. Save conflicts open a merge view instead of overwriting.</p>
<ul class="ticks">
<li>Several vaults, switch at any time</li>
<li>Optional file watcher for external changes</li>
<li>Three themes: Drey, Anthrazit and Cyberpunk</li>
<li>Office documents open in their own program</li>
</ul>
</div>
<figure><div class="shot">{pic('drey-git','Drey Source control panel with changed files and commit history',1800,1125)}</div></figure>
</div></div></section>

<section id="download"><div class="wrap">
<h2>Download Drey</h2>
<p class="lead">Version {DREY_VER}. Installers are around 200 MB.</p>
<table class="dl">
<tr><th>Windows</th><td>Installer (<code>drey-{DREY_VER}-setup.exe</code>) or single-file portable build</td></tr>
<tr><th>Linux AppImage</th><td><code>drey-{DREY_VER}.AppImage</code>: make it executable and run it; updates in place</td></tr>
<tr><th>Linux .deb</th><td><code>sudo apt install ./drey_{DREY_VER}_amd64.deb</code></td></tr>
</table>
<div class="cta" style="margin-top:22px"><a class="btn primary" href="{dl}">Go to the downloads</a></div>
<p class="note">Drey checks GitHub for new versions on startup. That request carries no note content, and downloading or installing always asks you first.</p>
</div></section>

<section><div class="wrap">
<h2>Questions</h2>
<details><summary>Does Drey send my notes anywhere?</summary><p>No. Notes stay in your vault folder. Only if you switch on a hosted AI provider, or allow web search or an external MCP server, does the content of a question leave your computer.</p></details>
<details><summary>Which AI models can I use?</summary><p>Any local server that speaks the OpenAI-compatible API, such as LM Studio, llama.cpp, vLLM or Ollama. OpenRouter, the Anthropic API, Z.ai and the Claude Code CLI are available as opt-in providers.</p></details>
<details><summary>Can I use Drey without AI?</summary><p>Yes. The assistant is optional; the editor, tasks, tags, search, templates and Git features work on their own.</p></details>
<details><summary>Can I keep using my existing Markdown files?</summary><p>Yes. Point Drey at any folder of Markdown notes. It never adds frontmatter to a note on its own, and it never moves your folders around.</p></details>
<details><summary>Is Drey free?</summary><p>Yes. Drey is open source under the GNU GPL v3.</p></details>
</div></section>
"""
faq = [
 ("Does Drey send my notes anywhere?","No. Notes stay in your vault folder. Only if you switch on a hosted AI provider, or allow web search or an external MCP server, does the content of a question leave your computer."),
 ("Which AI models can I use?","Any local server that speaks the OpenAI-compatible API, such as LM Studio, llama.cpp, vLLM or Ollama. OpenRouter, the Anthropic API, Z.ai and the Claude Code CLI are available as opt-in providers."),
 ("Can I use Drey without AI?","Yes. The assistant is optional; the editor, tasks, tags, search, templates and Git features work on their own."),
 ("Can I keep using my existing Markdown files?","Yes. Point Drey at any folder of Markdown notes. It never adds frontmatter to a note on its own, and it never moves your folders around."),
 ("Is Drey free?","Yes. Drey is open source under the GNU GPL v3."),
]
drey_schema = [
 {"@context":"https://schema.org","@type":"SoftwareApplication","name":"Drey","applicationCategory":"ProductivityApplication",
  "operatingSystem":"Windows, Linux","softwareVersion":DREY_VER,"description":"Local-first Markdown note vault with live preview, tasks, tags, search and an optional permissioned AI assistant.",
  "url":BASE+"/drey/","image":BASE+"/assets/og-drey.png","downloadUrl":dl,"license":"https://www.gnu.org/licenses/gpl-3.0.html",
  "offers":{"@type":"Offer","price":"0","priceCurrency":"EUR"},"publisher":{"@type":"Organization","name":"Lariscus","url":BASE+"/"}},
 {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},
 {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Lariscus","item":BASE+"/"},{"@type":"ListItem","position":2,"name":"Drey","item":BASE+"/drey/"}]},
]
drey = page(path="/drey/", title="Drey – private local-first Markdown note vault",
  desc="Drey is a free, open-source Markdown note app with live preview, tasks, tags, search and an optional AI assistant with permissions. Plain files, Windows and Linux.",
  og="og-drey.png", body_class="drey", body=drey_body, schema=drey_schema, nav="drey")

# ---------------------------------------------------------------- dricket
dk_body = f"""
<div class="wrap hero"><div class="grid two">
<div>
<p class="eyebrow">dricket · Git tickets</p>
<h1>Tickets that live in Git. Claimed by fast-forward.</h1>
<p class="lead">dricket is a ticketing system with no server. Every ticket is a Markdown file in a Git repository, and who is working on it right now is decided by Git itself: only one fast-forward publication lands.</p>
<div class="cta"><a class="btn primary" href="{GH}/dricket/releases/latest">Download dk {DK_VER}</a><a class="btn" href="{GH}/dricket">View source</a></div>
<p class="note">One static binary · Linux, macOS and Windows · GPL-3.0-or-later</p>
</div>
<figure>{TERM}</figure>
</div></div>

<section><div class="wrap">
<h2>Why dricket</h2>
<div class="cards">
<div class="card"><span class="tag">No server</span><h3>Git is the database</h3><p>Your Git host is the database and the lock manager. There is nothing to deploy, patch or pay for.</p></div>
<div class="card"><span class="tag">Atomic</span><h3>One claim wins</h3><p>Claiming is a fast-forward publication. Exactly one claimant succeeds and the others are told immediately.</p></div>
<div class="card"><span class="tag">Plain files</span><h3>Markdown you can edit</h3><p>Claim, sync, use any editor, publish with <code>dk commit</code>. Humans and agents work on the same files.</p></div>
<div class="card"><span class="tag">Guardrails</span><h3>Safe for agents</h3><p>Leases, cooperative fencing with epochs, immutable identity and transition checks keep shared state coherent.</p></div>
</div></div></section>

<section><div class="wrap"><div class="split">
<div>
<h2>How a claim works</h2>
<p>Two runners race for the same ticket. Git accepts the first fast-forward and rejects the second. The loser fetches, sees who owns it and moves on to the next ticket.</p>
<ul class="ticks">
<li>Leases have a size (S, M, L) instead of a guessed duration</li>
<li>Owners extend a lease with a reason</li>
<li>A stale epoch is refused and local work is kept</li>
<li>Comments reach the owner without touching the ticket file</li>
</ul>
</div>
<figure><pre class="term" role="img" aria-label="Sequence: runner A claims app-6842 and is accepted as a fast-forward; runner B's claim is rejected as not fast-forward and B fetches to see that A owns it.">  runner A                Git remote               runner B
     |  fetch                  |                        |
     |&lt;------------------------|                        |
     |  claim app-6842         |                        |
     |------------------------&gt;|  <span class="ok">accepted: fast-forward</span> |
     |                         |  claim app-6842        |
     |                         |&lt;------------------------|
     |                         |  <span style="color:#f07a72">rejected: not fast-forward</span>
     |                         |------------------------&gt;|
     |                         |  B fetches, sees A owns it</pre></figure>
</div></div></section>

<section><div class="wrap"><div class="split flip">
<div>
<h2>A small, strict CLI for agents</h2>
<p>Inside the ticket repository <code>dk</code> finds the store, branch and project by itself, with no flags and no environment. Exit codes are part of the contract, so an agent knows what to do next.</p>
<ul class="ticks">
<li><code>11</code> already claimed · <code>13</code> claim lost, stop immediately</li>
<li><code>dk guide</code> prints instructions that match your version</li>
<li><code>dk setup-agent</code> installs an agent skill and the <code>AGENTS.md</code> pointer</li>
<li>Ticket text is treated as untrusted input</li>
</ul>
</div>
<pre class="term"><span class="p">$</span> dk show app-1 &gt; ticket.md
<span class="c"># edit ticket.md in an editor</span>
<span class="p">$</span> dk put app-1 -F ticket.md --claim --if-version 2 --json
<span class="p">$</span> dk validate
<span class="ok">validate ok</span>
<span class="p">$</span> dk setup-agent
<span class="ok">installed .agents/skills/dricket/SKILL.md</span></pre>
</div></div></section>

<section id="install"><div class="wrap">
<h2>Install</h2>
<p class="lead">One static binary, shipped under one name: <code>dk</code>. Git 2.32 or newer must be installed.</p>
<pre class="term"><span class="c"># release archive: github.com/HenrikPuls/dricket/releases (SHA-256 checksums included)</span>
<span class="p">$</span> go install github.com/HenrikPuls/dricket/cmd/dk@latest
<span class="p">$</span> dk init tickets-store app
<span class="p">$</span> cd tickets-store
<span class="p">$</span> dk add -m "First ticket"</pre>
<div class="cta" style="margin-top:22px"><a class="btn primary" href="{GH}/dricket/releases/latest">Download releases</a><a class="btn" href="{GH}/dricket#readme">Read the README</a></div>
</div></section>

<section><div class="wrap">
<h2>Trust model</h2>
<p class="lead" style="max-width:70ch">Everyone allowed to push the ticket repository can edit tickets; your Git host owns authentication and branch rules. dricket validates documents and every identity, revision, epoch and claim transition, and <code>dk validate</code> can also run as a host-side gate. Report vulnerabilities privately as described in the <a href="{GH}/dricket/blob/main/SECURITY.md">security policy</a>.</p>
</div></section>

<section><div class="wrap">
<h2>Questions</h2>
<details><summary>Do I need a ticket server?</summary><p>No. dricket needs only a Git remote. A local repository works too.</p></details>
<details><summary>How is it different from a hosted issue tracker?</summary><p>The tickets are files in your repository, and claiming is an atomic Git operation, so several people and agents can work in parallel without a central service. It is a coordination layer, not a project-management suite.</p></details>
<details><summary>What happens if two agents claim the same ticket?</summary><p>One fast-forward push lands. The other gets exit code 11 (already claimed) and is told who owns the ticket.</p></details>
<details><summary>Is it ready for my team?</summary><p>dricket is in an early phase. It is built for teams and agents that share a ticket repository, and it works well there. Use in large-scale setups with many simultaneous writers has not been tested yet.</p></details>
</div></section>
"""
dk_faq = [
 ("Do I need a ticket server?","No. dricket needs only a Git remote. A local repository works too."),
 ("How is it different from a hosted issue tracker?","The tickets are files in your repository, and claiming is an atomic Git operation, so several people and agents can work in parallel without a central service. It is a coordination layer, not a project-management suite."),
 ("What happens if two agents claim the same ticket?","One fast-forward push lands. The other gets exit code 11 (already claimed) and is told who owns the ticket."),
 ("Is it ready for my team?","dricket is in an early phase. It is built for teams and agents that share a ticket repository, and it works well there. Use in large-scale setups with many simultaneous writers has not been tested yet."),
]
dk_schema = [
 {"@context":"https://schema.org","@type":"SoftwareApplication","name":"dricket","applicationCategory":"DeveloperApplication",
  "operatingSystem":"Linux, macOS, Windows","softwareVersion":DK_VER,"description":"Serverless ticketing in Git: tickets are Markdown files and claims are fast-forward pushes. Built for humans and AI agents.",
  "url":BASE+"/dricket/","image":BASE+"/assets/og-dricket.png","downloadUrl":f"{GH}/dricket/releases/latest","license":"https://www.gnu.org/licenses/gpl-3.0.html",
  "offers":{"@type":"Offer","price":"0","priceCurrency":"EUR"},"publisher":{"@type":"Organization","name":"Lariscus","url":BASE+"/"}},
 {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in dk_faq]},
 {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Lariscus","item":BASE+"/"},{"@type":"ListItem","position":2,"name":"dricket","item":BASE+"/dricket/"}]},
]
dk = page(path="/dricket/", title="dricket – serverless Git tickets for humans and agents",
  desc="dricket stores tickets as Markdown in Git and claims them by fast-forward push. No server, one atomic claim, a strict CLI that is safe for AI agents. Open source.",
  og="og-dricket.png", body_class="dricket", body=dk_body, schema=dk_schema, nav="dricket")

# ---------------------------------------------------------------- 404
nf = page(path="/404.html", title="Page not found – Lariscus", desc="This page does not exist.", og="og-lariscus.png", robots="noindex",
  body='<div class="wrap hero"><p class="eyebrow">404</p><h1>This page is not here.</h1><p class="lead">The link may be old or mistyped.</p><div class="cta"><a class="btn primary" href="/">Back to Lariscus</a><a class="btn" href="/drey/">Drey</a><a class="btn" href="/dricket/">dricket</a></div></div>')

for rel, content in {"index.html":home, "drey/index.html":drey, "dricket/index.html":dk, "404.html":nf}.items():
    p = ROOT/rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(content, encoding="utf-8")

urls = ["/", "/drey/", "/dricket/"]
(ROOT/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
  + "".join(f"  <url><loc>{BASE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
(ROOT/"robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
(ROOT/".nojekyll").write_text("")
print("ok")
