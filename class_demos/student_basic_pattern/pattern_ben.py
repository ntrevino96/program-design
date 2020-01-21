from random import random

size(1000,1000)
width = range(0, width(), 100)
height = range(0, height(), 100)

def pattern():
    for x in width:
        for y in height:
            fill(random(),random(),random(),1)
            oval(x, y, 90, 90)

for p in range(10):
    if p == 0:
        pattern() 
    else:
        newPage()
        pattern()
saveImage("~/Desktop/pattern.gif")
