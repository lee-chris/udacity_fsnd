'''
Created on Apr 17, 2017

@author: Chris
'''
import turtle
import math

def draw_triangle(t, length):
    
    for i in range(1, 4):
        t.forward(length)
        t.left(120)


def draw_triforce(t, length, depth):
    
    if (depth == 0):
        draw_triangle(t, length)
    
    else:
        depth = depth - 1
        length = length / 2
        
        # draw bottom left
        draw_triforce(t, length, depth)
        
        t.forward(length)
        
        # draw bottom right
        draw_triforce(t, length, depth)
        
        t.left(120)
        t.forward(length)
        t.right(120)
        
        # draw top
        draw_triforce(t, length, depth)
        
        # reset turtle to bottom left corner
        t.right(120)
        t.forward(length)
        t.left(120)


def draw_fractal():
    
    window = turtle.Screen()
    
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("green")
    t.speed(0)
    
    length = 800
    
    # move turtle to lower left
    t.penup()
    t.right(90)
    t.forward(math.sqrt((length ** 2 - (length / 2) ** 2)) / 2)
    t.right(90)
    t.forward(length / 2)
    t.right(180)
    t.pendown()
    
    draw_triforce(t, length, 8)
    
    window.exitonclick()


draw_fractal()