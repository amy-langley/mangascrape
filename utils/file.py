import os
import shutil
import tempfile

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

#with mkdtemp("foo", chdir=True) as dirname:
#    print "I'm in", dirname