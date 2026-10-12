---
title: "Meten van productiviteit: Melk produceren of poepscheppen!"
date: 2014-08-27T10:20:00+01:00
slug: meten-van-productiviteit-melkproductie-of-poepscheppen
translationKey: meten-van-productiviteit-melkproductie-of-poepscheppen
categories: [Agile metrieken, Continu verbeteren, Productiviteit]
tags: []
original_url: https://newgility.eu/2014/08/27/meten-van-productiviteit-melkproductie-of-poepscheppen/
featured_image: /images/blog/cow.jpg
---

![cow.jpg](/images/blog/cow.jpg)

## Inleiding

Nee, ik ben niet afkomstig van het platteland, maar mijn voorvaders wel, en ik heb boeren in de familie. De metafoor met melkproductie heb ik al vaker gebruikt bij het uitleggen van wat ik versta onder het meten van productiviteit in een agile omgeving. Ik kom in mijn praktijk veel teams tegen die aan brandjes blussen doen. Dit is een teken dat de geleverde kwaliteit slecht is, en/of dat de technische schuld in het product hoog is. Je zou kunnen zeggen, die teams werken hard, maar zijn alle werkzaamheden die zij uitvoeren van toegevoegde waarde voor het business product? Ik denk het wel. Maar willen we nu meten of de werkzaamheden van toegevoegde waarde zijn voor het business product? Of willen we meten of het team business waarde toevoegt aan het business product? Ik pleit voor het laatste. Er zijn genoeg teams die van allerlei rand activiteiten opnemen in hun product backlog, en de realisatie daarvan beschouwen als productief. En nee, ik beledig een team niet als ik zeg: Nee, die zaken vallen wat mij betreft niet onder de productiviteit. Ze werken ongetwijfeld hard en in weekenden door om de held van een brandweerman te zijn.

## Technische schuld, slechte kwaliteit en brandjes blussen

Trend die ik zie is dat bij nagenoeg alle bedrijven de technische schuld enorm is opgelopen. Het water staat aan de lippen. Wat mij betreft in belangrijke mate veroorzaakt door de projecten matrix organisaties. Deze maken bij gebrek aan eigenaarschap van applicaties en onder druk van project managers met zwepen dat de technische schuld gestaag toeneemt in een IT landschap (geen enkele project manager ruimt de rotzooi op van zijn voorganger(s).

Gevolg is dat Scrum teams (bij voorkeur vaste product teams met eigenaarschap over een applicatie of deeldomein) geconfronteerd worden met oplossen van productie problemen en langdurige impact analyses. Dit belemmerd deze teams om tijd te besteden aan innovatie (toevoegen nieuwe features, of aanpassen van bestaande features (changes)). Indien een team niet in staat wordt gesteld om aan terugdringen van de technische schuld te doen, of om aan procesverbetering te doen, zal de trend zijn dat de productiviteit (toevoegen van business waarde in de vorm van nieuwe features of aanpassen van bestaande features) zal afnemen. Dit is weergegeven in volgende figuur:

![Figuur 1: trend zonder continu verbeteren](/images/blog/Trend-zonder.png)

*Figuur 1: trend zonder continu verbeteren*

Deze teams zullen dus steeds minder melk produceren, en meer en meer poep gaan scheppen.

## Terugdringen technische schuld en continue procesverbetering leveren op termijn een toename in productiviteit

Als je de poep maar laat opstapelen, dan zal dat ten koste gaan van de melkproductie. Middels goede coaching dienen teams aangeleerd te krijgen dat zij in elke sprint ook terugdringen technische schuld dienen te overwegen en aan procesverbetering te doen. Deze coaching strekt zich uit tot het Product Management, dat zich bewust moet worden van het feit hoe het is gesteld met de technische schuld, en wat het ze kost om die berg schuld NIET in te lossen. Hiertoe dienen zij wel concrete inzage te hebben in die technische schuld. Met SQALe als methodiek op de open source tool SONAR krijgt elk team periodiek met een druk op de knop inzage in de hersteltijd in mandagen die nog in de applicatie zit.

![Figuur 2: SCALE Dashboard](/images/blog/SCALE-dashboard.png)

*Figuur 2: SCALE Dashboard*

Voorbeeld SQALE dashboard met histogram ingedeeld op hersteltijd (remediation cost) in mandagen voor:

- Portabiliteit
- Onderhoudbaarheid
- Veiligheid
- Efficiency
- Aanpasbaarheid
- Betrouwbaarheid
- Testbaarheid

Heb je Product management en team zover dat ze de genoemde zaken meeplannen elke sprint, dan zal een tijdelijke dip in de productiviteit te zien zijn. Maar op lange termijn zal dit een bodem zijn voor structurele productiviteitsverhoging. Het eerste Toyota principe zegt: lange termijn gaat voor korte termijn. Dat geldt ook voor het creëren van een goede voedingsbodem voor het doen stijgen van je productiviteit.

Dit levert het volgende plaatje op:

![Figuur 3: Trend met continu verbeteren](/images/blog/Trend-met.png)

*Figuur 3: Trend met continu verbeteren*

Je ziet, niet alleen het wegruimen van de poep, maar ook het kijken naar de voeding van de koeien, gezondheid van de koeien, snelheid waarmee melkmachine kan worden aangesloten en afgekoppeld, Manier waarop de schuur is ingedeeld, manier waarop poep wordt geruimd, dragen bij aan de uiteindelijke toename van de melkproductie. Dat zal elke melkboer beamen. Deze manier van productiviteit meten draagt dus bij aan een potentie om te groeien enerzijds, en anderzijds geeft het inzicht in het echte toevoegen van business waarde door de teams.

## Sprint planning: 4 backlogs!

In principe leiden voor mij het verwerken van items uit 4 backlogs tot een sprint backlog.

- De Product Owner is eigenaar en houdt de backlog bij met User Stories (Toeveoegen van features, of aanpassen van bestaande features).
- De applicatie of systeem architect is eigenaar van en houdt een backlog bij met items voor technische schuld. Net zo opgebroken in kleine stories als een Product backlog, opdat de items in 1 sprint kunnen worden gerealiseerd.
- De Scrum master is eigenaar van en houdt een backlog bij met proces verbeter acties, die uit de retrospective komen, geprioriteerd door het team op basis van welke verbeter story het team als eerste het meeste rendement zal bieden.
- De Tester in het team is eigenaar van en houdt de backlog bij van openstaande productie problemen (let wel, de backlog met openstaande defects uit onderhanden werk (Stories) is er ook, maar oplossen van die defects in de sprints geldt wel als productiviteit).

Dit resulteert in de volgende visualisatie:

![Figuur 4: Input voor sprint backlog](/images/blog/backlogs.png)

*Figuur 4: Input voor sprint backlog*

Het bijhouden van de mate waarin teams per sprint aan deze soorten werkzaamheden besteden kan zeer nuttig zijn voor het leggen van verbanden tussen de mate van terugdringen technische schuld en het doen aan procesverbetering, en de toe- dan wel afname van de productiviteit. Dat geeft een Product management pas een middel om te sturen!

## Hoe stellen we de gerealiseerde productiviteit vast per sprint: de strenge manier!

Als Agile coach ben ik voorstander van een eenduidige en strenge manier van vaststellen van de productiviteit over teams heen. Het is leuk als elk team dat zelf bepaalt, en dat zullen agile puristen wellicht beamen. Maar in grote organisaties, en voor de opzet van een goede agile governance en middelen om te sturen voor product management, is standaardisatie (jaja, eng woord) op dit punt key.

Dit zijn mijn regels:

- Van een Story die de Definition of Done niet heeft gehaald, maar waar aan was begonnen in de sprint, worden de punten NOOIT meer geteld voor zowel geplande als gerealiseerde velocity. Dit maakt dat de sprint en project of release burndown de nullijn nooit meer zullen raken, maar dat geeft niet.
- Van een Story waaraan niet is begonnen in de sprint mogen de punten voor de volgende sprint weer worden geteld voor de geplande velocity. Als de betreffende Story ook wordt ingepland door de PO.

Teams die ik coach ageren altijd erg tegen deze methode van vaststellen gerealiseerde velocity. Maar het dwingt teams wel om te proberen elke sprint weer alle doelen te halen. Een team dat redeneert als een Story half af is om de helft van de punten in de af te sluiten sprint te tellen, en de andere helft in de volgende sprint, zal snel de neiging hebben het normaal te vinden dat een Story niet afkomt. Wat doe je dan wel om te borgen dat de Story in de volgende sprint afkomt? Je plant wel de resterende taken voor die Story in voor de volgende sprint. Maar dat betekent dat de geplande velocity voor die sprint wordt gedrukt, doordat minder capaciteit beschikbaar is voor nieuwe Stories. Zolang teams dus niet hun doelen halen, zal de velocity blijven schommelen en niet stabiel worden. Dat willen we ook zien, want dat geeft teams de drive om te verbeteren.

## Epiloog

Voorlopig zal het nog veel poep scheppen zijn wat de klok slaat bij de meeste bedrijven. Het besef dat er zoveel technische schuld in hun applicatie landschap zit, dat het zware sanering vereist, dringt nu pas door tot vele management teams. Aan de andere kant verschaft een agile werkwijze een middel om structureel, en stapje voor stapje, zonder big bang scenario, aan terugdringen van technische schuld te doen. Zolang er maar eigenaarschap is van de producten door teams, en zolang er maar op een goede manier wordt gemeten en inzicht gegeven. Voor mij verschaft het de komende jaren nog wel werk als Agile coach, werk dat ik met zeer veel plezier doe!
