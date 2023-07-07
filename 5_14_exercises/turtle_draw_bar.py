#!/usr/bin/env python3

import turtle


def draw_bar(t, height):
    """Get turtle t to draw one bar, of height"""
    t.begin_fill()
    t.left(90)
    t.forward(height)
    if height > 0:
        t.right(90)
        t.write(f" {height}", font=("Arial", 18, "normal"))
    else:
        t.penup()
        t.forward(-21)
        t.write(f"{height}", font=("Arial", 18, "normal"))
        t.back(-21)
        t.pendown()
        t.right(90)
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
tess.speed(8)
tess.color('blue', 'red')
tess.pensize(3)
tess.penup()
tess.setpos((-200, -70))
tess.pendown()

xs = [48, -117, -200, 240, 160, 260, 220, -20]

for a in xs:
    if a >= 200:
        tess.color('blue', 'red')
    elif a >= 100 and a < 200:
        tess.color('blue', 'yellow')
    elif a < 100:
        tess.color('blue', 'green')
    draw_bar(tess, a)

wn.mainloop()
