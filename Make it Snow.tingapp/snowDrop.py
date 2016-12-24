import tingbot
from tingbot import screen
import random
from random import randint
import remap
from remap import *

maxDepth = 20
minSpeed = 1
maxSpeed = 6
minLength = 3
maxLength = 20
minStroke = 1
maxStroke = 2
minFlake = 1
maxFlake = 3

class Drop:
    def __init__(self):
        # Position
        self.x = randint(0, screen.width) # Across the screen width
        self.y = randint(-(screen.height + 100), -100) # On top of the screen
        # Depth
        self.z = randint(0, maxDepth) # Third dimension
        # Proportionnal to the Depth
        self.yspeed = remap(self.z, 0, maxDepth, minSpeed, maxSpeed)
        self.length = remap(self.z, 0, maxDepth, minLength, maxLength)
        self.stroke = remap(self.z, 0, maxDepth, minStroke, maxStroke)
        self.snowFlake = remap(self.z, 0, maxDepth,  minFlake, maxFlake)
    
    def fall(self):
        self.y += self.yspeed # Move down from speed
        self.yspeed += 0.05 # Increase speed for gravity
        # Drop reaches the bottom
        if self.y > screen.height:
            self.y = randint(-(screen.height + 100), -100)
            self.yspeed = remap(self.z, 0, maxDepth, minSpeed, maxSpeed)

    def show(self):
        # Vertical
        screen.line(
            start_xy = (self.x, self.y - self.length/2),
            end_xy = (self.x, self.y + self.length/2),
            color = 'white',
            width = int(self.stroke),
            )
        # Horizontal
        screen.line(
            start_xy = (self.x - self.length/2 , self.y),
            end_xy = (self.x + self.length/2, self.y),
            color = 'white',
            width = int(self.stroke),
            )
        # Diagonal top left to bottom right (bit shorter)
        screen.line(
            start_xy = (self.x - self.length/2 + self.snowFlake, self.y - self.length/2 + self.snowFlake),
            end_xy = (self.x + self.length/2 - self.snowFlake, self.y + self.length/2 - self.snowFlake),
            color = 'white',
            width = int(self.stroke),
            )
        # Diagonal bottom left to top right (bit shorter)
        screen.line(
            start_xy = (self.x + self.length/2 - self.snowFlake, self.y - self.length/2 + self.snowFlake),
            end_xy = (self.x - self.length/2 + self.snowFlake, self.y + self.length/2 - self.snowFlake),
            color = 'white',
            width = int(self.stroke),
            )
    