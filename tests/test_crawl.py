import crawler.crawl
from testix import *

def test_no_links__return_only_root_url():
    with Scenario() as s:
        s.find_links("http://localhost:9999") >> []

        tested = crawler.crawl.Crawl("http://localhost:9999", find_links=Fake('find_links'))
        assert tested.web_of_links() == [
                ["http://localhost:9999"],
           ]
