'''
robofont-extensions-and-scripts
TFSMath.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''




import math
from TFSRectangle import *


_DEFAULT_PRECISION_DIGITS = 4

def getDefaultPrecisionDigits():
    return _DEFAULT_PRECISION_DIGITS

def setDefaultPrecisionDigits(value):
    global _DEFAULT_PRECISION_DIGITS
    _DEFAULT_PRECISION_DIGITS = value

_FLOAT_ROUNDING_TOLERANCE = 0.0001

def getFloatRoundingTolerance():
    return _FLOAT_ROUNDING_TOLERANCE

def setFloatRoundingTolerance(value):
    global _FLOAT_ROUNDING_TOLERANCE
    _FLOAT_ROUNDING_TOLERANCE = value


#DEFAULT_PRECISION_DIGITS = 4
#FLOAT_ROUNDING_TOLERANCE = 0.0001
T_ROUNDING_TOLERANCE = 0.001
RADIANS_ROUNDING_TOLERANCE = 0.0001


def clamp01(value):
    return max(0, min(1, value))

def evaluateCubicSpline2D_points_all(p0, p1, p2, p3, t):
    t = clamp01(t)
    p01 = p0.midpoint(p1, t)
    p12 = p1.midpoint(p2, t)
    p23 = p2.midpoint(p3, t)
    p012 = p01.midpoint(p12, t)
    p123 = p12.midpoint(p23, t)
    p0123 = p012.midpoint(p123, t)
    return p0123, p01, p012, p123, p23

def evaluateCubicSpline2D_point(p0, p1, p2, p3, t):
    p0123, p01, p012, p123, p23 = evaluateCubicSpline2D_points_all(p0, p1, p2, p3, t)
    return p0123

def evaluateCubicSpline2D_pointAndTangent(p0, p1, p2, p3, t):
    p0123, p01, p012, p123, p23 = evaluateCubicSpline2D_points_all(p0, p1, p2, p3, t)
    tangent = p123.minus(p012).normalize()
    return p0123, tangent, p012, p123

def evaluateCubicSpline2DWithT(p0, p1, p2, p3, resolution):
    result = []
    for i in xrange(resolution):
        t = i / float(resolution - 1)
        result.append((evaluateCubicSpline2D_point(p0, p1, p2, p3, t),
                       t, ) )
    return result

def evaluateQuadraticSpline2D_points_all(p0, p1, p2, t):
    t = clamp01(t)
    p01 = p0.midpoint(p1, t)
    p12 = p1.midpoint(p2, t)
    p012 = p01.midpoint(p12, t)
    return p012, p01, p12

def evaluateQuadraticSpline2D_point(p0, p1, p2, t):
    p012, p01, p12 = evaluateQuadraticSpline2D_points_all(p0, p1, p2, t)
    return p012

def evaluateQuadraticSpline2D_pointAndTangent(p0, p1, p2, t):
    p012, p01, p12 = evaluateQuadraticSpline2D_points_all(p0, p1, p2, t)
    tangent = p12.minus(p01).normalize()
    return p012, tangent, p01, p12

def evaluateQuadraticSpline2DWithT(p0, p1, p2, resolution):
    result = []
    for i in xrange(resolution):
        t = i / float(resolution - 1)
        result.append((evaluateQuadraticSpline2D_point(p0, p1, p2, t),
                       t, ) )
    return result

def normalizeRadiansDiff(value):
    while value < -math.pi:
        value += math.pi * 2
    while value > math.pi:
        value -= math.pi * 2
    return value

def normalizeRadians(value):
    while value < 0:
        value += math.pi * 2
    value %= 2 * math.pi
    return value

def randomBoolean():
    import random
    return 0 == random.randint(0, 1)

def normalizeRadiansAboveAngle(angle, referenceAngle):
    while angle > referenceAngle + math.pi * 2.0:
        angle -= math.pi * 2.0
    while angle <= referenceAngle:
        angle += math.pi * 2.0
    return angle

def boundingBox_points(points):
    minX = reduce(min, [point.x for point in points])
    maxX = reduce(max, [point.x for point in points])
    minY = reduce(min, [point.y for point in points])
    maxY = reduce(max, [point.y for point in points])
    return TFSRectangle(minX, minY, maxX - minX, maxY - minY)
