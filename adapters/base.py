import abc


class AdapterBase(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def enumerate_series(self):
        """Return a list of (title, url) tuples for series on this site"""
        return

    @abc.abstractmethod
    def search_series(self, search_string):
        """Return a list of (title, url) tuples for series on this site \
           matching the specified search string"""
        return

    @abc.abstractmethod
    def enumerate_chapters(self, url):
        """Return a list of (index, url) tuples for the chapters \
        of this manga"""
        return

    @abc.abstractmethod
    def enumerate_images(self, chapter_url):
        """Return a list of urls for images in this chapter"""
        return
