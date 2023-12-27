import pytest
import subprocess

@pytest.fixture
def file_server():
    PORT = 9999
    process = subprocess.Popen(['python', 'tests/files_http_server.py', '-p', str(PORT), '-d', 'tests/example'])
    yield f'http://localhost:{PORT}'
    process.kill()


def test_end_2_end__crawler_actually_works(file_server):
    print()
    print(f'got {file_server=}')
