"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Evan Valencia

********* HEY, READ THIS FIRST **********

This is a description of the code that is written out below. This script is start code for PC04 + beyond. 
It imports random and math libraries along with the turtle libraries.
You should add your name(s), to line 4, and replace this description with one that describes what your code does!
(Hint: what patterns does it make? should it evoke any emotions?

"""
import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
turtle.tracer(0)

#make color pallet
SPOOKY = ["orange", "black", "grey"]

#create 1 random x value and 1 random y value to be used as locations for swirls
place1 = random.randint(1, 300)
place2 = random.randint(1, 300)

#make first turtle
swirlTurt1 = turtle.Turtle()

#randomize thickness of pen
thickness = random.randint(1, 5)
swirlTurt1.penup()
swirlTurt1.goto(-place1,place2)
swirlTurt1.pensize(thickness)
panel.bgcolor(SPOOKY[1])
swirlTurt1.color(SPOOKY[0])
swirlTurt1.pendown()

#create first swirl
for i in range(50):
    swirlTurt1.forward(5+i)
    swirlTurt1.right(15)
    
#make second turtle
swirlTurt2 = turtle.Turtle()

swirlTurt2.penup()
swirlTurt2.goto(place1,-place2)
swirlTurt2.color(SPOOKY[2])
swirlTurt2.pendown()
swirlTurt2.pensize(thickness)

#create seconf swirl
for i in range(50):
    swirlTurt2.forward(5+i)
    swirlTurt2.right(15)
    
    
    



# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
# turtle.done()
