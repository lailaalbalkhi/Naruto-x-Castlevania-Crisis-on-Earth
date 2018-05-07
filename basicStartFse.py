#Importing necessary libraries
from pygame import *
from random import *
from math import *
from tkinter import *

#Defining colours and other constants
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RUNNING = True

#Defining player variables
xPos = 20
yPos = 20
hurtbox = Rect(xPos, yPos, 20, 20) #hurtbox[:2] to be adjusted depending on player size
xSpeed = 0
ySpeed = 0
health = 100
player = [hurtbox, xSpeed, ySpeed, health]

#Defining screen variables
SIZE = (1000, 800)
screen = display.set_mode(SIZE)

#defining level functions





#starting main game loop
while RUNNING:
    for evt in event.get():
        if evt.type == QUIT: 
            RUNNING = False
    hurtbox[0] += 1
    hurtbox = Rect(xPos, yPos, 20, 20)
    player = [hurtbox, xSpeed, ySpeed, health]
    print(player)


#is this working?


#blah

quit()
