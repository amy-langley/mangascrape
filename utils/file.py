import os
import shutil
import tempfile
import os.path
import re

def iterate_filename(sample, min, max):
    path, sample = os.path.split(sample)
    sample, ext = os.path.splitext(sample)
    match = re.match(r"(?P<prefix>.*)\D(?P<varies>\d+)",sample)
    prefix = match.group('prefix')
    varylen = len(match.group('varies'))
    items = [os.path.join(path, prefix + '.' + str(i).zfill(varylen) + ext) for i in range(min,max+1)]
    return items

class mkdtemp(object):

    def __init__(self, *args, **kwargs):
        self.should_chdir = kwargs.pop("chdir")
        self.original_dir = None
        self.dirname = tempfile.mkdtemp(*args, **kwargs)

    def __enter__(self):
        if self.should_chdir:
            self.original_dir = os.getcwd()
            os.chdir(self.dirname)
        return self.dirname

    def __exit__(self, *exc):
        if self.original_dir:
            os.chdir(self.original_dir)
        shutil.rmtree(self.dirname)

# with mkdtemp("foo", chdir=True) as dirname:
#    print "I'm in", dirname
