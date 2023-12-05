import crawler.crawl
from testix import *

def test_no_links__return_only_root_url():
    with Scenario() as s:
        s.find_links('root') >> []

        tested = crawler.crawl.Crawl('root', find_urls=Fake('find_links'))
        assert tested.web_of_links() == [
                ['root'],
           ]

def test_depth_2_link_tree():
    with Scenario() as s:
        s.find_links('root') >> ['link1', 'link2']
        s.find_links('link1') >> []
        s.find_links('link2') >> []

        tested = crawler.crawl.Crawl('root', find_urls=Fake('find_links'))
        assert tested.web_of_links() == [
                ['root'],
                ['link1', 'link2'],
           ]

def test_edge_case__depth_2_loop():
    with Scenario() as s:
        s.find_links('root') >> ['link1', 'link2']
        s.find_links('link1') >> []
        s.find_links('link2') >> ['root']

        tested = crawler.crawl.Crawl('root', find_urls=Fake('find_links'))
        assert tested.web_of_links() == [
                ['root'],
                ['link1', 'link2'],
           ]

def test_depth_4_link_tree():
    with Scenario() as s:
        s.find_links('root') >> ['link1', 'link2']
        s.find_links('link1') >> ['link1.1', 'link1.2']
        s.find_links('link2') >> ['link2.1']
        s.find_links('link1.1') >> []
        s.find_links('link1.2') >> ['link1.2.1']
        s.find_links('link2.1') >> []
        s.find_links('link1.2.1') >> []

        tested = crawler.crawl.Crawl('root', find_urls=Fake('find_links'))
        assert tested.web_of_links() == [
                ['root'],
                ['link1', 'link2'],
                ['link1.1', 'link1.2', 'link2.1'],
                ['link1.2.1',]
           ]
