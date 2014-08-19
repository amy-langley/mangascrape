import requests
from urlparse import urlparse
from urlparse import urlunparse
from os.path import split as pathsplit

def do_unparse(urlobj, withpath):
	tuple = urlobj[:]
	return urlunparse(tuple[0:2] + (withpath,) + tuple[3:7])

def grabfile(url, index = None):
    __, local_filename = pathsplit(urlparse(url).path)
    r = requests.get(url, stream=True)
    #print r.status_code
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename
