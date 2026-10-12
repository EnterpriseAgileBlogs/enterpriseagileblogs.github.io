# Blog Brian Teunissen (NL/EN)

Statische, tweetalige blogsite (Hugo) en de centrale plek voor alle blogs van Brian Teunissen.
Nederlands is de standaardtaal (`/nl/`), Engels staat op `/en/`. Elke blog bestaat in beide talen
en de taalknop (NL | EN) linkt altijd naar de vertaling van dezelfde pagina.

- Geen advertenties, geen trackers, geen externe fonts/scripts (Lato staat lokaal in `static/fonts/`).
- Vaste permalinks: `/nl/blog/<slug>/` en `/en/blog/<slug>/`. **Wijzig een slug nooit meer** na publicatie, anders breken gedeelde links.
- RSS per taal: `/nl/index.xml` en `/en/index.xml`.

## Lokaal bekijken

```bash
hugo server            # http://localhost:1313/nl/
hugo --minify          # bouwt de site naar ./public
```

Benodigd: Hugo extended ≥ 0.140 (getest met 0.151.0).

## Structuur

```
content/nl/blog/*.md     Nederlandse blogs
content/en/blog/*.md     Engelse blogs
content/nl/over.md       Over Brian (NL)
content/en/about.md      About Brian (EN)
static/images/blog/      Afbeeldingen in blogs
static/images/photos/    Portretfoto's / sfeerfoto's (fotoshoot 2017)
layouts/, assets/css/    Thema (eigen, Newgility-kleuren: oranje #F15A24, groen #46C646, Lato)
i18n/                    Vaste teksten per taal
tools/                   Eenmalige importscripts (WordPress/3pro-export naar Hugo)
```

## Een nieuwe blog toevoegen

1. Kies een korte, stabiele slug per taal, bijvoorbeeld `teams-van-teams` (NL) en `teams-of-teams` (EN).
2. Maak de Nederlandse versie:
   ```bash
   hugo new content/nl/blog/teams-van-teams.md
   ```
3. Maak de Engelse versie:
   ```bash
   hugo new content/en/blog/teams-of-teams.md
   ```
4. Vul de frontmatter in. **Belangrijk:** beide versies krijgen dezelfde `translationKey`, zo weet Hugo dat het
   een vertaalpaar is (en werkt de taalknop):
   ```yaml
   ---
   title: "Teams van teams"
   date: 2026-11-01T10:00:00+01:00
   slug: teams-van-teams
   translationKey: teams-van-teams
   categories: ["Scaling agile", "Agile organisatie structuur"]
   tags: []
   featured_image: /images/blog/teams.jpg   # optioneel, wordt de kaartafbeelding
   ---
   ```
   In de Engelse versie: `slug: teams-of-teams`, **dezelfde** `translationKey: teams-van-teams`, Engelse titel/categorieën.
5. Afbeeldingen zet je in `static/images/blog/` en gebruik je zo: `![Goede alt-tekst](/images/blog/teams.jpg)`.
6. Is een versie automatisch of door iemand anders vertaald? Zet dan `translated: true` in de frontmatter.
   Onderaan het bericht verschijnt dan een kleine notitie ("Vertaald uit het Engels" / "Translated from Dutch").
7. Controleer lokaal met `hugo server`, en commit daarna:
   ```bash
   git add . && git commit -m "Nieuwe blog: Teams van teams"
   ```

Een link delen met collega's: open de blog en klik op **Kopieer link**, of kopieer de URL uit de adresbalk.

## Publiceren (nog NIET actief)

De site staat nu alleen lokaal. Er is niets online gezet. Kies later één van deze twee gratis opties.

### Optie A: GitHub Pages

1. Maak een repository op GitHub, bijvoorbeeld `brianteunissen.github.io` (dan staat de site op de root van dat domein),
   of gebruik een eigen domein. *Let op:* een projectrepo zonder eigen domein (`gebruiker.github.io/repo/`) zet de site
   in een submap; de afbeeldingslinks in de blogs beginnen met `/images/...` en werken dan niet. Gebruik daarom een
   user-site of een eigen domein.
2. `git remote add origin git@github.com:<gebruiker>/<repo>.git && git push -u origin main`
3. Ga in GitHub naar *Settings → Pages → Source: GitHub Actions*. De workflow `.github/workflows/hugo.yml` staat al klaar:
   bij elke push naar `main` bouwt GitHub de site (`hugo --minify`) en publiceert hem.
4. Eigen domein (optioneel): vul het in bij *Settings → Pages → Custom domain* en zet een CNAME-record bij je DNS-provider.

### Optie B: Netlify

1. Maak een gratis account op netlify.com en kies *Add new site → Import from Git* (de GitHub-repo van hierboven).
2. Netlify leest `netlify.toml` (build command `hugo --minify`, publish directory `public`, Hugo-versie vastgezet).
3. Elke push naar `main` publiceert automatisch. Eigen domein koppel je via *Domain settings*.

Zet na de keuze van het definitieve domein ook `baseURL` in `hugo.toml` goed (bijv. `https://www.brianteunissen.nl/`),
zodat RSS, canonical-links en de sitemap kloppen.
