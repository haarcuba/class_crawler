import pytest
import subprocess
import crawler.crawl
import crawler.links


@pytest.fixture
def file_server():
    PORT = 9999
    process = subprocess.Popen(['python', 'tests/files_http_server.py', '-p', str(PORT), '-d', 'tests/example'])
    yield f'http://localhost:{PORT}'
    process.kill()


def test_end_2_end__crawler_actually_works(file_server):
    tested = crawler.crawl.Crawl(file_server, depth=100, find_urls=crawler.links.Links)
    assert list(map(set, tested.web_of_links())) == [
        {f'{file_server}'},
        {f'{file_server}/a/', f'{file_server}/d/', f'{file_server}/myfile.html'},
        {f'{file_server}/a/b/', f'{file_server}/a/myfile.html', f'{file_server}/d/myfile.html'},
        {f'{file_server}/a/b/c/', f'{file_server}/a/b/myfile.html'},
        {f'{file_server}/a/b/c/c.html'},
    ]
