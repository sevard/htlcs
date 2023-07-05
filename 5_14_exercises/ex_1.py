#!/usr/bin/env python3

import turtle


def draw_bar(t, height):
    """Get turtle t to draw one bar, of height"""
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.write(f"  {height}", font=("Arial", 20, "normal"))
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()


wn = turtle.Screen()
wn.bgcolor('lightgreen')

tess = turtle.Turtle()
tess.color('blue', 'red')
tess.pensize(3)
tess.penup()
tess.setpos((-150, -70))
tess.pendown()

xs = [48, 117, 200, 240, 160, 260, 220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()
