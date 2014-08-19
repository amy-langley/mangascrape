import os
import sys

from utils.file import mkdtemp
from utils.net import grabfile
from adapters.mangahere import MangaHereAdapter
from processors.grayscale import GrayscaleProcessor
from processors.color import ColorProcessor
import targets.nook

# find . -name '*.py' -type f -not -path "*venv*" | xargs wc -l

target = targets.nook.SIMPLE_TOUCH
print target

print 'Fetching metadata'
adapter = MangaHereAdapter()
__, series_url = adapter.search_series('Hourou Musuko')[0]
print 'Located series'
chapters = [url for index, url in adapter.enumerate_chapters(series_url)][0:2]
print 'Loaded chapters'
allitems = [(chapter_url, adapter.enumerate_images(chapter_url)[0:2])
            for chapter_url in chapters]
print 'Loaded image list'

processor = None

if target.is_color:
    processor = ColorProcessor()
else:
    processor = GrayscaleProcessor()

# TODO: AR: find a way to solve this problem that doesn't introduce order
# dependency
seq_offset = 1
with mkdtemp("foo", chdir=True) as dirname:
    for chapter_url, items in allitems:
        print "From " + chapter_url
        for index, item in enumerate(items):
            print "Fetching page " + str(index + 1)
            grabfile(item, str(index + seq_offset).zfill(6))
        seq_offset += len(items)
    print dirname
    for fn in os.listdir(dirname):
        processor.describe(os.path.join(dirname, fn))
    print 'Complete; press Enter to terminate'
    sys.stdin.read(1)
