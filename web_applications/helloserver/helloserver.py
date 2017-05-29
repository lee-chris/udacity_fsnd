import threading
import urllib.parse

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn


class ThreadHTTPServer(ThreadingMixIn, HTTPServer):
    """This is an HTTPServer that supports thread-based concurrency."""


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


class FormHandler(BaseHTTPRequestHandler):
    """Example of GET/POST using a simple form"""
    
    def do_GET(self):
        
        self.send_response(200)
        
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        html = """
            <html>
                <body>
                    <form method="post">
                        <div>Login: <input name="l"/></div>
                        <div>Password: <input type="password" name="p"/></div>
                        <div><input type="submit" value="Submit"/></div>
                    </form>
                </body>
            </html>
            """
        
        self.wfile.write(html.encode())
    
    def do_POST(self):
        
        length = int(self.headers.get("Content-length", 0))
        data = self.rfile.read(length).decode()
        query_string = urllib.parse.parse_qs(data)
        
        login = query_string["l"][0]
        password = query_string["p"][0]
        
        message = "login: " + login + "\npassword: " + password
        
        self.send_response(200)
        
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        
        self.wfile.write(message.encode())


class PRGHandler(BaseHTTPRequestHandler):
    """Example of Post-Redirect-Get pattern"""
    
    i = 0
    
    def do_GET(self):
        
        self.send_response(200)
        
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        html = """
            <html>
                <body>
                    <div>{i}</div>
                    <form method="post">
                        <div><input type="submit" value="Add 1"/></div>
                    </form>
                </body>
            </html>
            """
        
        self.wfile.write(html.format(html, i=PRGHandler.i).encode())
    
    def do_POST(self):
        
        # increment static member variable
        PRGHandler.i += 1
        
        # set redirect reponse code
        self.send_response(303)
        
        # set redirect uri
        self.send_header("Location", "/")
        self.end_headers()


class BookmarkServer(BaseHTTPRequestHandler):
    """This http request handler stores a dict of shortcut names to full urls.
    
    On a basic GET to / a simple form will be displayed to get the URL
    and its shortcut. Then when the shortcut string is used as the path
    to the web server, the user is redirected to the saved url.    
    """
    
    bookmarks = {}
    
    def do_GET(self):
        
        path = self.path[1:]
        
        if (len(path) == 0):
            
            self.send_response(200)
            
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            html = """
                <html>
                    <body>
                        <form method="post">
                            <div>URL: <input name="url"/></div>
                            <div>Shortcut: <input name="shortcut"/></div>
                            <div><input type="submit" value="Submit"/></div>
                        </form>
                    </body>
                </html>
                """
            
            self.wfile.write(html.encode())
        
        else:
            
            # debugging
            print(path + "=>" + BookmarkServer.bookmarks.get(path, ""))
            
            if path not in BookmarkServer.bookmarks:
                
                self.send_response(404)
                
            else:
                
                # Note: the url needs to include http: if it is going to
                # another domain
                self.send_response(301)
                self.send_header("Location", BookmarkServer.bookmarks[path])
                self.end_headers()
    
    def do_POST(self):
        
        length = int(self.headers.get("Content-length", 0))
        data = self.rfile.read(length).decode()
        query_string = urllib.parse.parse_qs(data)
        
        url = query_string["url"][0]
        path = query_string["shortcut"][0]
        
        # add short to dict
        BookmarkServer.bookmarks[path] = url
        
        # redirect to main form
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()



if __name__ == "__main__":
    
    server_address = ("", 8000) #Serve on all addresses, port 8000
    httpd = ThreadHTTPServer(server_address, BookmarkServer)
    httpd.serve_forever()
