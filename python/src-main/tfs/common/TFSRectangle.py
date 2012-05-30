'''
robofont-extensions-and-scripts
TFSRectangle.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''




class TFSRectangle(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = x
        self.bottom = y
        self.right = x + width
        self.top = y + height

#    def union(self, other):
#        minX = min(self.x, other.x)
#        maxX = max(self.x, other.x)
#        minY = min(self.y, other.y)
#        maxY = max(self.y, other.y)
#        return _Rectangle(minX, minY, maxX - minX, maxY - minY)

    def containsPoint(self, p):
        if ((self.right < p.x) or
            (self.top < p.y) or
            (self.left > p.x) or
            (self.bottom > p.y)):
            return False
        return True

    def intersects(self, other):
        if ((self.right < other.left) or
            (self.top < other.bottom) or
            (self.left > other.right) or
            (self.bottom > other.top)):
            return False
        return True
