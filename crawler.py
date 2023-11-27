#This is Raviv's and Noam's project :)

from html.parser import HTMLParser
import argparse
from yaml import dump
from re import search
from urllib.request import urlopen, Request
from urllib.parse import urljoin

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
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    if not search(arguments.ignore_regex, attr[1]):
                        if not attr[1] in self.links:
                            self.links.append(attr[1])


def scan_urls(url):
    HTMLparser = MyHTMLParser()
    HTMLparser.feed(str(urlopen(url).read()))
    return [urljoin(url, link) for link in HTMLparser.links]

def get_yaml():
    temp = [{"level":i, "links":[]} for i in range(arguments.depth+1)]
    dictionary = {"root":arguments.url, "web":temp}
    dictionary["web"][0]["links"] = [arguments.url]
    for i in range(arguments.depth):
        for link in dictionary["web"][i]["links"]:
            dictionary["web"][i+1]["links"] += scan_urls(link)
    return dump(dictionary)

if __name__ == "__main__":
    print(get_yaml())
