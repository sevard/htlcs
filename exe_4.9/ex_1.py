#!/usr/bin/env python3


import turtle


def make_window(colr, ttle):
    """
        Set up the window with the given background color and title.
        Returns the new window
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, sz):
    """ 
        Set up a turtle with the given color and pensize.
        Returns the new turtle     
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t


def draw_square(t, sz):
    """
        Make a given turtle to draw a square.
        Returns None.
    """
    for i in range(4):
        t.forward(sz)
        t.left(90)


def set_position(t, x=0, y=0):
    """
      Set up position of a given turtle t. 
      Parameter x corresponds to position x 
      Parameter y corresponds to position y 
      Returns None.
    """
    tess.penup()
    tess.setpos(-100, 0)
    tess.pendown()


wn = make_window("Lightgreen", "Tess and Alex dancing")

tess = make_turtle("hotpink", 5)
# alex = make_turtle("black", 1)
# dave = make_turtle("yellow", 2)

set_position(tess, -100, 0)

for i in range(5):
    draw_square(tess, 20)
    tess.penup()
    tess.forward(40)
    tess.pendown()

wn.mainloop()
