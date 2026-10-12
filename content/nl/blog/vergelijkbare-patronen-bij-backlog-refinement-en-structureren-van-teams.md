---
title: "Vergelijkbare patronen bij backlog refinement en structureren van teams"
date: 2018-01-14T11:47:00+01:00
slug: vergelijkbare-patronen-bij-backlog-refinement-en-structureren-van-teams
translationKey: vergelijkbare-patronen-bij-backlog-refinement-en-structureren-van-teams
categories: [Agile organisatie structuur, Agile requirements, Enterprise agility, Product oriëntatie, Scaling agile, Waardestromen, Wendbaarheid]
tags: []
original_url: https://newgility.eu/2018/01/14/vergelijkbare-patronen-bij-backlog-refinement-en-structureren-van-teams/
featured_image: /images/blog/wordcloud-engineering.jpg
---

![wordcloud-engineering.jpg](/images/blog/wordcloud-engineering.jpg)

'Van denken in oplossingen naar denken in klantwensen' en ‘Van denken in indeling IT landschap naar denken in waardestromen’

## **Introductie**

Telkens als ik in contact kom met nieuwe teams en nieuwe organisaties die gewend zijn om te werken op de traditionele manier, kom ik ook moeilijk te doorbreken gewoonten tegen. Mensen in de IT zijn gewend om te werken in een bepaalde modus en structuur voor zo vele jaren, dat het heel moeilijk is geworden om de paradigmaverschuivingen te ondergaan die nodig zijn om agile te worden als een organisatie, laat staan team. In een eerdere blog heb ik al een aantal paradigma-verschuivingen opgesomd ([/nl/blog/paradigma-verschuivingen-bij-scaling-agile/](/nl/blog/paradigma-verschuivingen-bij-scaling-agile/)), en hier heb ik het over slechts twee van die  paradigma-verschuivingen: 'van denken in oplossingen naar denken in klantwensen' en ‘Van denken in indeling IT landschap naar denken in waardestromen’

## **Scrum**

Natuurlijk lijkt het gemakkelijk om een team te hebben dat is opgeleid in Scrum en dan te beginnen. Bij voorkeur onder begeleiding van een ervaren coach. Scrum lijkt gemakkelijk om toe te passen, maar als je een geschiedenis van traditioneel werken hebt, is er veel meer discipline en verandering noodzakelijk dan je zou verwachten. Dat geldt voor teamleden zowel als hun management.

## **Backlog refinement en denken in bedrijfswaarde**

Een van de meest onderschatte zaken die ik tegenkom, vooral bij architecten en engineers, is denken in bedrijfswaarde. Denken in bedrijfswaarde betekent dat je de effectiviteit van het geheel laat prevaleren óver de efficiëntie van de onderdelen. Wat ik hiermee bedoel is dat architecten en ingenieurs gewend zijn om in technische componenten te denken. Technische componenten maken deel uit van de OPLOSSING en vertegenwoordigen niet noodzakelijkerwijs bedrijfswaarde. In feite doen ze dat meestal niet. Architecten en ingenieurs denken: 'Als ik deze code aan het bewerken ben, kan ik net zo goed de code bewerken voor de volgende User Story, omdat deze in hetzelfde onderdeel zit. Waarom zou ik deze Story bouwen en implementeren, als ik dezelfde code opnieuw moet inchecken voor de volgende Story?'. Dit is denken in efficiëntie, niet in effectiviteit. Als we dit op een eenvoudige  manier visualiseren,  ziet het er als volgt uit:

![req1.png](/images/blog/req1.png)

![Figuur 1 en 2: Componenten binnen 1 applicatie met aanpassingen per component](/images/blog/req2.png)

*Figuur 1 en 2: Componenten binnen 1 applicatie met aanpassingen per component*

Hierboven zie je dat component voor component worden aangepast, ongeacht of deze aanpassingen onafhankelijk businesswaarde vertegenwoordigen. Fenomeen dat je vaak ziet bij beginnende Scrum teams is dat hun backlog is gevuld met dit soort technische ‘changes’. Echter, de backlog items dienen anders te worden 'gesneden' of ‘gesliced’. Bij de backlog refinement dienen we zoveel als mogelijk klantwensen te definieren, en geen technisch werk. Tenslotte: Een Product Owner moet van de business zijn, en diezelfde persoon moet de backlog opstellen. Deze persoon heeft in de regel geen verstand van technische zaken, en kan dan de backlog ook niet prioriteren!

Hierna zie je gevisualiseerd hoe het werk dan wel ‘gesliced’ zou moeten worden (gesteld dat een feature voor deze applicatie onafhankelijk in productie genomen zou kunnen worden):

![Afbeelding met schermafbeelding Automatisch gegenereerde beschrijving](/images/blog/req3.png)

*Figuur 3: features ‘slicen’ dwars door meerdere componenten van een applicatie*


Dit is wat de Scrum guide zegt over backlog items: '*De Product Backlog bevat alle features, functies, vereisten, verbeteringen en fixes die de wijzigingen vormen die moeten worden aangebracht in het product in toekomstige releases'*.

De gids vermeldt niet in het bijzonder User Stories als het voorgeschreven formaat. Verschillende formaten zijn toegestaan. Maar het gebruik van het User Story formaat is een veel voorkomende ‘practice’ en het dwingt teams om te denken in businesswaarde. En dit blijkt in de praktijk dus best moeilijk.

'Als \<stakeholder\> wil ik \<klantwens\> opdat \<businesswaarde\>'. Dit formaat is zeer krachtig. Het dwingt teams om na te denken over de eindgebruiker/klant, wie is dat? Het dwingt teams om te denken in de context (wensen) van de klant en de bedrijfswaarde die het zal leveren voor diezelfde klant.

**Story mapping als hulpmiddel om te denken in bedrijfswaarde**

Het blijkt in de praktijk zeer taai om dit juiste ‘slicing’ gedrag aan te leren. Als coach blijf ik de teams herinneren aan de noodzaak van frequent leveren van bedrijfswaarde. Het instrument dat ik hen vaak aanreik, is Story Mapping. Story Mapping is in mijn ervaring het meest krachtige instrument om teams te laten denken in bedrijfswaarde, customer journeys, minimaal haalbare producten en ga zo maar door. Maar zelfs dan kost het vaak perioden van 3 tot 6 maanden voordat teams echt de kracht van dit instrument begrijpen. Backlog refinement is niet simpel, en er wordt te vaak simpel over gedacht. Zolang de organisatie werkt met componentteams (teams die verantwoordelijk zijn voor het innoveren en onderhouden van 1 of een paar applicaties, in plaats van een business product) is het nog moeilijker om teams dit aan te leren, omdat backlog items voor slechts één applicatie niet noodzakelijkerwijs bedrijfswaarde vertegenwoordigen, meestal doen ze dat niet. Laat staan dat de product owner werk voor het team kan definiëren in termen van bedrijfswaarde..

**Patroon dat ontstaat bij het bedrijfsbreed invoeren van agile werken**

Sinds 2013 help ik organisaties bij het bereiken van hun bedrijfsdoelstellingen door gebruik te maken van elementen van ‘scaling agile’, met name het ‘Scaled Agile Framework’. Het fenomeen dat ik hierboven beschrijf heb ik sindsdien als een terugkerend patroon ervaren. Echter ik zag hetzelfde patroon ook op organisatie (structuur) niveau terugkomen! Kijk met me mee:

Het enterprise IT-landschap ziet er meestal ongeveer als volgt uit (Vereenvoudigd):

![Afbeelding met schermafbeelding Automatisch gegenereerde beschrijving](/images/blog/req4.png)

*Figuur 4: De lagen van het IT landschap*


Het IT landschap is horizontaal gelaagd, volgens de strategie van het convergeren van het landschap naar minder applicaties per laag om de totale eigendomskosten te verminderen. Teams zijn op een traditionele manier gericht op een van die lagen. In de front office zie je veel web- en app-teams, en in de backoffice zie je veel teams die de legacy applicaties onderhouden. Nogmaals, dit is meer dan vereenvoudigd en zeer algemeen. Hier zie je in eerste instantie dat component teams op de drie lagen worden ‘geplakt’:

![Afbeelding met schermafbeelding Automatisch gegenereerde beschrijving](/images/blog/req5.png)

*Figuur 5: Component teams zijn gepositioneerd op de drie lagen van het IT landschap*


In een geschaalde omgeving willen we teams die zich oriënteren op een bedrijfsproduct of waardestroom zoals we het noemen. Voorbeelden van belangrijkste waardestromen voor een verzekeringsmaatschappij zijn: Schade, Leven en Pensioenverzekeringen. Maar de klantwensen voor deze product(groep)en hebben meestal impact op front, mid én back office. We hebben ook geen projecten meer. De omvang van de projecten is gedefinieerd in zogenaamde Epics, en we brengen deze naar de vaste teams van teams. Een andere paradigmaverschuiving waar ik het vaak over heb. Epics zijn grote klanteisen die ook onafhankelijk klantwaarde dienen te vertegenwoordigen, en niet alleen een willekeurige opdracht. En elke waardestroom maakt gebruik van bepaalde applicaties van elke laag. Dit ziet er als volgt uit:

![Afbeelding met schermafbeelding Automatisch gegenereerde beschrijving](/images/blog/req6.png)

*Figuur 6: Teams van teams georiënteerd op een business product(groep) of waardestroom doorsnijden juist de drie lagen van het IT landschap*


Hier zie je dat teams zich op een traditionele manier specialiseren op een bepaalde technologie of technische laag. In plaats daarvan moeten ze organiseren in featureteams of tribes die gespecialiseerd zijn op een bepaald bedrijfsproduct, of sub-business product. Hoe kan iemand product owner zijn als het team slechts één applicatie onderhoudt? Van welk bedrijfsproduct is zij dan de eigenaar?

In wezen zegt deze blog: 'stop horizontaal denken, en begin verticaal te denken!'. Of met andere woorden:  Het vullen van een backlog is niet zo eenvoudig als men zou denken als je begint als product owner. Daarom raad ik alle disciplines, die betrokken zijn bij een of andere vorm van analyse, aan om kennis te maken met agile requirements engineering. Er is veel meer te ontdekken dan alleen de User Story practice en storymapping. Usecase 2.0 van Ivar Jacobson bijvoorbeeld is een andere practice, en er is meer.

Als deze blog te complex overkomt, begrijp je waarom veel training en coaching nodig is (ook vooral voor het management) om alle benodigde paradigma verschuivingen tot stand te brengen. En ik raak hiermee slechts het topje van de ijsberg van de tientallen paradigmaverschuivingen.

Ik hoop dat het patroon wordt herkend. En ja, het zijn enorme uitdagingen. Zowel het op de juiste manier ‘slicen’ van backlog items (Dus niet op component gericht, maar op klantwaarde gericht) en  om teams te organiseren op productniveau in plaats van op laag (of applicatie) in het IT landschap. Wat te denken van configuratie management, resourcing en een flexibel IT landschap. Dit zijn zaken die niet allemaal zomaar geregeld zijn. Sterker nog, bij de meeste bedrijven is het IT landschap nog verre van flexibel. Dus zullen we de combi van feature en component teams voorlopig nog wel blijven tegenkomen. In een volgende blog ga ik dan ook verder in op dit patroon van component-gewijze oriëntatie versus feature / waardestroom oriëntatie. [/nl/blog/fractale-structuurpatronen-bij-het-bedrijfsbreed-schalen-van-agile/](/nl/blog/fractale-structuurpatronen-bij-het-bedrijfsbreed-schalen-van-agile/)
