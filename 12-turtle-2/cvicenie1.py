import turtle
import tkinter

t= turtle.Turtle()

def terc(n, farba1='blue', farba2='yellow'):
    for i in reversed(range(1, n + 1)):
        t.dot(i * 15, farba1)
        farba1, farba2 = farba2, farba1
terc(6)
turtle.done()