class Crawl:
    def __init__(self, root_url):
        self._root_url = root_url

    def web_of_links(self):
        return [ [self._root_url] ]
