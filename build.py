#!/usr/bin/env python3
# Generator voor bodybalance-online.nl - Body Balance Online (Rachel Hulshof, Slinc, In Shape Afslankstudio).
import os, json, html, hashlib

def _ver(relpath):
    try: return hashlib.md5(open(os.path.join(os.path.dirname(__file__),relpath),'rb').read()).hexdigest()[:8]
    except Exception: return "1"

BASE = "https://bodybalance-online.nl"
SITE = "Body Balance Online"
TAGLINE = "afvallen met Slinc"
EMAIL = "info@bodybalance-online.nl"
OUT = os.path.join(os.path.dirname(__file__), "site")
SRC = os.path.dirname(__file__)
CSS_VER = _ver("assets/css/style.css")

# YouTube-kanaal van Rachel Hulshof
YT_CHANNEL = "https://www.youtube.com/@rachelhulshof4653"
YT_SHORTS_TAB = "https://www.youtube.com/@rachelhulshof4653/shorts"
YT_UPLOADS = "UUFrfJyf0yW3hVWEBFSz_N2w"   # uploads-playlist (blijft vanzelf actueel)
# Specifieke video's om uit te lichten (ID's van youtube.com/watch?v=ID). Aanvullen kan hier.
VIDEOS = [
  {"id":"0ehpTB2QOhM", "title":"Afvallen met gezond eten met Slinc"},
  {"id":"xmGXk2Cz0m0", "title":"Afvallen met een simpel voedingsschema"},
]
# Shorts: vul aan met ID's van youtube.com/shorts/ID. Leeg = knop naar de Shorts-tab.
SHORTS = []

LINKS = {
  "rachel":"https://rachelhulshof.nl/",
  "slinc":"https://rachelhulshof.nl/afvallen-met-slinc/",
  "verhaal":"https://rachelhulshof.nl/mijn-verhaal",
  "inshape":"https://www.inshape-afslankstudio.nl/",
  "podcast":"https://rachelhulshof.nl/podcast-afvallen/",
  "youtube":YT_CHANNEL,
}

def esc(s): return html.escape(str(s), quote=True)

IC = {
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "leaf":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"/><path d="M2 21c0-3 1.85-5.36 5.08-6"/></svg>',
 "apple":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 7c0-3 2-5 5-5 0 2.5-2 5-5 5z"/><path d="M12 7c-1.5-2-4-3-6-2-2.5 1.3-3 5-1.5 8.5C6 17 8 21 12 21s6-4 7.5-7.5C21 10 20.5 6.3 18 5c-2-1-4.5 0-6 2z"/></svg>',
 "heart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.29 1.51 4.04 3 5.5l7 7Z"/></svg>',
 "users":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></svg>',
 "scale":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v3"/><path d="M5 6h14l2 12a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 6a3 3 0 0 0 6 0"/></svg>',
 "sun":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
 "spark":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/></svg>',
 "play":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>',
 "pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "menu":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
}
SPRIG='<svg class="sprig" viewBox="0 0 48 48" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round"><path d="M24 42V16"/><path d="M24 22c-4 0-7-2-8-6 4 0 7 2 8 6z"/><path d="M24 22c4 0 7-2 8-6-4 0-7 2-8 6z"/><path d="M24 30c-3.5 0-6-2-7-5 3.5 0 6 2 7 5z"/><path d="M24 30c3.5 0 6-2 7-5-3.5 0-6 2-7 5z"/></svg>'

NAV = [("Home","/"),("Slinc","/slinc/"),("Afslankstudio's","/afslankstudios/"),("Over Rachel","/over-rachel/"),("Video's","/videos/"),("Partners","/partners/"),("Contact","/contact/")]

def yt_video(vid):
    return f'<div class="video16"><iframe src="https://www.youtube-nocookie.com/embed/{vid}" title="Video van Rachel Hulshof op YouTube" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>'

def yt_playlist(listid):
    return f'<div class="video16"><iframe src="https://www.youtube-nocookie.com/embed/videoseries?list={listid}" title="Video\'s van Rachel Hulshof op YouTube" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>'

def yt_short(vid):
    return f'<div class="video9"><iframe src="https://www.youtube-nocookie.com/embed/{vid}" title="Short van Rachel Hulshof op YouTube" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>'

def head(title, desc, path, ld=None):
    can = BASE + path
    j = "".join('<script type="application/ld+json">'+json.dumps(b, ensure_ascii=False)+'</script>' for b in (ld or []))
    nav = "".join(f'<a class="navlink" href="{href}">{esc(label)}</a>' for label,href in NAV)
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{esc(SITE)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{can}">
<meta name="theme-color" content="#8E3B5E">
<link rel="icon" href="/assets/icons/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Nunito+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_VER}">
{j}
</head>
<body>
<header class="site-head">
  <nav class="nav" id="nav">
    <a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Body Balance</b><span>Online</span></span></a>
    {nav}
    <a class="btn btn-rose" href="/slinc/">Ontdek Slinc</a>
    <button class="menu-toggle" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('open')">{IC['menu']}</button>
  </nav>
</header>
"""

def footer():
    return f"""<footer class="foot">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="brand" href="/" style="color:#fff"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Body Balance</b><span style="color:#A695A0">Online</span></span></a>
        <p class="note">Body Balance Online belicht de aanpak van afslank- en voedingscoach Rachel Hulshof: het leefstijlprogramma Slinc en de In Shape Afslankstudio's. Een informatieve wegwijzer naar afvallen met gezond eten en in balans blijven.</p>
        <p class="note">Resultaten verschillen per persoon. Deze site geeft algemene informatie en is geen medisch of voedingskundig advies.</p>
      </div>
      <div>
        <h4>Ontdekken</h4>
        <a href="/slinc/">Het Slinc programma</a>
        <a href="/afslankstudios/">In Shape Afslankstudio's</a>
        <a href="/over-rachel/">Over Rachel Hulshof</a>
        <a href="/videos/">Video's en shorts</a>
      </div>
      <div>
        <h4>Meer</h4>
        <a href="{LINKS['rachel']}" target="_blank" rel="noopener">rachelhulshof.nl</a>
        <a href="{LINKS['youtube']}" target="_blank" rel="noopener">YouTube-kanaal</a>
        <a href="/contact/">Contact</a>
        <a href="/privacybeleid/">Privacybeleid</a>
        <a href="/cookiebeleid/">Cookiebeleid</a>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; 2026 {esc(SITE)}</span>
      <span><a href="/contact/">Contact</a> &middot; <a href="/privacybeleid/">Privacy</a> &middot; <a href="/cookiebeleid/">Cookies</a></span>
    </div>
  </div>
</footer>
</body>
</html>"""

def breadcrumb(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate(items)]}

def crumbs_html(items):
    out=[f'<a href="{u}">{esc(n)}</a>' for n,u in items[:-1]]
    out.append(f'<span>{esc(items[-1][0])}</span>')
    return '<div class="wrap"><nav class="crumbs">'+' / '.join(out)+'</nav></div>'

def write(path, content):
    full = os.path.join(OUT, "index.html") if path=="/" else os.path.join(OUT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full,"w",encoding="utf-8").write(content)

def page_home():
    path="/"; crumbs=[("Home","/")]
    ld=[
      {"@context":"https://schema.org","@type":"WebSite","@id":BASE+"/#website","url":BASE+"/","name":SITE,"inLanguage":"nl-NL","description":"Body Balance Online belicht de aanpak van Rachel Hulshof: het leefstijlprogramma Slinc en de In Shape Afslankstudio's."},
      {"@context":"https://schema.org","@type":"Person","@id":BASE+"/#rachel","name":"Rachel Hulshof","jobTitle":"Afslank- en voedingscoach","url":LINKS["rachel"],"sameAs":[LINKS["youtube"],LINKS["rachel"]]},
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":"Wat is Slinc?","acceptedAnswer":{"@type":"Answer","text":"Slinc is een leefstijlprogramma in drie fasen: afslanken, stabiliseren en balans. Het draait om normaal eten uit de supermarkt, een vast eetritme met meerdere eetmomenten per dag en ondersteuning met plantaardige voedingssupplementen. Het programma is opgericht door Rachel Hulshof."}},
        {"@type":"Question","name":"Kan Slinc online gevolgd worden?","acceptedAnswer":{"@type":"Answer","text":"Ja. Slinc is zelfstandig vanuit huis te volgen. Voor persoonlijke begeleiding zijn er daarnaast de In Shape Afslankstudio's in Brabant."}},
        {"@type":"Question","name":"Voor wie is de aanpak bedoeld?","acceptedAnswer":{"@type":"Answer","text":"De begeleiding richt zich vooral op vrouwen die willen afvallen en op gewicht willen blijven, in elke levensfase. Resultaten verschillen per persoon."}},
      ]},
      breadcrumb(crumbs),
    ]
    aanpak=[("apple","Gezonde voeding","Normaal eten uit de supermarkt, verdeeld over meerdere eetmomenten per dag. Geen maaltijdvervangers of shakes, maar een vast eetritme met koolhydraten, eiwitten en vetten."),
            ("sun","Beweging","Thuis met dagelijkse beweging, of in de studio met trainingen in warmte- en vacuümcabines. Bewegen hoort bij de aanpak, naast de voeding."),
            ("users","Persoonlijke begeleiding","In de studio wordt wekelijks gewogen en gemeten, met coaching op maat. Online biedt Slinc houvast met een duidelijk schema en recepten.")]
    aanpak_html="".join(f'<div class="card"><div class="ic">{IC[i]}</div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i,t,d in aanpak)
    fases=[("1","Afslanken","Fase 1 richt zich op afvallen met gezonde voeding en een vast eetritme, ondersteund door plantaardige voedingssupplementen."),
           ("2","Stabiliseren","Fase 2 helpt het bereikte gewicht vast te houden, met een stapsgewijze overgang naar volwaardiger eten en ruimte voor af en toe iets lekkers."),
           ("3","Balans","Fase 3 draait om een blijvende, gezonde leefstijl en een stabiel gewicht, gericht op het tegengaan van het jojo-effect.")]
    fases_html="".join(f'<div class="phasecard"><div class="num">{n}</div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for n,t,d in fases)
    h=head("Body Balance Online | afvallen met Slinc en in balans blijven",
      "Body Balance Online belicht de aanpak van afslank- en voedingscoach Rachel Hulshof: het leefstijlprogramma Slinc en de In Shape Afslankstudio's. Gezond eten en blijvend resultaat.",path,ld)
    h+=f"""<section class="hero">
  <div class="wrap hero-inner">
    <div>
      <span class="eyebrow">{IC['leaf']}Online afvallen met Slinc</span>
      <h1>Afvallen met gezond eten en in <em>balans</em> blijven</h1>
      <p class="lead">Body Balance Online bundelt de aanpak van afslank- en voedingscoach Rachel Hulshof: het leefstijlprogramma Slinc en de In Shape Afslankstudio's. Gezond eten, een vast eetritme en persoonlijke begeleiding, gericht op een blijvend resultaat.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="/slinc/">Ontdek het Slinc programma {IC['arrow']}</a>
        <a class="btn btn-ghost" href="/videos/">Bekijk de video's</a>
      </div>
      <div class="hero-meta">
        <span>{IC['check']}3-fasen programma</span>
        <span>{IC['check']}Online of in de studio</span>
        <span>{IC['check']}Al bijna 20 jaar ervaring</span>
      </div>
    </div>
    <div class="hero-art">
      <div class="arch"><div class="arch-in">{SPRIG}<span class="k">Slinc</span><span class="s">Gezond afvallen</span></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['spark']}De aanpak</span>
      <h2>Voeding, beweging en begeleiding</h2>
      <p class="lead">De methode van Rachel Hulshof combineert drie elementen. Samen vormen ze de basis voor een gezond gewicht dat vol te houden is.</p>
    </div>
    <div class="grid cols-3">{aanpak_html}</div>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['leaf']}Het programma</span>
      <h2>Slinc in drie fasen</h2>
      <p class="lead">Slinc is een leefstijlprogramma dat in drie fasen toewerkt naar een blijvend en gezond gewicht.</p>
    </div>
    <div class="phase">{fases_html}</div>
    <p style="margin-top:24px"><a class="more" href="/slinc/">Meer over het Slinc programma {IC['arrow']}</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid cols-2" style="align-items:center;gap:44px">
      <div>
        <span class="eyebrow">{IC['pin']}In Shape Afslankstudio</span>
        <h2>Persoonlijke begeleiding in de studio</h2>
        <p class="lead">Naast het online programma zijn er de In Shape Afslankstudio's: kleinschalige studio's speciaal voor vrouwen, met vijf vestigingen in Brabant. De aanpak combineert Slinc met beweging in warmte- en vacuümcabines en wekelijkse begeleiding.</p>
        <p><a class="more" href="/afslankstudios/">Bekijk de studio's {IC['arrow']}</a></p>
      </div>
      <div>
        <ul class="ticks">
          <li>{IC['check']}<span>Studio's in Eindhoven, Veldhoven, Helmond, Rosmalen en Valkenswaard.</span></li>
          <li>{IC['check']}<span>Alleen voor vrouwen, in een kleinschalige en persoonlijke setting.</span></li>
          <li>{IC['check']}<span>Wekelijks wegen en meten, met coaching op voeding en beweging.</span></li>
          <li>{IC['check']}<span>In 2018 uitgeroepen tot beste Afslankstudio.</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    <div class="grid cols-2" style="align-items:center;gap:44px">
      <div class="hero-art" style="min-height:0">
        <div class="arch" style="max-width:300px"><div class="arch-in">{SPRIG}<span class="k">19 kg</span><span class="s">Ervaringsdeskundige</span></div></div>
      </div>
      <div>
        <span class="eyebrow">{IC['heart']}Over Rachel</span>
        <h2>Van eigen strijd naar een eigen methode</h2>
        <p class="lead">Rachel Hulshof viel zelf 19 kilo af en is sindsdien op gewicht gebleven. Die ervaring werd de basis voor Slinc en de In Shape Afslankstudio's. Al bijna twintig jaar begeleidt ze vrouwen bij afvallen en op gewicht blijven.</p>
        <p><a class="more" href="/over-rachel/">Lees het verhaal van Rachel {IC['arrow']}</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">{IC['play']}Op video</span>
      <h2>Tips en verhalen van Rachel</h2>
      <p class="lead">Op haar YouTube-kanaal deelt Rachel praktische tips, video-podcasts en verhalen over afvallen met gezond eten.</p>
    </div>
    {yt_video(VIDEOS[0]["id"])}
    <p style="text-align:center;margin-top:24px"><a class="btn btn-ghost" href="/videos/">Naar alle video's en shorts {IC['arrow']}</a></p>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <div class="cta-band">
      <h2>Klaar voor de eerste stap?</h2>
      <p>Ontdek hoe Slinc werkt en welke aanpak past. Een gratis en vrijblijvend adviesgesprek is zo geregeld via Rachel Hulshof.</p>
      <a class="btn btn-rose" style="background:#fff;color:var(--plum);border-color:#fff" href="{LINKS['slinc']}" target="_blank" rel="noopener">Ontdek Slinc op rachelhulshof.nl {IC['arrow']}</a>
    </div>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_slinc():
    path="/slinc/"; crumbs=[("Home","/"),("Slinc",path)]
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":"Slinc: afvallen met gezond eten in drie fasen","inLanguage":"nl-NL","author":{"@type":"Person","name":"Rachel Hulshof"},"publisher":{"@type":"Organization","name":SITE}},breadcrumb(crumbs)]
    fases=[("1","Afslanken","Fase 1 richt zich op afvallen met gezonde voeding en een vast eetritme, ondersteund door plantaardige voedingssupplementen. Het eetschema is elke dag hetzelfde van opzet, maar de keuze wat er op tafel komt, blijft vrij."),
           ("2","Stabiliseren","Fase 2 helpt het bereikte gewicht vast te houden. De voeding wordt stapsgewijs volwaardiger, met een overstap naar volkoren en volle producten en ruimte voor af en toe iets lekkers."),
           ("3","Balans","Fase 3 draait om een blijvende, gezonde leefstijl en een stabiel gewicht. Het doel is om het jojo-effect tegen te gaan en de balans in eten vast te houden.")]
    fases_html="".join(f'<div class="phasecard"><div class="num">{n}</div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for n,t,d in fases)
    h=head("Slinc: afvallen met gezond eten in drie fasen | "+SITE,
      "Slinc is het leefstijlprogramma van Rachel Hulshof: afvallen met normaal eten, een vast eetritme en drie fasen, afslanken, stabiliseren en balans. Online of in de studio.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap prose">
    <span class="eyebrow">{IC['leaf']}Het programma</span>
    <h1>Slinc: afvallen met gezond eten</h1>
    <p class="lead">Slinc is een leefstijlprogramma dat draait om normaal en voedzaam eten, in plaats van streng lijnen of maaltijdvervangers. Het is opgericht door afslank- en voedingscoach Rachel Hulshof en werkt toe naar een blijvend gezond gewicht.</p>
    <h2>Normaal eten, in een vast ritme</h2>
    <p>Bij Slinc komt het eten gewoon uit de supermarkt. Het idee is om verspreid over de dag meerdere keren voedzaam te eten, met koolhydraten, eiwitten en vetten. Een vast eetritme met meerdere eetmomenten helpt de bloedsuikerspiegel stabiel te houden. In de avond kan er gewoon met het gezin worden meegegeten, aan de hand van recepten die voor het hele gezin geschikt zijn.</p>
    <p>Plantaardige voedingssupplementen ondersteunen het programma. Ze zijn een aanvulling op de voeding, geen vervanging ervan.</p>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{IC['spark']}Drie fasen</span><h2>Van afslanken naar balans</h2></div>
    <div class="phase">{fases_html}</div>
  </div>
</section>

<section class="section">
  <div class="wrap prose">
    <h2>Online of in de studio</h2>
    <p>Slinc is zelfstandig vanuit huis te volgen. Wie meer houvast en persoonlijke begeleiding wil, kan terecht bij de In Shape Afslankstudio's in Brabant, waar Slinc wordt gecombineerd met beweging en wekelijkse begeleiding.</p>
    <div class="callout">
      <p><strong>Eerst kennismaken.</strong> Bij Rachel Hulshof kan een gratis en vrijblijvend adviesgesprek worden aangevraagd om te kijken welke aanpak past.</p>
    </div>
    <p class="disclaimer">Slinc is een voedings- en leefstijlprogramma. Het is geen medische behandeling en resultaten verschillen per persoon. Bij twijfel of bij gezondheidsklachten is overleg met een huisarts of diëtist verstandig.</p>
    <p style="margin-top:18px"><a class="btn btn-primary" href="{LINKS['slinc']}" target="_blank" rel="noopener">Ontdek Slinc op rachelhulshof.nl {IC['arrow']}</a> <a class="btn btn-ghost" href="/afslankstudios/">Naar de studio's</a></p>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_studios():
    path="/afslankstudios/"; crumbs=[("Home","/"),("In Shape Afslankstudio's",path)]
    studios=[("Eindhoven","Twee studio's, in Blixembosch en in het centrum. De eerste In Shape opende hier in 2006."),
             ("Veldhoven","De studio in Meerhoven, met een centrale ligging voor vrouwen uit Veldhoven en omgeving."),
             ("Helmond","Een studio speciaal voor vrouwen die onder begeleiding willen afvallen met Slinc en beweging."),
             ("Rosmalen","Afvallen met Slinc en beweging onder persoonlijke begeleiding van de coach en haar team."),
             ("Valkenswaard","Centraal in het dorp, met Slinc, sporten en coaching voor vrouwen uit de buurt.")]
    tiles="".join(f'<div class="tile"><h3>{esc(n)}</h3><p>{esc(d)}</p></div>' for n,d in studios)
    ld=[{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":"In Shape Afslankstudio's","inLanguage":"nl-NL"},
        {"@context":"https://schema.org","@type":"ItemList","name":"In Shape Afslankstudio's in Brabant","itemListElement":[{"@type":"ListItem","position":i+1,"name":"In Shape Afslankstudio "+n} for i,(n,d) in enumerate(studios)]},
        breadcrumb(crumbs)]
    h=head("In Shape Afslankstudio's | vijf studio's in Brabant | "+SITE,
      "In Shape Afslankstudio, opgericht door Rachel Hulshof, telt vijf vestigingen in Brabant. Kleinschalige studio's voor vrouwen, met Slinc, beweging en persoonlijke begeleiding.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['pin']}In Shape Afslankstudio</span>
      <h1>Persoonlijke begeleiding in de studio</h1>
      <p class="lead">In Shape Afslankstudio is opgericht door Rachel Hulshof en is uitgegroeid tot vijf kleinschalige studio's in Brabant, speciaal voor vrouwen. De aanpak combineert het Slinc programma met beweging en wekelijkse begeleiding.</p>
    </div>
    <div class="tiles">{tiles}</div>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    <div class="grid cols-3">
      <div class="card"><div class="ic">{IC['apple']}</div><h3>Voeding met Slinc</h3><p>De basis is het Slinc programma: normaal eten in een vast ritme, met persoonlijke voedingsbegeleiding.</p></div>
      <div class="card"><div class="ic">{IC['sun']}</div><h3>Beweging in cabines</h3><p>Trainingen in warmte- en vacuümcabines, gericht op bewegen en inspanning tijdens de sessie.</p></div>
      <div class="card"><div class="ic">{IC['scale']}</div><h3>Wegen en meten</h3><p>Wekelijks wegen en periodiek meten van omvang, zodat de voortgang zichtbaar blijft en het programma kan worden bijgesteld.</p></div>
    </div>
    <div class="callout" style="margin-top:26px"><p><strong>Alleen voor vrouwen.</strong> De studio's zijn kleinschalig en persoonlijk. In 2018 werd In Shape uitgeroepen tot beste Afslankstudio.</p></div>
    <p style="margin-top:22px"><a class="btn btn-primary" href="{LINKS['inshape']}" target="_blank" rel="noopener">Naar inshape-afslankstudio.nl {IC['arrow']}</a></p>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_rachel():
    path="/over-rachel/"; crumbs=[("Home","/"),("Over Rachel",path)]
    ld=[{"@context":"https://schema.org","@type":"Person","@id":BASE+"/#rachel","name":"Rachel Hulshof","jobTitle":"Afslank- en voedingscoach","url":LINKS["rachel"],"sameAs":[LINKS["youtube"]]},
        {"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":"Over Rachel Hulshof","inLanguage":"nl-NL"},breadcrumb(crumbs)]
    h=head("Over Rachel Hulshof | afslank- en voedingscoach | "+SITE,
      "Rachel Hulshof viel zelf 19 kilo af en maakte daar haar vak van. Oprichtster van Slinc en de In Shape Afslankstudio's, en al bijna twintig jaar coach voor vrouwen.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap prose">
    <span class="eyebrow">{IC['heart']}Over Rachel</span>
    <h1>Het verhaal van Rachel Hulshof</h1>
    <p class="lead">Rachel Hulshof is afslank- en voedingscoach en vooral ook ervaringsdeskundige. Haar eigen strijd met eten werd de basis voor een methode die inmiddels bijna twintig jaar vrouwen begeleidt.</p>
    <h2>Van eigen strijd naar een methode</h2>
    <p>Rachel was naar eigen zeggen altijd net iets te zwaar, van kind tot jonge vrouw, met een overgewicht dat rond de vijftien kilo bleef schommelen. Diverse dieetclubjes en pogingen op eigen kracht hielpen niet blijvend. Uiteindelijk verdiepte ze zich in voeding en goot ze die kennis in een uitgewerkt programma.</p>
    <p>Op haar achtentwintigste was ze vijftien kilo lichter. Dat programma introduceerde ze eerst in haar eigen studio en later op de Nederlandse markt als Slinc. In totaal viel ze negentien kilo af en sinds 2006 is ze op gewicht gebleven.</p>
    <h2>Slinc en In Shape</h2>
    <p>In 2006 opende Rachel haar eerste In Shape Afslankstudio in Eindhoven. Die groeide uit tot vijf studio's in Brabant. Daarnaast staat Slinc, het leefstijlprogramma in drie fasen, dat zowel in de studio als online wordt gevolgd.</p>
    <h2>Kennis delen</h2>
    <p>Via haar podcast en YouTube-kanaal deelt Rachel praktische tips, recepten en persoonlijke verhalen over afvallen met gezond eten en op gewicht blijven. Haar doel is om vrouwen te motiveren om een aanpak te vinden die bij hen past.</p>
    <p style="margin-top:18px"><a class="btn btn-primary" href="/videos/">Bekijk de video's {IC['arrow']}</a> <a class="btn btn-ghost" href="{LINKS['podcast']}" target="_blank" rel="noopener">Naar de podcast</a></p>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_videos():
    path="/videos/"; crumbs=[("Home","/"),("Video's",path)]
    ld=[{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":"Video's en shorts van Rachel Hulshof","inLanguage":"nl-NL"},breadcrumb(crumbs)]
    featured="".join(f'<div>{yt_video(v["id"])}<p style="margin-top:10px;font-weight:700">{esc(v["title"])}</p></div>' for v in VIDEOS[1:])
    featured_block=(f'<h2 style="margin-top:44px">Meer video\'s</h2><div class="grid cols-2">{featured}</div>' if featured else "")
    if SHORTS:
        shorts_block=f'<div class="shorts">'+"".join(yt_short(s["id"]) for s in SHORTS)+'</div>'
    else:
        shorts_block=f'''<div class="callout"><p><strong>Shorts.</strong> Korte video's met tips staan als Shorts op het YouTube-kanaal.</p><p style="margin:10px 0 0"><a class="btn btn-ghost" href="{YT_SHORTS_TAB}" target="_blank" rel="noopener">Bekijk de Shorts op YouTube {IC['arrow']}</a></p></div>'''
    h=head("Video's en shorts | Rachel Hulshof op YouTube | "+SITE,
      "Video's, video-podcasts en shorts van afslankcoach Rachel Hulshof over afvallen met gezond eten, recepten en op gewicht blijven met Slinc.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['play']}Video's</span>
      <h1>Video's van Rachel Hulshof</h1>
      <p class="lead">Op haar YouTube-kanaal deelt Rachel praktische tips, video-podcasts, recepten en verhalen over afvallen met gezond eten. Hieronder een greep uit de video's. Het volledige en actuele aanbod staat op het kanaal zelf.</p>
    </div>
    {yt_video(VIDEOS[0]["id"])}
    <p style="margin-top:12px;font-weight:700">{esc(VIDEOS[0]["title"])}</p>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    {featured_block}
    <h2 style="margin-top:44px">Shorts</h2>
    {shorts_block}
    <p style="margin-top:24px"><a class="btn btn-primary" href="{LINKS['youtube']}" target="_blank" rel="noopener">Naar het YouTube-kanaal {IC['arrow']}</a> <a class="btn btn-ghost" href="{LINKS['podcast']}" target="_blank" rel="noopener">Beluister de podcast</a></p>
  </div>
</section>"""
    h+=footer(); write(path,h)


def page_partners():
    path="/partners/"; crumbs=[("Home","/"),("Partners",path)]
    ld=[breadcrumb(crumbs),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":"Partners","inLanguage":"nl-NL"}]
    h=head("Partners | "+SITE,"Bronnen en linkpartners waar Body Balance Online naar verwijst.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap prose">
    <span class="eyebrow">{IC['leaf']}Partners</span>
    <h1>Partners en bronnen</h1>
    <p class="lead">Body Balance Online verwijst hier naar externe partners en bronnen.</p>
    <div class="grid cols-2" style="margin-top:14px">
      <div class="card"><h3>Tatanka</h3><p style="margin-bottom:14px">Tatanka is een Nederlandse smartshop met paddo growkits en smartshopproducten, met uitleg per soort en een overzicht van het aanbod.</p><a class="more" href="https://www.tatanka.nl/nl/shroomshop/magic-mushroom-grow-kits/" target="_blank" rel="noopener">Paddo mushroom growkit {IC['arrow']}</a></div>
      <div class="card"><h3>Smartific</h3><p style="margin-bottom:14px">Smartific is een Nederlandse smartshop met magic truffels, growkits en smartshopproducten, inclusief productinformatie per artikel.</p><a class="more" href="https://smartific.nl/joint-roller/" target="_blank" rel="noopener">Joint roller kopen {IC['arrow']}</a></div>
      <div class="card"><h3>The Headshop</h3><p style="margin-bottom:14px">The Headshop is een Nederlandse headshop met kratom en smartshopproducten, met een uitgebreid overzicht per soort en sterkte.</p><a class="more" href="https://www.headshop.nl/nl/super-bali-gold-kratom/" target="_blank" rel="noopener">Super Bali Gold Kratom {IC['arrow']}</a></div>
      <div class="card"><h3>Paddo.shop</h3><p style="margin-bottom:14px">Paddo.shop is een Nederlandse webshop gespecialiseerd in paddo growkits, met uitleg per kweekset en kweekinstructies.</p><a class="more" href="https://www.paddo.shop/mexican-paddo-growkit/" target="_blank" rel="noopener">Mexican paddo {IC['arrow']}</a></div>
      <div class="card"><h3>Magictruffels.shop</h3><p style="margin-bottom:14px">Magictruffels.shop is een Nederlandse webshop voor magic truffels, met een overzicht per soort en de werking ervan.</p><a class="more" href="https://www.magictruffels.shop/" target="_blank" rel="noopener">mushrocks truffels {IC['arrow']}</a></div>
      
    </div>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_contact():
    path="/contact/"; crumbs=[("Home","/"),("Contact",path)]
    ld=[breadcrumb(crumbs),{"@context":"https://schema.org","@type":"ContactPage","@id":BASE+path,"url":BASE+path,"name":"Contact","inLanguage":"nl-NL"}]
    h=head("Contact | "+SITE,"Meer weten over Slinc, de In Shape Afslankstudio's of een adviesgesprek met Rachel Hulshof? Hier staan de directe wegen.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap prose">
    <span class="eyebrow">{IC['mail']}Contact</span>
    <h1>Meer weten</h1>
    <p class="lead">Body Balance Online is een informatieve wegwijzer. Voor het programma, een adviesgesprek of een studio in de buurt gaan de directe wegen via Rachel Hulshof en In Shape.</p>
    <div class="grid cols-2" style="margin-top:14px">
      <div class="card"><div class="ic">{IC['leaf']}</div><h3>Slinc en Rachel</h3><p style="margin-bottom:14px">Het programma, recepten en een gratis adviesgesprek.</p><a class="more" href="{LINKS['rachel']}" target="_blank" rel="noopener">rachelhulshof.nl {IC['arrow']}</a></div>
      <div class="card"><div class="ic">{IC['pin']}</div><h3>In Shape Afslankstudio</h3><p style="margin-bottom:14px">De vijf studio's in Brabant en de mogelijkheden ter plekke.</p><a class="more" href="{LINKS['inshape']}" target="_blank" rel="noopener">inshape-afslankstudio.nl {IC['arrow']}</a></div>
      <div class="card"><div class="ic">{IC['play']}</div><h3>YouTube</h3><p style="margin-bottom:14px">Video's, video-podcasts en shorts met tips.</p><a class="more" href="{LINKS['youtube']}" target="_blank" rel="noopener">Het kanaal {IC['arrow']}</a></div>
      <div class="card"><div class="ic">{IC['mail']}</div><h3>Deze site</h3><p style="margin-bottom:14px">Vragen over Body Balance Online zelf.</p><a class="more" href="mailto:{EMAIL}">{EMAIL}</a></div>
    </div>
  </div>
</section>"""
    h+=footer(); write(path,h)

def legal_page(path, title, blocks):
    crumbs=[("Home","/"),(title,path)]
    ld=[breadcrumb(crumbs),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":title,"inLanguage":"nl-NL"}]
    h=head(f"{title} | {SITE}", f"{title} van {SITE}.", path, ld)
    h+=crumbs_html(crumbs)
    h+=f'<section class="section"><div class="wrap prose"><h1>{esc(title)}</h1>{"".join(blocks)}</div></section>'
    h+=footer(); write(path,h)

def privacy():
    legal_page("/privacybeleid/","Privacybeleid",[
      "<p>Body Balance Online is een informatieve website over de aanpak van Rachel Hulshof, Slinc en de In Shape Afslankstudio's. De site verwerkt zo min mogelijk persoonsgegevens.</p>",
      "<h2>Welke gegevens</h2><p>Er is geen contactformulier. Wie via een e-mailadres of een externe link contact opneemt, deelt gegevens rechtstreeks met de betreffende partij, niet met deze site.</p>",
      "<h2>Externe video's</h2><p>Op de site staan ingesloten video's van YouTube. Bij het afspelen daarvan verwerkt YouTube gegevens volgens het eigen privacybeleid. De embeds gebruiken de privacyvriendelijke variant van YouTube.</p>",
      "<h2>Vragen</h2><p>Vragen over privacy kunnen per e-mail gesteld worden via "+EMAIL+".</p>",
    ])

def cookies():
    legal_page("/cookiebeleid/","Cookiebeleid",[
      "<p>Deze site plaatst zelf zo min mogelijk cookies en gebruikt geen advertentiecookies.</p>",
      "<h2>Functioneel</h2><p>Functionele cookies zorgen dat de site goed werkt en zijn noodzakelijk.</p>",
      "<h2>YouTube-video's</h2><p>De video's en shorts op de site worden ingesloten via YouTube. Zodra een video wordt afgespeeld, kan YouTube cookies plaatsen. De embeds gebruiken de variant youtube-nocookie, die pas bij het afspelen gegevens laadt. Wie dit wil voorkomen, speelt de video's niet af of blokkeert cookies in de browser.</p>",
      "<h2>Vragen</h2><p>Vragen over cookies kunnen per e-mail gesteld worden via "+EMAIL+".</p>",
    ])

def not_found():
    h=head("Pagina niet gevonden | "+SITE,"De opgevraagde pagina bestaat niet.","/404.html",None)
    h+=f"""<section class="section"><div class="wrap prose" style="text-align:center">
      <span class="eyebrow" style="justify-content:center">404</span>
      <h1>Deze pagina bestaat niet</h1>
      <p class="lead">Mogelijk is de link verouderd. Terug naar de startpagina of ontdek het Slinc programma.</p>
      <p><a class="btn btn-primary" href="/">Naar de homepage {IC['arrow']}</a> <a class="btn btn-ghost" href="/slinc/">Ontdek Slinc</a></p>
    </div></section>"""
    h+=footer()
    open(os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(h)

def extras():
    urls=["/","/slinc/","/afslankstudios/","/over-rachel/","/videos/","/partners/","/contact/","/privacybeleid/","/cookiebeleid/"]
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{u}</loc></url>\n" for u in urls)+"</urlset>\n"
    open(os.path.join(OUT,"sitemap.xml"),"w").write(sm)
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT,"_headers"),"w").write("/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    open(os.path.join(OUT,"_redirects"),"w").write("https://www.bodybalance-online.nl/* https://bodybalance-online.nl/:splat 301!\n")

def copy_assets():
    import shutil
    dst=os.path.join(OUT,"assets")
    if os.path.exists(dst): shutil.rmtree(dst)
    shutil.copytree(os.path.join(SRC,"assets"), dst)

def main():
    import shutil
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT, exist_ok=True)
    copy_assets()
    page_home(); page_slinc(); page_studios(); page_rachel(); page_videos()
    page_partners()
    page_contact(); privacy(); cookies(); not_found(); extras()
    print("Build klaar in", OUT)

if __name__=="__main__":
    main()
