from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    """Simple example http handler"""
    
    def do_GET(self):
        
        # Set server response code
        self.send_response(200)
        
        # Set response headers
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        
        # Write response body
        self.wfile.write("Hello, HTTP!\n".encode())


class EchoHandler(BaseHTTPRequestHandler):
    """This handler echoes back the request path in the response body"""
    
    def do_GET(self):
        
        self.send_response(200)
        
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        
        message = self.path[1:] # Extract 'bears' fram '/bears', for example
        message_bytes = message.encode()
        self.wfile.write(message_bytes)


if __name__ == "__main__":
    server_address = ("", 8000) #Serve on all addresses, port 8000
    httpd = HTTPServer(server_address, EchoHandler)
    httpd.serve_forever()
