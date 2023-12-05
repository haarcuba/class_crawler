import dataclasses
import collections


@dataclasses.dataclass
class _Link:
    url: str
    depth: int

    def __hash__(self):
        return hash(self.url)

    def __eq__(self, other):
        return self.url == other.url

class Crawl:
    def __init__(self, root_url, *, find_links):
        self._find_links = find_links
        self._seen = set()
        self._result = collections.defaultdict(list)
        root_link = _Link(root_url, depth=0)
        self._go(root_link)

    def _go(self, root_link):
        self._result[0] = [root_link]
        self._to_explore = [root_link]
        while len(self._to_explore) > 0:
            link = self._to_explore.pop(0)
            self._add_links_from(link)

    def _add_links_from(self, link):
        urls = self._find_links(link.url)
        links = [_Link(url, link.depth + 1) for url in urls]
        self._seen.add(link)
        links = [link_ for link_ in links if link_ not in self._seen]
        if len(links) == 0:
            return

        self._result[link.depth + 1] += links
        self._to_explore += links

    def web_of_links(self):
        result = []
        for depth in range(len(self._result)):
            links = self._result[depth]
            urls = [link.url for link in links]
            result.append(urls)

        return result
