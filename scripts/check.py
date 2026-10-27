#!/usr/bin/env python3
"""Check generated pages, metadata, structured data, local links and assets."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=set();self.refs=[];self.h1=0;self.canonical=[];self.lang=None;self.json=False;self.structured='';self.alts=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, f'duplicate id {a["id"]}'
            self.ids.add(a['id'])
        if tag=='html': self.lang=a.get('lang')
        if tag=='h1':self.h1+=1
        if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
        if tag=='link' and a.get('rel')=='alternate':self.alts.add(a.get('hreflang'))
        if tag=='script' and a.get('type')=='application/ld+json':self.json=True
        for attr in ['href','src']:
            if a.get(attr):self.refs.append(a[attr])
    def handle_endtag(self,tag):
        if tag=='script':self.json=False
    def handle_data(self,data):
        if self.json:self.structured+=data
pages={}
for p in [ROOT/'index.html',*sorted((ROOT/'it').rglob('*.html')),*sorted((ROOT/'en').rglob('*.html'))]:
    obj=Page();obj.feed(p.read_text());pages[p]=obj
    assert obj.h1==1,(p,'h1')
    assert obj.lang in ['it','en'],p
    assert len(obj.canonical)==1,p
    assert {'it','en','x-default'} <= obj.alts,p
    assert json.loads(obj.structured)['@type']=='ProfessionalService',p
for p,obj in pages.items():
    for ref in obj.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc:continue
        dest=(ROOT/u.path.lstrip('/')) if u.path.startswith('/') else (p.parent/u.path)
        if dest.is_dir():dest=dest/'index.html'
        assert dest.exists(),(p,ref,'missing local target')
        if u.fragment:
            target=pages.get(dest)
            if not target:
                target=Page();target.feed(dest.read_text())
            assert unquote(u.fragment) in target.ids,(p,ref,'missing anchor')
ET.parse(ROOT/'sitemap.xml')
assert len(pages)==9
print(f'PASS: {len(pages)} pages, localized metadata, JSON-LD, local links, fragments, assets and sitemap.')
