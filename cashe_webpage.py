from urllib.request import urlopen
import time
class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None
        self.timex = time.time()
    @property
    def content(self, n):
        #timer = time.time()
        #now_time = n + 1 + timer
        if time.time() - self.timex < n:
            if not self._content:
                print("Retrieving New Page...")
                self._content = urlopen(self.url).read()
            #now_time = time.time()
        #else:
            #timer = time.time()
        #if timer - now_time < n:
            #self._content = urlopen(self.url).read()
        return self._content

