import re,os,shutil,glob
NG='/home/box/keep/newgility-website/blogs'; TP='/home/box/keep/3pro-website/blogs'
OUT='/workspace/brian-blog'
pairs={ # en slug : nl slug
'agile-demand-and-supply-the-glass-box':'agile-opdrachtgeverschap-en-leverancierschap-vergen-partnership-en-transparantie',
'from-scrum-team-to-agile-organization-part-one':'van-scrum-team-naar-agile-organisatie-deel-1',
'from-scrum-team-to-agile-organization-part-two':'van-scrum-team-naar-agile-organisatie-deel-2',
'from-scrum-team-to-agile-organization-part-three':'van-scrum-team-naar-agile-organisatie-deel-3',
'from-scrum-team-to-agile-organization-part-four':'van-scrum-team-naar-agile-organisatie-deel-4',
'measuring-velocity-producing-milk-or-shoveling-shit':'meten-van-productiviteit-melkproductie-of-poepscheppen',
'first-anti-patterns-in-scaling-agile-arising':'eerste-antipatronen-bij-scaling-agile'}
nl2en_slug={ # NL-only -> EN slug for translation
'van-scrum-team-naar-agile-organisatie-deel-5':'from-scrum-team-to-agile-organization-part-five',
'prince2-agile-versus-scaling-agile':'prince2-agile-versus-scaling-agile',
'paradigma-verschuivingen-bij-scaling-agile':'paradigm-shifts-in-scaling-agile',
'van-trend-naar-gevestigde-orde-scaling-agile':'from-trend-to-established-order-scaling-agile',
'de-zichzelf-vervullende-voorspelling':'the-self-fulfilling-prophecy',
'van-scrum-team-naar-agile-organisatie-deel-6-epiloog':'from-scrum-team-to-agile-organization-part-six-epilogue',
'vergelijkbare-patronen-bij-backlog-refinement-en-structureren-van-teams':'similar-patterns-in-backlog-refinement-and-structuring-teams',
'fractale-structuurpatronen-bij-het-bedrijfsbreed-schalen-van-agile':'fractal-structure-patterns-when-scaling-agile-enterprise-wide',
'functiehuizen-slopen':'job-classification-systems-demolish-them',
'organisaties-willen-wendbaar-worden-maar-niet-veranderen':'organizations-want-to-become-agile-but-not-change',
'de-wendbare-organisatie-analoog-de-boston-matrix':'the-agile-organization-analogous-to-the-boston-matrix',
'cultuur-volgt-structuur':'culture-follows-structure',
'agile-besturing-van-een-keten-van-organisaties-wat-is-de-zwakste-schakel':'agile-governance-of-a-chain-of-organizations-what-is-the-weakest-link',
'6-oude-schoenen-om-zo-snel-mogelijk-weg-te-doen':'6-old-shoes-to-get-rid-of-as-soon-as-possible',
'starre-silos-en-afdelingen-weg-ermee':'rigid-silos-and-departments-away-with-them'}
en2nl_slug={
'agile-misunderstanding-number-one-you-can-not-plan-and-estimate-agile-projects':'agile-misverstand-nummer-een-je-kunt-agile-projecten-niet-plannen-en-schatten',
'agile-misconception-no-2-working-agile-takes-more-time-and-money':'agile-misvatting-nr-2-agile-werken-kost-meer-tijd-en-geld',
'agile-misconception-no-3-agile-scrum':'agile-misvatting-nr-3-agile-is-scrum',
'eat-your-own-dogfood':'eet-je-eigen-hondenvoer'}
en2nl={**pairs}; nl2en={v:k for k,v in pairs.items()}
for k,v in nl2en_slug.items(): nl2en[k]=v
for k,v in en2nl_slug.items(): en2nl[k]=v
def parse(p):
    s=open(p,encoding='utf-8').read(); _,fm,body=s.split('---\n',2); d={}
    for l in fm.splitlines():
        if ':' in l: k,v=l.split(':',1); d[k.strip()]=v.strip()
    return d,body
def linkmap(m):
    url=m.group(0); slug=url.rstrip('/>').rstrip('/').split('/')[-1]
    if 'newgility' in url: return '/nl/blog/%s/'%slug
    import urllib.parse; slug=urllib.parse.unquote(slug).replace('‘','').replace('’','')
    slug=re.sub('-+','-',slug)
    if slug=='agile-misunderstanding-number-one-you-can-not-plan-and-estimate-agile-projects': pass
    if slug=='agile-demand-and-supply-the-glass-box': pass
    return '/en/blog/%s/'%slug
def clean(body,title,src):
    body=body.lstrip()
    if body.startswith('# '): body=body.split('\n',1)[1]
    body=re.sub(r'^Alt-tekst:.*\n?','',body,flags=re.M)
    body=re.sub(r'^\*Bijschrift: ','*',body,flags=re.M)
    body=re.sub(r'\]\(images/',r'](/images/blog/',body)
    body=re.sub(r'https?://(newgility\.eu|3pro\.wordpress\.com)/\d{4}/\d\d/\d\d/[^)\s"\]>]+/?',linkmap,body)
    return body.strip()+'\n'
def cats(d): return d.get('categories','[]')
for src,lang in ((NG,'nl'),(TP,'en')):
    for p in sorted(glob.glob(src+'/2*.md')):
        d,body=parse(p); slug=d['slug']
        if lang=='en': slug=re.sub('-+','-',slug)
        key = slug if lang=='nl' else en2nl.get(slug,slug)
        if lang=='nl' and slug in nl2en_slug: key=slug
        fm=['---','title: '+d['title'],'date: '+d['date'].replace(' ','T')+'+01:00','slug: '+slug,'translationKey: '+key,'categories: '+cats(d),'tags: '+d.get('tags','[]'),'original_url: '+d.get('url','')]
        if d.get('featured_image'): fm.append('featured_image: /images/blog/'+os.path.basename(d['featured_image']))
        fm.append('---')
        open(f'{OUT}/content/{lang}/blog/{slug}.md','w').write('\n'.join(fm)+'\n\n'+clean(body,d['title'],lang))
    for img in glob.glob(src+'/images/*'):
        dst=f'{OUT}/static/images/blog/'+os.path.basename(img)
        shutil.copy(img,dst)
import json; json.dump({'nl2en':nl2en_slug,'en2nl':en2nl_slug},open(OUT+'/tools/slugs.json','w'),indent=1)
