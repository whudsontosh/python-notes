##
#  SimpleGraphics basics
#
#  A walkthrough of the core ideas in SimpleGraphics, a small wrapper around
#  tkinter.  Run this file from the same folder as SimpleGraphics.py.
#
#  Topics covered:
#    1. Importing the library (this opens the window)
#    2. The coordinate system
#    3. Colors: outline, fill and background
#    4. Drawing primitives: line, rect, ellipse, circle, polygon, arc, ...
#    5. Text and fonts
#    6. Line styles: width and arrows
#    7. Keeping a reference to a shape so it can be moved, scaled or deleted
#    8. Mouse input and a simple animation loop
#
from SimpleGraphics import *

# ---------------------------------------------------------------------------
# 1. Importing SimpleGraphics opens an 800 x 600 window straight away.
#    When the program reaches the end, the library keeps the window open
#    until you close it (or press Escape), so no mainloop() call is needed.
# ---------------------------------------------------------------------------
setWindowTitle("SimpleGraphics Basics")

# ---------------------------------------------------------------------------
# 2. Coordinate system
#    (0, 0) is the TOP-LEFT corner.  x increases to the right and y increases
#    DOWNWARD.  getWidth() and getHeight() give the window size in pixels.
# ---------------------------------------------------------------------------
width = getWidth()     # 800 by default
height = getHeight()   # 600 by default
# resize(1000, 700)    # uncomment to change the window size

# ---------------------------------------------------------------------------
# 3. Colors
#    Every color function accepts EITHER a color name ("red", "skyblue") OR
#    three 0-255 values for red, green and blue.
#      setOutline(...) - color of shape borders (and of text)
#      setFill(...)    - color used to fill shapes
#      setColor(...)   - sets both outline and fill at once
#      background(...) - color of the whole window
#    A color stays in effect until you change it, so set it BEFORE drawing.
# ---------------------------------------------------------------------------
background("lightyellow")       # by name
background(240, 248, 255)       # by RGB values (this replaces the line above)

# ---------------------------------------------------------------------------
# 4. Drawing primitives
#    Shapes are drawn in the order you call them; later shapes appear on top.
# ---------------------------------------------------------------------------

# line(x1, y1, x2, y2, ...) - connects each point to the next one.
# Lines use the OUTLINE color and the current width.
setOutline("black")
line(20, 20, 200, 20)                    # a single segment
line(20, 40, 100, 80, 180, 40)           # several points make a "V" shape

# rect(x, y, w, h) - (x, y) is the upper-left corner, then width and height.
setOutline("darkblue")
setFill("lightblue")
rect(20, 100, 120, 70)

# ellipse(x, y, w, h) - (x, y) is the upper-left of the ellipse's BOUNDING BOX.
setOutline("darkgreen")
setFill(144, 238, 144)                   # RGB fill
ellipse(180, 100, 140, 70)

# circle(x, y, d) - also positioned by its bounding box; d is the DIAMETER.
setOutline("darkred")
setFill("salmon")
circle(360, 100, 70)

# polygon(x1, y1, x2, y2, ...) - a filled shape joined by straight edges.
setOutline("purple")
setFill("plum")
polygon(500, 170, 540, 100, 580, 170)    # a triangle

# arc(x, y, w, h, start, extent) - just the curved edge of an ellipse.
# pieSlice(...) - the same, but closed and filled like a slice of pie.
# Angles are in degrees: 0 is at 3 o'clock and positive angles go
# COUNTER-clockwise.  The last argument is the extent, not the end angle.
setOutline("orange")
setFill("gold")
arc(620, 100, 70, 70, 0, 270)
pieSlice(710, 100, 70, 70, 45, 270)

# curve(...) draws a smooth line through points; blob(...) is a smooth filled
# shape.  They take points the same way line and polygon do.
setOutline("teal")
setFill("paleturquoise")
curve(20, 260, 80, 200, 140, 260, 200, 200)
blob(240, 260, 300, 200, 360, 260, 300, 280)

# ---------------------------------------------------------------------------
# 5. Text and fonts
#    text(x, y, string) draws in the OUTLINE color.  By default the text is
#    centered on (x, y).  Pass an alignment as the 4th argument using compass
#    letters: "w" = left edge at x, "e" = right edge at x, "nw" = top-left...
#    setFont(name, size, modifiers) changes the font for later text calls;
#    modifiers can include "bold", "italic", "underline" and "overstrike".
# ---------------------------------------------------------------------------
setOutline("black")
setFont("Arial", 14)
text(20, 320, "Left-aligned text", "w")
setFont("Times", 18, "bold italic")
text(400, 320, "Centered, bold and italic (the default alignment)")
setFont("Arial", 12)
text(780, 320, "Right-aligned text", "e")
print("That last string was", textWidth("Right-aligned text"), "pixels wide")

# ---------------------------------------------------------------------------
# 6. Line styles
#    setWidth(n) sets the thickness of lines and shape borders in pixels.
#    setArrow(tk.LAST) puts an arrowhead at the end of lines and curves.
#    Other options: tk.FIRST, tk.BOTH and tk.NONE (the default).
#    Remember to switch things back once you're done with them!
# ---------------------------------------------------------------------------
setColor("black")            # sets fill AND outline together
setWidth(4)
line(20, 360, 200, 360)

setArrow(tk.LAST)
line(20, 390, 200, 390)
setArrow(tk.NONE)            # turn arrowheads back off

setWidth(1)                  # back to thin lines

# ---------------------------------------------------------------------------
# 7. Keeping a reference to a shape
#    Every drawing function RETURNS an object.  Store it in a variable and you
#    can change the shape later:
#      move(obj, x, y)    - move it so its anchor point is at (x, y)
#      scale(obj, xs, ys) - stretch it by the given factors (1.0 = unchanged)
#      delete(obj)        - remove it
#      bringToFront(obj) / sendToBack(obj) - change the drawing order
#    clear() removes EVERYTHING (the background color is kept).
# ---------------------------------------------------------------------------
setOutline("black")
setFill("orange")
box = rect(300, 350, 60, 40)          # keep the reference in "box"

setFill("dodgerblue")
ball = circle(420, 350, 40)

move(box, 320, 360)                   # move the box's upper-left corner
scale(ball, 1.5, 1.5)                 # grow the ball to 1.5x its size
bringToFront(box)                     # draw the box above the ball

doomed = rect(560, 350, 50, 40)
delete(doomed)                        # drawn, then immediately removed

# ---------------------------------------------------------------------------
# 8. Mouse input and animation
#    closed() returns True once the user clicks the window's close button, so
#    "while not closed():" is the standard animation loop.  Each pass:
#      - delete / redraw (or move) things
#      - sleep for a moment so the motion is visible
#    mousePos() returns (x, y) for the pointer; leftButtonPressed() tells you
#    whether the left button is currently down.
# ---------------------------------------------------------------------------
from time import sleep

setColor("crimson")
follower = circle(0, 0, 30)           # this circle will chase the mouse
setColor("black")
text(width // 2, height - 20, "Move the mouse. Hold the left button to turn green.")

while not closed():
    x, y = mousePos()

    # SimpleGraphics has no "change color" call for an existing shape, so to
    # change color we delete the old shape and redraw it in the new color.
    delete(follower)
    if leftButtonPressed():
        setColor("green")
    else:
        setColor("crimson")
    follower = circle(x - 15, y - 15, 30)   # subtract the radius to center

    sleep(0.02)                       # ~50 frames per second

# When the loop ends the window is already closed, so the program just exits.
