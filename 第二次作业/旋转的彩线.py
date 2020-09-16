#旋转的彩线.py
import turtle
turtle.setup(1000,1000,0,0)
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange","purple"]
turtle.pensize(1)
for i in range(1800):
    turtle.left(-299)
    turtle.color(colors[i%6])
    turtle.fd(i*1.1)
    turtle.pensize(i*6/500)
turtle.Pendone()
    
    
