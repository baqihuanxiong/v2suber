from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from urllib.parse import urlparse

PORT = 8079
DATA_DIR = "/data"


class Subscription(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path_params = parsed_path.path.split("/")[1:]
        if len(path_params) != 2:
            self.send_response(400)
            self.end_headers()
            return

        usr, profile = path_params[0], path_params[1]

        try:
            with open(f"{DATA_DIR}/{usr}/{profile}", 'r') as fh:
                content = fh.read()
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    with TCPServer(("", PORT), Subscription) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
