##
#  Stretching shapes with SimpleGraphics
#
#  Every function takes the CENTER (cx, cy) of the shape, its original width
#  and height, and a stretch factor.  The shape grows or shrinks around its
#  center, so it stays in place.  (rect() and ellipse() themselves take the
#  top-left corner, so we shift by half the size to compensate.)
#
#  The library also has scale(obj, xs, ys), which stretches a shape that has
#  already been drawn, but it anchors at the top-left corner instead.
#
from SimpleGraphics import *


## Draw a rectangle centered on (cx, cy) with the given width and height.
def __centered_rect(cx, cy, w, h):
    return rect(cx - w / 2, cy - h / 2, w, h)


## Draw an ellipse centered on (cx, cy) with the given width and height.
def __centered_ellipse(cx, cy, w, h):
    return ellipse(cx - w / 2, cy - h / 2, w, h)


# --- Rectangles -------------------------------------------------------------

def rect_height_stretch(cx, cy, w, h, factor):
    return __centered_rect(cx, cy, w, h * factor)

def rect_width_stretch(cx, cy, w, h, factor):
    return __centered_rect(cx, cy, w * factor, h)

## Scale both dimensions by the same factor (a uniform resize).
def rect_scale(cx, cy, w, h, factor):
    return __centered_rect(cx, cy, w * factor, h * factor)


# --- Ellipses ---------------------------------------------------------------

def ellipse_height_stretch(cx, cy, w, h, factor):
    return __centered_ellipse(cx, cy, w, h * factor)

def ellipse_width_stretch(cx, cy, w, h, factor):
    return __centered_ellipse(cx, cy, w * factor, h)

## Scale both dimensions by the same factor (a uniform resize).
def ellipse_scale(cx, cy, w, h, factor):
    return __centered_ellipse(cx, cy, w * factor, h * factor)


# --- Anchored at the top-left corner ----------------------------------------
# rect() and ellipse() already position by the top-left corner, so (x, y) never
# moves: the shape simply grows right and down, or shrinks back toward (x, y).

def rect_scale_corner(x, y, w, h, factor):
    return rect(x, y, w * factor, h * factor)

def ellipse_scale_corner(x, y, w, h, factor):
    return ellipse(x, y, w * factor, h * factor)


# --- Anchored at the bottom (a flipped y axis) ------------------------------
# y grows DOWNWARD in SimpleGraphics, so a shape's top edge is y and its bottom
# edge is y + height.  To keep the BASE fixed we measure upward from it: the top
# is (base_y - height).  Growing the height then moves the top up the screen
# while the bottom stays put, like a bar in a bar chart or a plant growing.
# (bx, by) is the bottom-center of the shape; it never moves.

def rect_scale_base(bx, by, w, h, factor):
    nw, nh = w * factor, h * factor
    return rect(bx - nw / 2, by - nh, nw, nh)

def ellipse_scale_base(bx, by, w, h, factor):
    nw, nh = w * factor, h * factor
    return ellipse(bx - nw / 2, by - nh, nw, nh)


# --- Demo -------------------------------------------------------------------
# Each column shows the stretched shape (filled) with the original size drawn
# on top as a gray outline.  Both share the same center.  setFill("") makes a
# shape transparent, so the stretched shape stays visible underneath.
if __name__ == "__main__":
    setWindowTitle("Transformations Demo")
    background("white")

    W, H = 80, 50              # original size used by every example
    FACTOR = 1.6

    columns = [
        ("height", rect_height_stretch, ellipse_height_stretch),
        ("width",  rect_width_stretch,  ellipse_width_stretch),
        ("scale",  rect_scale,          ellipse_scale),
    ]

    for i, (label, rect_fn, ellipse_fn) in enumerate(columns):
        cx = 150 + i * 250

        # Rectangle row: stretched (filled) first, then the original outline
        setOutline("darkblue")
        setFill("lightblue")
        rect_fn(cx, 120, W, H, FACTOR)
        setOutline("gray")
        setFill("")
        rect(cx - W / 2, 120 - H / 2, W, H)

        # Ellipse row
        setOutline("darkred")
        setFill("salmon")
        ellipse_fn(cx, 320, W, H, FACTOR)
        setOutline("gray")
        setFill("")
        ellipse(cx - W / 2, 320 - H / 2, W, H)

        setOutline("black")
        text(cx, 200, label + " x" + str(FACTOR))
        text(cx, 400, label + " x" + str(FACTOR))

    # -----------------------------------------------------------------------
    # Animated demo: the same shapes pulsing in three different ways.
    # Click the window to start it.  The dot in each column is the ANCHOR, the
    # point that never moves.
    #   left column   - top-left corner fixed (grows right and down)
    #   middle column - center fixed (grows in every direction)
    #   right column  - bottom fixed (grows upward from the ground line)
    # -----------------------------------------------------------------------
    from math import sin
    from time import sleep

    setOutline("black")
    text(400, 500, "Click the window to see the animated version")
    while not closed() and not leftButtonPressed():
        sleep(0.02)

    clear()
    background("white")

    # (title, rect function, ellipse function, anchor x for rect, anchor x for
    #  ellipse, anchor y).  What "anchor" means depends on the function.
    modes = [
        ("top-left fixed", rect_scale_corner, ellipse_scale_corner, 30, 180, 200),
        ("center fixed",    rect_scale,        ellipse_scale,        320, 480, 250),
        ("bottom fixed",    rect_scale_base,   ellipse_scale_base,   610, 730, 400),
    ]

    # Titles, anchor dots and the ground line only need drawing once.  The
    # dots are kept so they can be brought in front of the shapes every frame.
    dots = []
    for title, _, _, ax1, ax2, ay in modes:
        setOutline("black")
        text((ax1 + ax2) / 2, 60, title)
        setColor("black")
        dots.append(circle(ax1 - 3, ay - 3, 6))   # anchor for the rectangle
        dots.append(circle(ax2 - 3, ay - 3, 6))   # anchor for the ellipse
    setOutline("gray")
    line(550, 400, 790, 400)               # the "ground" for the bottom column

    shapes = []
    t = 0
    while not closed():
        for s in shapes:                   # remove last frame's shapes
            delete(s)
        shapes = []

        factor = 1 + 0.5 * sin(t)          # oscillates between 0.5 and 1.5

        for _, rect_fn, ellipse_fn, ax1, ax2, ay in modes:
            setOutline("darkblue")
            setFill("lightblue")
            shapes.append(rect_fn(ax1, ay, W, H, factor))
            setOutline("darkred")
            setFill("salmon")
            shapes.append(ellipse_fn(ax2, ay, W, H, factor))

        for d in dots:                     # keep the anchors visible on top
            bringToFront(d)

        t += 0.05
        sleep(0.02)
