import time
from urllib.request import urlopen
import cashe_webpage


webpage = WebPage("https://www.gutenberg.org/wiki/Animals-Domestic_(Bookshelf)")
def test(webpage):
    content1 = webpage.content
    content2 = webpage.content
    if content1 == content2:
        return True
    else:
        return False
