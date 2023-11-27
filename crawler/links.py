import html.parser


class _LinksParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return

        for name, value in attrs:
            if name != 'href':
                continue

            self.links.append(value)

class Links:
    def __init__(self, html):
        self._parser = _LinksParser()
        self._parser.feed(html)

    def all(self):
        return self._parser.links
