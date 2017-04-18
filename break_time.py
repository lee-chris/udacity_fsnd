'''
Created on Apr 16, 2017

@author: Chris
'''

import time
import webbrowser

i = 0

# get the current time
print("Program started on " + time.ctime())

while (i < 3):
    
    # sleep 10 seconds
    time.sleep(10)
    
    # open browser to specific url
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
    i = i + 1

print("Program ended")