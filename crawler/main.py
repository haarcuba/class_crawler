import argparse
import crawl
import find_urls
import links
import sys
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--depth', type=int, default=2)
    parser.add_argument('-ir', '--ignore_regex', type=str, default='^$')
    parser.add_argument('url', type=str)
    arguments = parser.parse_args()
    urls = crawl.Crawl(arguments.url,
                       depth=arguments.depth,
                       ignore_pattern=arguments.ignore_regex,
                       find_urls=find_urls.FindUrls(links.Links))\
        .web_of_links()
    urls_formatted = {f"level {i}": {"links": j} for i, j in enumerate(urls)}
    yaml.dump(urls_formatted, stream=sys.stdout)


if __name__ == "__main__":
    main()
