'''
robofont-extensions-and-scripts
TFSTesselation.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''


import math
from TFSTest import TFSTest
from tfs.common.TFSPoint import TFSPoint, TFSPoint0
from tfs.common.TFSSegment import TFSSegment
from tfs.common.TFSPath import TFSPath, openPathWithPoints, debugPaths
from tfs.common.TFSTesselation import TFSTesselation


class TFSTesselationTest(TFSTest):

    def setUp(self):
        pass

    def test_subdividePathWithPaths(self):
        divided, intersections = TFSTesselation().subdividePathWithPaths([openPathWithPoints(TFSPoint(0, 2),
                                                                                             TFSPoint(4, 2)),
                                                                          openPathWithPoints(TFSPoint(6, 0),
                                                                                             TFSPoint(6, 4)),
                                                                          ])
        self.assertEqual(len(divided), 2)
        self.assertEqual(len(intersections), 0)
        
        divided, intersections = TFSTesselation().subdividePathWithPaths([openPathWithPoints(TFSPoint(0, 2),
                                                                                             TFSPoint(4, 2)),
                                                                          openPathWithPoints(TFSPoint(2, 0),
                                                                                             TFSPoint(2, 4)),
                                                                          ])
#        debugPaths('divided', divided)
        self.assertEqual(len(divided), 4)
        self.assertEqual(len(intersections), 1)

        divided, intersections = TFSTesselation().subdividePathWithPaths([openPathWithPoints(TFSPoint(0, 2),
                                                                                             TFSPoint(4, 2)),
                                                                          openPathWithPoints(TFSPoint(2, 0),
                                                                                             TFSPoint(2, 4)),
                                                                          openPathWithPoints(TFSPoint(3, 0),
                                                                                             TFSPoint(3, 4)),
                                                                          ])
#        debugPaths('divided', divided)
        self.assertEqual(len(divided), 7)
        self.assertEqual(len(intersections), 2)

        divided, intersections = TFSTesselation().subdividePathWithPaths([openPathWithPoints(TFSPoint(0, 2),
                                                                                             TFSPoint(4, 2)),
                                                                          openPathWithPoints(TFSPoint(0, 1),
                                                                                             TFSPoint(4, 1)),
                                                                          openPathWithPoints(TFSPoint(2, 0),
                                                                                             TFSPoint(2, 4)),
                                                                          openPathWithPoints(TFSPoint(3, 0),
                                                                                             TFSPoint(3, 4)),
                                                                          ])
#        debugPaths('divided', divided)
        self.assertEqual(len(divided), 12)
        self.assertEqual(len(intersections), 4)
        
        '''
        Endpoint intersection
        '''
        divided, intersections = TFSTesselation().subdividePathWithPaths([openPathWithPoints(TFSPoint(0, 2),
                                                                                             TFSPoint(4, 2)),
                                                                          openPathWithPoints(TFSPoint(4, 2),
                                                                                             TFSPoint(4, 4)),
                                                                          ])
        self.assertEqual(len(divided), 2)
        self.assertEqual(len(intersections), 0)        
#        try:
#            TFSSegment()
#            self.fail('Missing exception')
#        except Exception, e:
#            pass
#
#        try:
#            TFSSegment(TFSPoint0())
#            self.fail('Missing exception')
#        except Exception, e:
#            pass


#from collections import defaultdict
#
#from TFSPath import *
#from TFSMath import *
#from TFSContoursException import TFSContoursException
#
#
#class TFSTesselation(object):
#
#    def subdividePathWithPaths(self, paths):
#
#        DEBUG_SUBDIVIDE = False
##        DEBUG_SUBDIVIDE = True
#
#        def findIntersection(path0, paths):
#    #        print 'findIntersection', type(paths), paths
#            for index, path1 in enumerate(paths):
#                intersection = path0.intersectionWithPath_tOnly(path1, ignoreEndpoints=True, ignoreEqualSegments=True)
#                if intersection:
#                    index0, index1, segment0, segment1, t0, t1, p = intersection
#                    if DEBUG_SUBDIVIDE:
#                        print 'index0, index1', index0, index1
#                        print 't0, t1', t0, t1
#                    subpaths0 = path0.singleSplit(index0, t0, p)
#                    subpaths1 = path1.singleSplit(index1, t1, p)
#
#                    return subpaths0, subpaths1, index, p
#
#            return None
#
#        if DEBUG_SUBDIVIDE:
#            for path in paths:
#                print 'input path', path.description()
#                for segment in path:
#                    print '\t\t', segment.description()
#
#        processed = []
#        unprocessed = list(paths)
#        intersections = []
#        while unprocessed:
#    #        print 'subdividePathWithPaths iteration', 'processed', len(processed), 'unprocessed', len(unprocessed)
#            path0 = unprocessed.pop()
#
#            # First try to intersect path with itself.
#            intersection = path0.intersectionWithPath_tOnly(path0, ignoreEndpoints=True, ignoreEqualSegments=True)
#            if intersection:
#                index0, index1, segment0, segment1, t0, t1, p = intersection
#
#                if DEBUG_SUBDIVIDE:
#                    print 'index0, index1', index0, index1, 't0, t1', t0, t1
#
#                subpaths = path0.doubleSplit(index0, index1, t0, t1, p, p)
#
#                if DEBUG_SUBDIVIDE:
#                    print 'self-cut', path0.description()
#                    for subpath in subpaths:
#                        print '\t', subpath.description()
#                        for segment in subpath:
#                            print '\t\t', segment.description()
#
#                unprocessed.extend(subpaths)
#                intersections.append(p)
#                continue
#
#            if not unprocessed:
#                processed += [path0,]
#                break
#
##            print 'subdividePathWithPaths', 'paths', type(paths), paths
#    #        print 'subdividePathWithPaths', 'unprocessed', type(unprocessed), unprocessed
#    #        print 'path0', type(path0)
#            intersection = findIntersection(path0, unprocessed)
#            if intersection:
#                subpaths0, subpaths1, index, p = intersection
#
#                if DEBUG_SUBDIVIDE:
#                    print 'index', index, 'p', p
#
#                path1 = unprocessed.pop(index)
#
#                if DEBUG_SUBDIVIDE:
#                    print 'classic cut'
#                    print '\t', 'path0', path0.description()
#                    print '\t', 'path1', path1.description()
#                    for subpath0 in subpaths0:
#                        print '\t', 'subpath0', subpath0.description()
#                        for segment in subpath0:
#                            print '\t\t', segment.description()
#                    for subpath1 in subpaths1:
#                        print '\t', 'subpath1', subpath1.description()
#                        for segment in subpath1:
#                            print '\t\t', segment.description()
#
#                unprocessed.extend(subpaths0 + subpaths1)
#                intersections.append(p)
#            else:
#                processed += [path0,]
#
#        return processed, intersections
#
#
#    def buildEndpointSubpathMap(self, paths):
#        result = defaultdict(list)
#        for path in paths:
#            result[path.startPoint()].append(path)
#        return result
#
#
#    def simplifySubpaths(self, paths):
#        '''
#        During the path subdivision process, some subpaths can be trivially combined.
#        When only two subpaths share a given endPoint, we can combine them.
#        '''
#
#        DEBUG_SIMPLIFY_SUBPATHS = False
##        DEBUG_SIMPLIFY_SUBPATHS = True
#
#        # Decompose paths into segments.
#        # This ensures that intersections at endPoints are split.
#        newpaths = []
#        for path in paths:
#            newpaths.extend(path.decompose())
#        paths = newpaths
#
#        while True:
#            if DEBUG_SIMPLIFY_SUBPATHS:
#                print 'simplifySubpath', 'iteration', 'paths', len(paths)
#            for tempKey, path in enumerate(paths):
#                path._tempKey = tempKey
#
#            endPointSubpathMap = self.buildEndpointSubpathMap(paths)
#            if DEBUG_SIMPLIFY_SUBPATHS:
#                print 'endPointSubpathMap', len(endPointSubpathMap)
#                for endPoint in endPointSubpathMap:
#                    print '\t', endPoint.description(), len(endPointSubpathMap[endPoint])
#                print
#            success = False
#            for path0 in paths:
#                paths1 = endPointSubpathMap[path0.endPoint()]
#                if len(paths1) == 1:
#                    path1 = paths1[0]
#
#                    if path0._tempKey == path1._tempKey:
#                        continue
#
#                    path01 = path0 + path1
#                    paths = [path for path in paths if path._tempKey not in (path0._tempKey, path1._tempKey, )]
#                    paths.append(path01)
#
#                    if DEBUG_SIMPLIFY_SUBPATHS:
#                        print 'merging.0', path0.description()
#                        print 'merging.1', path1.description()
#                        print 'merged', path01.description()
#
#                    success = True
#                    break
#            if not success:
#                return paths
#
#
#    def buildMinimumShapes(self, paths, ignoreStrayEdges=False):
#        '''
#        Given a subdivided set of paths, built all possible minimum shapes.
#        Each subpath can only be once in each direction.
#        '''
#
#        DEBUG_BUILD_SHAPES = False
##        DEBUG_BUILD_SHAPES = True
#
#        def pathEndpointAngleDelta(path0, path1):
#            '''
#            Basically, we're interested in the angle between a path
#            arriving at a point and another leaving that path.
#            We use their start and end tangents to calculate this.
#
#            However, we need to handle the edge case where the tangents
#            are equal.  This may be because one (or both) of the is a curve.
#            imagine a triangle where one of the sides is a curve.
#
#            .
#            .
#            .
#            ..
#            . ..
#            .   ..
#            ........
#
#            To handle this properly, we want to slightly bias the "endpoint angles"
#            towards the path's other endpoint.
#
#            '''
#            if path0.endPoint() != path1.startPoint():
#                raise Exception('Non-contiguous paths')
#
#            TWEAK_FACTOR = 0.01
#
#            tangent0 = path0.endTangent()
#            segment0 = path0[-1]
#            tangentTweak0 = segment0.endPoint().minus(segment0.startPoint()).normalize()
#            tangent0 = tangent0.blend(tangentTweak0, TWEAK_FACTOR)
#            angle0 = tangent0.atan2()
#
#            tangent1 = path1.startTangent()
#            segment1 = path1[0]
#            tangentTweak1 = segment1.endPoint().minus(segment1.startPoint()).normalize()
#            tangent1 = tangent1.blend(tangentTweak1, TWEAK_FACTOR)
#            angle1 = tangent1.atan2()
#
##            angle0 = path0.endTangent().atan2()
##            angle1 = path1.startTangent().atan2()
#            angleDiff = normalizeRadiansDiff(angle1 - angle0)
#            return angleDiff
#
#        def buildMinimumShape(path, endPointSubpathMap, usedSet):
##            DEBUG_BUILD_SHAPES = True
#            if DEBUG_BUILD_SHAPES:
#                print
#                print 'buildMinimumShape'
#            lastPath = path
##            visitedPoints = []
#            visitedPaths = []
#            for _ in xrange(len(endPointSubpathMap) * 2 + 1):
#                if DEBUG_BUILD_SHAPES:
#                    print
#                    print 'buildMinimumShape cycle', lastPath.description()
#                if lastPath in usedSet:
#                    if DEBUG_BUILD_SHAPES:
#                        print 'abandoning redundant shape'
#                    return None
##                visitedPoints += [lastPath.startPoint(),]
#                visitedPaths += [lastPath,]
#                point = lastPath.endPoint()
#                nextPaths = endPointSubpathMap[point]
#                bestNextPath = None
#                bestAngleDelta = None
#                for nextPath in nextPaths:
#                    if nextPath.startPoint() != lastPath.endPoint():
##                        print '\t', 'error lastPath', lastPath.description()
##                        print '\t', 'error nextPath', nextPath.description()
##                        print '\t', '...', nextPath.startPoint(), type(nextPath.startPoint() )
##                        print '\t', '...', lastPath.endPoint(), type(lastPath.endPoint())
##                        print '\t', '...', nextPath.startPoint() == lastPath.endPoint()
##                        print '\t', '...', nextPath.startPoint() != lastPath.endPoint()
##                        print '\t', '...', nextPath.startPoint().distanceTo(lastPath.endPoint())
#                        raise Exception('unexpected path')
#                    angleDelta = pathEndpointAngleDelta(lastPath, nextPath)
#
#                    if DEBUG_BUILD_SHAPES:
#                        print
#                        print '\t', 'angleDelta', angleDelta
#                        print '\t', 'bestAngleDelta', bestAngleDelta
#                        print '\t', 'lastPath', lastPath.description(), 'endTangent', lastPath.endTangent(), lastPath.endTangent().atan2()
#                        print '\t', 'nextPath', nextPath.description(), 'startTangent', nextPath.startTangent(), nextPath.startTangent().atan2()
#                        print '\t', 'p', lastPath.endPoint(), nextPath.startPoint(), lastPath.endPoint() == nextPath.startPoint()
#
##                    if (bestNextPath is None) or (angleDelta < bestAngleDelta):
#                    if (bestNextPath is None) or (angleDelta > bestAngleDelta):
#                        if DEBUG_BUILD_SHAPES:
#                            print '\t\t', 'chosen!'
##                        if (bestNextPath is not None):
##                            print
##                            print '\t', 'angleDelta', angleDelta
##                            print '\t', 'bestAngleDelta', bestAngleDelta
##                            print '\t', 'lastPath', lastPath.endTangent(), lastPath.endTangent().atan2()
##                            print '\t', 'nextPath', nextPath.startTangent(), nextPath.startTangent().atan2()
#                        bestNextPath = nextPath
#                        bestAngleDelta = angleDelta
#                if bestNextPath is None:
#                    if ignoreStrayEdges:
#                        return None
#                    print 'lastPath', lastPath.description()
#                    print 'endPointSubpathMap'
#                    for key in endPointSubpathMap.keys():
#                        print '\t', key, len(endPointSubpathMap[key])
#                    print 'nextPaths', len(nextPaths)
#                    for nextPath in nextPaths:
#                        print '\t', nextPath.description()
#                    raise Exception('Could not find a next path')
#
#                if bestNextPath in visitedPaths:
#                    index = visitedPaths.index(bestNextPath)
#                    shapePaths = visitedPaths[index:]
#                    return shapePaths
#                lastPath = bestNextPath
#
##        DEBUG_BUILD_SHAPES = True
#        if DEBUG_BUILD_SHAPES:
#            print
#            for path in paths:
#                print '\t', 'input path', path.description()
#                for segment in path:
#                    print '\t\t', segment.description()
#            print
##        DEBUG_BUILD_SHAPES = False
#
#        endPointSubpathMap = self.buildEndpointSubpathMap(paths)
#        result = []
#        usedSet = set()
#        for path in paths:
#            '''
#            The algorithm:
#            * For each path, do:
#              * starting at endPoint, at every node select left-most edge.
#              * repeat until you find a cycle in the graph (ie. visit an edge you have already visited).
#              * Use only the edges in the cycle to form a new shape.
#            * add all edges in the shape to the "used edge" set.
#            * Repeat, but ignoring any future paths that encounter an already used edge.
#            '''
#
#            if DEBUG_BUILD_SHAPES:
#                pass
#                print
#                print 'endPointSubpathMap'
#                for key in endPointSubpathMap:
#                    print '\t', 'key', key
#                    for path in endPointSubpathMap[key]:
#                        print '\t\t', 'path', path.description()
#                        pass
#
#            if DEBUG_BUILD_SHAPES:
#                print 'endPointSubpathMap0', len(endPointSubpathMap)
#
#            shapePaths = buildMinimumShape(path, endPointSubpathMap, usedSet)
#            if shapePaths is None:
#                continue
#
#            for shapePath in shapePaths:
#                usedSet.add(shapePath)
#
#            shape = returnArg(concatenatePath(True, *shapePaths))
#
#            if DEBUG_BUILD_SHAPES:
#                print 'shape!'
#                for segment in shape:
#                    print '\t\t', segment.description()
#
#            result.append(shape)
#
##            shapes = splitShapeOnEndpoints(shape)
###            print 'shapes after split', len(shapes)
##            shapes = [shape for shape in shapes if isClosedPathClockwise(shape)]
###            print 'shapes after filter', len(shapes)
##            result.extend(shapes)
#
#        return result
#
#    def cullEmptyAngles(self, paths):
#        '''
#        We may end up with degenerate geometry in which a path has an "empty"
#        angle.
#        Consider the polygon ABCBDFE.
#
#           C
#           .
#        A..B..D
#        .     .
#        E.....F
#
#        Empty angles may "point" inward or outward.
#        '''
#
#        def hasEmptyAngle(path):
#            for index, segment0 in enumerate(path):
#                segment1 = path[(index + 1) % len(path)]
#                if segment0 == segment1.reverse():
#                    '''
#                    If two segments are opposites, they by definition constitute an empty angle.
#                    This will work for beziers and straight lines, but only if the two edges
#                    are exactly equal.
#                    '''
#                    return index, index + 1, []
#
#                if segment0.isStraight() and segment1.isStraight():
#                    '''
#                    We only detect empty angles with straight edges.
#                    '''
#                    tangent0 = segment0.startTangent()
#                    tangent1 = segment1.startTangent()
#                    if tangent0 == tangent1.invert():
#                        '''
#                        Empty angle removed by replacing the two segments with one.
#                        '''
#                        newSegment = TFSSegment(segment0.startPoint(), segment1.endPoint())
#                        return index, index + 1, [newSegment,]
#                else:
#                    '''
#                    TODO: work on general bezier solution.
#                    '''
#
#
#            return None
#
#        def removeEmptyAngles(path):
#            while True:
#                emptyAngle = hasEmptyAngle(path)
#                if emptyAngle is None:
#                    return path
#                print 'culling an empty angle', emptyAngle
#                index0, index1, newSegments = emptyAngle
#                if index1 < index0:
#                    newSegments = list(path[index1 + 1:index0]) + list(newSegments)
#                else:
#                    newSegments = list(path[:index0]) + list(newSegments) + list(path[index1 + 1:])
#
#                if len(newSegments) < 1:
#                    return None
#                path = TFSPath(True, *newSegments)
#            pass
#
#        debugPaths('cullEmptyAngles.0', paths)
#
#        result = []
#        for path in paths:
#            path = removeEmptyAngles(path)
#            if path is not None:
#                result.append(path)
#        debugPaths('cullEmptyAngles.1', result)
#        return result
#
#
#    def tesselateContours(self, paths, reorientPaths=True, ignoreStrayEdges=False, debugMode=False):
#        DEBUG_TESSELATE = False
#        TIME_TESSELATE = False
#        if debugMode:
#            DEBUG_TESSELATE = True
#
##        DEBUG_TESSELATE = True
#        if DEBUG_TESSELATE:
#            print 'tesselateContours', len(paths)
##        if reorientPaths:
##            paths = [orientClosedPathClockwise(path) for path in paths]
#
#        if DEBUG_TESSELATE:
#            print 'paths clockwise', len(paths)
##        return paths, None
#        if TIME_TESSELATE:
#            import time
#            time0 = time.time()
#        subpaths, intersections = self.subdividePathWithPaths(paths)
#        if TIME_TESSELATE:
#            time1 = time.time()
#            print '\t', 'tesselateContours.subdividePathWithPaths', time1 - time0
#        if DEBUG_TESSELATE:
#            print 'subpaths', len(subpaths)
#
##        if debugMode:
##            return subpaths, intersections
##        return subpaths, intersections
##        if debugMode:
##            raise TFSContoursException('argh', subpaths)
#
##        # Decompose paths.
##        newpaths = []
##        for path in subpaths:
##            newpaths.extend(path.decompose())
##        subpaths = newpaths
#
#        if DEBUG_TESSELATE:
#            print
#            print 'decomposed'
#            for path in subpaths:
#                print '\t', 'subdivided path', path.description()
#            print
#
##        return subpaths, intersections
#        if TIME_TESSELATE:
#            time0 = time.time()
#        subpaths = self.simplifySubpaths(subpaths)
#        if TIME_TESSELATE:
#            time1 = time.time()
#            print '\t', 'tesselateContours.simplifySubpaths', time1 - time0
#        if DEBUG_TESSELATE:
#            print 'simplified subpaths', len(subpaths)
##        return subpaths
#
#
#        if DEBUG_TESSELATE:
#            print
#            print 'simplified'
#            for path in subpaths:
#                print '\t', 'subdivided path', path.description()
#            print
#
#        if debugMode:
#            raise TFSContoursException('argh', subpaths)
#
##        if debugMode:
##            return subpaths, intersections
##        return subpaths, intersections
#
#        if TIME_TESSELATE:
#            time0 = time.time()
#        shapes = self.buildMinimumShapes(subpaths, ignoreStrayEdges=ignoreStrayEdges)
#        if TIME_TESSELATE:
#            time1 = time.time()
#            print '\t', 'tesselateContours.buildMinimumShapes', time1 - time0
#        if DEBUG_TESSELATE:
#            print 'shapes', len(shapes)
#
#        if TIME_TESSELATE:
#            time0 = time.time()
#        shapes = self.cullEmptyAngles(shapes)
#        if TIME_TESSELATE:
#            time1 = time.time()
#            print '\t', 'tesselateContours.cullEmptyAngles', time1 - time0
#        if DEBUG_TESSELATE:
#            print 'shapes', len(shapes)
##        return shapes, intersections
#
##        return shapes, intersections
#
#
##        shapes = [shape for shape in shapes if not self.isClosedPathClockwise(shape)]
##        print 'clockwise shapes', len(shapes)
#
##        shapes = self.mergeShapes(shapes)
##        print 'shapes', len(shapes)
#
#        if reorientPaths:
#            if TIME_TESSELATE:
#                time0 = time.time()
#            shapes = [orientClosedPathClockwise(shape) for shape in shapes]
#            if TIME_TESSELATE:
#                time1 = time.time()
#                print '\t', 'tesselateContours.cleanup', time1 - time0
#
#        return shapes, intersections
