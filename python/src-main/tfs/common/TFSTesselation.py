'''
robofont-extensions-and-scripts
TFSTesselation.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com

Apache License

Version 2.0, January 2004

http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.

"Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.

"You" (or "Your") shall mean an individual or Legal Entity exercising permissions granted by this License.

"Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.

"Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).

"Derivative Works" shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.

"Contribution" shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.

3. Grant of Patent License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.

4. Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:

You must give any other recipients of the Work or Derivative Works a copy of this License; and

You must cause any modified files to carry prominent notices stating that You changed the files; and

You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and

If the Work includes a "NOTICE" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License. You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.

9. Accepting Warranty or Additional Liability. While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS
'''


from collections import defaultdict

from TFSPath import *
from TFSMath import *
from TFSContoursException import TFSContoursException


class TFSTesselation(object):

    def subdividePathWithPaths(self, paths):

        DEBUG_SUBDIVIDE = False
#        DEBUG_SUBDIVIDE = True

        def findIntersection(path0, paths):
    #        print 'findIntersection', type(paths), paths
            for index, path1 in enumerate(paths):
                intersection = path0.intersectionWithPath_tOnly(path1, maxEndpoints=1, ignoreEqualSegments=True)
                if intersection:
                    index0, index1, segment0, segment1, t0, t1, p = intersection
                    if DEBUG_SUBDIVIDE:
                        print 'index0, index1', index0, index1
                        print 't0, t1', t0, t1
                    subpaths0 = path0.singleSplit(index0, t0, p)
                    subpaths1 = path1.singleSplit(index1, t1, p)

                    return subpaths0, subpaths1, index, p

            return None

        if DEBUG_SUBDIVIDE:
            for path in paths:
                print 'input path', path.description()
                for segment in path:
                    print '\t\t', segment.description()

        processed = []
#        unprocessed = list(paths)
        '''
        Decompose all paths into single-segment paths.
        This simplifies the subdivision algorithm.
        It doesn't matter; paths will be re-composed later
        by simplifySubpaths() and buildMinimumShapes().
        '''
        unprocessed = []
        for path in paths:
            unprocessed.extend(path.decompose())
        intersections = []
        while unprocessed:
#            print 'subdividePathWithPaths iteration', 'processed', len(processed), 'unprocessed', len(unprocessed)
            path0 = unprocessed.pop()

#            # First try to intersect path with itself.
#            intersection = path0.intersectionWithPath_tOnly(path0, maxEndpoints=1, ignoreEqualSegments=True)
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

            if not unprocessed:
                processed += [path0,]
                break

#            print 'subdividePathWithPaths', 'paths', type(paths), paths
    #        print 'subdividePathWithPaths', 'unprocessed', type(unprocessed), unprocessed
    #        print 'path0', type(path0)
            intersection = findIntersection(path0, unprocessed)
            if intersection:
                subpaths0, subpaths1, index, p = intersection

                if DEBUG_SUBDIVIDE:
                    print 'index', index, 'p', p

                path1 = unprocessed.pop(index)

                if DEBUG_SUBDIVIDE:
                    print 'classic cut'
                    print '\t', 'path0', path0.description()
                    print '\t', 'path1', path1.description()
                    for subpath0 in subpaths0:
                        print '\t', 'subpath0', subpath0.description()
                        for segment in subpath0:
                            print '\t\t', segment.description()
                    for subpath1 in subpaths1:
                        print '\t', 'subpath1', subpath1.description()
                        for segment in subpath1:
                            print '\t\t', segment.description()

                unprocessed.extend(subpaths0 + subpaths1)
                intersections.append(p)
            else:
                processed += [path0,]

        return processed, intersections


    def buildEndpointSubpathMap(self, paths):
        result = defaultdict(list)
        for path in paths:
            result[path.startPoint()].append(path)
        return result


    def simplifySubpaths(self, paths):
        '''
        During the path subdivision process, some subpaths can be trivially combined.
        When only two subpaths share a given endPoint, we can combine them.
        '''

        DEBUG_SIMPLIFY_SUBPATHS = False
#        DEBUG_SIMPLIFY_SUBPATHS = True

        # Decompose paths into segments.
        # This ensures that intersections at endPoints are split.
        newpaths = []
        for path in paths:
            newpaths.extend(path.decompose())
        paths = newpaths

        while True:
            if DEBUG_SIMPLIFY_SUBPATHS:
                print 'simplifySubpath', 'iteration', 'paths', len(paths)
            for tempKey, path in enumerate(paths):
                path._tempKey = tempKey

            endPointSubpathMap = self.buildEndpointSubpathMap(paths)
            if DEBUG_SIMPLIFY_SUBPATHS:
                print 'endPointSubpathMap', len(endPointSubpathMap)
                for endPoint in endPointSubpathMap:
                    print '\t', endPoint.description(), len(endPointSubpathMap[endPoint])
                print
            success = False
            for path0 in paths:
                paths1 = endPointSubpathMap[path0.endPoint()]
                if len(paths1) == 1:
                    path1 = paths1[0]

                    if path0._tempKey == path1._tempKey:
                        continue

                    path01 = path0 + path1
                    paths = [path for path in paths if path._tempKey not in (path0._tempKey, path1._tempKey, )]
                    paths.append(path01)

                    if DEBUG_SIMPLIFY_SUBPATHS:
                        print 'merging.0', path0.description()
                        print 'merging.1', path1.description()
                        print 'merged', path01.description()

                    success = True
                    break
            if not success:
                return paths


    def buildMinimumShapes(self, paths, ignoreStrayEdges=False):
        '''
        Given a subdivided set of paths, built all possible minimum shapes.
        Each subpath can only be once in each direction.
        '''

        DEBUG_BUILD_SHAPES = False
#        DEBUG_BUILD_SHAPES = True

        def pathEndpointAngleDelta(path0, path1):
            '''
            Basically, we're interested in the angle between a path
            arriving at a point and another leaving that path.
            We use their start and end tangents to calculate this.

            However, we need to handle the edge case where the tangents
            are equal.  This may be because one (or both) of the is a curve.
            imagine a triangle where one of the sides is a curve.

            .
            .
            .
            ..
            . ..
            .   ..
            ........

            To handle this properly, we want to slightly bias the "endpoint angles"
            towards the path's other endpoint.

            '''
            if path0.endPoint() != path1.startPoint():
                raise Exception('Non-contiguous paths')

            TWEAK_FACTOR = 0.01

            tangent0 = path0.endTangent()
            segment0 = path0[-1]
            tangentTweak0 = segment0.endPoint().minus(segment0.startPoint()).normalize()
            tangent0 = tangent0.blend(tangentTweak0, TWEAK_FACTOR)
            angle0 = tangent0.atan2()

            tangent1 = path1.startTangent()
            segment1 = path1[0]
            tangentTweak1 = segment1.endPoint().minus(segment1.startPoint()).normalize()
            tangent1 = tangent1.blend(tangentTweak1, TWEAK_FACTOR)
            angle1 = tangent1.atan2()

#            angle0 = path0.endTangent().atan2()
#            angle1 = path1.startTangent().atan2()
            angleDiff = normalizeRadiansDiff(angle1 - angle0)
            return angleDiff

        def buildMinimumShape(path, endPointSubpathMap, usedSet):
#            DEBUG_BUILD_SHAPES = True
            if DEBUG_BUILD_SHAPES:
                print
                print 'buildMinimumShape'
            lastPath = path
#            visitedPoints = []
            visitedPaths = []
            for _ in xrange(len(endPointSubpathMap) * 2 + 1):
                if DEBUG_BUILD_SHAPES:
                    print
                    print 'buildMinimumShape cycle', lastPath.description()
                if lastPath in usedSet:
                    if DEBUG_BUILD_SHAPES:
                        print 'abandoning redundant shape'
                    return None
#                visitedPoints += [lastPath.startPoint(),]
                visitedPaths += [lastPath,]
                point = lastPath.endPoint()
                nextPaths = endPointSubpathMap[point]
                bestNextPath = None
                bestAngleDelta = None
                for nextPath in nextPaths:
                    if nextPath.startPoint() != lastPath.endPoint():
#                        print '\t', 'error lastPath', lastPath.description()
#                        print '\t', 'error nextPath', nextPath.description()
#                        print '\t', '...', nextPath.startPoint(), type(nextPath.startPoint() )
#                        print '\t', '...', lastPath.endPoint(), type(lastPath.endPoint())
#                        print '\t', '...', nextPath.startPoint() == lastPath.endPoint()
#                        print '\t', '...', nextPath.startPoint() != lastPath.endPoint()
#                        print '\t', '...', nextPath.startPoint().distanceTo(lastPath.endPoint())
                        raise Exception('unexpected path')
                    angleDelta = pathEndpointAngleDelta(lastPath, nextPath)

                    if DEBUG_BUILD_SHAPES:
                        print
                        print '\t', 'angleDelta', angleDelta
                        print '\t', 'bestAngleDelta', bestAngleDelta
                        print '\t', 'lastPath', lastPath.description(), 'endTangent', lastPath.endTangent(), lastPath.endTangent().atan2()
                        print '\t', 'nextPath', nextPath.description(), 'startTangent', nextPath.startTangent(), nextPath.startTangent().atan2()
                        print '\t', 'p', lastPath.endPoint(), nextPath.startPoint(), lastPath.endPoint() == nextPath.startPoint()

#                    if (bestNextPath is None) or (angleDelta < bestAngleDelta):
                    if (bestNextPath is None) or (angleDelta > bestAngleDelta):
                        if DEBUG_BUILD_SHAPES:
                            print '\t\t', 'chosen!'
#                        if (bestNextPath is not None):
#                            print
#                            print '\t', 'angleDelta', angleDelta
#                            print '\t', 'bestAngleDelta', bestAngleDelta
#                            print '\t', 'lastPath', lastPath.endTangent(), lastPath.endTangent().atan2()
#                            print '\t', 'nextPath', nextPath.startTangent(), nextPath.startTangent().atan2()
                        bestNextPath = nextPath
                        bestAngleDelta = angleDelta
                if bestNextPath is None:
                    if ignoreStrayEdges:
                        return None
                    print 'lastPath', lastPath.description()
                    print 'endPointSubpathMap'
                    for key in endPointSubpathMap.keys():
                        print '\t', key, len(endPointSubpathMap[key])
                    print 'nextPaths', len(nextPaths)
                    for nextPath in nextPaths:
                        print '\t', nextPath.description()
                    raise Exception('Could not find a next path')

                if bestNextPath in visitedPaths:
                    index = visitedPaths.index(bestNextPath)
                    shapePaths = visitedPaths[index:]
                    return shapePaths
                lastPath = bestNextPath

#        DEBUG_BUILD_SHAPES = True
        if DEBUG_BUILD_SHAPES:
            print
            for path in paths:
                print '\t', 'input path', path.description()
                for segment in path:
                    print '\t\t', segment.description()
            print
#        DEBUG_BUILD_SHAPES = False

        endPointSubpathMap = self.buildEndpointSubpathMap(paths)
        result = []
        usedSet = set()
        for path in paths:
            '''
            The algorithm:
            * For each path, do:
              * starting at endPoint, at every node select left-most edge.
              * repeat until you find a cycle in the graph (ie. visit an edge you have already visited).
              * Use only the edges in the cycle to form a new shape.
            * add all edges in the shape to the "used edge" set.
            * Repeat, but ignoring any future paths that encounter an already used edge.
            '''

            if DEBUG_BUILD_SHAPES:
                pass
                print
                print 'endPointSubpathMap'
                for key in endPointSubpathMap:
                    print '\t', 'key', key
                    for path in endPointSubpathMap[key]:
                        print '\t\t', 'path', path.description()
                        pass

            if DEBUG_BUILD_SHAPES:
                print 'endPointSubpathMap0', len(endPointSubpathMap)

            shapePaths = buildMinimumShape(path, endPointSubpathMap, usedSet)
            if shapePaths is None:
                continue

            for shapePath in shapePaths:
                usedSet.add(shapePath)

            shape = returnArg(concatenatePath(True, *shapePaths))

            if DEBUG_BUILD_SHAPES:
                print 'shape!'
                for segment in shape:
                    print '\t\t', segment.description()

            result.append(shape)

#            shapes = splitShapeOnEndpoints(shape)
##            print 'shapes after split', len(shapes)
#            shapes = [shape for shape in shapes if isClosedPathClockwise(shape)]
##            print 'shapes after filter', len(shapes)
#            result.extend(shapes)

        return result

    def cullEmptyAngles(self, paths):
        '''
        We may end up with degenerate geometry in which a path has an "empty"
        angle.
        Consider the polygon ABCBDFE.

           C
           .
        A..B..D
        .     .
        E.....F

        Empty angles may "point" inward or outward.
        '''

        def hasEmptyAngle(path):
            for index, segment0 in enumerate(path):
                segment1 = path[(index + 1) % len(path)]
                if segment0 == segment1.reverse():
                    '''
                    If two segments are opposites, they by definition constitute an empty angle.
                    This will work for beziers and straight lines, but only if the two edges
                    are exactly equal.
                    '''
                    return index, index + 1, []

                if segment0.isStraight() and segment1.isStraight():
                    '''
                    We only detect empty angles with straight edges.
                    '''
                    tangent0 = segment0.startTangent()
                    tangent1 = segment1.startTangent()
                    if tangent0 == tangent1.invert():
                        '''
                        Empty angle removed by replacing the two segments with one.
                        '''
                        newSegment = TFSSegment(segment0.startPoint(), segment1.endPoint())
                        return index, index + 1, [newSegment,]
                else:
                    '''
                    TODO: work on general bezier solution.
                    '''


            return None

        def removeEmptyAngles(path):
            while True:
                emptyAngle = hasEmptyAngle(path)
                if emptyAngle is None:
                    return path
#                print 'culling an empty angle', emptyAngle
                index0, index1, newSegments = emptyAngle
                if index1 < index0:
                    newSegments = list(path[index1 + 1:index0]) + list(newSegments)
                else:
                    newSegments = list(path[:index0]) + list(newSegments) + list(path[index1 + 1:])

                if len(newSegments) < 1:
                    return None
                path = TFSPath(True, *newSegments)
            pass

#        debugPaths('cullEmptyAngles.0', paths)

        result = []
        for path in paths:
            path = removeEmptyAngles(path)
            if path is not None:
                result.append(path)
#        debugPaths('cullEmptyAngles.1', result)
        return result


    def tesselateContours(self, paths,
                          reorientPaths=True,
                          ignoreStrayEdges=False, debugMode=False):
        DEBUG_TESSELATE = False
        TIME_TESSELATE = False
        if debugMode:
            DEBUG_TESSELATE = True

#        DEBUG_TESSELATE = True
        if DEBUG_TESSELATE:
            print 'tesselateContours', len(paths)
#        if reorientPaths:
#            paths = [orientClosedPathClockwise(path) for path in paths]

        if DEBUG_TESSELATE:
            print 'paths clockwise', len(paths)
#        return paths, None
        if TIME_TESSELATE:
            import time
            time0 = time.time()
        subpaths, intersections = self.subdividePathWithPaths(paths)
        if TIME_TESSELATE:
            time1 = time.time()
            print '\t', 'tesselateContours.subdividePathWithPaths', time1 - time0
        if DEBUG_TESSELATE:
            print 'subpaths', len(subpaths)

#        if debugMode:
#            return subpaths, intersections
#        return subpaths, intersections
#        if debugMode:
#            raise TFSContoursException('argh', subpaths)

#        # Decompose paths.
#        newpaths = []
#        for path in subpaths:
#            newpaths.extend(path.decompose())
#        subpaths = newpaths

        if DEBUG_TESSELATE:
            print
            print 'decomposed'
            for path in subpaths:
                print '\t', 'subdivided path', path.description()
            print

#        return subpaths, intersections
        if TIME_TESSELATE:
            time0 = time.time()
        subpaths = self.simplifySubpaths(subpaths)
        if TIME_TESSELATE:
            time1 = time.time()
            print '\t', 'tesselateContours.simplifySubpaths', time1 - time0
        if DEBUG_TESSELATE:
            print 'simplified subpaths', len(subpaths)
#        return subpaths


        if DEBUG_TESSELATE:
            print
            print 'simplified'
            for path in subpaths:
                print '\t', 'subdivided path', path.description()
            print

        if debugMode:
            raise TFSContoursException('argh', subpaths)

#        if debugMode:
#            return subpaths, intersections
#        return subpaths, intersections

        if TIME_TESSELATE:
            time0 = time.time()
        shapes = self.buildMinimumShapes(subpaths, ignoreStrayEdges=ignoreStrayEdges)
        if TIME_TESSELATE:
            time1 = time.time()
            print '\t', 'tesselateContours.buildMinimumShapes', time1 - time0
        if DEBUG_TESSELATE:
            print 'shapes', len(shapes)

        if TIME_TESSELATE:
            time0 = time.time()
        shapes = self.cullEmptyAngles(shapes)
        if TIME_TESSELATE:
            time1 = time.time()
            print '\t', 'tesselateContours.cullEmptyAngles', time1 - time0
        if DEBUG_TESSELATE:
            print 'shapes', len(shapes)
#        return shapes, intersections

#        return shapes, intersections


#        shapes = [shape for shape in shapes if not self.isClosedPathClockwise(shape)]
#        print 'clockwise shapes', len(shapes)

#        shapes = self.mergeShapes(shapes)
#        print 'shapes', len(shapes)

        if reorientPaths:
            if TIME_TESSELATE:
                time0 = time.time()
            shapes = [orientClosedPathClockwise(shape) for shape in shapes]
            if TIME_TESSELATE:
                time1 = time.time()
                print '\t', 'tesselateContours.cleanup', time1 - time0

        return shapes, intersections
