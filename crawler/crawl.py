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
    def __init__(self, root_url, *, depth=10, find_urls):
        self._find_urls = find_urls
        self._seen = set()
        self._result = collections.defaultdict(list)
        root_link = _Link(root_url, depth=1)
        self._go(root_link)

    def _go(self, root_link):
        self._result[root_link.depth] = [root_link]
        self._to_explore = [root_link]
        while len(self._to_explore) > 0:
            link = self._to_explore.pop(0)
            self._add_links_from(link)

    def _add_links_from(self, link):
        links = self._find_links(link)
        self._seen.add(link)
        new_links = [link_ for link_ in links if link_ not in self._seen]
        if len(new_links) == 0:
            return

        self._result[link.depth + 1] += new_links
        self._to_explore += new_links

    def _find_links(self, link):
        urls = self._find_urls(link.url)
        return [_Link(url, link.depth + 1) for url in urls]

    def web_of_links(self):
        result = []
        for depth in range(1, len(self._result) + 1):
            links = self._result[depth]
            urls = [link.url for link in links]
            result.append(urls)

        return result
