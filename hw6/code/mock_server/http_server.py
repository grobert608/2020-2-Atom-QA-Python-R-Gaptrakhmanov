import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

import requests


class StubHandleRequests(BaseHTTPRequestHandler):
    data = None
    users = ['Rob', 'Ivan']

    def _set_headers(self):
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/timeout':
            time.sleep(1)
        elif self.path == '/errorfzz':
            self.send_response(500)
            self._set_headers()
        elif self.path == '/auth':
            login = self.headers['Authorization']
            if str(login) in self.users:
                self.send_response(200)
                self.send_header('Authorization', f'{login}')
                self._set_headers()
            else:
                self.send_response(403)
                self._set_headers()
        else:
            self.send_response(200)
            self._set_headers()
        self.wfile.write(self.data)


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.data = post_data
        self.send_response(200)
        self._set_headers()
        self.wfile.write(self.data)

    def do_PUT(self):
        self.do_POST()


class SimpleHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = StubHandleRequests
        self.handler.data = None
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever, daemon=True)
        th.start()
        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()

    def set_data(self, data):
        self.handler.data = json.dumps(data).encode()


if __name__ == '__main__':
    server = SimpleHTTPServer('127.0.0.1', 5005)
    server.start()
    response = requests.post('http://127.0.0.1:5005/', json.dumps({'company': 'BMW', 'car': 'X5'}))
    print(response.content)
    print(json.loads(response.content.decode()))
    server.stop()
