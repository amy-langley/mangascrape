from lxml import html
import requests

#page = requests.get('http://www.mangahere.co/mangalist/')
#tree = html.fromstring(page.text)

#titlelinks = tree.cssselect('a.manga_info')
#items = [[i.text_content(), i.get('href')] for i in titlelinks]
#items = [[i.text_content(), i.get('href')] for i in titlelinks if 'Hourou' in i.text_content()]

#print items


page2 = requests.get('http://www.mangahere.co/manga/hourou_musuko/')
tree2 = html.fromstring(page2.text)
chapterlinks = tree2.cssselect('div.detail_list ul span.left a')

items = [i.get('href') for i in chapterlinks]

print items