# Write a program to print the users name
name = input('What is your name? ')
print('Hello, {}'.format(name))
​
# Write a program to determine the users favourite animal
animal = input('Do you like dogs or cats more? ')
pet_name = input('What would name your pet? ')
print('You like {} and you would name your pet {}'.format(animal, pet_name))
​
# Write a program to calculate how many apples you have
purchased_apples = input('How many apples did you buy? ')
total_apples = int(purchased_apples) + 5
print(total_apples)
​
# Write a program to calculate the amount of pizza you need to feed all your friends
friends = int(input('How many friends do you have? '))
pizzas = friends * 0.5
print('You need {} pizzas for {} friends'.format(pizzas, friends))

# Draw a coloured square
import turtle
​
side_length = 200
angle = 90
​
turtle.color('red', 'pink')
turtle.begin_fill()
​
turtle.forward(side_length)
turtle.right(angle)
​
turtle.forward(side_length)
turtle.right(angle)
​
turtle.forward(side_length)
turtle.right(angle)
​
turtle.forward(side_length)
turtle.right(angle)
​
turtle.end_fill()
​
turtle.done()
​
# Draw a coloured triangle
import turtle
​
side_length = 100
angle = 120
​
turtle.color('blue', 'blue')
turtle.begin_fill()
​
turtle.forward(side_length)
turtle.right(angle)
​
turtle.forward(side_length)
turtle.right(angle)
​
turtle.forward(side_length)
turtle.right(angle)
​
turtle.end_fill()
​
turtle.done()
# Draw a coloured square using a loop
import turtle
​
side_length = 200
angle = 90
​
turtle.color('pink', 'red')
turtle.begin_fill()
​
for side in range(4):
    turtle.forward(side_length)
    turtle.right(angle)
​
turtle.end_fill()
​
turtle.done()
​
# Draw a coloured shape using a loop that takes a user input for number of sides
​
import turtle
​
sides = int(input('Number of sides: '))
​
angle = 360 / sides
side_length = 60
​
turtle.color('pink', 'red')
turtle.begin_fill()
​
for side in range(sides):
    turtle.forward(side_length)
    turtle.right(angle)
​
turtle.end_fill()
​
turtle.done()
​
# Draw a coloured triangle using a loop
import turtle
​
side_length = 200
angle = 120
​
turtle.color('pink', 'red')
turtle.begin_fill()
​
for side in range(3):
    turtle.forward(side_length)
    turtle.right(angle)
​
turtle.end_fill()
​
turtle.done()

# Write a function that will draw a coloured square
import turtle
​
def square():
    side_length = 100
    angle = 90
​
    turtle.color('pink', 'red')
    turtle.begin_fill()
​
    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)
​
    turtle.end_fill()
​
square()
turtle.done()
​
# Write a function that will draw a coloured triangle
import turtle
​
def triangle():
    side_length = 100
    angle = 120
​
    turtle.color('pink', 'red')
    turtle.begin_fill()
​
    for side in range(3):
        turtle.forward(side_length)
        turtle.right(angle)
​
    turtle.end_fill()
​
triangle()
turtle.done()
​
# Write a function that will draw a coloured square, which will take in an argument for side_length
import turtle
​
def square(side_length):
    angle = 90
​
    turtle.color('pink', 'red')
    turtle.begin_fill()
​
    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)
​
    turtle.end_fill()
​
square(100)
turtle.done()
​
# Write a function that will draw a coloured triangle, which will take in an argument for side_length
import turtle
​
def triangle(side_length):
    angle = 120
​
    turtle.color('pink', 'red')
    turtle.begin_fill()
​
    for side in range(3):
        turtle.forward(side_length)
        turtle.right(angle)
​
    turtle.end_fill()
​
triangle(100)
turtle.done()
# Write a function that will calculate the area of a circle, taking in an argument for the radius, and return the value
def circle_area(radius):  # add the radius argument inside the brackets
    area = 3.14 * (radius ** 2)
    return area
​
circle_1 =  circle_area(10)
print(circle_1)

# another solution

import turtle
# Rather than trying to draw my house all in one go, I've split it into functions for each part of the house I want to
# draw. So I have a function for the main body of the house, the roof, door and windows.
def draw_roof(colour):
    # You can use hexadecimal colour codes to get even more colours - https://htmlcolorcodes.com/color-picker/
    turtle.fillcolor(colour)
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(135)
    turtle.forward(400)
    turtle.end_fill()
def draw_house(colour):
    # Using a for loop to make the main square of the house
    turtle.fillcolor(colour)
    turtle.begin_fill()
    for side in range(4):  # Loops from 0 - 3, so we get 4 sides to the house
        turtle.forward(300)
        turtle.right(90)
    turtle.end_fill()
def draw_door(colour):
    # Using a for loop to make the main square of the house
    turtle.fillcolor(colour)
    turtle.begin_fill()
    for side in range(2):  # Loops from 0 - 3, so we get 4 sides to the house
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    # drawing a doorknob
    # You can call functions from inside other functions
    move_pen(220, -250)
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
def draw_window(size, colour):
    turtle.fillcolor(colour)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
# a helper function to move the pen to a new place on the screen
# It takes the coordinates I want to move to as arguments
def move_pen(x, y):
    # the penup() function lifts the turtle pen, so you don't draw while it moves!
    turtle.penup()
    turtle.goto(x, y)
    # don't forget to put the pen back down again!
    turtle.pendown()
# Calling all the functions to draw the house!
# Another cool function to set the background colour - going for a blue sky!
def draw_full_house():
    turtle.bgcolor('light blue')
    draw_roof('#E03C26')
    move_pen(360, -300)
    draw_house('#FFF5B8')
    move_pen(230, -300)
    draw_door('red')
    move_pen(130, -20)
    draw_window(40, 'blue')
    move_pen(300, -20)
    draw_window(40, 'blue')
    turtle.done()
draw_full_house()
React











​​
​
​
