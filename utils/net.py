import requests
from urlparse import urlparse
from urlparse import urlunparse
from os.path import split, splitext

def do_unparse(urlobj, withpath):
	tuple = urlobj[:]
	return urlunparse(tuple[0:2] + (withpath,) + tuple[3:7])

def grabfile(url, local_file = None):
    __, remote_name = split(urlparse(url).path)
    __, remote_ext = splitext(remote_name)
    local_file = local_file or remote_name
    local_file = ''.join([local_file, remote_ext])
    r = requests.get(url, stream=True)
    #print r.status_code
    with open(local_file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_file
