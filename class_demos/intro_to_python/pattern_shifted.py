from random import random

w = 200
h = 1000
module = 100
padding = 5

size(w,h)

width = range(0, width(), module)
height = range(0, height(), module)

def draw(x, y, width, height):
    fill(random(),random(),random(),1)
    rect(x, y, width, height)

def pattern():
    for i, x in enumerate(width):
        for y in height:
            if i % 2 == 0:
                y = y+(module/2)
            image = module - padding
            d = padding/2
            draw(x+d, y+d, image, image)

pattern()
