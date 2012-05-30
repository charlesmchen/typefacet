'''
robofont-extensions-and-scripts
TFSSegment.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''




import sys
import math

from TFSMath import *
import TFSIntersection
from TFSPoint import *
from TFSMap import TFSMap
from TFSValidationException import TFSValidationException

onJython = sys.platform.startswith('java')


def inferTValue(minValue, maxValue, value):
    return clamp01((value - minValue) / float(maxValue - minValue))


class TFSSegment(object):

    def __init__(self, *points):
        self.points = points
        self.startT = 0
        self.endT = 1
        self.validate()

    def validate(self):
        try:
            if not onJython:
                import types
                if type(self.points) not in (types.ListType, types.TupleType):
                    raise TFSValidationException('Unexpected points type: ' + str(type(self.points)))
                for point in self.points:
                    if not isinstance(point, TFSPoint):
                        raise TFSValidationException('Unexpected points type: ' + str(type(point)))

            if not (2 <= len(self.points) <= 4):
                raise TFSValidationException('Invalid segment')
            for point in self.points:
                point.validate()
            if self.startPoint() == self.endPoint():
                print 'self.startPoint()', self.startPoint(), 'self.endPoint()', self.endPoint()
                raise TFSValidationException('Empty segment')
            startVector = self.startVector()
            endVector = self.endVector()
#            if startVector.length() == 0:
#                print 'startVector', startVector
#                raise TFSValidationException('Empty start vector')
#            if endVector.length() == 0:
#                print 'endVector', endVector
#                raise TFSValidationException('Empty end vector')

            if len(self) == 4:
                cpIntersection = TFSIntersection.calculateIntersectPoint(*self.points)
                if cpIntersection is not None:
                    startVectorLength = startVector.length()
                    endVectorLength = endVector.length()
                    startIntersectionLength = cpIntersection.distanceTo(self.startPoint())
                    endIntersectionLength = cpIntersection.distanceTo(self.endPoint())
                    if ((startIntersectionLength > startVectorLength * 0.5) and
                        (endIntersectionLength > endVectorLength * 0.5)):
                        # this curve will cross itself.
                        raise TFSValidationException('Crossed cubic bezier')
        except TFSValidationException, e:
            print 'TFSSegment.validate', self.description()
            raise e

    def __repr__(self):
        return 'TFSSegment(%s)' % ( ', '.join([repr(point) for point in self.points]), )

    def __getitem__(self, index):
        return self.points[index]

    def __len__(self):
        return len(self.points)

    def __iter__(self):
        for point in self.points:
            yield point

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
#        return self.points == other.points
        return tuple(self.points) == tuple(other.points)

    def __hash__(self):
        return hash(tuple(self.points))

    def __str__(self):
        return self.description()

    def controlPoints(self):
        return self.points[1:-1]

    def description(self):
        return '[Segment(%d): %s ~%0.3f]' % ( len(self.points),
                                       ','.join(point.description() for point in self.points),
                                       self.startPoint().distanceTo(self.endPoint()),
                                      )

    def startPoint(self):
        return self.points[0]

    def endPoint(self):
        return self.points[-1]

    def copy(self):
        newPoints = list(self.points)
        return TFSSegment(*newPoints)

    def applyFunction(self, function):
        newPoints = list([function(point) for point in self.points])
        return TFSSegment(*newPoints)

    def roundWithDefaultPrecision(self):
        newPoints = list([point.roundWithDefaultPrecision() for point in self.points])
        return TFSSegment(*newPoints)

    def applyPlus(self, value):
        def function(point):
            return point.plus(value)
        return self.applyFunction(function)

    def applyScale(self, value):
        def function(point):
            return point.scale(value)
        return self.applyFunction(function)

    def applyScaleXY(self, xFactor, yFactor):
        newPoints = list([point.scaleXY(xFactor, yFactor) for point in self.points])
        return TFSSegment(*newPoints)

    def reverse(self):
        newPoints = list(self.points)
        newPoints.reverse()
        return TFSSegment(*newPoints)

    def split(self, t, forceMidpoint=None):
        t = clamp01(t)
        if t == 0 or t == 1:
            return [self,]
        if len(self.points) == 2:
            p0 = self.points[0]
            p1 = self.points[1]
            midpoint = p0.midpoint(p1, t)
            if forceMidpoint:
                midpoint = forceMidpoint
            return [TFSSegment(p0, midpoint), TFSSegment(midpoint, p1)]
        elif len(self.points) == 3:
            p0, p1, p2 = self.points
            midpoint, cp0, cp1 = evaluateQuadraticSpline2D_points_all(p0, p1, p2, t)
            if forceMidpoint:
                midpoint = forceMidpoint
            return [TFSSegment(p0, cp0, midpoint), TFSSegment(midpoint, cp1, p1)]
        elif len(self.points) == 4:
            p0, p1, p2, p3 = self.points
            midpoint, cp0, cp1, cp2, cp3 = evaluateCubicSpline2D_points_all(p0, p1, p2, p3, t)
            if forceMidpoint:
                midpoint = forceMidpoint
            return [TFSSegment(p0, cp0, cp1, midpoint), TFSSegment(midpoint, cp2, cp3, p3)]
        else:
            raise Exception('split(): Invalid segment point count: %d' % len(self.points))

    def boundingBox(self):
        return boundingBox_points(self.points)

    def evaluate(self, t):
        if len(self.points) == 2:
            p0, p1 = self.points
            return p0.midpoint(p1, t)
        elif len(self.points) == 3:
            p0, p1, p2 = self.points
            return evaluateQuadraticSpline2D_point(p0, p1, p2, t)
        elif len(self.points) == 4:
            p0, p1, p2, p3 = self.points
            return evaluateCubicSpline2D_point(p0, p1, p2, p3, t)
        else:
            raise Exception('evaluatePointsWithT(): Invalid segment point count: %d' % len(self.points))

    def evaluateWithTangent(self, t):
        if len(self.points) == 2:
            p0, p1 = self.points
            return p0.midpoint(p1, t), p1.minus(p0).normalize(), p0, p1
        elif len(self.points) == 3:
            p0, p1, p2 = self.points
            return evaluateQuadraticSpline2D_pointAndTangent(p0, p1, p2, t)
        elif len(self.points) == 4:
            p0, p1, p2, p3 = self.points
            return evaluateCubicSpline2D_pointAndTangent(p0, p1, p2, p3, t)
        else:
            raise Exception('evaluateWithTangent(): Invalid segment point count: %d' % len(self.points))

    def startTangent(self):
        try:
            return self.points[1].minus(self.points[0]).normalize()
        except ZeroDivisionError, e:
            print 'Segment.normalize() ZeroDivisionError', self.description()
            raise e

    def endTangent(self):
        return self.points[-1].minus(self.points[-2]).normalize()

    def startVector(self):
        return self.points[1].minus(self.points[0])

    def endVector(self):
        return self.points[-1].minus(self.points[-2])

    def evaluateRangeWithPrecision(self, precision):
        if len(self.points) == 2:
            return list(self.points)
        elif len(self.points) in (3, 4):
            result = [self.points[0],]
            for i in xrange(1, precision):
                t = i / float(precision)
                result.append(self.evaluate(t))
            result.append(self.points[-1])
            return result
        else:
            raise Exception('evaluatePointsWithT(): Invalid segment point count: %d' % len(self.points))

    def evaluateWithMaxPrecision(self, precision):
        # Backward compatability
        return self.evaluateRangeWithPrecision(precision)

    def isColinear_linear(self, p):
        bBox = self.boundingBox()
        if not bBox.containsPoint(p):
            return None
        p0 = self.startPoint()
        p1 = self.endPoint()
        if p0.x == p1.x:
            if p0.x == p.x:
                t = inferTValue(p0.y, p1.y, p.y)
#                print 'isColinear_linear horizontal', p0.description(), p1.description(), p.description(), t
                return t
            else:
                return None
        if p0.y == p1.y:
            if p0.y == p.y:
                t = inferTValue(p0.x, p1.x, p.x)
#                print 'isColinear_linear vertical', p0.description(), p1.description(), p.description(), t
                return t
            else:
                return None

        tx = inferTValue(p0.x, p1.x, p.x)
        ty = inferTValue(p0.y, p1.y, p.y)
        if abs(tx - ty) > getFloatRoundingTolerance():
            return None
        t = (tx + ty) * 0.5
#        print 'isColinear_linear', p0.description(), p1.description(), p.description(), t
        return t

    def isColinear_recursiveClipping(self, p, level=0):
#        print '\t' * level, 'isColinear_recursiveClipping', self.description(), p.description()

        if p == self.startPoint():
            return self.startT
        if p == self.endPoint():
            return self.endT

        bbox = self.boundingBox()
        if not bbox.containsPoint(p):
            return None

        scaleFactor = max(bbox.width, bbox.height)
        SCALE_FACTOR_THRESHOLD = 0.001
        if scaleFactor < SCALE_FACTOR_THRESHOLD:
            selfT = self.isColinear_linear(p)
            if selfT is None:
                return None
            return self.startT + (self.endT - self.startT) * selfT

        left, right = self.split_recursiveClipping(0.5)
#        print '\t' * level, 'left', left
#        print '\t' * level, 'right', right

        for subsegment in (left, right):
#            print '\t' * level, 'dividing into', subsegment.description()
            selfT = subsegment.isColinear_recursiveClipping(p, level=level+1)
            if selfT is not None:
                return selfT
        return None


    def isColinear(self, p):
        '''
        If point is colinear, return t
        else return None
        '''
        if p == self.startPoint():
            return None
        if p == self.endPoint():
            return None

        if len(self.points) == 2:
            return self.isColinear_linear(p)
        elif len(self.points) == 3:
            return self.isColinear_recursiveClipping(p)
        elif len(self.points) == 4:
            return self.isColinear_recursiveClipping(p)
        else:
            raise Exception('evaluatePointsWithT(): Invalid segment point count: %d' % len(self.points))


    def split_recursiveClipping(self, t):
#        MIN_SPLIT_LENGTH = 0.0001
#        if self.startPoint().distanceTo(self.endPoint()) < MIN_SPLIT_LENGTH:
#            return [self,]

#        left, right = self.split(t)
        try:
            left, right = self.split(t)
        except TFSValidationException, e:
            '''
            Due to rounding error, we may get validation errors
            when slicing bezier curves very finely.
            '''
            return [self,]


        left.startT = self.startT
        left.endT = right.startT = self.startT + (self.endT - self.startT) * t
        right.endT = self.endT

#        print 'cutting', self.description(), self.startT, self.endT
#        print '\t', 't', t
#        print '\t', 'left', left.description(), left.startT, left.endT
#        print '\t', 'left', right.description(), right.startT, right.endT
        return left, right


    def findIntersection_naive(self, other_segment, debugMode=False):
        point = TFSIntersection.calculateIntersectPoint(self.startPoint(),
                                                         self.endPoint(),
                                                         other_segment.startPoint(),
                                                         other_segment.endPoint(),
                                                         debugMode=debugMode)
#        print 'findIntersection_naive', '', self.startPoint(), self.endPoint(), other_segment.startPoint(), other_segment.endPoint()
#        print 'findIntersection_naive', 'point', point
        if debugMode:
            print 'findIntersection_naive', 'point', point
        if not point:
            if debugMode:
                print 'findIntersection_naive.0'
            return None

        def findT(p0, p1, p):
            if p0.x == p1.x:
                return inferTValue(p0.y, p1.y, p.y)
            else:
                return inferTValue(p0.x, p1.x, p.x)

        def interpolateT(startT, endT, t):
            result = startT + (endT - startT) * t
#            print 'interpolateT', startT, endT, 't', t, '->', result
            return result
        selfT = findT(self.startPoint(), self.endPoint(), point)
        selfT = interpolateT(self.startT, self.endT, selfT)
        otherT = findT(other_segment.startPoint(), other_segment.endPoint(), point)
        otherT = interpolateT(other_segment.startT, other_segment.endT, otherT)

        if debugMode:
            print 'findIntersection_naive.3'
        return selfT, otherT, point


    def findIntersection_recursiveClipping(self, other_segment, level=0):
#        if level > 2:
#            return None
#        print '\t' * level, 'findIntersection_recursiveClipping considering', self.description(), other_segment.description()

        bbox = self.boundingBox()
        other_bbox = other_segment.boundingBox()
        if not bbox.intersects(other_bbox):
            return None

        '''
        TODO: refactor to only subdivide non-linear bezier curves.
        Threshold should also only be based on non-linear segments.
        '''

        scaleFactor = max(bbox.width, bbox.height, other_bbox.width, other_bbox.height)
        SCALE_FACTOR_THRESHOLD = 0.001
        if scaleFactor < SCALE_FACTOR_THRESHOLD:
            intersection = self.findIntersection_naive(other_segment)
#            intersection = self.findIntersection_naive(other_segment, debugMode=True)
            if intersection is None:
                return None

#            selfT, otherT, point = intersection
#            print 'selfT, otherT, point', selfT, otherT, point, point.description()
            return intersection

        selfCuts = self.split_recursiveClipping(0.5)
        otherCuts = other_segment.split_recursiveClipping(0.5)

        if len(selfCuts) == len(otherCuts) == 1:
            '''
            If neither segment can be split further due to rounding error,
            Use naive intersection logic.
            '''
            subsegment, = selfCuts
            other_subsegment, = otherCuts

            intersection = subsegment.findIntersection_naive(other_subsegment, debugMode=True)
            if intersection is None:
                return None

#            selfT, otherT, point = intersection
#            print 'selfT, otherT, point', selfT, otherT, point, point.description()
            return intersection

        for subsegment in selfCuts:
            for other_subsegment in otherCuts:
#                print '\t' * level, 'dividing into', subsegment.description(), other_subsegment.description()
#                intersection = None
                intersection = subsegment.findIntersection_recursiveClipping(other_subsegment, level=level+1)
                if intersection:
#                    selfT, otherT, point = intersection
#                    print 'selfT, otherT, point', selfT, otherT, point, point.description()
                    return intersection
        return None

    def isStraight(self):
        return len(self.points) == 2

    def plusOffset(self, offset):
        newPoints = []
        for point in self.points:
            newPoints.append(point.plus(offset))
        return TFSSegment(*newPoints)

    def findIntersection_raw(self, other_segment, debugMode=False):
        DEBUG = False
        if DEBUG:
            print 'findIntersection considering', self.description(), other_segment.description()

        minmax0 = self.minmax()
        minmax1 = other_segment.minmax()
        if ((minmax0.maxX < minmax1.minX) or
            (minmax1.maxX < minmax0.minX) or
            (minmax0.maxY < minmax1.minY) or
            (minmax1.maxY < minmax0.minY)):
            if debugMode:
                print 'findIntersection_raw.0'
            return None

        selfT = self.isColinear(other_segment.startPoint())
        if selfT is not None:
            if DEBUG:
                print 'colinear1', selfT
            if debugMode:
                print 'findIntersection_raw.1'
            return selfT, 0, other_segment.startPoint()
        selfT = self.isColinear(other_segment.endPoint())
        if selfT is not None:
            if DEBUG:
                print 'colinear2', selfT
            if debugMode:
                print 'findIntersection_raw.2'
            return selfT, 1, other_segment.endPoint()

        otherT = other_segment.isColinear(self.startPoint())
        if otherT is not None:
            if DEBUG:
                print 'colinear3', otherT
            if debugMode:
                print 'findIntersection_raw.3'
            return 0, otherT, self.startPoint()
        otherT = other_segment.isColinear(self.endPoint())
        if otherT is not None:
            if DEBUG:
                print 'colinear4', otherT
            if debugMode:
                print 'findIntersection_raw.4'
            return 1, otherT, self.endPoint()

        '''
        Now that we know the neither segment has an endPoint that is collinear,
        check endPoints.
        '''
        if self.startPoint() in (other_segment.startPoint(),
                                 other_segment.endPoint()):
            if debugMode:
                print 'findIntersection_raw.5'
            return None
        if self.endPoint() in (other_segment.startPoint(),
                                 other_segment.endPoint()):
            if debugMode:
                print 'findIntersection_raw.6'
            return None

        if self.isStraight() and other_segment.isStraight():
#        if self.isStraight() and other_segment.isStraight() and False:
            intersection = self.findIntersection_naive(other_segment, debugMode=debugMode)
        else:
            intersection = self.findIntersection_recursiveClipping(other_segment)

        if intersection:
            selfT, otherT, point = intersection
            if debugMode:
                print 'findIntersection_raw.7'
            return selfT, otherT, point
        if debugMode:
            print 'findIntersection_raw.8'
        return None

    def findIntersection(self, other_segment):
        intersection = self.findIntersection_raw(other_segment)
        if intersection:
            selfT, otherT, point = intersection
            return self, other_segment, selfT, otherT, point
        return None

    def tangentToSegment(self, other):


        DEBUG = True
        DEBUG = False

        if DEBUG:
            print
            print 'tangentToSegment', self.description(), other.description()

        def createPoint(segment, t):
            result = TFSMap()
            result.t = t
            result.p, result.tangent, _, _ = segment.evaluateWithTangent(t)
#            result.angle = result.tangent.atan2()
            result.angle = normalizeRadians(result.tangent.atan2())
            return result

        def printPoint(name, point):
            print name,
            for attr in ('t', 'p', 'tangent', 'angle'):
                print attr, getattr(point, attr),
            print

        endPoint00 = createPoint(self, 0)
        endPoint01 = createPoint(self, 1)
        endPoint10 = createPoint(other, 0)
        endPoint11 = createPoint(other, 1)

        if DEBUG:
            printPoint('endPoint00', endPoint00)
            printPoint('endPoint01', endPoint01)
        if DEBUG:
            printPoint('endPoint10', endPoint10)
            printPoint('endPoint11', endPoint11)

        # Invert ts if necessary so that angles always increase with t.
        if normalizeRadiansDiff(endPoint01.angle - endPoint00.angle) < 0:
            endPoint00, endPoint01 = endPoint01, endPoint00
        if normalizeRadiansDiff(endPoint11.angle - endPoint10.angle) < 0:
            endPoint10, endPoint11 = endPoint11, endPoint10


        endPoint01.angle = normalizeRadiansAboveAngle(endPoint01.angle, endPoint00.angle)
        endPoint11.angle = normalizeRadiansAboveAngle(endPoint11.angle, endPoint10.angle)

        # Start at the midpoint of each segment
        t0 = 0.5
        t1 = 0.5

        if DEBUG:
            printPoint('endPoint00\'', endPoint00)
            printPoint('endPoint01\'', endPoint01)
            printPoint('endPoint10\'', endPoint10)
            printPoint('endPoint11\'', endPoint11)

        MAX_ATTEMPTS = 32
        for _ in xrange(MAX_ATTEMPTS):
#        while True:
            point0 = createPoint(self, t0)
            point1 = createPoint(other, t1)

            point0.angle = normalizeRadiansAboveAngle(point0.angle, endPoint00.angle)
            point1.angle = normalizeRadiansAboveAngle(point1.angle, endPoint10.angle)

            if DEBUG:
                print
                printPoint('point0', point0)
                printPoint('point1', point1)

            angle = point1.p.minus(point0.p).atan2()
            if DEBUG:
                print 'angle', angle
            diff0 = normalizeRadiansDiff(angle - point0.angle)
            diff1 = normalizeRadiansDiff(angle - point1.angle)
            if DEBUG:
                print 'diff0', diff0, 'diff1', diff1

            TANGENT_TO_SEGMENT_PRECISION = getFloatRoundingTolerance()
            if abs(diff0) < TANGENT_TO_SEGMENT_PRECISION and abs(diff1) < TANGENT_TO_SEGMENT_PRECISION:
                # success
                if DEBUG:
                    print 'success', 't0, t1, point0.p, point1.p', t0, t1, point0.p, point1.p
                    print
                return t0, t1, point0.p, point1.p

            # Select an endPoint to move towards.
            endPoint0 = endPoint01 if diff0 > 0 else endPoint00
            endPoint1 = endPoint11 if diff1 > 0 else endPoint10
            if DEBUG:
                printPoint('endPoint0', endPoint0)
                printPoint('endPoint1', endPoint1)
            factor0 = normalizeRadiansDiff(angle - point0.angle) / normalizeRadiansDiff(endPoint0.angle - point0.angle)
            factor1 = normalizeRadiansDiff(angle - point1.angle) / normalizeRadiansDiff(endPoint1.angle - point1.angle)
            BREAKING_FACTOR = 0.85
            factor0 *= BREAKING_FACTOR
            factor1 *= BREAKING_FACTOR
            t0 = t0 + (endPoint0.t - t0) * factor0
            t1 = t1 + (endPoint1.t - t1) * factor1

            if DEBUG:
                print 'factor0', factor0, 't0', t0
                print 'factor1', factor1, 't1', t1

        raise Exception('Algorithm did not converge.')

    def setEndPoint(self, value):
        self.points = list(self.points)
        self.points[-1] = value

    def setStartPoint(self, value):
        self.points = list(self.points)
        self.points[0] = value

    def tangentToPoint(self, dst):
        if len(self.points) not in (3, 4):
            raise Exception('Not a bezier curve')

        t0 = 0
        t1 = 1

        def radiansDiff(angle0, angle1):
            result = angle1 - angle0
            while result < -math.pi:
                result += 2 * math.pi
            while result > math.pi:
                result -= 2 * math.pi
            return result

        def evaluateTValue(t, dst):
            p, tangent, _, _ = self.evaluateWithTangent(t)
            pDiff = dst.minus(p)
            pAngle = math.atan2(pDiff.y, pDiff.x)
            tangentAngle = math.atan2(tangent.y, tangent.x)
            angleDiff = radiansDiff(pAngle, tangentAngle)
            score = pDiff.normalize().dotProduct(tangent.normalize())
            return p, tangent, angleDiff, score

        p0, tangent0, angleDiff0, score0 = evaluateTValue(t0, dst)
#        print 't0, p0, tangent0, angleDiff0, score0', t0, p0, tangent0, angleDiff0, score0
        p1, tangent1, angleDiff1, score1 = evaluateTValue(t1, dst)
#        print 't1, p1, tangent1, angleDiff1, score1', t1, p1, tangent1, angleDiff1, score1

        # We can't interpolate if the tangents of the endPoints of the bezier curve don't
        # enclose the destination point.
        if angleDiff0 < 0 and angleDiff1 < 0:
            raise Exception('Invalid bezier curve')
        if angleDiff0 > 0 and angleDiff1 > 0:
            raise Exception('Invalid bezier curve')

        if angleDiff0 < angleDiff1:
            tmin, pmin, tangentmin, angleDiffmin, scoremin = t0, p0, tangent0, angleDiff0, score0
            tmax, pmax, tangentmax, angleDiffmax, scoremax = t1, p1, tangent1, angleDiff1, score1
        else:
            tmin, pmin, tangentmin, angleDiffmin, scoremin = t1, p1, tangent1, angleDiff1, score1
            tmax, pmax, tangentmax, angleDiffmax, scoremax = t0, p0, tangent0, angleDiff0, score0

        while True:
            tm = (tmin + tmax) * 0.5
            pm, tangentm, angleDiffm, scorem = evaluateTValue(tm, dst)
#            print 'tm, pm, tangentm, angleDiffm, scorem', tm, pm, tangentm, angleDiffm, scorem

            TANGENT_TO_POINT_PRECISION = 0.9999

            if scorem >= TANGENT_TO_POINT_PRECISION:
                return tm, pm
            if angleDiffm < 0:
                tmin, pmin, tangentmin, angleDiffmin, scoremin = tm, pm, tangentm, angleDiffm, scorem
            else:
                tmax, pmax, tangentmax, angleDiffmax, scoremax = tm, pm, tangentm, angleDiffm, scorem

    def minmax(self):
        return minmaxPoints(self.points)

    def minmaxEvaluated(self, precision):
        return minmaxPoints(self.evaluateWithMaxPrecision(precision))

    def endPointDistance(self):
        return self.startPoint().distanceTo(self.endPoint())
