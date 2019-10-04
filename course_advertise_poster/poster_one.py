# get python's random module to pull random numbers for design decisions
import random

# Set page size
s = "Tabloid"
size(s)

# handy to set the page width/height to a variable
# as to not have to keep calling method
pageWidth = width()
pageHeight = height()

# varible for indent value
indents = 10


def drawBackground(x, y, width, height, p):
    """
    Draws the patteren background
    Takes in:
    x,y start point
    width of tile
    height of tile
    p, a variable that sets the stroke width
    """
    stroke(1)
    strokeWidth(1+p)

    # Flip a 'coin' to determine line direction
    flip = random.randint(0, 1)

    if flip == 0:
        line((x, y), (x+width, y+height))
        line((x, y+height/2), (x+width/2, y+height))
        line((x+width/2, y), (x+width, y+height/2))
    else:
        line((x+width, y), (x, y+height))
        line((x+width/2, y), (x, y+height/2))
        line((x+width, y+height/2), (x+width/2, y+height))


def getFont(text):
    """
    Retuns a random font from list of fonts installed on the machine
    that runs the script.

    The method takes in some text and uses returns a point size and leading
    based on the width of that text. A randomized point size is chosen based
    on the document width.
    """
    f = random.choice(installedFonts())
    font(f)
    fontSize(10)
    textWidth, textHeight = textSize(text)

    # here we set a random scale factor for the text based on the pageWidth
    m = (pageWidth/(random.random()+1))/textWidth
    fs = 10*m

    # testing showed that a line height of 8.5 times
    # the scale factor worked well
    lh = 8.5*m
    return f, fs, lh


def drawText(txt):
    """
    Function to take in a FormattedText string and draw the text in
    a random page location.
    """

    # get the width and height of the text box
    textWidth, textHeight = txt.size()
    # add a bit to the box to account for descenders
    textHeight += abs(txt.fontDescender())
    w = int(pageWidth-textWidth)
    x = random.randint(0, w)
    y = random.randint(int(textHeight), pageHeight)
    box = (x, y, textWidth, textHeight)

    # Need to make sure that we don't overflow the box, so test for
    # text overflow, and if the text does overflow, add to the height of
    # the box up to 100 times to try to fit the text in the box
    c = 0
    while len(textOverflow(txt, box)) != 0 and c < 100:
        c += 1
        box = (x, y, textWidth, textHeight+1)

    # If the function tried 100 times and still now box size was found that
    # didn't overflow, let the caller know none was found.
    if c == 100:
        return False
    else:
        # With a good size for the text box, draw a white background for the
        # text and then draw the text
        fill(1)

        # This draws the white box larger than the text box based
        # on the indent value.
        rect(box[0]-indents,
             box[1]-indents,
             box[2]+indents*2,
             box[3]+indents*2)
        textBox(txt, box)

        # Let the caller know that the text was drawn.
        return True


def header(text, widthText, align):
    """
    Draws the pieces of large type on the page.

    Takes in the *text* as a list, drawing draw each item of the list in
    a new location.

    *widthText* is the text used to set the point size of the header
    *align* is how you want the text aligned ('left', 'center', 'right')
    """

    # Get a font, point size, and line height
    f, fs, lh = getFont(widthText)

    # A loop that goes through the list of text to be drawn
    for i in text:
        # format the text to the font, point size, line height
        txt = FormattedString(txt=i,
                              font=f,
                              fontSize=fs,
                              lineHeight=lh,
                              align=align)
        # Try to draw the text. If *drawText* returns True, the following loop
        # doesn't happen. If it returns False, then a new font is chosen and
        # the script tries until text is drawn
        dt = drawText(txt)
        while dt is False:
            f, fs, lh = getFont(widthText)
            txt = FormattedString(txt=i,
                                  font=f,
                                  fontSize=fs,
                                  lineHeight=lh,
                                  align=align)
            dt = drawText(txt)


def sales():
    """
    Formats and draws the sales pitch text in a random location.
    """

    # get a FormattedString
    txt = FormattedString()

    # set the font to a chosen font
    txt.font("GrepD06-Bold")

    # set the point size to a value based on page width
    fontSize = pageWidth*.017
    txt.fontSize(fontSize)

    # Add the text, switching the font to bold where desired for emphasis
    txt.append("What unconscious ways do your design tools influence your work? Would your work look different if you made all of the tools used to create it?\n\n")
    txt.font("GrepD06-Regular")
    txt.append("These questions and more will be explored in this new course by building your own design tools with the Python programming language. The class assumes no prior programming experience, so don’t worry if you have never written a line of code.\n\nIf you are a fundamentally curious, willing community participant, capable self-learner, and a student who is tolerant of failure, this is an ideal course for you. The course will be held in the Book Studio, where we’ll bridge your digital tools to analog output.\n\nSee more at:\n")
    txt.font("GrepD06-Bold")
    txt.append("github.com/benkiel/program-design\n")
    txt.font("GrepD06-Regular")
    txt.append("and register for Programming Design, F10 ART 338Y. Class meets Tuesdays and Thursdays, 8:30am to 11:20am.\n\nQuestions? ben@typefounding.com")

    # Set the width of the text box
    w = pageWidth/2.5
    # Get the height of the text box based on the known width
    w, h = textSize(txt, width=w)

    # Pick a random location for the text box
    xr = int(pageWidth-w)
    x = random.randint(0, xr)
    y = random.randint(0, pageHeight-h)

    # Draw the backing white rectangle
    fill(1)
    rect(x-indents, y-indents, w+indents*2, h+indents*2)

    # Draw the text
    textBox(txt, (x, y, w, h))


# Main bit of the script that draws everything
# Set a size for the pattern module
module = 100

# We are going to make 40 pages of posters, this loop executes 40 times.
for i in range(40):

    # If this is the not the first page of our document, start with a new page.
    if i != 0:
        newPage(pageWidth, pageHeight)

    # Draw a black background
    rect(0, 0, pageWidth, pageHeight)

    # Draw our pattern
    for x in range(0, pageWidth, module):
        for y in range(0, pageHeight, module):
            drawBackground(x, y, module, module, i)

    # Draw the header text
    header(["Spring 2020", "Programming\nDesign"], "Programming", "right")

    # Draw the sales copy text
    sales()

# Save a pdf of all 40 pages for printing
saveImage(f"~/Desktop/programming_design_posters_{s}.pdf")
