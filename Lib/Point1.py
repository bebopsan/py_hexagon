# -*- coding: utf-8 -*-

"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
s
"""

class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self, id_tag, phys_tag, x=0, y = 0):
        self.x = x
        self.y = y
        self.tag = tag
        self.id_tag= 
 
def print_point(p):
    """Print a Point object in human-readable format."""
    print '(%g, %g)' % (p.x, p.y)


class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


    def find_center(self):
        """Returns a Point at the center of a Rectangle."""
        p = Point()
        p.x = self.corner.x + self.width/2.0
        p.y = self.corner.y + self.height/2.0
        return p


def grow_rectangle(rect, dwidth, dheight):
    """Modify the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight

