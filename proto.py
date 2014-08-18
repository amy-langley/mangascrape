from lxml import html
import requests
from utils.file import mkdtemp
from utils.net import grabfile

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
items = [i.get('src') for i in tree3.cssselect('section.read_img img')]

with mkdtemp("foo", chdir=True) as dirname:
    print "I'm in", dirname
    for item in items:
         grabfile(item)

print items
