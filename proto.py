from lxml import html
import requests
from utils.file import mkdtemp, iterate_filename
from utils.net import grabfile, do_unparse
from urlparse import urlparse
import os
import adapters.mangahere

SAMPLE_URL = r"http://www.mangahere.co/manga/hourou_musuko/v01/c001/"

adapter = adapters.mangahere.MangaHereAdapter()
items = adapter.enumerate_images(
    SAMPLE_URL)

print "From " + SAMPLE_URL
with mkdtemp("foo", chdir=True) as dirname:
    for index, item in enumerate(items):
        print "Fetching page " + str(index+1)
        grabfile(item)
    for fn in os.listdir(dirname):
        print fn
