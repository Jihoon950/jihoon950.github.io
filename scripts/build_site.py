"""Build the public English site from content.json. Python standard library only."""
from pathlib import Path
import json
import html

ROOT = Path(__file__).resolve().parents[1]
d = json.loads((ROOT / "content.json").read_text(encoding="utf-8"))
e = lambda value: html.escape(str(value), quote=True)
tags = lambda values: "".join(f"<span>{e(v)}</span>" for v in values)

hero_art = """<svg viewBox="0 0 580 540" role="img" aria-labelledby="network-title">
<title id="network-title">An illustrative network connecting mobility, wireless communication, and AI</title>
<defs><pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#b9c5dc"/></pattern>
<linearGradient id="core" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#4571ff"/><stop offset="1" stop-color="#2449dc"/></linearGradient></defs>
<rect width="580" height="540" fill="url(#dots)" opacity=".55"/>
<g fill="none" stroke="#c4cfee"><circle cx="290" cy="270" r="208"/><circle cx="290" cy="270" r="148"/><circle cx="290" cy="270" r="88"/></g>
<g stroke="#a5b8eb" stroke-width="1.5" fill="none"><path d="M290 270L142 122M290 270L457 176M290 270L424 429M290 270L93 348"/><path stroke-dasharray="4 7" d="M142 122L457 176L424 429L93 348Z"/></g>
<circle class="signal-ring" cx="290" cy="270" r="67" fill="none" stroke="#3763f4" opacity=".3"/>
<rect x="226" y="206" width="128" height="128" rx="36" fill="url(#core)" transform="rotate(-12 290 270)"/>
<g stroke="white" stroke-width="3" fill="none" stroke-linecap="round"><path d="M263 260Q290 236 317 260M272 271Q290 254 308 271M282 282Q290 275 298 282"/><circle cx="290" cy="293" r="3" fill="white" stroke="none"/></g>
<g fill="#fff" stroke="#d6dff1"><rect x="96" y="87" width="92" height="70" rx="20"/><rect x="414" y="141" width="86" height="70" rx="20"/><rect x="383" y="394" width="86" height="70" rx="20"/><rect x="49" y="313" width="88" height="70" rx="20"/></g>
<g font-family="Arial,sans-serif" font-size="21" font-weight="700" fill="#1e315b" text-anchor="middle"><text x="142" y="130">V2X</text><text x="457" y="185">6G</text><text x="426" y="438">AI</text><text x="93" y="357">RAN</text></g>
<g fill="#3763f4"><circle cx="252" cy="65" r="5"/><circle cx="492" cy="324" r="5"/><circle cx="244" cy="473" r="5"/></g>
<g font-family="monospace" font-size="10" letter-spacing="2" fill="#697a9c"><text x="22" y="30">COMMUNICATION × INTELLIGENCE</text><text x="355" y="520">CONNECTED SYSTEMS</text></g>
</svg>"""

diagrams = {
"aircons": """<svg viewBox="0 0 360 190" role="img" aria-label="Three vehicles coordinating through a shared wireless signal">
<path d="M25 141H335M25 151H335" stroke="#bcc9df"/><path d="M45 98Q180-20 315 98" stroke="#2f5ef4" stroke-width="1.5" fill="none" stroke-dasharray="4 6"/>
<path d="M105 96Q180 26 255 96" stroke="#2f5ef4" fill="none"/><circle cx="180" cy="43" r="18" fill="#2f5ef4"/><text x="180" y="49" text-anchor="middle" fill="white" font-family="serif" font-size="22">Σ</text>
<g fill="white" stroke="#354f7a" stroke-width="1.5"><rect x="28" y="105" width="76" height="28" rx="8"/><rect x="142" y="105" width="76" height="28" rx="8"/><rect x="256" y="105" width="76" height="28" rx="8"/><path d="M43 105L53 91H80L90 105M157 105L167 91H194L204 105M271 105L281 91H308L318 105"/></g>
<g fill="#354f7a"><circle cx="46" cy="134" r="6"/><circle cx="86" cy="134" r="6"/><circle cx="160" cy="134" r="6"/><circle cx="200" cy="134" r="6"/><circle cx="274" cy="134" r="6"/><circle cx="314" cy="134" r="6"/></g>
<path d="M112 119H134M226 119H248" stroke="#2f5ef4" stroke-width="2"/><text x="180" y="177" text-anchor="middle" font-family="monospace" font-size="10" letter-spacing="1" fill="#617293">SHARED CHANNEL · COLLECTIVE STATE</text></svg>""",
"beam": """<svg viewBox="0 0 360 190" role="img" aria-label="A directional wireless beam tracking a moving receiver">
<path d="M52 132L276 33L307 88Z" fill="#2f5ef4" opacity=".1"/><path d="M52 132L276 33M52 132L307 88" stroke="#8fa9f8" stroke-width="1.5"/><path d="M52 132L300 142L291 181Z" fill="#2f5ef4" opacity=".05"/>
<path d="M240 26Q331 89 288 165" fill="none" stroke="#98a8c6" stroke-dasharray="4 5"/>
<path d="M52 96V155M37 155L52 113L67 155M43 131H61" stroke="#354f7a" stroke-width="2" fill="none"/><circle cx="52" cy="96" r="5" fill="#2f5ef4"/>
<circle cx="280" cy="64" r="12" fill="white" stroke="#2f5ef4" stroke-width="2"/><circle cx="280" cy="64" r="4" fill="#2f5ef4"/>
<path d="M52 132L280 64" stroke="#2f5ef4" stroke-dasharray="4 5"/><text x="166" y="113" font-family="serif" font-style="italic" fill="#2f5ef4" font-size="20">θ</text>
<text x="180" y="177" text-anchor="middle" font-family="monospace" font-size="10" letter-spacing="1" fill="#617293">POSITION · ALIGNMENT · THROUGHPUT</text></svg>""",
"semantic": """<svg viewBox="0 0 360 190" role="img" aria-label="Tokens grouped by meaning and transmitted through a channel">
<g fill="white" stroke="#a9b9d7"><rect x="24" y="40" width="63" height="28" rx="7"/><rect x="24" y="81" width="63" height="28" rx="7"/><rect x="24" y="122" width="63" height="28" rx="7"/></g>
<g font-family="monospace" font-size="11" fill="#526a94" text-anchor="middle"><text x="55" y="58">token</text><text x="55" y="99">token</text><text x="55" y="140">token</text></g>
<path d="M92 54L136 95M92 95H136M92 136L136 95M224 95H279" stroke="#9cafda" fill="none" stroke-width="1.5"/>
<rect x="137" y="51" width="86" height="87" rx="21" fill="#2f5ef4"/><g fill="white"><circle cx="166" cy="78" r="5"/><circle cx="190" cy="80" r="5"/><circle cx="178" cy="99" r="5"/><circle cx="161" cy="116" r="5"/><circle cx="198" cy="111" r="5"/></g>
<rect x="280" y="69" width="55" height="52" rx="13" fill="white" stroke="#a9b9d7"/><path d="M293 95L303 104L323 85" stroke="#2f5ef4" stroke-width="2" fill="none"/>
<text x="180" y="177" text-anchor="middle" font-family="monospace" font-size="10" letter-spacing="1" fill="#617293">TOKENS · STRUCTURE · MEANING</text></svg>"""
}

research = "".join(f"""<article class="research-card"><div class="diagram">{diagrams[r['id']]}</div>
<div class="card-body"><p class="eyebrow">{i:02d} / {e(r['label'])}</p><h3>{e(r['title'])}</h3><p>{e(r['description'])}</p>
<div class="tags">{tags(r['tags'])}</div><a class="text-link" href="{e(r['link'])}">{e(r['link_label'])} <span aria-hidden="true">↗</span></a></div></article>""" for i,r in enumerate(d["research"],1))

publications = "".join(f"""<article class="publication" data-publication="{p['type']}">
<div class="pub-year">{p['year']}<span>{'Journal' if p['type']=='journal' else 'Conference'}</span></div>
<div class="pub-body"><h3><a href="{e(p['url'])}">{e(p['title'])}</a></h3><p class="authors">{e(p['authors']).replace('Jihoon Lee','<strong>Jihoon Lee</strong>')}</p>
<p class="venue">{e(p['venue'])}</p><p class="pub-details">{e(p['details'])}</p>
<div class="pub-actions"><a href="{e(p['url'])}">{e(p['link_label'])} <span aria-hidden="true">↗</span></a><button type="button" data-cite="bib-{p['id']}" aria-label="Cite {e(p['title'])}">Cite <span aria-hidden="true">↗</span></button></div>
<template id="bib-{p['id']}">{e(p['bibtex'])}</template></div></article>""" for p in d["publications"])

domestic = "".join(f"""<li><span class="domestic-year">{p['year']}</span><div><h4>{e(p['title'])}</h4><p>{e(p['authors'])}<br>{e(p['venue'])} · {e(p['format'])}</p></div></li>""" for p in d["domestic"])
education = "".join(f"""<article class="education-item"><p class="eyebrow">{e(item['period'])}</p><h3>{e(item['degree'])}</h3><p>{e(item['institution'])}</p><p class="muted">{e(item['detail'])}</p></article>""" for item in d["education"])
projects = "".join(f"""<article class="project"><p class="project-period">{e(item['period'])}</p><div><h3>{e(item['title'])}</h3><p>{e(item['description'])}</p><div class="tags">{tags(item['tags'])}</div></div><span class="project-index" aria-hidden="true">{i:02d}</span></article>""" for i,item in enumerate(d["projects"],1))
patents = "".join(f"""<article class="patent"><p class="eyebrow"><span class="patent-status">{e(item['status'])}</span> KR {e(item['number'])}</p><h3>{e(item['title'])}</h3><p>{e(item['inventors'])}</p></article>""" for item in d["patents"])

url=d["site_url"].rstrip("/")+"/" if d["site_url"] else ""
canonical=f'<link rel="canonical" href="{e(url)}"><meta property="og:url" content="{e(url)}">' if url else ""
qr_button='<button id="share-button" class="text-link" type="button">Share via QR <span aria-hidden="true">↗</span></button>' if url else ""
qr_dialog=f"""<dialog id="share-dialog" class="share-dialog"><button class="dialog-close" data-close type="button" aria-label="Close QR code">×</button><p class="eyebrow">Connect & share</p><h2>Take this page with you.</h2><img src="assets/jihoon-lee-qr.svg" width="240" height="240" alt="QR code linking to {e(url)}"><p><a href="{e(url)}">{e(url)}</a></p><a class="button primary" href="assets/jihoon-lee-qr.png" download>Download QR code ↓</a></dialog>""" if url else ""
schema=json.dumps({"@context":"https://schema.org","@type":"Person","name":d["name"],"jobTitle":d["role"],"affiliation":{"@type":"CollegeOrUniversity","name":d["institution"]},"url":url,"sameAs":[f"https://orcid.org/{d['orcid']}",d["lab_url"]]},ensure_ascii=False)

page=f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Jihoon Lee — Wireless Networks & Intelligent Systems</title>
<meta name="description" content="Jihoon Lee is a Ph.D. student at Yonsei University researching V2X, 6G beam management, semantic communication, and intelligent wireless networks.">
<meta name="theme-color" content="#f5f7fc"><meta property="og:type" content="website"><meta property="og:title" content="Jihoon Lee — Wireless Networks & Intelligent Systems">
<meta property="og:description" content="Academic portfolio · Yonsei University · V2X, 6G and semantic communication.">{canonical}
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="styles.css">
<script type="application/ld+json">{schema}</script><script src="site.js" defer></script></head>
<body><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="header-inner"><a href="#top" class="wordmark" aria-label="Jihoon Lee home">JL<span>.</span></a>
<button class="menu-toggle" aria-expanded="false" aria-controls="navigation" aria-label="Toggle navigation">Menu <span aria-hidden="true">☰</span></button>
<nav id="navigation" aria-label="Main navigation"><a href="#research">Research</a><a href="#publications">Publications</a><a href="#about">About</a><a href="#projects">Projects</a><a href="#contact" class="nav-contact">Let’s connect <span aria-hidden="true">↗</span></a></nav></div></header>
<main id="main"><section class="hero section-shell" id="top"><div class="hero-copy"><p class="eyebrow"><span class="status-dot"></span> {e(d['institution'])} · RAMO Lab</p>
<h1>Jihoon<br><span>Lee.</span></h1><p class="hero-role">Ph.D. Student · Electrical & Electronic Engineering</p>
<h2>Connecting mobility,<br>meaning & intelligence.</h2><p class="hero-description">{e(d['intro'])}</p>
<div class="hero-actions"><a class="button primary" href="#research">Explore my research <span aria-hidden="true">↗</span></a><a class="button secondary" href="assets/Jihoon_Lee_CV.pdf" download>Download CV <span aria-hidden="true">↓</span></a></div></div>
<div class="hero-visual">{hero_art}<div class="visual-caption"><span>WIRELESS NETWORKS</span><span>INTELLIGENT SYSTEMS</span></div></div>
<div class="hero-bottom"><span>Based in Seoul, South Korea</span><a href="#research">Scroll to explore <span aria-hidden="true">↓</span></a><span>V2X / 6G / SEMANTIC AI</span></div></section>
<section class="research-section section-shell" id="research"><div class="section-heading"><div><p class="eyebrow">01 / Research directions</p><h2>Networks that move.<br>Signals that mean more.</h2></div><p>I work at the intersection of wireless communication, distributed control, and AI.</p></div><div class="research-grid">{research}</div></section>
<section class="publications-section" id="publications"><div class="section-shell"><div class="section-heading"><div><p class="eyebrow">02 / Selected publications</p><h2>Ideas, in print.</h2></div><a class="text-link" href="assets/publications.bib" download>Download BibTeX <span aria-hidden="true">↓</span></a></div>
<div class="filters" role="group" aria-label="Filter publications"><button type="button" data-filter="all" aria-pressed="true">All <span>03</span></button><button type="button" data-filter="journal" aria-pressed="false">Journal <span>01</span></button><button type="button" data-filter="conference" aria-pressed="false">Conference <span>02</span></button></div>
<p class="sr-only" id="filter-status" role="status" aria-live="polite">3 publications shown</p>
<div class="publication-list">{publications}</div>
<details class="domestic"><summary>Domestic conferences <span>05 <span aria-hidden="true">＋</span></span></summary><p class="translation-note">English translations of Korean titles.</p><ol>{domestic}</ol></details></div></section>
<section class="about-section section-shell" id="about"><div class="about-intro"><p class="eyebrow">03 / Background</p><h2>A researcher<br>in motion.</h2><p>{e(d['about'])}</p><a class="text-link" href="{e(d['lab_url'])}">Meet the RAMO Lab <span aria-hidden="true">↗</span></a>
<div class="toolkit"><h3>Research toolkit</h3><div class="tags">{tags(d['tools'])}</div><p class="languages">{' &nbsp; / &nbsp; '.join(e(x) for x in d['languages'])}</p></div></div><div class="education"><p class="eyebrow">Education</p>{education}<a class="button secondary" href="assets/Jihoon_Lee_CV.pdf" download>Full academic CV <span aria-hidden="true">↓</span></a></div></section>
<section class="projects-section" id="projects"><div class="section-shell"><div class="section-heading"><div><p class="eyebrow">04 / Research projects</p><h2>From models<br>to connected systems.</h2></div><p>Research across the wireless stack, from physical-layer coordination to AI-enabled networks.</p></div><div class="project-list">{projects}</div></div></section>
<section class="patents-section section-shell" id="patents"><div class="section-heading"><div><p class="eyebrow">05 / Intellectual property</p><h2>Ideas into applications.</h2></div><p>Selected Korean patents.<br>Titles shown in English translation.</p></div><div class="patent-grid">{patents}</div></section>
<section class="contact-section" id="contact"><div class="section-shell"><p class="eyebrow">06 / Get in touch</p><h2>Let’s connect<br>the next idea<span>.</span></h2><a class="contact-email" href="mailto:{e(d['email'])}">{e(d['email'])} <span aria-hidden="true">↗</span></a>
<div class="contact-bottom"><p>{e(d['lab'])}<br>{e(d['institution'])} · {e(d['location'])}</p><div class="contact-links"><a href="https://orcid.org/{e(d['orcid'])}">ORCID ↗</a><a href="{e(d['lab_url'])}">RAMO Lab ↗</a><a href="assets/Jihoon_Lee_CV.pdf">CV PDF ↗</a>{qr_button}</div></div></div></section>
</main><footer class="site-footer section-shell"><span>© 2026 Jihoon Lee</span><span>Last updated · {e(d['updated'])}</span><a href="#top">Back to top ↑</a></footer>
<dialog id="citation-dialog"><button class="dialog-close" type="button" data-close aria-label="Close citation">×</button><p class="eyebrow">Reference</p><h2>Cite this work.</h2><pre id="citation-text"></pre><button type="button" class="button primary" id="copy-citation">Copy BibTeX</button></dialog>{qr_dialog}
</body></html>"""
(ROOT/"index.html").write_text(page,encoding="utf-8")
(ROOT/"assets").mkdir(exist_ok=True)
(ROOT/"assets"/"publications.bib").write_text("\n\n".join(p["bibtex"] for p in d["publications"])+"\n",encoding="utf-8")
print("Built index.html and assets/publications.bib")
