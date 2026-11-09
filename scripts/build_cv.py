"""Generate the public English CV (requires reportlab)."""
from pathlib import Path
from html import escape
import json
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/"content.json").read_text(encoding="utf-8"))
for name,filename in [("Arial","arial.ttf"),("Arial-Bold","arialbd.ttf"),("Arial-Italic","ariali.ttf"),("Arial-BoldItalic","arialbi.ttf")]:
    pdfmetrics.registerFont(TTFont(name,str(Path("C:/Windows/Fonts")/filename)))
pdfmetrics.registerFontFamily("Arial",normal="Arial",bold="Arial-Bold",italic="Arial-Italic",boldItalic="Arial-BoldItalic")
blue=HexColor("#305ff2"); ink=HexColor("#17233d"); muted=HexColor("#596985")
base=ParagraphStyle("base",fontName="Arial",fontSize=9.2,leading=13.3,textColor=ink,spaceAfter=4)
styles={
 "body":base,
 "small":ParagraphStyle("small",parent=base,fontSize=8.2,leading=11.5,textColor=muted),
 "title":ParagraphStyle("title",parent=base,fontName="Arial-Bold",fontSize=35,leading=40,spaceAfter=8),
 "section":ParagraphStyle("section",parent=base,fontName="Arial-Bold",fontSize=11.8,leading=16,textColor=blue,spaceBefore=17,spaceAfter=9,keepWithNext=True),
 "item":ParagraphStyle("item",parent=base,fontName="Arial-Bold",fontSize=9.4,leading=13.1,spaceAfter=3),
}
def clean(s): return str(s).replace("–","-").replace("—","-").replace("‑","-")
def p(s,style="body"): return Paragraph(clean(s),styles[style])
def esc(s): return escape(clean(s))
def section(s): return p(s.upper(),"section")
def authors(s): return esc(s).replace("Jihoon Lee","<b>Jihoon Lee</b>").replace("J. Lee","<b>J. Lee</b>")
def item(title,detail,extra=None):
    content=[p(esc(title),"item"),p(detail,"small")]
    if extra: content.append(p(extra,"small"))
    content.append(Spacer(1,7))
    return KeepTogether(content)
story=[
 p("Jihoon Lee","title"),
 p("<b>Ph.D. Student · Electrical &amp; Electronic Engineering</b>"),
 p("Yonsei University · Robotic and Mobile Networks Laboratory (RAMO)","small"),
 p('Seoul, South Korea · <link href="mailto:'+d["email"]+'" color="#305ff2">'+d["email"]+"</link>","small"),
 p('<link href="https://orcid.org/'+d["orcid"]+'" color="#305ff2">ORCID '+d["orcid"]+'</link>'+((' · <link href="'+d["site_url"]+'" color="#305ff2">'+d["site_url"].replace("https://","").rstrip("/")+"</link>") if d["site_url"] else ""),"small"),
 Spacer(1,8),
 p('<b>Postdoctoral opportunities:</b> '+esc(d['postdoc_statement']),"small"),
 section("Research interests"),
 p(esc(d["intro"])),
 p("<b>Focus:</b> Semantic token communication; RAN-aware GPU sharing; AI-and-RAN systems; V2X and distributed control; position-aided beam management.","small"),
 section("Education")
]
for x in d["education"]:
    story.append(item(x["degree"],esc(x["institution"])+" · "+esc(x["period"]),esc(x["detail"])))
story.append(section("Publications"))
for i,x in enumerate(d["publications"],1):
    if i == 4:
        story += [PageBreak(),section("Publications (continued)")]
    citation=[
        p("["+str(i)+"] "+esc(x["title"]),"item"),
        p(authors(x["authors"]),"small"),
        p("<i>"+esc(x["venue"])+"</i>, "+str(x["year"])+". "+esc(x["details"])+".","small"),
    ]
    if x.get("url"):
        citation.append(p('<link href="'+escape(x["url"],quote=True)+'" color="#305ff2">'+esc(x["url"] if "doi.org" in x["url"] else "Conference paper")+"</link>","small"))
    citation.append(Spacer(1,8))
    story.append(KeepTogether(citation))
story.append(section("In preparation"))
for x in d['manuscripts']:
    if x['status']=='planned':
        story.append(item(x['title'],authors(x['authors']),'<b>'+esc(x['status_text'])+'</b>'))
story.append(section("Demonstrations"))
for x in d.get('demonstrations',[]):
    story.append(item(x['title'],authors(x['authors']),
        '<i>'+esc(x['event'])+'</i> · '+esc(x['date'])+'<br/>'+esc(x['location'])+' · <b>'+esc(x['status_text'])+'</b>'))
    story.append(p('<link href="'+d['site_url'].rstrip('/')+'/#demo-'+x['id']+'" color="#305ff2">Demo video (90 seconds, English subtitles)</link>',"small"))
story.append(section("Research projects"))
for x in d["projects"]:
    story.append(item(x["title"],esc(x["period"])+" · "+esc(x["description"])))
story += [PageBreak(),section("Domestic conferences")]
story.append(p("English translations of Korean titles.","small"))
for x in d["domestic"]:
    story.append(item(str(x["year"])+" · "+x["title"],esc(x["authors"])+" · "+esc(x["venue"])+" · "+esc(x["format"])))
story.append(section("Patents"))
story.append(p("Selected Korean patents. Titles shown in English translation.","small"))
for x in d["patents"]:
    story.append(item(x["title"],"KR "+esc(x["number"])+" · "+esc(x["status"])+" · "+esc(x["inventors"])))
story += [section("Technical skills & languages"),p(esc(", ".join(d["tools"])),"small"),p("Korean: Native · English: Fluent","small")]

def footer(canvas,doc):
    w,h=A4
    canvas.setStrokeColor(HexColor("#dce3ef"));canvas.line(45,38,w-45,38)
    canvas.setFont("Arial",8);canvas.setFillColor(muted)
    canvas.drawString(45,25,"Jihoon Lee | Academic CV")
    canvas.drawRightString(w-45,25,d["updated"]+"  /  "+str(doc.page))
    if doc.page>1:
        canvas.setFont("Arial-Bold",9);canvas.setFillColor(ink)
        canvas.drawString(45,h-30,"JIHOON LEE")

(ROOT/"assets").mkdir(exist_ok=True)
out=ROOT/"assets"/"Jihoon_Lee_CV.pdf"
doc=SimpleDocTemplate(str(out),pagesize=A4,rightMargin=45,leftMargin=45,topMargin=45,bottomMargin=51,title="Jihoon Lee - Academic CV",author="Jihoon Lee")
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print("Built assets/Jihoon_Lee_CV.pdf")
