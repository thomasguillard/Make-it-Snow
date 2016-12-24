import tingbot
from tingbot import *
import snowDrop
from snowDrop import *
import remap
from remap import *

'''
Inspired by Daniel Shiffman's "Purple Rain in Processing"
youtube video: https://www.youtube.com/watch?v=KkyIDI6rQJI

'''

# Create the snow drops:
drops = []
dropAmount = 5
dropMax = 300
dropPeriod = 1.0

# Background Images Bank
images = ['backgroundNight.png', 'background.png']
nbrImages = len(images)

# Selected Image
selectedImage = {'idx': 0}

# Adding or removing snow flakes
state = {'adding': True}

@right_button.down
def shuffleBackgroundImage():
    if selectedImage['idx'] < nbrImages - 1:
        selectedImage['idx'] += 1
    else:
        selectedImage['idx'] = 0
        
@left_button.down
def addFlake():
    for i in xrange(dropAmount):
        drops.append(Drop())
    
@midleft_button.down
def removeFlake():
    if len(drops) <> 0:
        for i in xrange(dropAmount):
            drops.pop()
    else:
        state['adding'] = True
    
@every(seconds = dropPeriod)
def time():
    if state['adding'] and len(drops) < dropMax:
        addFlake()
    else:
        state['adding'] = False
        removeFlake()

@every(seconds=1.0/30)
def loop():
    screen.image(images[selectedImage['idx']])
    for drop in drops:
        # Update the current drop position:
        drop.fall()
        # Show the current drop:
        drop.show()
    # Title Text
    screen.text(
        'MERRY CHRISTMAS',
        font = "Santa's Air Mail.ttf",
        font_size = 32,
        color = 'white'
        )

tingbot.run()