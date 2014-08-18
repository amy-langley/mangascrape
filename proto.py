import os

from utils.file import mkdtemp
from utils.net import grabfile
from adapters.mangahere import MangaHereAdapter

SAMPLE_URL = r"http://www.mangahere.co/manga/hourou_musuko/v01/c001/"

adapter = MangaHereAdapter()
items = adapter.enumerate_images(
    SAMPLE_URL)

print "From " + SAMPLE_URL
with mkdtemp("foo", chdir=True) as dirname:
    for index, item in enumerate(items):
        print "Fetching page " + str(index+1)
        grabfile(item)
    for fn in os.listdir(dirname):
        print fn
