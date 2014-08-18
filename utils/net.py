import requests
from urlparse import urlparse
from urlparse import urlunparse
from os.path import split as pathsplit


def grabfile(url):
    __, local_filename = pathsplit(urlparse(url).path)
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename
