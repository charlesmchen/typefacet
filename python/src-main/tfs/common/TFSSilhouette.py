'''
robofont-extensions-and-scripts
TFSSilhouette.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''



import math

from TFSPoint import scaleVectorHV
from TFSPath import *
import TFSIntersection as TFSntersection
from TFSTesselation import TFSTesselation as FTesselation
from TFSMath import *
from TFSOval import TFSOval as TFSOval
from TFSContoursException import TFSContoursException


def inflateSegmentLeft(segment, hDistance, vDistance):
    p0 = segment.startPoint()
    p1 = segment.endPoint()
    startTangent = segment.startTangent()


    if len(segment) == 2:
        offset = scaleVectorHV(startTangent.rotate(math.pi * 0.5), hDistance, vDistance)
        p0 = p0.plus(offset)
        p1 = p1.plus(offset)
        newPoints = (p0, p1)
    elif len(segment) == 3:
        endTangent = segment.endTangent()
        startOffset = scaleVectorHV(startTangent.rotate(math.pi * 0.5), hDistance, vDistance)
        endOffset = scaleVectorHV(endTangent.rotate(math.pi * 0.5), hDistance, vDistance)
        p0 = p0.plus(startOffset)
        p1 = p1.plus(endOffset)
        cp0 = TFSntersection.intersectionWithTangents(p0, startTangent, p1, endTangent.invert())
        newPoints = (p0, cp0, p1)
    elif len(segment) == 4:
        endTangent = segment.endTangent()
        startOffset = scaleVectorHV(startTangent.rotate(math.pi * 0.5), hDistance, vDistance)
        endOffset = scaleVectorHV(endTangent.rotate(math.pi * 0.5), hDistance, vDistance)
        oldScale = p0.distanceTo(p1)
        p0 = p0.plus(startOffset)
        p1 = p1.plus(endOffset)
        newScale = p0.distanceTo(p1)
        cp0 = p0.plus(segment.startVector().scale(newScale / oldScale))
        cp1 = p1.minus(segment.endVector().scale(newScale / oldScale))
        newPoints = (p0, cp0, cp1, p1)
    else:
        raise Exception('Invalid segment')

    try:
        return TFSSegment(*newPoints).roundWithDefaultPrecision()
    except TFSValidationException, e:
        '''
        Inflating a segment can result in an empty or otherwise invalid segment.
        In fact, this will happen often since we'll be deflating previously
        inflated rounding curves.
        That's fine; ignore them.
        '''
        return None


def inflatePaths(paths, hDistance, vDistance=None, debugMode=False):
    return inflateDeflatePaths(paths, reversePaths=False, hDistance=hDistance, vDistance=vDistance, debugMode=debugMode)

inflatePathsLeft = inflatePaths

def deflatePaths(paths, hDistance, vDistance=None, debugMode=False):
    return inflateDeflatePaths(paths, reversePaths=True, hDistance=hDistance, vDistance=vDistance, debugMode=debugMode)

def inflateDeflatePath(path, deflating, hDistance, vDistance=None, debugMode=False):
    '''
    Edge case: What happens if we inflate an oval curve beyond it's center?
    Edge case: What happens if segment has a start or end vector of zero length?
        Should be fine.

    '''

    def isEmptySegment(segment):
        return segment.startPoint() == segment.endPoint()

    if vDistance is None:
        vDistance = hDistance

    # TODO: We don't want to do this, right?
#    paths = [orientClosedPathClockwise(path) for path in paths]

    path = path.removeEmptySegments()

    TIME_INFLATE_DEFLATE_PATHS = False
#    debugMode = True

    if TIME_INFLATE_DEFLATE_PATHS:
        import time
        time0 = time.time()

    if deflating:
        path = path.reverse()

#    raise TFSContoursException('argh', [path,])

    if debugMode:
        print 'inflateDeflatePaths inputs'
        for index, segment in enumerate(path):
            print '\t', 'segment', index, segment.description()
        print

    offsetSegments = []
    for index, segment in enumerate(path):
        newSegment = inflateSegmentLeft(segment, hDistance, vDistance)
        if newSegment is None:
            '''
            Inflating a segment can result in an empty or otherwise invalid segment.
            In fact, this will happen often since we'll be deflating previously
            inflated rounding curves.
            That's fine; ignore them.
            '''
            offsetSegments.append(None)
            continue

        if debugMode:
            print 'inflating segment'
            print '\t', 'from', index, segment.description()
            print '\t', 'to', index, newSegment.description()

#        newSegment.srcSegment = segment
        offsetSegments.append(newSegment)

#    if debugMode:
#        raise TFSContoursException('argh', [TFSPath(False, segment) for segment in offsetSegments if segment is not None])

    del segment

    newSegments = []
#    lastSegment = offsetSegments[-1]
    lastSegmentInvalid = False
#    for index, segment in enumerate(offsetSegments):
    for index in xrange(len(path)):
        offsetSegment = offsetSegments[index]
        lastOffsetSegment = offsetSegments[(index + len(path) - 1) % len(path)]
        srcSegment = path[index]
        lastSrcSegment = path[(index + len(path) - 1) % len(path)]

        if debugMode:
            print 'checking join'
            print '\t', 'offsetSegment', index, offsetSegment.description() if offsetSegment is not None else ''
            print '\t', 'lastOffsetSegment', index, lastOffsetSegment.description() if lastOffsetSegment is not None else ''
            print '\t', 'srcSegment', index, srcSegment.description() if srcSegment is not None else ''
            print '\t', 'srcSegment', index, srcSegment.description() if srcSegment is not None else ''
#            print '\t', 'to', index, segment.description()

        if ((offsetSegment is not None) and
            (lastOffsetSegment is not None) and
            (offsetSegment.startPoint() == lastOffsetSegment.endPoint())):
            '''
            No join necessary if inflated segments align perfectly.
            '''
            if debugMode:
                print 'No join necessary (segments aligned)'
        else:
            lastTangent = lastSrcSegment.endTangent()
            nextTangent = srcSegment.startTangent()
            lastAngle = lastTangent.atan2()
            nextAngle = nextTangent.atan2()
            angleDiff = normalizeRadiansDiff(nextAngle - lastAngle)
            if debugMode:
                print 'lastTangent', lastTangent
                print 'nextTangent', nextTangent
                print 'lastAngle', lastAngle
                print 'nextAngle', nextAngle
                print 'angleDiff', angleDiff

            if angleDiff < 0 or angleDiff == math.pi:
                if debugMode:
                    print 'rounding join'

#                if lastSegmentInvalid and not deflating:
                if lastSegmentInvalid:
                    '''
                    No join necessary if last segment was invalid.
                    '''
                    if debugMode:
                        print 'No join necessary (last segment invalid)'
                else:
                    roundingCenter = srcSegment.startPoint()
                    roundingc = TFSOval(roundingCenter, hDistance, vDistance)
#                    roundingStartAngle = offsetSegment.startPoint().minus(roundingCenter).atan2()
#                    roundingEndAngle = lastOffsetSegment.endPoint().minus(roundingCenter).atan2()
                    roundingStartAngle = srcSegment.startTangent().atan2() + math.pi * 0.5
                    roundingEndAngle = lastSrcSegment.endTangent().atan2() + math.pi * 0.5

                    if debugMode:
#                        print 'angleDiff', angleDiff
#                        print 'segment', segment.description()
#                        print 'lastSegment', lastSegment.description()
                        print 'roundingCenter', roundingCenter
                        print 'roundingStartAngle', roundingStartAngle
                        print 'roundingEndAngle', roundingEndAngle

                    rounding = roundingc.createArc(roundingStartAngle, roundingEndAngle).reverse()
                    # Make sure the rounding endpoints exactly align.
                    if lastOffsetSegment is not None:
                        rounding[0].setStartPoint(lastOffsetSegment.endPoint())
                    if offsetSegment is not None:
                        rounding[-1].setEndPoint(offsetSegment.startPoint())
#                    if debugMode:
#                        rounding = openPathWithPoints(rounding.startPoint(), roundingCenter, rounding.endPoint())
                    if debugMode:
                        debugPath('rounding', rounding)

                    newSegments.extend(rounding.segments)
                    if debugMode:
                        print 'inserting join'
                        for value in rounding.segments:
                            print '\t', '*', index, value.description()
            else:
                if debugMode:
                    print 'cross join'
                if ((offsetSegment is not None) and
                    (lastOffsetSegment is not None)):
                    joinTangent0 = offsetSegment.startPoint().minus(lastOffsetSegment.endPoint())
                    joinTangent1 = offsetSegment.endPoint().minus(lastOffsetSegment.endPoint())
                    joinAffinity0 = joinTangent0.dotProduct(nextTangent)
                    joinAffinity1 = joinTangent1.dotProduct(nextTangent)
    #                if debugMode:
        #            print 'nextTangent', nextTangent
        #            print 'joinTangent0', joinTangent0
        #            print 'joinTangent1', joinTangent1
        #            print 'joinAffinity0', joinAffinity0
        #            print 'joinAffinity1', joinAffinity1
                    if (joinAffinity0 < 0) and (joinAffinity1 < 0):
                        if debugMode:
                            print 'invalid segment'
#                        lastSegment = segment
                        lastSegmentInvalid = True
                        continue

        if offsetSegment is not None:
            newSegments.append(offsetSegment)
#        lastSegment = segment
        lastSegmentInvalid = False

#    if debugMode:
#        raise TFSContoursException('argh', [TFSPath(False, segment) for segment in newSegments])

    newSegments = [segment.roundWithDefaultPrecision() for segment in newSegments if not isEmptySegment(segment)]
    newPaths = [TFSPath(False, segment) for segment in newSegments]

    if debugMode:
        debugPaths('newPaths', newPaths)

#    newPath = concatenatePath(True, *newSegments)

#    raise TFSContoursException('argh', newPaths)

    if TIME_INFLATE_DEFLATE_PATHS:
        time1 = time.time()
        print '\t', 'TFSSilhouette.deflatePaths.core', time1 - time0

#    unTesselatedPaths = newPaths
#    if debugMode:
#        raise TFSContoursException('argh', unTesselatedPaths)

    if TIME_INFLATE_DEFLATE_PATHS:
        time0 = time.time()
#    newPaths, intersections = FTesselation().tesselateContours(newPaths, reorientPaths=False, ignoreStrayEdges=deflating)
#    newPaths, intersections = FTesselation().tesselateContours(newPaths, reorientPaths=False, ignoreStrayEdges=deflating, debugMode=debugMode)
    newPaths, intersections = FTesselation().tesselateContours(newPaths, reorientPaths=False, ignoreStrayEdges=True, debugMode=debugMode)
#    newPaths, intersections = FTesselation().tesselateContours(newPaths, reorientPaths=False, ignoreStrayEdges=True, debugMode=debugMode)
#    newPaths, intersections = FTesselation().tesselateContours(newPaths, reorientPaths=False, debugMode=True)
    if TIME_INFLATE_DEFLATE_PATHS:
        time1 = time.time()
        print '\t', 'TFSSilhouette.deflatePaths.tesselateContours', time1 - time0

#    raise TFSContoursException('argh', newPaths)

    if deflating:
        newPaths = [path.reverse() for path in newPaths]

    if TIME_INFLATE_DEFLATE_PATHS:
        time1 = time.time()
        print '\t', 'TFSSilhouette.deflatePaths.cleanup', time1 - time0

    return newPaths


def inflateDeflatePaths(paths, reversePaths, hDistance, vDistance=None, debugMode=False):
    '''
    Edge case: What happens if we inflate an oval curve beyond it's center?
    Edge case: What happens if segment has a start or end vector of zero length?
        Should be fine.

    '''

    newPaths = []
    for path in paths:
        inflatedPaths = inflateDeflatePath(path, reversePaths, hDistance, vDistance, debugMode)

        for inflatedPath in inflatedPaths:
            if isClosedPathClockwise(inflatedPath) == isClosedPathClockwise(path):
                '''
                If deflating path has reversed its orientation, discard it.
                It is a hole that has collapsed on itself.
                '''
                newPaths.append(inflatedPath)

        newPaths.extend(inflatedPaths)

#    raise TFSContoursException('argh', newPaths)

    TIME_INFLATE_DEFLATE_PATHS = False

    if TIME_INFLATE_DEFLATE_PATHS:
        import time
        time0 = time.time()
    newPaths, intersections = FTesselation().tesselateContours(newPaths, reorientPaths=False, debugMode=debugMode)
    if TIME_INFLATE_DEFLATE_PATHS:
        time1 = time.time()
        print '\t', 'TFSSilhouette.inflateDeflatePaths.tesselateContours', time1 - time0

    return newPaths


def resolveSilhouette(rawSilhouette, minEvalY, maxEvalY, minMaxFunction):
    '''
    Given a list of tuples representing the evaluated segments,
    interpolate values along the y axis and use this to update the
    x-axis silhouette.
    '''
    evalSize = 1 + maxEvalY - minEvalY
    silhouette = [None,] * evalSize

    def updateSilhouetteValue(x, y):
        if y < minEvalY or y > maxEvalY:
            return
        index = y - minEvalY
        if silhouette[index] is None:
            silhouette[index] = x
        else:
            silhouette[index] = minMaxFunction(silhouette[index], x)

    def updateSilhouetteRange(point0, point1):
        if point0.y > point1.y:
            # Ensure that point1 has a higher y value.
            point0, point1 = point1, point0
        x0 = point0.x
        x1 = point1.x
        y0 = int(round(point0.y))
        y1 = int(round(point1.y))
        if y0 == y1:
            x = minMaxFunction(x0, x1)
            updateSilhouetteValue(x, y0)
        else:
            for y in xrange(y0, y1 + 1):
                # Interpolate
                if y == y0:
                    x = x0
                elif y == y1:
                    x = x1
                else:
                    x = x0 + (x1 - x0) * (y - point0.y) / (point1.y - point0.y)
                updateSilhouetteValue(x, y)

    for segmentPoints in rawSilhouette:
        for index in xrange(len(segmentPoints) - 1):
            point0 = segmentPoints[index + 0]
            point1 = segmentPoints[index + 1]
            updateSilhouetteRange(point0, point1)

    return silhouette


def evaluateSilhouetteSegments(paths):
    '''
    return the set of all evaluated segments in all paths.
    '''
    SILHOUETTE_PRECISION = 32
    result = []
    for path in paths:
        for segment in path:
            result.append(segment.evaluateRangeWithPrecision(SILHOUETTE_PRECISION))
    return result


def findSilhouetteContactSpacing(paths0, paths1, resolutionPerUnits):
    '''
    Find the minimum distance X between two glyphs (groups of closed paths)
    such that when glyph1 is advanced X to the right, the two glyphs
    barely touch and do not overlap.
    '''
    rawSilhouette0 = evaluateSilhouetteSegments(paths0)
    rawSilhouette1 = evaluateSilhouetteSegments(paths1)

    minY = None
    maxY = None
    for segmentPoints in rawSilhouette0 + rawSilhouette1:
        for point in segmentPoints:
            if minY is None:
                minY = maxY = point.y
            else:
                minY = min(minY, point.y)
                maxY = max(maxY, point.y)

    minEvalY = int(math.floor(minY * resolutionPerUnits))
    maxEvalY = int(math.ceil(maxY * resolutionPerUnits))

    silhouette0 = resolveSilhouette(rawSilhouette0, minEvalY, maxEvalY, max)
    silhouette1 = resolveSilhouette(rawSilhouette1, minEvalY, maxEvalY, min)

#    print 'silhouette0', silhouette0
#    print 'silhouette1', silhouette1
#    print 'len(silhouette0)', len(silhouette0)
#    print 'len(silhouette1)', len(silhouette1)

    minSpacing = None
    for x0, x1 in zip(silhouette0, silhouette1):
        if x0 is None or x1 is None:
            continue
        xDiff = x0 - x1
        if minSpacing is None:
            minSpacing = xDiff
        else:
            minSpacing = max(minSpacing, xDiff)
    return minSpacing
