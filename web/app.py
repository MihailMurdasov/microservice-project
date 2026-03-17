import socket
from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        hostname = socket.gethostname()
        message = f"Hello from {hostname}\n"
        self.wfile.write(message.encode("utf-8"))

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    server.serve_forever()
