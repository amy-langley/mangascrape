from lxml import html
import requests
from utils.file import mkdtemp, iterate_filename
from utils.net import grabfile, do_unparse
from urlparse import urlparse
import os

#page = requests.get('http://www.mangahere.co/mangalist/')
#tree = html.fromstring(page.text)

#titlelinks = tree.cssselect('a.manga_info')
#items = [[i.text_content(), i.get('href')] for i in titlelinks]
#items = [[i.text_content(), i.get('href')] for i in titlelinks if 'Hourou' in i.text_content()]

# print items


#page2 = requests.get('http://www.mangahere.co/manga/hourou_musuko/')
#tree2 = html.fromstring(page2.text)
#chapterlinks = tree2.cssselect('div.detail_list ul span.left a')

#items = [i.get('href') for i in chapterlinks]

page3 = requests.get('http://www.mangahere.co/manga/hourou_musuko/v01/c001/')
tree3 = html.fromstring(page3.text)

[baseurl] = [i.get('src') for i in tree3.cssselect('section.read_img img')]
urlobj = urlparse(baseurl)
print urlobj[:]
pagecount = len(
    tree3.cssselect('section.readpage_top span.right select option'))

items = [do_unparse(urlobj, i) for i in iterate_filename(urlobj.path, 1, pagecount)]

with mkdtemp("foo", chdir=True) as dirname:
    print "I'm in", dirname
    for item in items:
        print "Fetching " + item
        grabfile(item)
    for fn in os.listdir(dirname):
        print fn
