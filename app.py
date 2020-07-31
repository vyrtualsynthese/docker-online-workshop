import http.server as SimpleHTTPServer
import socketserver as SocketServer
import logging

PORT = 3000

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write("Hello World!".encode("utf-8"))

Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print(f"Server listen on http://127.0.0.1:{PORT}")
httpd.serve_forever()
