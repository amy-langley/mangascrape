from lxml import html
import requests
from urlparse import urlparse
from urlparse import urlunparse
from utils.mkdtemp import mkdtemp

def download_file(url):
    local_filename = urlparse(url).path.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

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

for item in items:
    download_file(item)

print items
