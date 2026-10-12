import re,glob,json,os
CAT={'Agile besturing':'Agile governance','Agile organisatie structuur':'Agile organization structure','Agile transities':'Agile transitions','Angelsaksisch naar Rijnlands':'Anglo-Saxon to Rhineland','Enterprise agility':'Enterprise agility','Product oriëntatie':'Product orientation','Projecten versus agile werken':'Projects versus agile working','Scaling agile':'Scaling agile','Waardestromen':'Value streams','Wendbaarheid':'Business agility','Agile leiderschap':'Agile leadership','Agile mindset':'Agile mindset','SAFe':'SAFe','Agile volwassenheid':'Agile maturity','Productiviteit':'Productivity','Continu verbeteren':'Continuous improvement','NeXuS':'Nexus','Agile verandermanagement':'Agile change management','Agile HR':'Agile HR','Spotify':'Spotify','Scaling frameworks':'Scaling frameworks','LeSS':'LeSS','Geen categorie':'Uncategorized','Agile requirements':'Agile requirements','Agile metrieken':'Agile metrics','Agile contracting':'Agile contracting','Agile':'Agile'}
TAG={'Besturing':'Governance','Cost of Delay':'Cost of Delay','Hybride organisatie':'Hybrid organization','Kosten van uitstel':'Cost of delay','Loslaten':'Letting go','Onzichtbare kosten':'Invisible costs','Paradigma verschuivingen':'Paradigm shifts','Netwerkorganisaties':'Network organizations','Organigram':'Org chart','Wendbaarheid':'Business agility','Wendbare organisaties':'Agile organizations'}
slugs=json.load(open('tools/slugs.json'))['nl2en']
for t in glob.glob('tools/tr/*.md'):
    nl=os.path.basename(t)[:-3]; en=slugs[nl]
    src=open(f'content/nl/blog/{nl}.md').read(); fm=src.split('---\n')[1]
    d=dict(l.split(': ',1) for l in fm.strip().splitlines())
    tr=open(t).read(); title,body=tr.split('\n',1); title=title.replace('TITLE: ','').strip()
    def mp(v,M): 
        items=[x.strip() for x in v.strip('[]').split(',') if x.strip()]
        return '['+', '.join('"%s"'%M.get(x,x) for x in items)+']'
    out=['---','title: "%s"'%title.replace('"','\\"'),'date: '+d['date'],'slug: '+en,'translationKey: '+d['translationKey'],'categories: '+mp(d['categories'],CAT),'tags: '+mp(d['tags'],TAG),'translated: true']
    if 'featured_image' in d: out.append('featured_image: '+d['featured_image'])
    out.append('---')
    # map internal NL links to EN counterparts
    def lk(m):
        s=m.group(1)
        from_pairs={'agile-opdrachtgeverschap-en-leverancierschap-vergen-partnership-en-transparantie':'agile-demand-and-supply-the-glass-box','van-scrum-team-naar-agile-organisatie-deel-1':'from-scrum-team-to-agile-organization-part-one','van-scrum-team-naar-agile-organisatie-deel-2':'from-scrum-team-to-agile-organization-part-two','van-scrum-team-naar-agile-organisatie-deel-3':'from-scrum-team-to-agile-organization-part-three','van-scrum-team-naar-agile-organisatie-deel-4':'from-scrum-team-to-agile-organization-part-four','meten-van-productiviteit-melkproductie-of-poepscheppen':'measuring-velocity-producing-milk-or-shoveling-shit','eerste-antipatronen-bij-scaling-agile':'first-anti-patterns-in-scaling-agile-arising'}
        e=slugs.get(s) or from_pairs.get(s)
        return '/en/blog/%s/'%e if e else m.group(0)
    body=re.sub(r'/nl/blog/([^/]+)/',lk,body)
    open(f'content/en/blog/{en}.md','w').write('\n'.join(out)+'\n\n'+body.strip()+'\n')
    print('ok',en)
