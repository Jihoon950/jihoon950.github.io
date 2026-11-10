"""Build the public English site from content.json. Python standard library only."""
from pathlib import Path
import json
import html
import hashlib

ROOT = Path(__file__).resolve().parents[1]
d = json.loads((ROOT / "content.json").read_text(encoding="utf-8"))
style_version = hashlib.sha256((ROOT / "styles.css").read_bytes()).hexdigest()[:12]
pdf_version = hashlib.sha256((ROOT / "assets/Jihoon_Lee_CV.pdf").read_bytes()).hexdigest()[:12]
e = lambda value: html.escape(str(value), quote=True)
tags = lambda values: "".join(f"<span>{e(v)}</span>" for v in values)
author_html = lambda value: e(value).replace('Jihoon Lee','<strong>Jihoon Lee</strong>').replace('J. Lee','<strong>J. Lee</strong>')

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

figure_alts = {
    "gpu": "RAN workload monitoring guides AI inference toward shared GPU SMs at low load and disjoint SMs at high load.",
    "semantic": "Semantic token groups map to prefix and suffix bits, followed by context-aware recovery after transmission.",
    "aircons": "Vehicle states combine over the wireless channel; the recovered neighbor mean supports local vehicle control.",
    "beam": "A transmitter aligns a narrow directional beam with a moving receiver.",
}
research = "".join(f"""<article class="research-card"><div class="diagram"><img src="{e(r['figure'])}" alt="{e(figure_alts[r['id']])}" width="1000" height="560" loading="lazy"></div>
<div class="card-body"><p class="eyebrow">{i:02d} / {e(r['label'])}</p><h3>{e(r['title'])}</h3><p>{e(r['description'])}</p>
<div class="tags">{tags(r['tags'])}</div><a class="text-link" href="{e(r['link'])}">{e(r['link_label'])} <span aria-hidden="true">↗</span></a></div></article>""" for i,r in enumerate(d["research"],1))

publications = "".join(f"""<article class="publication" data-publication="{p['type']}" data-status="{p['status']}">
<div class="pub-year">{p['year']}<span>{'Journal' if p['type']=='journal' else 'Conference'}</span></div>
<div class="pub-body">{('<p class="pub-status '+p['status']+'">'+p['status'].capitalize()+'</p>') if p['status'] in ('accepted','submitted') else ''}<h3>{('<a href="'+e(p['url'])+'">'+e(p['title'])+'</a>') if p.get('url') else e(p['title'])}</h3><p class="authors">{author_html(p['authors'])}</p>
<p class="venue">{e(p['venue'])}</p>{('<p class="pub-details">'+e(p['details'])+'</p>') if p['status']!='submitted' else ''}
<div class="pub-actions">{('<a href="'+e(p['url'])+'">'+e(p['link_label'])+' <span aria-hidden="true">↗</span></a>') if p.get('url') else ''}{('<button type="button" data-cite="bib-'+p['id']+'" aria-label="Cite '+e(p['title'])+'">Cite <span aria-hidden="true">↗</span></button><template id="bib-'+p['id']+'">'+e(p['bibtex'])+'</template>') if p.get('bibtex') else ''}</div>
</div></article>""" for p in d["publications"])

def manuscript_rows(status):
    return ''.join(f'''<article class="publication manuscript" data-status="{p['status']}"><div class="pub-year"><span>In preparation</span></div><div class="pub-body"><h3>{e(p['title'])}</h3><p class="authors">{author_html(p['authors'])}</p><p class="pub-status">{e(p['status_text'])}</p></div></article>''' for p in d['manuscripts'] if p['status']==status)

pub_counts={key:sum(p['type']==key for p in d['publications']) for key in ['journal','conference']}

domestic = "".join(f"""<li><span class="domestic-year">{p['year']}</span><div><h4>{e(p['title'])}</h4><p>{e(p['authors'])}<br>{e(p['venue'])} · {e(p['format'])}</p></div></li>""" for p in d["domestic"])
education = "".join(f"""<article class="education-item"><p class="eyebrow">{e(item['period'])}</p><h3>{e(item['degree'])}</h3><p>{e(item['institution'])}</p><p class="muted">{e(item['detail'])}</p></article>""" for item in d["education"])
projects = "".join(f"""<article class="project"><p class="project-period">{e(item['period'])}</p><div><h3>{e(item['title'])}</h3><p>{e(item['description'])}</p><div class="tags">{tags(item['tags'])}</div></div><span class="project-index" aria-hidden="true">{i:02d}</span></article>""" for i,item in enumerate(d["projects"],1))
patents = "".join(f"""<article class="patent"><p class="eyebrow"><span class="patent-status">{e(item['status'])}</span> KR {e(item['number'])}</p><h3>{e(item['title'])}</h3><p>{e(item['inventors'])}</p></article>""" for item in d["patents"])

demos = "".join(f'''<article class="demo-card" id="demo-{e(x['id'])}">
<div class="demo-copy"><p class="demo-status">{e(x['status_text'])}</p><h3>{e(x['title'])}</h3>
<p class="demo-authors">{author_html(x['authors'])}</p><p class="demo-event">{e(x['event'])}<br>{e(x['date'])} · {e(x['location'])}</p>
<p class="demo-description">{e(x['description'])}</p>
<div class="demo-links"><a class="text-link" href="{e(x['video'])}">Open video <span aria-hidden="true">↗</span></a><a class="text-link" href="{e(x['event_url'])}">Event program <span aria-hidden="true">↗</span></a></div></div>
<figure class="demo-video"><video controls playsinline preload="none" width="1920" height="1080" poster="{e(x['poster'])}" aria-label="{e(x['title'])}: 90-second demonstration with English subtitles"><source src="{e(x['video'])}" type="video/mp4">Your browser does not support embedded video. <a href="{e(x['video'])}">Open the demo video</a>.</video><figcaption>{e(x['duration'])} · {e(x['language'])}</figcaption></figure>
</article>''' for x in d.get('demonstrations',[]))

url=d["site_url"].rstrip("/")+"/" if d["site_url"] else ""
canonical=f'<link rel="canonical" href="{e(url)}"><meta property="og:url" content="{e(url)}">' if url else ""
qr_button='<button id="share-button" class="text-link" type="button">Share via QR <span aria-hidden="true">↗</span></button>' if url else ""
qr_dialog=f"""<dialog id="share-dialog" class="share-dialog"><button class="dialog-close" data-close type="button" aria-label="Close QR code">×</button><p class="eyebrow">Connect & share</p><h2>Profile QR Code</h2><img src="assets/jihoon-lee-qr.svg" width="240" height="240" alt="QR code linking to {e(url)}"><p><a href="{e(url)}">{e(url)}</a></p><a class="button primary" href="assets/jihoon-lee-qr.png" download>Download QR code ↓</a></dialog>""" if url else ""
schema=json.dumps({"@context":"https://schema.org","@type":"Person","name":d["name"],"jobTitle":d["role"],"affiliation":{"@type":"CollegeOrUniversity","name":d["institution"]},"url":url,"sameAs":[f"https://orcid.org/{d['orcid']}",d["lab_url"]]},ensure_ascii=False)
profile_visual = f'<div class="portrait-frame"><img class="profile-photo" src="{e(d["photo"])}" alt="Portrait of Jihoon Lee" width="1417" height="1890" fetchpriority="high"></div><div class="visual-caption"><span>JIHOON LEE</span><span>YONSEI UNIVERSITY</span></div>' if d.get('photo') else hero_art

page=f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Jihoon Lee — Wireless Networks & Intelligent Systems</title>
<meta name="description" content="Jihoon Lee is a Ph.D. student at Yonsei University researching semantic token communication, GPU sharing for AI-and-RAN, and wireless control.">
<meta name="theme-color" content="#f5f7fc"><meta property="og:type" content="website"><meta property="og:title" content="Jihoon Lee — Wireless Networks & Intelligent Systems">
<meta property="og:description" content="Academic portfolio · Yonsei University · Semantic communication, GPU sharing and AI-and-RAN.">{canonical}
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="styles.css?v={style_version}">
<script type="application/ld+json">{schema}</script><script src="site.js" defer></script></head>
<body><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="header-inner"><a href="#top" class="wordmark" aria-label="Jihoon Lee home">JL<span>.</span></a>
<button class="menu-toggle" aria-expanded="false" aria-controls="navigation" aria-label="Toggle navigation">Menu <span aria-hidden="true">☰</span></button>
<nav id="navigation" aria-label="Main navigation"><a href="#research">Research</a><a href="#demonstrations">Demos</a><a href="#publications">Publications</a><a href="#about">About</a><a href="#projects">Projects</a><a href="#contact" class="nav-contact">Contact <span aria-hidden="true">↗</span></a></nav></div></header>
<main id="main"><section class="hero section-shell" id="top"><div class="hero-copy"><p class="eyebrow"><span class="status-dot"></span> {e(d['institution'])} · RAMO Lab</p>
<h1>Jihoon<br><span>Lee.</span></h1><p class="hero-role">Ph.D. Student · Electrical & Electronic Engineering</p>
<h2>Wireless Communication and AI Systems</h2><p class="hero-description">{e(d['intro'])}</p>
<aside class="opportunity-note" aria-label="Postdoctoral opportunities"><p class="eyebrow">Postdoctoral opportunities</p><p>{e(d['postdoc_statement'])}</p><div class="opportunity-contact"><span>Get in touch</span><a href="mailto:{e(d['email'])}" class="text-link">{e(d['email'])} <span aria-hidden="true">↗</span></a></div></aside>
<div class="hero-actions"><a class="button primary" href="#research">Explore my research <span aria-hidden="true">↗</span></a><a class="button secondary" href="assets/Jihoon_Lee_CV.pdf?v={pdf_version}" download>Download CV <span aria-hidden="true">↓</span></a></div></div>
<div class="hero-visual portrait-visual">{profile_visual}</div>
<div class="hero-bottom"><span>Based in Seoul, South Korea</span><a href="#research">Scroll to explore <span aria-hidden="true">↓</span></a><span>SEMANTIC COMMUNICATION / AI-AND-RAN</span></div></section>
<section class="research-section section-shell" id="research"><div class="section-heading"><div><p class="eyebrow">01 / Research</p><h2>Research Interests</h2></div><p>I work at the intersection of wireless communication, distributed control, and AI.</p></div><div class="research-grid">{research}</div></section>
<section class="demos-section" id="demonstrations"><div class="section-shell"><div class="section-heading"><div><p class="eyebrow">02 / Demonstrations</p><h2>Demonstrations</h2></div><p>System demonstrations and experimental testbeds.</p></div>{demos}</div></section>
<section class="publications-section" id="publications"><div class="section-shell"><div class="section-heading"><div><p class="eyebrow">03 / Publications & ongoing work</p><h2>Publications</h2></div><a class="text-link" href="assets/publications.bib" download>Publication BibTeX <span aria-hidden="true">↓</span></a></div>
<h3 class="publication-group-title">Published, accepted & submitted</h3>
<div class="filters" role="group" aria-label="Filter publications"><button type="button" data-filter="all" aria-pressed="true">All <span>{len(d['publications']):02d}</span></button><button type="button" data-filter="journal" aria-pressed="false">Journal <span>{pub_counts['journal']:02d}</span></button><button type="button" data-filter="conference" aria-pressed="false">Conference <span>{pub_counts['conference']:02d}</span></button></div>
<p class="sr-only" id="filter-status" role="status" aria-live="polite">{len(d['publications'])} publications shown</p>
<div class="publication-list">{publications}</div>
<section id="work-in-progress" class="manuscript-group" aria-labelledby="progress-heading"><h3 id="progress-heading" class="publication-group-title">In preparation</h3>{manuscript_rows('planned')}</section>
<details class="domestic"><summary>Domestic conferences <span>05 <span aria-hidden="true">＋</span></span></summary><p class="translation-note">English translations of Korean titles.</p><ol>{domestic}</ol></details></div></section>
<section class="about-section section-shell" id="about"><div class="about-intro"><p class="eyebrow">04 / Background</p><h2>Education and Background</h2><p>{e(d['about'])}</p><a class="text-link" href="{e(d['lab_url'])}">RAMO Laboratory <span aria-hidden="true">↗</span></a>
<div class="toolkit"><h3>Technical Skills</h3><div class="tags">{tags(d['tools'])}</div><p class="languages">{' &nbsp; / &nbsp; '.join(e(x) for x in d['languages'])}</p></div></div><div class="education"><p class="eyebrow">Education</p>{education}<a class="button secondary" href="assets/Jihoon_Lee_CV.pdf?v={pdf_version}" download>Full academic CV <span aria-hidden="true">↓</span></a></div></section>
<section class="projects-section" id="projects"><div class="section-shell"><div class="section-heading"><div><p class="eyebrow">05 / Research projects</p><h2>Research Projects</h2></div><p>Research across the wireless stack, from physical-layer coordination to AI-enabled networks.</p></div><div class="project-list">{projects}</div></div></section>
<section class="patents-section section-shell" id="patents"><div class="section-heading"><div><p class="eyebrow">06 / Intellectual property</p><h2>Patents</h2></div><p>Selected Korean patents.<br>Titles shown in English translation.</p></div><div class="patent-grid">{patents}</div></section>
<section class="contact-section" id="contact"><div class="section-shell"><p class="eyebrow">07 / Contact</p><h2>Contact</h2><a class="contact-email" href="mailto:{e(d['email'])}">{e(d['email'])} <span aria-hidden="true">↗</span></a>
<div class="contact-bottom"><p>{e(d['lab'])}<br>{e(d['institution'])} · {e(d['location'])}</p><div class="contact-links"><a href="https://orcid.org/{e(d['orcid'])}">ORCID ↗</a><a href="{e(d['lab_url'])}">RAMO Lab ↗</a><a href="assets/Jihoon_Lee_CV.pdf?v={pdf_version}">CV PDF ↗</a>{qr_button}</div></div></div></section>
</main><footer class="site-footer section-shell"><span>© 2026 Jihoon Lee</span><span>Last updated · {e(d['updated'])}</span><a href="#top">Back to top ↑</a></footer>
<dialog id="citation-dialog"><button class="dialog-close" type="button" data-close aria-label="Close citation">×</button><p class="eyebrow">Reference</p><h2>Citation</h2><pre id="citation-text"></pre><button type="button" class="button primary" id="copy-citation">Copy BibTeX</button></dialog>{qr_dialog}
</body></html>"""
(ROOT/"index.html").write_text(page,encoding="utf-8")
(ROOT/"assets").mkdir(exist_ok=True)
(ROOT/"assets"/"publications.bib").write_text("\n\n".join(p["bibtex"] for p in d["publications"] if p.get('bibtex'))+"\n",encoding="utf-8")
print("Built index.html and assets/publications.bib")
