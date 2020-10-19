import sys
import socketserver
from http.server import SimpleHTTPRequestHandler
import logging
import settings


"""
Server setup
Enables CORS, Fix for WASM MIME  Type for older Python versions 
"""

class Handler(SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header("Content-type", "text/html")
        super().end_headers()


if sys.version_info < (3, 7, 5):
    Handler.extensions_map['.wasm'] = 'application/wasm'

def run():
    port = int(settings.PORT)
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("Serving at: {}".format(port))
        httpd.serve_forever()

if __name__ == '__main__':
    run()
