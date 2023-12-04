class Crawl:
    def __init__(self, root_url, *, find_links):
        self._root_url = root_url
        find_links(root_url)

    def web_of_links(self):
        return [ [self._root_url] ]
