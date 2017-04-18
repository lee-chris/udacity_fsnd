'''
Created on Apr 17, 2017

@author: Chris
'''
import turtle

def draw_triangle(t, length):
    
    for i in range(1, 4):
        t.forward(length)
        t.left(120)
    
    
def draw_fractal():
    
    window = turtle.Screen()
    
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("green")
    
    length = 200
    
    #draw_triangle(t, length)
    
    #length = length / 2
    
    draw_triangle(t, length)
    t.forward(length)
    draw_triangle(t, length)
    t.left(120)
    t.forward(length)
    t.right(120)
    draw_triangle(t, length)
    
    length = length / 2
    
    draw_triangle(t, length)
    t.forward(length)
    draw_triangle(t, length)
    t.left(120)
    t.forward(length)
    t.right(120)
    draw_triangle(t, length)
        
    window.exitonclick()
        
        
draw_fractal()