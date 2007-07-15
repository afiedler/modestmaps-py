"""
>>> p = Point(0, 1)
>>> p
(0.000, 1.000)
>>> p.x
0
>>> p.y
1

>>> c = Coordinate(0, 1, 2)
>>> c
(0.000, 1.000 @2.000)
>>> c.row
0
>>> c.column
1
>>> c.zoom
2
>>> c.zoomTo(3)
(0.000, 2.000 @3.000)
>>> c.zoomTo(1)
(0.000, 0.500 @1.000)
>>> c.up()
(-1.000, 1.000 @2.000)
>>> c.right()
(0.000, 2.000 @2.000)
>>> c.down()
(1.000, 1.000 @2.000)
>>> c.left()
(0.000, 0.000 @2.000)
"""

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return '(%(x).3f, %(y).3f)' % self.__dict__
    
class Coordinate:
    MAX_ZOOM = 20

    def __init__(self, row, column, zoom):
        self.row = row
        self.column = column
        self.zoom = zoom
    
    def __repr__(self):
        return '(%(row).3f, %(column).3f @%(zoom).3f)' % self.__dict__
        
    def copy(self):
        return Coordinate(self.row, self.column, self.zoom)
        
    def container(self):
        return Coordinate(math.floor(self.row), math.floor(self.column), self.zoom)

    def zoomTo(self, destination):
        return Coordinate(self.row * math.pow(2, destination - self.zoom),
                          self.column * math.pow(2, destination - self.zoom),
                          destination)
    
    def zoomBy(self, distance):
        return Coordinate(self.row * math.pow(2, distance),
                          self.column * math.pow(2, distance),
                          self.zoom + distance)

    def up(self, distance=1):
        return Coordinate(self.row - distance, self.column, self.zoom)

    def right(self, distance=1):
        return Coordinate(self.row, self.column + distance, self.zoom)

    def down(self, distance=1):
        return Coordinate(self.row + distance, self.column, self.zoom)

    def left(self, distance=1):
        return Coordinate(self.row, self.column - distance, self.zoom)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
