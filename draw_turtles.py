'''
Created on Apr 17, 2017

@author: Chris
'''
import turtle

def draw_square(window):
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
    for i in range(1, 5):
        
        brad.forward(100)
        brad.right(90)


def draw_circle(window):
    
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    

def draw_triangle(window):
    
    jen = turtle.Turtle()
    jen.shape("circle")
    jen.color("white")
    
    for i in range(1, 4):
        
        jen.forward(200)
        jen.right(120)


def draw_shapes():
    
    window = turtle.Screen()
    window.bgcolor("red")
    
    draw_square(window)
    draw_circle(window)
    draw_triangle(window)
    
    window.exitonclick()

#draw_shapes()

def draw_art():
    
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
    for j in range(1, 37):
        for i in range(1, 5):
            
            brad.forward(100)
            brad.right(90)
        
        brad.right(10)
    
    window.exitonclick()


draw_art()