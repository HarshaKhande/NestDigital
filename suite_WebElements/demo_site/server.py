# -*- coding: utf-8 -*-
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
HERE = Path(__file__).resolve().parent
os.chdir(HERE)
host, port = "127.0.0.1", 8000
print("Squish demo site running at http://%s:%s" % (host, port))
print("Press Ctrl+C to stop.")
ThreadingHTTPServer((host, port), SimpleHTTPRequestHandler).serve_forever()
