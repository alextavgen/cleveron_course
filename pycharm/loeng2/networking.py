import urllib2

URL = "http://www.gutenberg.org/files/11/11-0.txt"

data = urllib2.urlopen(URL)


def get_from_network(url):
    data = urllib2.urlopen(url)

    lines = data.readlines()
    return lines