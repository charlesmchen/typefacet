'''
robofont-extensions-and-scripts
TFSOval.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''




import math

from TFSPoint import *
from TFSPath import TFSPath, TFSSegment
from TFSMap import TFSMap

CIRCLE_SPLINE_CONSTANT = 0.55228475

class TFSOval(object):

    def __init__(self, center, hRadius, vRadius, rotation=0):
        self.center = center
        self.hRadius = hRadius
        self.vRadius = vRadius
        self.rotation = rotation

    def alignBottom(self, value):
        p = self.evaluate(math.pi * 1.5)
        adj = value - p.y
        self.center.y += adj
        return self

    def alignTop(self, value):
        p = self.evaluate(math.pi * 0.5)
        adj = value - p.y
        self.center.y += adj
        return self

    def alignRight(self, value):
        p = self.evaluate(math.pi * 0.0)
        adj = value - p.x
        self.center.x += adj
        return self

    def alignLeft(self, value):
        p = self.evaluate(math.pi * 1.0)
        adj = value - p.x
        self.center.x += adj
        return self

    def alignCenterX(self, value):
        self.center.x = value
        return self

    def alignCenterY(self, value):
        self.center.y = value
        return self

    def withScalingDoubled(self, value):
        hDiff = self.hRadius * (value - 1)
        vDiff = self.vRadius * (value - 1)
        return TFSOval(self.center.copy(),
                      self.hRadius + 2 * hDiff,
                      self.vRadius + 2 * vDiff,
                      rotation=self.rotation,
                      tweakRadii=False)

    def copy(self):
        return TFSOval(self.center.copy(),
                      self.hRadius,
                      self.vRadius,
                      rotation=self.rotation,
                      tweakRadii=False)

    def withScaling(self, value):
        hDiff = self.hRadius * (value - 1)
        vDiff = self.vRadius * (value - 1)
        return TFSOval(self.center.copy(),
                      self.hRadius + hDiff,
                      self.vRadius + vDiff,
                      rotation=self.rotation,
                      tweakRadii=False)

    def withHRadius(self, value):
        return TFSOval(self.center.copy(),
                      value,
                      self.vRadius,
                      rotation=self.rotation,
                      tweakRadii=False)

    def withVRadius(self, value):
        return TFSOval(self.center.copy(),
                      self.hRadius,
                      value,
                      rotation=self.rotation,
                      tweakRadii=False)

    def rotatePointAroundCenter(self, value):
        value = value.minus(self.center)
        value = value.rotate(self.rotation)
        value = value.plus(self.center)
        return value

    def createQuarterPathSegment(self, p0, p1, p2):
        diff01 = p1.minus(p0)
        diff12 = p2.minus(p1)
        v01 = diff01.normalize()
        v12 = diff12.normalize()
        points = [p0,
                    p0.plus(v01.scale(diff01.length() * CIRCLE_SPLINE_CONSTANT)),
                    p2.minus(v12.scale(diff12.length() * CIRCLE_SPLINE_CONSTANT)),
                    p2]
        if self.rotation != 0:
            points = [self.rotatePointAroundCenter(point) for point in points]
        return TFSSegment(*points)

    def createPath(self):
        ps = controlPointsWithSides(self.center.x - self.hRadius,
                                    self.center.x + self.hRadius,
                                    self.center.y + self.vRadius,
                                    self.center.y - self.vRadius)
        return TFSPath(True,
                     self.createQuarterPathSegment(ps.lc, ps.tl, ps.tc),
                     self.createQuarterPathSegment(ps.tc, ps.tr, ps.rc),
                     self.createQuarterPathSegment(ps.rc, ps.br, ps.bc),
                     self.createQuarterPathSegment(ps.bc, ps.bl, ps.lc))

    def evaluate(self, angle):
        angle -= self.rotation
        point = TFSPoint(self.center.x + math.cos(angle) * self.hRadius,
                       self.center.y + math.sin(angle) * self.vRadius)
        point = self.rotatePointAroundCenter(point)
        return point

    def evaluateTangent(self, angle):
        arc = self.createArc(angle, angle + math.pi * 0.25)
        return arc.startTangent()

    def leftCrossTangentToCircle(self, other):
        return self.tangentToCircle(other, isLeft=True, isCross=True)

    def leftTangentToCircle(self, other):
        return self.tangentToCircle(other, isLeft=True)

    def rightTangentToCircle(self, other):
        return self.tangentToCircle(other, isLeft=False)

    def tangentToCircle(self, other, isLeft, isCross=False):

        def getTangentAngleDiff(tangentAngle):
#            tangentAngle = (maxAngle + minAngle) * 0.5
            if isLeft:
                sideAngle = tangentAngle + math.pi / 2
            else:
                sideAngle = tangentAngle - math.pi / 2

            p0 = self.evaluate(sideAngle)
            if isCross:
                otherAngle = sideAngle + math.pi * 1.0
            else:
                otherAngle = sideAngle
            p1 = other.evaluate(otherAngle)

            angle01 = p1.minus(p0).atan2()
            pTangent = self.evaluateTangent(sideAngle)
#            print 'pTangent', pTangent
            if isLeft:
                pTangent = pTangent.invert()
#            print 'pTangent', pTangent
            pTangentAngle = pTangent.atan2()

            anglesDiff = normalizeRadiansDiff(angle01 - pTangentAngle)
#            print 'tangentAngle', tangentAngle
#            print 'pTangentAngle', pTangentAngle
#            print 'angle01', angle01
#            print 'anglesDiff', anglesDiff
            return anglesDiff, p0, p1

        centersDiff = other.center.minus(self.center)
        centersAngle = math.atan2(centersDiff.y, centersDiff.x)
        maxAngle = centersAngle + math.pi * 0.5
        minAngle = centersAngle - math.pi * 0.5

        minDiff, _, _ = getTangentAngleDiff(minAngle)
        maxDiff, _, _ = getTangentAngleDiff(maxAngle)
#        print 'minAngle', minAngle
#        print 'maxAngle', maxAngle
#        print 'minDiff', minDiff
#        print 'maxDiff', maxDiff

        if maxDiff < minDiff:
            maxDiff, minDiff = minDiff, maxDiff
            maxAngle, minAngle = minAngle, maxAngle
#            print 'minAngle\'', minAngle
#            print 'maxAngle\'', maxAngle
#            print 'minDiff\'', minDiff
#            print 'maxDiff\'', maxDiff

        MAX_ATTEMPTS = 32
        for _ in xrange(MAX_ATTEMPTS):
            tangentAngle = (maxAngle + minAngle) * 0.5
            anglesDiff, p0, p1 = getTangentAngleDiff(tangentAngle)

#            print
#            print 'tangentAngle', tangentAngle
#            print 'anglesDiff', anglesDiff

            OVAL_TO_OVAL_TANGENT_PRECISION_RADIANS = getFloatRoundingTolerance()
            OVAL_TO_OVAL_TANGENT_APPROXIMATION_FACTOR = 0.65
            OVAL_TO_OVAL_TANGENT_APPROXIMATION_FACTOR = 0.5

#            print
#            print 'tangentAngle', tangentAngle
#            print 'centersAngle', centersAngle
##            print 'tangentsAngle', tangentsAngle
#            print 'anglesDiff', anglesDiff

            if abs(anglesDiff) < OVAL_TO_OVAL_TANGENT_PRECISION_RADIANS:
                result = TFSMap()
                result.p0 = p0
                result.p1 = p1
                result.angle = tangentAngle
                return result

            if anglesDiff > 0:
                maxAngle = tangentAngle
            else:
                minAngle = tangentAngle

        raise Exception('Did not converge')


    def tangentToCircle_base(self, other, tangentFunction):
        centersDiff = other.center.minus(self.center)
        centersAngle = math.atan2(centersDiff.y, centersDiff.x)
        maxAngle = centersAngle + math.pi * 0.5
        minAngle = centersAngle - math.pi * 0.5

        minDiff, _, _ = tangentFunction(minAngle)
        maxDiff, _, _ = tangentFunction(maxAngle)
#        print 'minAngle', minAngle
#        print 'maxAngle', maxAngle
#        print 'minDiff', minDiff
#        print 'maxDiff', maxDiff

        if maxDiff < minDiff:
            maxDiff, minDiff = minDiff, maxDiff
            maxAngle, minAngle = minAngle, maxAngle
#            print 'minAngle\'', minAngle
#            print 'maxAngle\'', maxAngle
#            print 'minDiff\'', minDiff
#            print 'maxDiff\'', maxDiff

        MAX_ATTEMPTS = 32
        for _ in xrange(MAX_ATTEMPTS):
            tangentAngle = (maxAngle + minAngle) * 0.5
            anglesDiff, p0, p1 = tangentFunction(tangentAngle)

#            print
#            print 'tangentAngle', tangentAngle
#            print 'anglesDiff', anglesDiff

            OVAL_TO_OVAL_TANGENT_PRECISION_RADIANS = getFloatRoundingTolerance()

#            print
#            print 'tangentAngle', tangentAngle
#            print 'centersAngle', centersAngle
##            print 'tangentsAngle', tangentsAngle
#            print 'anglesDiff', anglesDiff

            if abs(anglesDiff) < OVAL_TO_OVAL_TANGENT_PRECISION_RADIANS:
                result = TFSMap()
                result.p0 = p0
                result.p1 = p1
                result.angle = tangentAngle
                return result

            if anglesDiff > 0:
                maxAngle = tangentAngle
            else:
                minAngle = tangentAngle

        raise Exception('Did not converge')

    def tangentToCircleCrossFixedWidth(self, other, isLeft=True, isCross=False, otherOffsetH=0, otherOffsetV=0):
        def tangentFunction(tangentAngle):
#            tangentAngle = (maxAngle + minAngle) * 0.5
            if isLeft:
                sideAngle = tangentAngle + math.pi / 2
            else:
                sideAngle = tangentAngle - math.pi / 2

            p0 = self.evaluate(sideAngle)
            if isCross:
                otherAngle = sideAngle + math.pi * 1.0
            else:
                otherAngle = sideAngle
            p1 = other.evaluate(otherAngle)
            if otherOffsetH and otherOffsetV:
                otherTangent = self.evaluateTangent(otherAngle).normalize()
                otherAxis = otherTangent.rotate(math.pi * 0.5)
#                otherAxis = other.center.minus(p1).normalize()
                otherOffset = scaleVectorHV(otherAxis, otherOffsetH, otherOffsetV)
                p1 = p1.plus(otherOffset)

            angle01 = p1.minus(p0).atan2()

            pTangent = self.evaluateTangent(sideAngle)
#            print 'pTangent', pTangent
            if isLeft:
                pTangent = pTangent.invert()
#            print 'pTangent', pTangent
            pTangentAngle = pTangent.atan2()

            anglesDiff = normalizeRadiansDiff(angle01 - pTangentAngle)
#            print 'tangentAngle', tangentAngle
#            print 'pTangentAngle', pTangentAngle
#            print 'angle01', angle01
#            print 'anglesDiff', anglesDiff
            return anglesDiff, p0, p1

        return self.tangentToCircle_base(other, tangentFunction)


    def findAngleWithTangentAngle(self, value):
#        value = normalizeRadians(value)

        angle0 = math.pi * 0.0
        angle1 = math.pi * 2.0

        while True:
            angle = (angle0 + angle1) * 0.5

            FIND_ANGLE_WITH_TANGLE_ANGLE_PRECISION_RADIANS = getFloatRoundingTolerance()
            angleDiff = angle1 - angle0
            if abs(angleDiff) < FIND_ANGLE_WITH_TANGLE_ANGLE_PRECISION_RADIANS:
#                print 'angle', angle, 'angleDiff', angleDiff
                return angle

            tangentAngle0 = self.evaluateTangent(angle0).atan2()
            tangentAngle1 = self.evaluateTangent(angle1).atan2()

            tangentAngle1 = normalizeRadiansAboveAngle(tangentAngle1, tangentAngle0)
            value = normalizeRadiansAboveAngle(value, tangentAngle0)

            if not (tangentAngle0 <= value <= tangentAngle1):
                raise Exception('Could not bracket tangent angle')

            tangentAngle = self.evaluateTangent(angle).atan2()
            if tangentAngle < value:
                angle0 = angle
            else:
                angle1 = angle

#            print '', locals()

    def createArc(self, startAngle, endAngle):
        startAngle -= self.rotation
        endAngle -= self.rotation

#        startPoint = TFSPoint(self.center.x + math.cos(startAngle) * self.hRadius,
#                          self.center.y + math.sin(startAngle) * self.vRadius)
#        endPoint = TFSPoint(self.center.x + math.cos(endAngle) * self.hRadius,
#                          self.center.y + math.sin(endAngle) * self.vRadius)

        # normalize radians
        while endAngle < startAngle:
            endAngle += math.pi * 2
        angleDiff = endAngle - startAngle
        # No angle should be longer than a quarter of the circle, for precision purposes.
        segmentCount = max(1, int(math.ceil(angleDiff / (math.pi * 0.5))))

        # The bezier control point offsets have to be scaled down to reflect that each
        # segment is less than a "quarter circle".
        segmentAngle = angleDiff / segmentCount
        segmentFactor = segmentAngle / (math.pi * 0.5)

#        print 'segmentAngle', segmentAngle
#        print 'segmentFactor', segmentFactor
#        print 'segmentCount', segmentCount, type(segmentCount)
#        controls = []
        lastAngle = None
        lastPoint = None
        segments = []
        for index in xrange(segmentCount + 1):
            phase = index / float(segmentCount)
            angle = startAngle + phase * angleDiff
            point = TFSPoint(self.center.x + math.cos(angle) * self.hRadius,
                                  self.center.y + math.sin(angle) * self.vRadius)
            if index > 0:
                controlPoint0 = TFSPoint(lastPoint.x + math.cos(lastAngle + math.pi * 0.5) * self.hRadius * CIRCLE_SPLINE_CONSTANT * segmentFactor,
                                       lastPoint.y + math.sin(lastAngle + math.pi * 0.5) * self.vRadius * CIRCLE_SPLINE_CONSTANT * segmentFactor)
                controlPoint1 = TFSPoint(point.x - math.cos(angle + math.pi * 0.5) * self.hRadius * CIRCLE_SPLINE_CONSTANT * segmentFactor,
                                       point.y - math.sin(angle + math.pi * 0.5) * self.vRadius * CIRCLE_SPLINE_CONSTANT * segmentFactor)
#                controls.append( (angle, controlPoint0, ) )
#                controls.append( (angle, controlPoint1, ) )
                points = [lastPoint, controlPoint0, controlPoint1, point]
                if self.rotation != 0:
                    points = [self.rotatePointAroundCenter(point) for point in points]
                segments.append(TFSSegment(*points))
                pass
            lastAngle = angle
            lastPoint = point
#            controls.append( (angle, point, ) )
        return TFSPath(False, *segments)
#        return openPathWithPoints( *[ point for angle, point in controls])
##        return TFSPath(False, )
#        return startPoint
