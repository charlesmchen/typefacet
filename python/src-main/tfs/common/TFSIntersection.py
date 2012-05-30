'''
robofont-extensions-and-scripts
TFSIntersection.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''




from TFSPoint import *


def getIntersectPoint(p1, p2, p3, p4):
    try:
        denom = float((p1.x - p2.x) * (p3.y - p4.y) - (p1.y - p2.y) * (p3.x - p4.x))
        x = ((p1.x * p2.y - p1.y * p2.x) * (p3.x - p4.x) - (p1.x - p2.x) * (p3.x * p4.y - p3.y * p4.x)) / denom
        y = ((p1.x * p2.y - p1.y * p2.x) * (p3.y - p4.y) - (p1.y - p2.y) * (p3.x * p4.y - p3.y * p4.x)) / denom
    except ZeroDivisionError:
        return
    return TFSPoint(x, y).roundWithDefaultPrecision()


# For line segments (ie not infinitely long lines) the intersect point
# may not lay on both lines.
#
# If the point where two lines intersect is inside both line's bounding
# rectangles then the lines intersect. Returns intersect point if the line
# intesect o None if not
def calculateIntersectPoint(p1, p2, p3, p4, debugMode=False):
    '''
    We need to be very careful with rounding error.
    '''

    p = getIntersectPoint(p1, p2, p3, p4)
    if debugMode:
        print 'calculateIntersectPoint', 'p', p
    #   print 'p', p
    #   print 'p1', p1
    #   print 'p2', p2
    #   print 'p3', p3
    #   print 'p4', p4
    if not p:
        if debugMode:
            print 'calculateIntersectPoint.0'
        return None

    '''
    Check to make sure that the point of intersection is on both segments.
    We use rounded values for the sake of comparison t avoid rounding error.
    '''
    _p = p.roundWithDefaultPrecision()
    _p1 = p1.roundWithDefaultPrecision()
    _p2 = p2.roundWithDefaultPrecision()
    _p3 = p3.roundWithDefaultPrecision()
    _p4 = p4.roundWithDefaultPrecision()
    if ((_p.x < min(_p1.x, _p2.x) or _p.x < min(_p3.x, _p4.x)) or
        (_p.x > max(_p1.x, _p2.x) or _p.x > max(_p3.x, _p4.x)) or
        (_p.y < min(_p1.y, _p2.y) or _p.y < min(_p3.y, _p4.y)) or
        (_p.y > max(_p1.y, _p2.y) or _p.y > max(_p3.y, _p4.y))):
        if debugMode:
            print '_p', _p.x, _p.y
            print '_p1', _p1.x, _p1.y
            print '_p2', _p2.x, _p2.y
            print '_p3', _p3.x, _p3.y
            print '_p4', _p4.x, _p4.y
            print '1', (_p.x < min(_p1.x, _p2.x) or _p.x < min(_p3.x, _p4.x))
            print '2', (_p.x > max(_p1.x, _p2.x) or _p.x > max(_p3.x, _p4.x))
            print '3', (_p.y < min(_p1.y, _p2.y) or _p.y < min(_p3.y, _p4.y))
            print '4', (_p.y > max(_p1.y, _p2.y) or _p.y > max(_p3.y, _p4.y))
            print '1', (_p.x < min(_p1.x, _p2.x), _p.x < min(_p3.x, _p4.x))
            print '2', (_p.x > max(_p1.x, _p2.x), _p.x > max(_p3.x, _p4.x))
            print '3', (_p.y < min(_p1.y, _p2.y), _p.y < min(_p3.y, _p4.y))
            print '4', (_p.y > max(_p1.y, _p2.y), _p.y > max(_p3.y, _p4.y))
            print 'calculateIntersectPoint.1'
        return None

    '''
    To avoid rounding error, make sure endpoint values don't exceed the segment endpoints.
    '''
    p.x = max(p.x, min(p1.x, p2.x, p3.x, p4.x))
    p.x = min(p.x, max(p1.x, p2.x, p3.x, p4.x))
    p.y = max(p.y, min(p1.y, p2.y, p3.y, p4.y))
    p.y = min(p.y, max(p1.y, p2.y, p3.y, p4.y))

#    if ((p.x < min(p1.x, p2.x) or p.x < min(p3.x, p4.x)) or
#        (p.x > max(p1.x, p2.x) or p.x > max(p3.x, p4.x)) or
#        (p.y < min(p1.y, p2.y) or p.y < min(p3.y, p4.y)) or
#        (p.y > max(p1.y, p2.y) or p.y > max(p3.y, p4.y))):
#        if debugMode:
#            print 'p', p.x, p.y
#            print 'p1', p1.x, p1.y
#            print 'p2', p2.x, p2.y
#            print 'p3', p3.x, p3.y
#            print 'p4', p4.x, p4.y
#            print '1', (p.x < min(p1.x, p2.x) or p.x < min(p3.x, p4.x))
#            print '2', (p.x > max(p1.x, p2.x) or p.x > max(p3.x, p4.x))
#            print '3', (p.y < min(p1.y, p2.y) or p.y < min(p3.y, p4.y))
#            print '4', (p.y > max(p1.y, p2.y) or p.y > max(p3.y, p4.y))
#            print '1', (p.x < min(p1.x, p2.x), p.x < min(p3.x, p4.x))
#            print '2', (p.x > max(p1.x, p2.x), p.x > max(p3.x, p4.x))
#            print '3', (p.y < min(p1.y, p2.y), p.y < min(p3.y, p4.y))
#            print '4', (p.y > max(p1.y, p2.y), p.y > max(p3.y, p4.y))
#            print 'calculateIntersectPoint.1'
#        return None
    #   if ((p.x < min(p1.x, p2.x, p3.x, p4.x)) or
    #       (p.x > max(p1.x, p2.x, p3.x, p4.x)) or
    #       (p.y < min(p1.y, p2.y, p3.y, p4.y)) or
    #       (p.y > max(p1.y, p2.y, p3.y, p4.y))):
    #       return None
    if debugMode:
        print 'calculateIntersectPoint.2'
    return p

    def intersectionWithTangents(p0, tangent0, p1, tangent1):
        p = getIntersectPoint(p0, p0.plus(tangent0),
                              p1, p1.plus(tangent1))
        return p


# Test script below...
if __name__ == "__main__":

    # line 1 and 2 cross, 1 and 3 don't but would if extended, 2 and 3 are parallel
    # line 5 is horizontal, line 4 is vertical
    p1 = TFSPoint(1,5)
    p2 = TFSPoint(4,7)

    p3 = TFSPoint(4,5)
    p4 = TFSPoint(3,7)

    p5 = TFSPoint(4,1)
    p6 = TFSPoint(3,3)

    p7 = TFSPoint(3,1)
    p8 = TFSPoint(3,10)

    p9 =  TFSPoint(0,6)
    p10 = TFSPoint(5,6)

    p11 = (472.0, 116.0)
    p12 = (542.0, 116.0)

    assert None != calculateIntersectPoint(p1, p2, p3, p4), "line 1 line 2 should intersect"
    assert None != calculateIntersectPoint(p3, p4, p1, p2), "line 2 line 1 should intersect"
    assert None == calculateIntersectPoint(p1, p2, p5, p6), "line 1 line 3 shouldn't intersect"
    assert None == calculateIntersectPoint(p3, p4, p5, p6), "line 2 line 3 shouldn't intersect"
    assert None != calculateIntersectPoint(p1, p2, p7, p8), "line 1 line 4 should intersect"
    assert None != calculateIntersectPoint(p7, p8, p1, p2), "line 4 line 1 should intersect"
    assert None != calculateIntersectPoint(p1, p2, p9, p10), "line 1 line 5 should intersect"
    assert None != calculateIntersectPoint(p9, p10, p1, p2), "line 5 line 1 should intersect"
    assert None != calculateIntersectPoint(p7, p8, p9, p10), "line 4 line 5 should intersect"
    assert None != calculateIntersectPoint(p9, p10, p7, p8), "line 5 line 4 should intersect"

    print "\nSUCCESS! All asserts passed for doLinesIntersect"
