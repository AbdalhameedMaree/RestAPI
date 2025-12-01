import socketserver

import http.server

PORT = 8000

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        if self.path == "/":
            response = b'{"message": "Hello, World!"}'
        elif self.path == "/health":
            response = b'{"status": "ok"}'
        elif self.path == "/products":
            response = b'''{
                "products": [
                    {"id": 1, "name": "Product A", "price": 10.99},
                    {"id": 2, "name": "Product B", "price": 12.99},
                    {"id": 3, "name": "Product C", "price": 9.99}
                ]
            }'''
        self.wfile.write(response)

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()