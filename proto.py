import os

from utils.file import mkdtemp
from utils.net import grabfile
from adapters.mangahere import MangaHereAdapter

# find . -name '*.py' -type f -not -path "*venv*" | xargs wc -l

adapter = MangaHereAdapter()
__, series_url = adapter.search_series('Hourou Musuko')[0]
chapters = [url for index, url in adapter.enumerate_chapters(series_url)][0:1]
allitems = [(chapter_url, adapter.enumerate_images(chapter_url)) for chapter_url in chapters]

with mkdtemp("foo", chdir=True) as dirname:
    for chapter_url, items in allitems:
        print "From " + chapter_url
        for index, item in enumerate(items):
            print "Fetching page " + str(index+1)
            grabfile(item)
    for fn in os.listdir(dirname):
        print fn
