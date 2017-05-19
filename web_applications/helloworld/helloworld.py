import webapp2

class MainPage(webapp2.RequestHandler):
    """Simple hello world"""
    
    def get(self):
        self.response.headers["Content-Type"] = "text/plain"
        self.response.write("Hello, World!")
        

class Google(webapp2.RequestHandler):
    """Form used to do a Google search"""
    
    form = """
    <form action="http://www.google.com/search">
        <input name="q">
        <input type="submit">
    </form>
    """
    
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(self.form)


class SimpleForm(webapp2.RequestHandler):
    """Simple form that submits to TestHandler"""
    
    def get(self):
        self.response.write("""
            <form action="/testForm">
                <input name="q">
                <input type="submit">
            </form>
        """)


class TestHandler(webapp2.RequestHandler):
    
    def get(self):
        q = self.request.get("q")
        self.response.out.write(q)


app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/search", Google),
    ("/input", SimpleForm),
    ("/testForm", TestHandler)
], debug=True)
    
