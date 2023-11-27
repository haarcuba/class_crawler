import crawler.crawl

def test_no_links__return_only_root_url():
    tested = crawler.crawl.Crawl("http://localhost:9999")
    assert tested.web_of_links() == [
            ["http://localhost:9999"],
       ]
