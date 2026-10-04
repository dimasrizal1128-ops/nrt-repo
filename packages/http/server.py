from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent / "www"
HOST = "0.0.0.0"
PORT = 8080

ROOT.mkdir(exist_ok=True)

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

print(f"NRT HTTP Server")
print(f"Root: {ROOT}")
print(f"Listening on http://{HOST}:{PORT}")

server = ThreadingHTTPServer((HOST, PORT), Handler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nHTTP server stopped.")
finally:
    server.server_close()
