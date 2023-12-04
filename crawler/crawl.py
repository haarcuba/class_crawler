class Crawl:
    def __init__(self, root_url, *, find_links):
        self._find_links = find_links
        self._go(root_url)

    def _go(self, root_url):
        self._result = [[root_url]]
        self._to_explore = [root_url]
        while len(self._to_explore) > 0:
            url = self._to_explore.pop(0)
            self._add_links_from(url)

    def _add_links_from(self, url):
        links = self._find_links(url)
        if len(links) == 0:
            return
        self._result.append(links)
        self._to_explore += links

    def web_of_links(self):
        return self._result
