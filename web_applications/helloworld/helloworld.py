import webapp2

form = """
<form action="http://www.google.com/search">
    <input name="q">
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers["Content-Type"] = "text/plain"
        self.response.write("Hello, World!")
        

class Google(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(form)
        


app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/search", Google)
], debug=True)
    
