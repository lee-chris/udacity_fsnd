'''
Created on Apr 20, 2017

@author: Chris
'''

'''
Read the contents of a text file
'''
def read_text(file_name):
    
    quotes = open(file_name)
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()


read_text("movie_quotes.txt") 