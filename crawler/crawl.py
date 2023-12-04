import collections

class Crawl:
    def __init__(self, root_url, *, find_links):
        self._find_links = find_links
        self._seen = set()
        self._result = collections.defaultdict(list)
        self._go(root_url)

    def _go(self, root_url):
        self._result[0] = [root_url]
        self._to_explore = [(0, root_url)]
        while len(self._to_explore) > 0:
            depth, url = self._to_explore.pop(0)
            self._add_links_from(depth, url)

    def _add_links_from(self, depth, url):
        links = self._find_links(url)
        self._seen.add(url)
        links = [link for link in links if link not in self._seen]
        if len(links) == 0:
            return

        self._result[depth + 1] += links
        self._to_explore += [(depth + 1, link) for link in links]

    def web_of_links(self):
        result = []
        for depth in range(len(self._result)):
            links = self._result[depth]
            result.append(links)

        return result
