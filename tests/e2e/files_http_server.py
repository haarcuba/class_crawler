import argparse
import http.server
import socketserver

def run_server(directory, port):
    class DirectoryHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

    with socketserver.TCPServer(("", port), DirectoryHandler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple HTTP server.")
    parser.add_argument('--port', '-p', type=int, default=9999, help="Specify the port on which the server will run.")
    parser.add_argument('--directory', '-d', type=str, default='.', help="Specify the directory from which to serve files.")
    arguments = parser.parse_args()

    print(f'running file server on port: {arguments.port}')
    run_server(arguments.directory, arguments.port)
