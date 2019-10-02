import random
s = "Tabloid"
size(s)
pageWidth=width()
pageHeight=height()

indents = 10
drawn = []

def drawBackground(x,y,width,height,p):
    stroke(1)
    strokeWidth(1+p)
    flip = randint(0,1)
    if flip == 0:
        line((x,y),(x+width,y+height))
        line((x,y+height/2),(x+width/2,y+height))
        line((x+width/2,y),(x+width,y+height/2))
    else:
        line((x+width,y),(x,y+height))
        line((x+width/2,y),(x,y+height/2))
        line((x+width,y+height/2),(x+width/2,y+height))    

def getFont(text):
    f = random.choice(installedFonts())
    font(f)
    fontSize(10)
    textWidth, textHeight = textSize(text)

    m = (width()/(random.random()+1))/textWidth
    fs = 10*m
    lh = 8.5*m
    return f, fs, lh

def drawText(txt):
    textWidth, textHeight = txt.size()
    textHeight += abs(txt.fontDescender())
    w = int(width()-textWidth)
    x = random.randint(0,w)
    y = random.randint(int(textHeight),height())
    box = (x,y,textWidth,textHeight)  
    
    c = 0
    while len(textOverflow(txt,box)) != 0 and c < 100:
        c += 1
        box = (x,y,textWidth,textHeight)
    if c == 100:
        return False
    else:
        fill(1)
        rect(box[0]-indents,box[1]-indents,box[2]+indents*2,box[3]+indents*2)
        textBox(txt,box)
        drawn.append(box)
        return True

  

def header(text, widthText, align):

    f, fs, lh = getFont(widthText)

    for i in text:
        txt = FormattedString(txt=i, font=f, fontSize=fs, lineHeight=lh, align=align)
        dt = drawText(txt)
        while dt is False:
            f, fs, lh = getFont(widthText)
            txt = FormattedString(txt=i, font=f, fontSize=fs, lineHeight=lh, align=align)            
            dt = drawText(txt)

def sales():
    txt = FormattedString()
    txt.font("GrepD06-Bold")
    fontSize = width()*.017
    txt.fontSize(fontSize)
    txt.append("What unconscious ways do your design tools influence your work? Would your work look different if you made all of the tools used to create it?\n\n")
    txt.font("GrepD06-Regular")
    txt.append("These questions and more will be explored in this new course by building your own design tools with the Python programming language. The class assumes no prior programming experience, so don’t worry if you have never written a line of code.\n\nIf you are a fundamentally curious, willing community participant, capable self-learner, and a student who is tolerant of failure, this is an ideal course for you. The course will be held in the Book Studio, where we’ll bridge your digital tools to analog output.\n\nSee more at:\n")
    txt.font("GrepD06-Bold")
    txt.append("github.com/benkiel/program-design\n")
    txt.font("GrepD06-Regular")
    txt.append("and register for Programming Design, F10 ART 338Y. Class meets Tuesdays and Thursdays, 8:30am to 11:20am.\n\nQuestions? ben@typefounding.com")
    w = width()/2.5
    w,h= textSize(txt,width=w)
    xr = int(width()-w)
    x = random.randint(0,xr)
    y = random.randint(0,height()-h)
    fill(1)
    rect(x-indents,y-indents,w+indents*2,h+indents*2)
    textBox(txt,(x,y,w,h))
    
module = 100
for i in range(40):
    if i == 0:
        rect(0,0,width(),height())
        for x in range(0, width(), module):
            for y in range(0, height(), module):
                drawBackground(x,y,module,module,i)
        header(["Spring 2020","Programming\nDesign"], "Programming", "right")
        sales()
    else:
        newPage(pageWidth,pageHeight)
        rect(0,0,width(),height())
        for x in range(0, width(), module):
            for y in range(0, height(), module):
                drawBackground(x,y,module,module,i)
        header(["Spring 2020","Programming\nDesign"], "Programming", "right")
        sales()

saveImage(f"~/Desktop/programming_design_posters_{s}.pdf")