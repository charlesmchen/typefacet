'''
robofont-extensions-and-scripts
TFSPoint.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''



import sys
import math

from TFSMath import *
from TFSMap import TFSMap
from TFSValidationException import TFSValidationException

onJython = sys.platform.startswith('java')


class TFSPoint(object):

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.validate()

    def validate(self):
        try:
            if not onJython:
                if (math.isnan(self.x) or
                    math.isinf(self.x) or
                    math.isnan(self.y) or
                    math.isinf(self.y)) :
                    raise TFSValidationException('Invalid point')
        except TFSValidationException, e:
            print 'TFSPoint.validate', self.description()
            raise e

    def __repr__(self):
        return 'TFSPoint(%f, %f)' % ( self.x, self.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
#        '''
#        HORROR: ?
#        '''
#        if (self.x == other.x) and (self.y == other.y):
#            return True
#        return self.distanceTo(other) < getFloatRoundingTolerance()
##        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __str__(self):
        return self.description()

    def description(self):
        return '[%s, %s]' % (str(self.x), str(self.y))

    def invert(self):
        return TFSPoint(-self.x,
                     -self.y)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def distanceTo(self, other):
        return self.minus(other).length()

    def midpoint(self, other, factor=0.5):
        factor = clamp01(factor)
        n_factor = clamp01(1.0 - factor)
        return TFSPoint(self.x * n_factor + other.x * factor,
                     self.y * n_factor + other.y * factor)

    def scale(self, value):
        return TFSPoint(self.x * value,
                     self.y * value)

    def copy(self):
        return TFSPoint(self.x,
                     self.y)

    def scaleXY(self, xFactor, yFactor):
        return TFSPoint(self.x * xFactor,
                     self.y * yFactor)

    def plus(self, other):
        return TFSPoint(self.x + other.x,
                     self.y + other.y)

    def minus(self, other):
        return TFSPoint(self.x - other.x,
                     self.y - other.y)

    def blend(self, other, factor=0.5):
        factor = clamp01(factor)
        return TFSPoint((self.x * (1.0 - factor)) + (other.x * factor),
                      (self.y * (1.0 - factor)) + (other.y * factor))

    def normalize(self):
        length = self.length()
        try:
            return TFSPoint(self.x / float(length),
                         self.y / float(length))
        except ZeroDivisionError, e:
            print 'Point.normalize() ZeroDivisionError', self.description()
            raise e

    def dotProduct(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def crossProductWZAxis(self):
        return TFSPoint(self.y,
                     -self.x)

    def rightAngleRight(self):
        return self.crossProductWZAxis()

    def left(self, value):
        return TFSPoint(self.x - value,
                     self.y)

    def right(self, value):
        return TFSPoint(self.x + value,
                     self.y)

    def up(self, value):
        return TFSPoint(self.x,
                     self.y + value)

    def down(self, value):
        return TFSPoint(self.x,
                     self.y - value)

    def absValue(self):
        return TFSPoint(abs(self.x), abs(self.y))

    def atan2(self):
        return math.atan2(self.y, self.x)

    def rotate(self, angleRadians):
        wx = self.x
        wy = self.y
        sa = math.sin(angleRadians)
        ca = math.cos(angleRadians)
        x = self.x * ca + (-wy) * sa
        y = self.y * ca + wx * sa
        return TFSPoint(x, y)

    def roundWithPrecision(self, precisionDigits):
        return TFSPoint(round(self.x, precisionDigits),
                      round(self.y, precisionDigits))

    def roundWithDefaultPrecision(self):
        return self.roundWithPrecision(getDefaultPrecisionDigits())


def TFSPoint0():
    return TFSPoint(0, 0)

def scaleVectorHV(vector, hLength, vLength):
#    factor = clamp01(vector.absValue().dotProduct(TFSPoint(0, 1)))
    factor = clamp01(abs(vector.dotProduct(TFSPoint(0, 1))))
    length = (vLength * factor) + (hLength * (1.0 - factor))
    result = vector.scale(length)
#    .roundWithDefaultPrecision()
#    print 'scaleVectorHV', 'vector, hLength, vLength', vector, hLength, vLength, 'length', length, 'factor', factor, 'result', result
    return result

def controlPointsWithSides(_left, _right, _top, _bottom):
    result = TFSMap()
    result.tl = TFSPoint(_left, _top)
    result.bl = TFSPoint(_left, _bottom)
    result.tr = TFSPoint(_right, _top)
    result.br = TFSPoint(_right, _bottom)

    result.tc = result.tl.midpoint(result.tr)
    result.bc = result.bl.midpoint(result.br)
    result.lc = result.tl.midpoint(result.bl)
    result.rc = result.tr.midpoint(result.br)

    result.left = _left
    result.right = _right
    result.top = _top
    result.bottom = _bottom
    return result

def minmaxPoints(points):
    result = TFSMap()
    result.minX = reduce(min, [point.x for point in points])
    result.maxX = reduce(max, [point.x for point in points])
    result.minY = reduce(min, [point.y for point in points])
    result.maxY = reduce(max, [point.y for point in points])
    return result

def minmaxMerge(minmax0, minmax1):
    if minmax0 is None and minmax1 is None:
        raise Exception('Invalid arguments')
    if minmax0 is None:
        return minmax1
    if minmax1 is None:
        return minmax0
    result = TFSMap()
    result.minX = min(minmax0.minX, minmax1.minX)
    result.maxX = max(minmax0.maxX, minmax1.maxX)
    result.minY = min(minmax0.minY, minmax1.minY)
    result.maxY = max(minmax0.maxY, minmax1.maxY)
    return result
