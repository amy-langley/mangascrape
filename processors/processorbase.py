import abc
import os

from PIL import Image

class ProcessorBase(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def resample(self, path, outputspec):
        """Resample the file to the specified dimensions"""
        return

    def describe(self, path):
        with Image.open(path) as im:
            __, name = os.path.split(path)
            print name, im.format, im.size, im.mode
        return

