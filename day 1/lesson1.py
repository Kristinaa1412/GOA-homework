print("hello world")
print("Kristina Tikurishvili")

#20.01.2024 year
print(5)  #integer int
print("5")  #string #str
print(5 + int("5"))
print("Kristina Tikurishvili "  + "38" + " wlis ") 
from turtle import *

#we want to paint a house

#step 1 draw a square
speed(10)

width(7)

color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill() 

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()   


#drawing window 1
penup()
goto(60, 120)
pendown()


color("brown")
begin_fill()
right(60)

forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


#drawing window 2
penup()
goto(190, 170)
pendown()

color("brown")
begin_fill()

right(90)

forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()




exitonclick()