#This is Raviv's and Noam's project :)

from html.parser import HTMLParser
import argparse
import yaml
from re import search
from urllib.request import urlopen, Request
from urllib.parse import urljoin
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--depth', type=int, default=2)
    parser.add_argument('-ir', '--ignore_regex', type=str, default="^$")
    parser.add_argument('url', type=str)
    arguments = parser.parse_args()


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return

        attributes = attrs
        for name, value in attributes:
            if name != 'href':
                continue

            if search(arguments.ignore_regex, value):
                continue

            if not value in self.links:
                self.links.append(value)


def scan_urls(url):
    HTMLparser = MyHTMLParser()
    HTMLparser.feed(str(urlopen(url).read()))
    return [urljoin(url, link) for link in HTMLparser.links]

def get_web_of_links():
    levels = [{"level":i, "links":[]} for i in range(arguments.depth+1)]
    result = {"root":arguments.url, "web":levels}
    result["web"][0]["links"] = [arguments.url]
    for i in range(arguments.depth):
        for link in result["web"][i]["links"]:
            result["web"][i+1]["links"] += scan_urls(link)
    return result

if __name__ == "__main__":
    yaml.dump(get_web_of_links(), stream=sys.stdout)
