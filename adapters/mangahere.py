from urlparse import urlparse

from lxml import html
import requests

from utils.net import do_unparse
from utils.file import iterate_filename
from adapters.adapterbase import AdapterBase

class MangaHereAdapter(AdapterBase):

    SERIES_LIST_URL = r"http://www.mangahere.co/mangalist/"

    def enumerate_series(self):
        """Return a list of (title, url) tuples for series on this site"""
        page = requests.get(self.SERIES_LIST_URL)
        tree = html.fromstring(page.text)
        titlelinks = tree.cssselect('a.manga_info')
        items = [(i.text_content(), i.get('href')) for i in titlelinks]
        return items

    def search_series(self, search_string):
        """Return a list of (title, url) tuples for series on this site \
        matching the specified search string"""
        page = requests.get(self.SERIES_LIST_URL)
        tree = html.fromstring(page.text)
        titlelinks = tree.cssselect('a.manga_info')
        items = [(i.text_content(), i.get('href'))
                 for i in titlelinks if search_string in i.text_content()]
        return items

    def enumerate_chapters(self, series_url):
        page = requests.get(series_url)
        tree = html.fromstring(page.text)
        chapters = tree.cssselect('div.detail_list ul span.left a')
        items = [(ind, i.get('href')) for ind, i in enumerate(chapters)]
        items.reverse()
        return items

    def enumerate_images(self, chapter_url):
        page = requests.get(chapter_url)
        tree = html.fromstring(page.text)

        [baseurl] = [i.get('src')
                     for i in tree.cssselect('section.read_img img')]
        urlobj = urlparse(baseurl)
        pagecount = len(
            tree.cssselect('section.readpage_top span.right select option'))
        items = [do_unparse(urlobj, i)
                 for i in iterate_filename(urlobj.path, 1, pagecount)]
        return items
