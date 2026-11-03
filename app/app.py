import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = os.environ.get("APP_VERSION", "v1")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = {
            "status": "ok",
            "message": VERSION
        }

        body = json.dumps(response).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


server = HTTPServer(("0.0.0.0", 8888), Handler)
print("Application running on port 8888")
server.serve_forever()
