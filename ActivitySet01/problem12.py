from turtle import *
 
bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
     color('red')
     circle(i)
     color("orange")
     circle(i*0.9)
     right(3)
     forward(5)
done()