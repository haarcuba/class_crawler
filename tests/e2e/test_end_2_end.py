import pytest
import subprocess
import signal
import crawler.crawl
import crawler.find_urls
import random


@pytest.fixture
def file_server():
    PORT = random.randint(10000, 65000)
    process = subprocess.Popen(['python', 'tests/e2e/files_http_server.py', '-p', str(PORT), '-d', 'tests/e2e/example'])
    yield f'http://localhost:{PORT}'
    process.send_signal(signal.SIGINT)


def test_end_2_end__crawler_actually_works(file_server):
    tested = crawler.crawl.Crawl(file_server, depth=100, find_urls=crawler.find_urls.FindUrls())
    assert tested.web_of_links() == [
        [f'{file_server}'],
        [f'{file_server}/a/', f'{file_server}/d/', f'{file_server}/myfile.html'],
        [f'{file_server}/a/b/', f'{file_server}/a/myfile.html', f'{file_server}/d/myfile.html'],
        [f'{file_server}/a/b/c/', f'{file_server}/a/b/myfile.html'],
        [f'{file_server}/a/b/c/c.html'],
    ]
