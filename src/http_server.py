from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import sys

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        send_news = subprocess.run(["python3", "src/news2kindle.py"])
        message = f"Sending news ... status: {send_news.returncode}"
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', sys.argv[1]), handler) as server:
    server.serve_forever()