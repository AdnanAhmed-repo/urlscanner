import urllib.request
import import

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request(path + "robots_txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()

