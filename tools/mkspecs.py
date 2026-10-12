import json
S={}
def it(nl,en,**k): d=dict(nl=nl,en=en); d.update(k); return d
S['Trend-zonder.png']=[
 it("Trend zonder continue proces en kwaliteitsverbetering (Huidige situatie)",["Trend without continuous process and","quality improvement (current situation)"],size=24),
 it("Continue proces en kwaliteitsverbetering is vaak geen cultuur, en vormt grote uitdaging","Continuous improvement is rarely part of the culture and a major challenge",align="l",size=10),
 it("Alleen effort besteed aan innovatie en onderhoud (backlog) telt mee voor de productiviteit!",["Only effort spent on innovation and maintenance","(backlog) counts towards productivity!"],align="l",bold=True),
 it("Stilstand betekent dalende productiviteit","Standing still means declining productivity",align="l",bold=True),
 it("Innovatie en onderhoud","Innovation and maintenance",align="l"),
 it("Verminderen technische schuld","Reducing technical debt",align="l"),
 it("Procesverbetering","Process improvement",align="l"),
 it("Wegwerken hotfixes en defects","Resolving hotfixes and defects",align="l")]
S['Trend-met.png']=[
 it("Tijdelijke terugval in productiviteit bij overgang naar continue proces en kwaliteitsverbetering",["Temporary drop in productivity when moving","to continuous process and","quality improvement"],size=24),
 it("Alleen effort besteed aan innovatie en onderhoud (backlog) telt mee voor de productiviteit!",["Only effort spent on innovation and maintenance (backlog) counts towards","productivity!"],align="l",bold=True),
 it("Overgang naar investeren in proces en kwaliteitsverbetering geeft eerst dalende, op langere duur stijgende productiviteit",["Investing in process and quality improvement first lowers, but in the","longer term increases productivity"],align="l",bold=True),
 it("Innovatie en onderhoud","Innovation and maintenance",align="l"),
 it("Verminderen technische schuld","Reducing technical debt",align="l"),
 it("Procesverbetering","Process improvement",align="l"),
 it("Wegwerken hotfixes en defects","Resolving hotfixes and defects",align="l")]
S['backlogs.png']=[
 it("Verschillende backlogs zijn input voor de sprint backlog",["Different backlogs are input for","the sprint backlog"]),
 it("Technische Schuld backlog",["Technical","debt","backlog"],align="l"),
 it("Verbeter backlog",["Improvement","backlog"],align="l"),
 it("(Bijv. Test automatisering items, maar ook aanpassen Scrum bord)","(E.g. test automation items, but also adjusting the Scrum board)",align="l"),
 it("Taken","Tasks")]
S['shift-scope.png']=[it("Traditionele aanpak","Traditional approach"),it("Agile aanpak","Agile approach")]
stapcommon=[it("Klant domein 1","Customer domain 1"),it("Klant domein 2","Customer domain 2"),it("Klant domein 3","Customer domain 3"),
 it("Functie of","Functional or",word=False),it("afdeling","department",word=True),it("domein team","domain team"),it("Product of","Product or")]
S['stap-1.png']=[it("Stap 1: Iteratief werken binnen projecten in de matrix","Phase 1: Working iteratively within projects in the matrix")]+stapcommon
S['Stap-2.png']=[it("Ontwikkelingsfase 2: Virtuele product teams over functie afdelingen heen","Phase 2: Virtual product teams across functional departments")]+stapcommon
S['Stap-3.png']=[it("Ontwikkelingsfase 3: Fysieke product teams, al dan niet virtueel aangevuld met Ops","Phase 3: Physical product teams, optionally virtually supplemented with Ops")]+stapcommon
S['Stap-4.png']=[it("Ontwikkelingsfase 4: DevOps binnen IT","Phase 4: DevOps within IT")]+stapcommon
S['Stap-5.png']=[it("Ontwikkelingsfase 5: Bedrijfs brede product of domein afdelingen","Phase 5: Enterprise-wide product or domain departments"),
 it("Klant domein 1","Customer domain 1"),it("Klant domein 2","Customer domain 2"),it("Klant domein 3","Customer domain 3"),
 it("DevOps Product of domein afdeling",["DevOps product or domain","department"],bold=True)]
S['7s.png']=[it("strategie","strategy",word=True),it("structuur","structure",word=True),it("stijl","style",word=True),it("syste- men",["sys-","tems"]),it("staf","staff",word=True),
 it("Het 7 essen model (peters en Waterman, 1986)","The 7S model (Peters and Waterman, 1986)",align="l")]
S['J-curve.png']=[it("Productiviteit","Productivity",rot=270),it("½ jaar tot 1 jaar per waardestroom","½ to 1 year per value stream"),it("Tijd","Time",word=True)]
S['Kosten-van-uitstel.jpg']=[
 it("Kosten van uitstel van agile transformaties (Cost of delay)","Cost of delay of agile transformations",bold=True,align="l"),
 it("€ potentiële baten","€ potential benefits",rot=270,bold=True),
 it("(Half tot 1 jaar per waardestroom)",["(Half a year to 1 year per","value stream)"]),
 it("Minimaal benodigde periode in hybride situatie (Oude schoenen na overgangsperiode tijdig weg)",["Minimum required period in","hybrid situation (old shoes","discarded in time after transition)"],align="l"),
 it("Potentiële periode van kosten van uitstel (Blijft op bodemniveau zolang oude schoenen niet weg)",["Potential period of cost of","delay (stays at bottom level as","long as old shoes are not discarded)"],align="l"),
 it("ROI moment ver in de tijd",["ROI moment","far in the future"]),
 it("Tijd","Time",word=True)]
boston=[it("Een wendbare organisatie in beeld analoog de Boston Matrix","An agile organization pictured analogous to the Boston Matrix"),
 it("Team van Teams","Team of Teams"),it("Product of","Product or"),it("Dienst A","Service A"),it("Dienst B","Service B"),it("Dienst C","Service C"),it("Dienst D","Service D"),
 it("Klanten","Customers",word=True),
 it("Team van teams = Afdeling","Team of teams = Department",align="l"),
 it("Afdelingsresources = Afdelingsbudget","Department resources = Department budget",align="l"),
 it("Afdelingsbudget = Productbudget","Department budget = Product budget",align="l"),
 it("(Totaal: 18 teams)","(Total: 18 teams)",align="l"),it("(Totaal: 20 teams)","(Total: 20 teams)",align="l")]
for i in range(1,6): S[f'boston{i}.png']=boston
S['fractal1.png']=[
 it("Kantelen van functionele naar product silo's","Shifting from functional to product silos"),
 it("Van Angelsaksisch","From Anglo-Saxon",bold=True),it("Naar Rijnlands","To Rhineland",bold=True),
 it("Product georiënteerde","Product-oriented"),it("Team van teams","team of teams"),
 it("Klantwensen","Customer needs"),it("Eindklant","End customer",word=True),
 it("De 'dommekrachten'","The 'brute force'"),it("The professionele kenniswerkers","The professional knowledge workers"),
 it("Faciliterend Management","Facilitating management",rot=270)]
S['fractal2.png']=[it("Component team of squad","Component team or squad"),it("Feature team of squad",["Feature team or","squad"],rot=270)]
S['fractal3.png']=[it("De ideale 'platte' organisatie","The ideal 'flat' organization",size=76),it("Feature team of squad",["Feature team or","squad"],rot=270)]
S['fractal4.png']=[it("Release train of tribe Y","Release train or tribe Y",size=80),it("Component team of squad","Component team or squad"),it("Feature team of squad",["Feature team or","squad"],rot=270)]
S['fractal6.png']=[it("Component team of squad","Component team or squad"),it("Feature team of squad",["Feature","team or","squad"],rot=270)]
S['fractal7.png']=[it("Bedrijf Z","Company Z")]
S['fractal8.png']=[it("Bedrijf Z","Company Z"),it("Component team of squad",["Component team or","squad"],size=16.7)]
silo_rt=[it("Release Train 4 (Generieke services)",["Release Train 4","(Generic services)"]),
 it("(Productgroep 1)","(Product group 1)",align="l"),it("(Productgroep 2)","(Product group 2)",align="l"),it("(Productgroep 3)","(Product group 3)",align="l"),
 it("STAF","STAFF",word=True),it("Staf 1 Staf 2 Staf 3","Staff 1 Staff 2 Staff 3")]
S['silo.png']=[it("Klassieke functionele silo's in organisaties","Classic functional silos in organizations"),
 it("Business afdeling 1","Business department 1",align="l"),it("Business afdeling 2","Business department 2",align="l"),it("Business afdeling 3","Business department 3",align="l")]+silo_rt
S['silo2.png']=[it("Overlay van Release Trains gebaseerd op waardestroom of shared service",["Overlay of Release Trains based on","value stream or shared service"])]+silo_rt
S['silo3.png']=[it("Verschillende soorten teams in Release Trains gebaseerd op waardestroom of shared service",["Different types of teams in Release Trains","based on value stream or shared service"]),
 it("Staf Team",["Staff","Team"])]+silo_rt
S['silo4.png']=[it("Bestaande structuur opgeheven, geen onderscheid meer in functionele silo's",["Existing structure dissolved, no more","distinction between functional silos"]),
 it("(Vakkennis geborgd middels communities)","(Expertise safeguarded through communities)"),it("Staf Team",["Staff","Team"])]+silo_rt
S['silo5.png']=[it("Zoom in op soorten teams in 1 Release Train","Zoom in on types of teams in 1 Release Train"),
 it("(Welke rollen passen bijvoorbeeld in de multi-disciplinaire teams)","(Which roles fit, for example, in the multidisciplinary teams)"),
 it("(Productgroep 1)","(Product group 1)"),it("Staf Team",["Staff","Team"]),it("System/ Tool ondersteuning Team",["System/","Tool","support","Team"])]
S['team1.png']=[it("Business Informatie Analist",["Business","Information","Analyst"]),it("Software Integratie Engineer",["Software","Integration","Engineer"])]
S['team2.png']=[it("System/ Tool ondersteuning Team",["System/","Tool","support","Team"]),it("Technische Schuld Tool Specialist",["Technical","Debt","Tool","Specialist"]),
 it("Integratie/ Configuratie Tool Specialist",["Integration/","Configuration","Tool","Specialist"]),it("OTAP","DTAP",word=True)]
S['team4.png']=[it("Staf Team",["Staff","Team"]),it("Jurist","Legal Counsel",word=True),it("Strategist","Strategist",word=True)]
S['Holo1.png']=[it("Traditionele organisatie","Traditional organization"),it("Formele structuur","Formal structure"),it("Informele structuur","Informal structure"),it("Gewenste structuur","Desired structure"),
 it("Organigram Functiebeschrijvingen",["Org chart","Job descriptions"]),it("Hoe de dingen echt werken",["How things","really work"]),
 it("De ideale organisatie structuur op elk gegeven moment",["The ideal","organization structure","at any given moment"])]
S['waardestromen.png']=[it("Business Waarde","Business value"),it("Business Domein 1","Business domain 1"),it("Business Domein 2","Business domain 2"),it("Business Domein 3","Business domain 3"),it("Business Domein 4","Business domain 4"),
 it("IT Afdeling 1","IT department 1"),it("IT Afdeling 2","IT department 2"),it("IT Afdeling 3","IT department 3"),it("IT Afdeling 4","IT department 4")]
S['Keten1.png']=[it("Ministerie A","Ministry A"),it("Ministerie B","Ministry B"),it("Klassieke aansturing Shared Service Center",["Classic","governance","Shared Service","Center"]),
 it("Klassieke aansturing semi overheid",["Classic","governance","semi-government"]),it("Klassieke aansturing IT",["Classic","governance IT"]),
 it("Overheid of Semi overheid",["Government or","semi-public"]),it("Shared Service Center",["Shared Service","Center"])]
S['keten2.png']=[it("Opdrachtgever Bedrijf A",["Client","company A"]),it("Opdrachtnemer Bedrijf B",["Contractor","company B"]),
 it("Klassieke inkoop afdeling",["Classic","procurement"]),it("Klassieke aanbesteding leverancier",["Classic","supplier","tendering"]),
 it("Leverancier","Supplier",word=True),it("Klassieke aansturing IT",["Classic","governance IT"])]
S['kink.png']=[it("Lean Agile besturing","Lean-Agile steering",box=[[8,174,192,32],[405,170,192,38]],size=20.9,bold=True,flat=False,maskfg=True,maskthr=330,color=[0,0,0],pad=1,align='l')]
S['boehms-law.jpg']=[it("Kosten","Cost",rot=270),it("FO","FD",word=True,bold=True),it("TO","TD",word=True,bold=True),it("Real","Build",word=True,bold=True),it("Gebruik","Operation",word=True,bold=True),it("Fase","Phase",word=True)]
S['prince2taart.png']=[it("Beheersing (Control)","Control",bold=True),it("Flexibiliteit (Agility)","Flexibility (Agility)",bold=True)]
req=[it("Applicatie","Application",word=True,bold=True),it("Technisch","Technical",word=True),it("Benodigde aanpassing",["Required","change"],bold=True),
 it("Enterprise IT Landschap","Enterprise IT Landscape",bold=True),it("Applicatie 1","Application 1"),it("Applicatie n","Application n")]
for i in range(1,7): S[f'req{i}.png']=req

def setitem(k,nl,**kw):
    for d in S[k]:
        if d['nl']==nl: d.update(kw); return
    raise SystemExit('geen '+k+' '+nl)
S['fractal1.png']=[d if d['nl']!='Eindklant' else it('Eindklant','Customer',word=True,size=12.5) for d in S['fractal1.png']]
for k in ['stap-1.png','Stap-2.png','Stap-3.png','Stap-4.png']:
    S[k]=[d for d in S[k] if not d['nl'].startswith('Klant') and d['nl'] not in ('Functie of','afdeling','domein team','Product of')]
    S[k]+= [it('Klant domein %d'%(i+1),'Customer domain %d'%(i+1),box=b) for i,b in enumerate([[89,56,74,8],[213,56,74,8],[338,56,74,8]])]
for k in ['stap-1.png','Stap-2.png']:
    S[k].append(it('Functie of component afdeling',['Functional or','component','department'],box=[[60,228,40,28],[127,228,40,28],[197,228,40,28],[262,227,46,30],[330,227,46,30],[398,227,46,30]],size=7.5,pitch=9.5,pad=1,color=[255,255,255],bold=True))
setitem('Stap-3.png',S['Stap-3.png'][0]['nl'],box=[45,14,410,14])
S['Stap-3.png'].append(it('Functie of component afdeling',['Functional or','component','department'],box=[[262,227,46,30],[330,227,46,30],[398,227,46,30]],size=7.5,pitch=9.5,pad=1,color=[255,255,255],bold=True))
S['Stap-3.png'].append(it('Product of domein team',['Product or','domain team'],box=[[53,227,50,23],[120,227,50,23],[188,227,50,23]],size=7.5,pitch=9.5,pad=0,color=[255,255,255],bold=True))
S['Stap-4.png'].append(it('DevOps Product of domein team',['DevOps','Product or','domain team'],box=[[154,172,56,32],[224,172,56,32],[292,172,56,32]],size=7.5,pitch=10,pad=1,color=[255,255,255],bold=True,flat=False,maskfg=True,maskthr=150))
setitem('Stap-4.png',S['Stap-4.png'][0]['nl'],box=[152,13,192,14])
setitem('Stap-5.png','DevOps Product of domein afdeling',box=[[45,244,250,50],[355,244,250,50],[667,244,250,50]],size=17,flat=False,color=[255,255,255],pitch=24)
S['7s.png']=[it('strategie','strategy',box=[204,58,66,17]),it('structuur','structure',box=[97,118,69,15]),
 it('stijl','style',box=[330,118,26,16]),it('syste- men',['sys-','tems'],box=[114,212,48,35],pitch=18),
 it('staf','staff',box=[316,230,31,17]),S['7s.png'][-1]]
for k in ['Trend-zonder.png','Trend-met.png']: setitem(k,'Innovatie en onderhoud',box=[52,222,80,9])
setitem('Trend-met.png','Verminderen technische schuld',box=[53,241,103,11])
setitem('boston1.png','Afdelingsresources = Afdelingsbudget',box=[9,395,180,12])
S['fractal2.png'][1]=it("Feature team of squad",["Feature team or","squad"],rot=270,box=[[453,428,264,79],[453,853,264,79]],size=40,pitch=40)
setitem('team2.png','System/ Tool ondersteuning Team',box=[410,468,610,465],size=105,color=[255,255,255],pitch=100)
setitem('team4.png','Jurist',box=[668,162,86,36],size=32)
setitem('Holo1.png','Formele structuur',box=[23,84,220,22])
setitem('Holo1.png','Informele structuur',box=[770,102,238,22])
setitem('Holo1.png','Organigram Functiebeschrijvingen',box=[268,216,184,50],size=19,pitch=23,pad=0)
setitem('Holo1.png','Hoe de dingen echt werken',box=[520,216,160,50],size=19,pitch=23)
setitem('Holo1.png','De ideale organisatie structuur op elk gegeven moment',box=[398,406,188,78],size=19,pitch=23)
xs=[(69,201),(266,398),(455,588),(644,776)]; xi=[(94,184),(292,382),(481,571),(670,760)]
for i in range(4):
    setitem('waardestromen.png','Business Domein %d'%(i+1),box=[xs[i][0],222,xs[i][1]-xs[i][0],17],fit=True,flat=False)
    setitem('waardestromen.png','IT Afdeling %d'%(i+1),box=[xi[i][0],485,xi[i][1]-xi[i][0],14],fit=True,flat=False)
S['Keten1.png']=[d for d in S['Keten1.png'] if d['nl']!='Shared Service Center']
setitem('Keten1.png','Overheid of Semi overheid',box=[568,135,112,45],size=19,color=[255,255,255],pitch=21,pad=0)
setitem('Keten1.png','Klassieke aansturing semi overheid',box=[476,94,80,38],size=11,color=[255,255,255],pitch=12.5,pad=0)
for k in ['silo3.png','silo4.png','silo5.png']:
    S[k]=[d for d in S[k] if d['nl'] not in ('Staf Team','System/ Tool ondersteuning Team')]
import copy
for k in ['silo.png','silo2.png','silo3.png','silo4.png','silo5.png']: S[k]=copy.deepcopy(S[k])
setitem('silo4.png','Release Train 4 (Generieke services)',box=[652,116,140,42],size=14.8,pitch=14,pad=4)
setitem('team2.png','System/ Tool ondersteuning Team',maskfg=True,maskthr=60)
setitem('team4.png','Staf Team',maskfg=True,color=[255,255,255])
S['team4.png']=[d for d in S['team4.png'] if d['nl']!='Strategist']
for k in ['silo3.png','silo4.png']: S[k].append(it('Staf','Staff',box=[[304,114,13,8],[303,194 if k=='silo3.png' else 193,13,8],[303,268,13,8],[303,341,13,8]],size=7,pad=1,color=[235,235,235]))
setitem('silo4.png','(Vakkennis geborgd middels communities)',box=[289,74,222,13],pad=0,size=12.8)
for d in S['7s.png'][:5]: d.update(size=17,flat='row',color=[0,0,0],pad=0 if d['nl']=='structuur' else 1)
setitem('J-curve.png','½ jaar tot 1 jaar per waardestroom',box=[335,1054,672,46],size=44.3,pad=3)
for k in ['Trend-zonder.png','Trend-met.png']:
    for d in S[k]:
        if d['nl'] in ('Innovatie en onderhoud','Verminderen technische schuld','Procesverbetering','Wegwerken hotfixes en defects'): d['size']=8.1
D={}
S['boston5.png']=[dict(d) for d in S['boston5.png']]
for d in S['boston5.png']:
    if d['nl']=='Product of': d.update(box=[[600,51,63,11],[600,187,63,11],[600,318,63,11]],fit=True)
S['fractal1.png'][0]=it("Kantelen van functionele naar product silo's","From functional to product silos",box=[36,28,645,44],size=42,flat=False,align="l")
for i in range(1,6):
    k='boston%d.png'%i
    S[k]=[d for d in S[k] if d['nl'] not in ('Team van teams = Afdeling','Afdelingsresources = Afdelingsbudget','Afdelingsbudget = Productbudget','(Totaal: 18 teams)','(Totaal: 20 teams)')]
    tot='18' if i in (1,5) else '20'
    K=[25,25,25]; z=12; c=124
    D[k]=[dict(erase=[8,380,200,56],texts=[[10,386,'Team of teams',z,False,K],[c,386,'= Department',z,False,K],
        [10,400,'Department resources',z,False,K],[c,400,'= Department budget',z,False,K],
        [10,414,'Department budget',z,False,K],[c,414,'= Product budget',z,False,K],[10,428,'(Total: %s teams)'%tot,z,False,K]])]
S['fractal1.png']=[d for d in S['fractal1.png'] if d['nl'] not in ('Product georiënteerde','Team van teams')]
S['fractal1.png'].append(it('Product georienteerde Team van teams',['Product-oriented','team of teams'],box=[[520,193,112,27],[520,242,112,27],[520,291,112,27]],size=11,pitch=13,color=[0,0,0]))
S['fractal8.png']=[d for d in S['fractal8.png'] if d['nl']!='Component team of squad']
S['fractal8.png'].append(it('Component team of squad',['Component team or','squad'],size=16.7,pitch=20,color=[0,0,0],box=[[112, 422, 145, 42], [351, 422, 145, 42], [649, 418, 145, 42], [887, 418, 145, 42], [112, 628, 145, 42], [351, 628, 145, 42], [649, 625, 145, 42], [887, 625, 145, 42], [112, 906, 145, 42], [351, 906, 145, 42], [648, 906, 145, 42], [887, 905, 145, 42], [112, 1112, 145, 42], [351, 1112, 145, 42], [648, 1112, 145, 42], [887, 1112, 145, 42]]))
S['fractal8.png'].append(it('of','or',rot=270,word=True,bgnear=[169,209,142]))
for k,v in S.items():
    json.dump(dict(src=k,items=v,**({'draw':D[k]} if k in D else {})),open(k.rsplit('.',1)[0]+'.json','w'),ensure_ascii=False,indent=0)
print(len(S))
