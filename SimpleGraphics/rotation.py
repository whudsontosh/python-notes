##
#  Rotating shapes with SimpleGraphics
#
#  SimpleGraphics has no rotate function: rect() and ellipse() are always
#  axis-aligned.  (Only text() accepts an angle.)  The workaround is to build
#  the shape as a polygon and rotate its points ourselves with trigonometry.
#
#  Run this file from the same folder as SimpleGraphics.py.  Close the window
#  or press Escape to quit.
#
from math import cos, sin, radians, pi
from time import sleep

from SimpleGraphics import *

setWindowTitle("Rotation Demo")
background("white")


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

## Rotate a list of (x, y) points around the pivot (cx, cy).
#  @param points  list of (x, y) tuples
#  @param cx, cy  the point to rotate around
#  @param degrees the angle; positive turns clockwise on screen (because the
#                 y axis points DOWN in SimpleGraphics)
#  @return a flat list [x1, y1, x2, y2, ...], which is what polygon() wants
def rotate_points(points, cx, cy, degrees):
    a = radians(degrees)
    c, s = cos(a), sin(a)          # compute once, reuse for every point
    flat = []
    for x, y in points:
        dx, dy = x - cx, y - cy    # 1. shift so the pivot is the origin
        flat.append(cx + dx * c - dy * s)   # 2. rotate, then 3. shift back
        flat.append(cy + dx * s + dy * c)
    return flat


## Draw a w x h rectangle centered on (cx, cy), rotated by `degrees`.
#  Note the position is the CENTER, unlike rect(), which uses the top-left.
#  @return the polygon object (usable with delete, move, etc.)
def rotated_rect(cx, cy, w, h, degrees):
    corners = [(cx - w / 2, cy - h / 2),   # top-left
               (cx + w / 2, cy - h / 2),   # top-right
               (cx + w / 2, cy + h / 2),   # bottom-right
               (cx - w / 2, cy + h / 2)]   # bottom-left
    return polygon(rotate_points(corners, cx, cy, degrees))


## Draw an ellipse of width w and height h centered on (cx, cy), rotated by
#  `degrees`.  It is approximated by a many-sided polygon; raise `steps` for a
#  smoother edge.
def rotated_ellipse(cx, cy, w, h, degrees, steps=60):
    pts = []
    for i in range(steps):
        t = 2 * pi * i / steps                       # angle around the ellipse
        pts.append((cx + (w / 2) * cos(t), cy + (h / 2) * sin(t)))
    return polygon(rotate_points(pts, cx, cy, degrees))


# ---------------------------------------------------------------------------
# 1. Static examples: the same shapes at several angles
# ---------------------------------------------------------------------------
setOutline("darkblue")
setFill("lightblue")
for i, angle in enumerate([0, 30, 60, 90]):
    rotated_rect(100 + i * 130, 80, 90, 40, angle)
    text(100 + i * 130, 140, str(angle) + " deg")

setOutline("darkred")
setFill("salmon")
for i, angle in enumerate([0, 30, 60, 90]):
    rotated_ellipse(100 + i * 130, 220, 100, 40, angle)
    text(100 + i * 130, 280, str(angle) + " deg")

# text() can rotate on its own through its optional angle argument
# (counter-clockwise, in degrees).
setOutline("black")
setFont("Arial", 14)
text(640, 150, "text rotates natively", "c", 30)

# ---------------------------------------------------------------------------
# 2. Animation: spin shapes by redrawing them with a growing angle each frame
#    The angle is the only thing that changes.  We delete the old polygons and
#    draw new ones, since a drawn shape can't be rotated in place.
# ---------------------------------------------------------------------------
angle = 0
rect_shape = None
ellipse_shape = None
orbit_shape = None

while not closed():
    # Remove last frame's shapes (delete(None) on the first pass does nothing)
    delete(rect_shape)
    delete(ellipse_shape)
    delete(orbit_shape)

    # A rectangle spinning clockwise around its own center
    setOutline("darkgreen")
    setFill("lightgreen")
    rect_shape = rotated_rect(200, 450, 150, 50, angle)

    # An ellipse spinning the other way, at a different speed
    setOutline("purple")
    setFill("plum")
    ellipse_shape = rotated_ellipse(450, 450, 160, 60, -2 * angle)

    # A small square orbiting a pivot: its OWN center sits 70 px from the pivot
    # and is rotated around the pivot, so the square travels in a circle.
    pivot_x, pivot_y = 680, 450
    corners = [(pivot_x + 70 - 15, pivot_y - 15), (pivot_x + 70 + 15, pivot_y - 15),
               (pivot_x + 70 + 15, pivot_y + 15), (pivot_x + 70 - 15, pivot_y + 15)]
    setOutline("darkorange")
    setFill("gold")
    orbit_shape = polygon(rotate_points(corners, pivot_x, pivot_y, angle))

    angle = (angle + 2) % 360      # advance and wrap at 360
    sleep(0.02)                    # ~50 frames per second
