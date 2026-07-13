# bodybalance-online.nl (Body Balance Online)

Statische site, gegenereerd met een Python-script. Geen frameworks nodig. Belicht de aanpak van Rachel Hulshof: het leefstijlprogramma Slinc en de In Shape Afslankstudio's.

## Bouwen
    python3 build.py
De site komt in `site/`.

## Deployen (Cloudflare Pages)
- Framework preset: None
- Build command: `python3 build.py`
- Build output directory: `site`

## Structuur
- Eigen huisstijl: pruim met oudroze op cremewit, Cormorant Garamond en Nunito Sans, boogvormen en zachte gradienten.
- Pagina's: home, Slinc, Afslankstudio's, Over Rachel, Video's, contact, privacy, cookies, 404.

## YouTube
- De hoofd-embed is de uploads-playlist van het kanaal (`YT_UPLOADS`), die vanzelf de laatste video's toont.
- Specifieke video's uitlichten: vul `VIDEOS` in `build.py` aan met ID's van `youtube.com/watch?v=ID`.
- Shorts embedden: vul `SHORTS` aan met ID's van `youtube.com/shorts/ID`. Zolang die leeg is, staat er een knop naar de Shorts-tab.
- Embeds gebruiken `youtube-nocookie.com` (privacyvriendelijk). Werkt een playlist-embed niet in een bepaalde omgeving, dan kan `youtube-nocookie.com` vervangen worden door `youtube.com`.

## Beeld en claims
- Bewust beeld-licht: geen stockfoto's van derden, wel elegante vormgeving en de eigen YouTube-video's als visueel middelpunt. Eigen foto's van Rachel of de studio's kunnen later in de hero of secties worden gezet.
- De teksten houden de gezondheidsclaims bewust feitelijk en gematigd, met een disclaimer dat resultaten per persoon verschillen en dit geen medisch advies is.
- Uitgaande links wijzen naar rachelhulshof.nl, inshape-afslankstudio.nl en het YouTube-kanaal.
