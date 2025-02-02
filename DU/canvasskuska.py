import turtle

t = turtle.Turtle()
t.lt(30)
for i in range(3, 300, 3):
    t.fd(i)
    t.rt(90)
turtle.done()