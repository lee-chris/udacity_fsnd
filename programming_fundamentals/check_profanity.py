'''
Created on Apr 20, 2017

@author: Chris
'''

'''
Read the contents of a text file
'''
import urllib.request

def read_text(file_name):
    
    quotes = open(file_name)
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    
    url = "http://www.wdylike.appspot.com"
    values = {"q" : text_to_check}
    
    # URL encode the inputs
    data = urllib.parse.urlencode(values)
    
    # Send POST request, make sure to encode data as bytes
    # Doesn't work with this url.
    # req = urllib.request.Request(url, data.encode())
    
    # With just using url parameter, this sends GET request
    req = urllib.request.Request(url + "?" + data)
    
    connection = urllib.request.urlopen(req)
    output = connection.read()
    print(output)
    connection.close()


read_text("movie_quotes.txt")
#check_profanity("fuck you") 