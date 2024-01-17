import urllib.request
import urllib.parse
import crawler.links


def _url_parser(url):
    def url_parse(link):
        return urllib.parse.urljoin(url, link)
    return url_parse


class FindUrls:
    def __init__(self, parser=crawler.links.Links):
        self.parser = parser

    def __call__(self, url):
        html = urllib.request.urlopen(url).read()
        parsed = self.parser(str(html))
        links = parsed.all()
        return map(_url_parser(url), links)
