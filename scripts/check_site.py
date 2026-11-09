"""Check generated static assets, anchors, and the downloadable CV."""
from pathlib import Path
from html.parser import HTMLParser
import re,json
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=[];self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if "id" in a:self.ids.append(a["id"])
        for key in ["href","src"]:
            if key in a:self.links.append(a[key])
source=(ROOT/"index.html").read_text(encoding="utf-8")
page=Page();page.feed(source)
assert len(page.ids)==len(set(page.ids)),"Duplicate IDs"
for link in page.links:
    if link.startswith("#"):assert link[1:] in page.ids,link
    elif ":" not in link:assert (ROOT/link.split("#")[0].split("?")[0]).is_file(),link
assert not re.search("[가-힣]",source),"Non-English site copy"
assert "010-" not in source and "dennis9508" not in source
assert 'lang="en"' in source
import pymupdf
pdf=pymupdf.open(ROOT/"assets"/"Jihoon_Lee_CV.pdf")
assert len(pdf)==3
text="".join(p.get_text() for p in pdf)
assert "Jihoon Lee" in text and "Technical skills".upper() in text
assert "010-" not in text
d=json.loads((ROOT/'content.json').read_text(encoding='utf-8'))
assert [p['status'] for p in d['manuscripts']]==['planned']
assert len(d['publications'])==6
assert [p['status'] for p in d['publications'][:3]]==['submitted','submitted','accepted']
assert all('GPU Sharing' not in p['title'] for p in d['projects'])
assert 'Submitted manuscripts' not in source
for r in d['research']:
    assert r['figure'] in source
for x in d['publications']+d['manuscripts']:
    assert x['title'] in source,x['title']
    assert x['title'] in re.sub(r'\s+',' ',text),x['title']
assert 'In preparation · Target: MobiCom 2027' in text
assert 'Semantics-Aware Representation, Protection, and Recovery' in text
assert 'Hyelin Nam, Jihoon Lee, Seung-Woo Ko, Jinho Choi, and Seong-Lyun Kim' in re.sub(r'\s+',' ',text)
assert source.count('data-status="submitted"')==2 and source.count('data-status="planned"')==1
assert 'H_TokCOM.pdf' not in source and 'Langsem.pdf' not in source
print("PASS: files, anchors, English copy, public contact data, 3-page CV, exact titles/authors and distinct publication statuses")
