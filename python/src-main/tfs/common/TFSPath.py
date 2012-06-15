'''
robofont-extensions-and-scripts
TFSPath.py

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


import sys
import math

from TFSMath import *
import TFSIntersection
from TFSPoint import *
from TFSMap import TFSMap
from TFSSegment import *
from TFSValidationException import TFSValidationException

onJython = sys.platform.startswith('java')


class TFSPath(object):

    def __init__(self, closed, *segments):
        self.closed = closed
        self.segments = segments
        self.validate()

    def validate(self):
        try:
            if not onJython:
                import types
                if type(self.closed) != types.BooleanType:
                    raise TFSValidationException('Unexpected closed type: ' + str(type(self.closed)))
                if type(self.segments) not in (types.ListType, types.TupleType):
                    raise TFSValidationException('Unexpected segments type: ' + str(type(self.segments)))
                for segment in self.segments:
                    if not isinstance(segment, TFSSegment):
                        raise TFSValidationException('Unexpected segment type: ' + str(type(segment)))

            if len(self.segments) < 1:
                raise TFSValidationException('Invalid path')
            for segment in self.segments:
                segment.validate()
            lastSegment = None
            for segment in self.segments:
                if lastSegment is not None:
                    if lastSegment.endPoint() != segment.startPoint():
                        raise TFSValidationException('Path not connected')
                lastSegment = segment
            if self.closed:
                firstSegment = self.segments[0]
                lastSegment = self.segments[-1]
                if lastSegment.endPoint() != firstSegment.startPoint():
                    raise TFSValidationException('Path not closed')
                # TODO: No paths that cross themselves?
        except TFSValidationException, e:
            print 'TFSPath.validate', self.description()
            raise e

    def __len__(self):
        return len(self.segments)

    def __repr__(self):
        return 'TFSPath(%s, %s)' % ( str(self.closed),
                                   ', '.join([repr(segment) for segment in self.segments]), )

    def __iter__(self):
        for segment in self.segments:
            yield segment

    def __getitem__(self, index):
        return self.segments[index]

    def __add__(self, other):
        return concatenatePath(False, self, other)

    def __eq__(self, other):
        return tuple(self.segments) == tuple(other.segments)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(tuple(self.segments))

    def description(self):
        return '[Path[%s]: %s]' % ( str(self.closed),
                                    (''.join((
                                        str(self.startPoint()),
                                        '... ',
                                        str(len(self.segments)),
                                        ' segments, ',
                                        '...',
                                        str(self.endPoint()),
                                        ))),
                                      )
#        return '[Path[%s](%d): %s]' % ( str(self.closed),
#                                        len(self.segments),
#                                       ','.join(segment.description() for segment in self.segments)
#                                      )

    def startPoint(self):
        return self.segments[0].startPoint()

    def endPoint(self):
        return self.segments[-1].endPoint()

    def plus(self, other, closed=False):
        newSegments = list(self.segments)
        if self.endPoint() != other.startPoint():
            newSegments.append(TFSSegment(self.endPoint(), other.startPoint()))
        newSegments += list(other.segments)
        return TFSPath(closed, *newSegments)

    def reverse(self):
        newSegments = [segment.reverse() for segment in self.segments]
        newSegments.reverse()
        return TFSPath(self.closed, *newSegments)

    def roundWithDefaultPrecision(self):
        newSegments = [segment.roundWithDefaultPrecision() for segment in self.segments]
        return TFSPath(self.closed, *newSegments)

    def copy(self):
        newSegments = [segment.copy() for segment in self.segments]
        return TFSPath(self.closed, *newSegments)

    def removeEmptySegments(self):
        newSegments = []
        for segment in self:
            if (segment.endPoint() == segment.startPoint()) and len(segment) == 2:
                continue
            newSegments.append(segment.copy())
        if len(newSegments) == 0:
            raise Exception('Empty path')
        return TFSPath(self.closed, *newSegments)

    def asOpen(self):
        newSegments = [segment.copy() for segment in self.segments]
        return TFSPath(False, *newSegments)

    def decompose(self):
        return [TFSPath(False, segment.copy()) for segment in self.segments]

    def minmax(self):
        result = self.segments[0].minmax()
        for segment in self.segments[1:]:
            result = minmaxMerge(result, segment.minmax())
        return result

    def minmaxEvaluated(self, precision):
        result = self.segments[0].minmaxEvaluated(precision)
        for segment in self.segments[1:]:
            result = minmaxMerge(result, segment.minmaxEvaluated(precision))
        return result

    def dump(self):
        print
        print 'path.dump'
        for segment in self.segments:
            print 'segment', segment

    def applyPlus(self, value):
        newSegments = [segment.applyPlus(value) for segment in self.segments]
        return TFSPath(self.closed, *newSegments)

    def applyScale(self, value):
        newSegments = [segment.applyScale(value) for segment in self.segments]
        return TFSPath(self.closed, *newSegments)

    def applyFunction(self, function):
        newSegments = [segment.applyFunction(function) for segment in self.segments]
        return TFSPath(self.closed, *newSegments)

    def applyScaleXY(self, xFactor, yFactor):
        newSegments = [segment.applyScaleXY(xFactor, yFactor) for segment in self.segments]
        return TFSPath(self.closed, *newSegments)

    def plusOffset(self, offset):
        newSegments = []
        for segment in self.segments:
            newSegments.append(segment.plusOffset(offset))
        return TFSPath(self.closed, *newSegments)

    def isStraightLine(self):
        return (len(self.segments) == 1) and self.segments[0].isStraight()

    def translateStraightLineRight(self, distance):
        if len(self.segments) != 1 or len(self.segments[0].points) != 2:
            raise Exception("Isn't a straight line")
        startPoint = self.startPoint()
        endPoint = self.endPoint()
        diff = endPoint.minus(startPoint)
        vector = diff.normalize()
        rightVector = vector.rightAngleRight()
        return TFSPath(False,
                     TFSSegment(startPoint.plus(rightVector.scale(distance))),
                     TFSSegment(endPoint.plus(rightVector.scale(distance))))

    def simpleIntersectionWithPath(self, other):
        if len(self.segments) != 1:
            raise Exception("Isn't a simple path")
        if len(other.segments) != 1:
            raise Exception("Isn't a simple path")
        return self.segments[0].findIntersection_raw(other.segments[0])
#        return self.segments[0].findIntersection_recursiveClipping(other.segments[0])

    def allIntersections(self, other):
#        newPath0 = self.copy()
        newPaths0 = [self.copy()]
        newPaths1 = [other.copy()]

        def allIntersections_iteration(paths0, paths1):
            for index0 in xrange(len(paths0)):
                path0 = paths0[index0]
                for index1 in xrange(len(paths1)):
                    path1 = paths1[index1]
                    intersection = path0.intersectionWithPath(path1, ignoreEndpoints=True)
                    if intersection:
                        print 'allIntersections', 'intersection!', intersection
                        path00, path01, path10, path11, _ = intersection
    #                    if path00.endPoint().distanceTo(path00.startPoint())
                        print '\t', 'path00', path00.endPoint().distanceTo(path00.startPoint())
                        print '\t', 'path01', path01.endPoint().distanceTo(path01.startPoint())
                        print '\t', 'path10', path10.endPoint().distanceTo(path10.startPoint())
                        print '\t', 'path11', path11.endPoint().distanceTo(path11.startPoint())
                        paths0 = paths0[:index0] + [path00, path01,] + paths0[index0 + 1:]
                        paths1 = paths1[:index1] + [path10, path11,] + paths1[index1 + 1:]
                        return paths0, paths1
            return None

        while True:
            print 'allIntersections', 'cycle'
            intersection = allIntersections_iteration(newPaths0, newPaths1)
            if not intersection:
                break
            newPaths0, newPaths1 = intersection

#        print 'newPaths0', len(newPaths0)
#        print 'newPaths1', len(newPaths1)
        return newPaths0 + newPaths1


    def intersectionWithPath_tOnly(self, other, maxEndpoints, ignoreEqualSegments=False, debugMode=False):
        '''
        maxEndpoints == 0 means no endpoints may be involved in the intersection.
        maxEndpoints == 1 means only endpoints may be involved in the intersection.
        maxEndpoints == 2 means endpoints of both segments may be involved in the intersection.
        '''
        if maxEndpoints < 0 or maxEndpoints > 2:
            raise Exception('Invalid maxEndpoints value: %d' % maxEndpoints)

        for index0, segment0 in enumerate(self.segments):
            for index1, segment1 in enumerate(other.segments):

                if debugMode:
                    print 'intersectionWithPath_tOnly considering'
                    print 'segment0 considering', segment0.description()
                    print 'segment1 considering', segment1.description()

                if ignoreEqualSegments and segment0 == segment1:
                    if debugMode:
                        print 'equal.0'
                    continue

                intersection = segment0.findIntersection2(segment1, maxEndpoints)
#                intersection = segment0.findIntersection_raw(segment1, debugMode=debugMode)
                if debugMode:
                    print 'intersection', intersection

                if intersection:
                    t0, t1, p = intersection
#                    print 't0, t1, p', t0, t1, p

                    '''
                    When intersecting a path with itself, we want to avoid
                    false intersection between sequential segments at their endPoints
                    due to rounding error.
                    '''
                    if self is other:
                        if (index0 + 1) % len(self) == index1:
                            if p.roundedEquals(segment0.endPoint()):
#                                print '---- ignoring endPoint intersection(0)'
                                continue
                        elif index0 == (index1 + 1) % len(self):
                            if p.roundedEquals(segment1.endPoint()):
#                                print '---- ignoring endPoint intersection(1)'
                                continue

#                        if (t0 <= MIN_T) or (t0 >= MAX_T) or (t1 <= MIN_T) or (t1 >= MAX_T):
#                            continue
#                    print
#                    print 'intersectionWithPath_tOnly'
#                    print 'index0, index1, t0, t1, p', index0, index1, t0, t1, p
#                    print 'segment0', segment0.description()
#                    print 'segment1', segment1.description()
#                    print
                    return index0, index1, segment0, segment1, t0, t1, p
        return None

    def singleSplit(self, index, t, p=None):
        segment = self.segments[index]

        paths0 = self.segments[:index]
        paths1 = self.segments[index + 1:]

        SPLIT_T_PRECISION = T_ROUNDING_TOLERANCE

        # do not bother to split if intersection is on an endPoint.
        if t > 1 - SPLIT_T_PRECISION:
            paths0 = paths0 + (segment,)
        elif t < SPLIT_T_PRECISION:
            paths1 = (segment,) + paths1
        else:
            split0, split1 = segment.split(t)
            if p is not None:
                # make sure both splits use the exact point of intersection.
                split0.setEndPoint(p)
                split1.setStartPoint(p)
            paths0 = paths0 + (split0,)
            paths1 = (split1,) + paths1

        result = []
        for subpaths in (paths0, paths1):
            if len(subpaths) > 0:
                result.append(TFSPath(False, *subpaths))
        return result

    def doubleSplit(self, index0, index1, t0, t1, p0=None, p1=None):
        segment0 = self.segments[index0]
        segment1 = self.segments[index1]

        # reverse if necessary.
        if (index0 > index1) or ((index0 == index1) and (t0 > t1)):
            index1, index0 = index0, index1
            segment1, segment0 = segment0, segment1
            t1, t0 = t0, t1
            p1, p0 = p0, p1

        paths0 = self.segments[:index0]
        paths1 = self.segments[index0 + 1:index1]
        paths2 = self.segments[index1 + 1:]

        SPLIT_T_PRECISION = T_ROUNDING_TOLERANCE

        # do not bother to split if intersection is on an endPoint.
        if t0 > 1 - SPLIT_T_PRECISION:
            paths0 = paths0 + (segment0,)
        elif t0 < SPLIT_T_PRECISION:
            paths1 = (segment0,) + paths1
        else:
            split00, split01 = segment0.split(t0)
            if p0 is not None:
                # make sure both splits use the exact point of intersection.
                split00.setEndPoint(p0)
                split01.setStartPoint(p0)
            paths0 = paths0 + (split00,)
            paths1 = (split01,) + paths1


        # do not bother to split if intersection is on an endPoint.
        if t1 > 1 - SPLIT_T_PRECISION:
            paths1 = paths1 + (segment1,)
        elif t1 < SPLIT_T_PRECISION:
            paths2 = (segment1,) + paths2
        else:
            split10, split11 = segment1.split(t1)
            if p1 is not None:
                # make sure both splits use the exact point of intersection.
                split10.setEndPoint(p1)
                split11.setStartPoint(p1)
            paths1 = paths1 + (split10,)
            paths2 = (split11,) + paths2


        if self.closed:
            subpaths = ( (paths2 + paths0),
                         paths1, )
        else:
            subpaths = ( paths0,
                         paths1,
                         paths2, )

        result = []
        for subpath in subpaths:
            if len(subpath) > 0:
                result.append(TFSPath(False, *subpath))
        return result

    def splitIntersectionWithPath(self, other, index0, index1, segment0, segment1, t0, t1, p):
        split00, split01 = segment0.split(t0)
        split10, split11 = segment1.split(t1)
        # make sure both splits use the exact point of intersection.
        split00.setEndPoint(p)
        split01.setStartPoint(p)
        split10.setEndPoint(p)
        split11.setStartPoint(p)
        path0 = TFSPath(False, *(self.segments[:index0] + (split00, )))
        path1 = TFSPath(False, *((split01, ) + self.segments[index0 + 1:]))
        path2 = TFSPath(False, *(other.segments[:index1] + (split10, )))
        path3 = TFSPath(False, *((split11, ) + other.segments[index1 + 1:]))
        return path0, path1, path2, path3, p

    def intersectionWithPath(self, other, maxEndpoints, ignoreEqualSegments=False):
        intersection = self.intersectionWithPath_tOnly(other, maxEndpoints=maxEndpoints, ignoreEqualSegments=ignoreEqualSegments)
        if intersection:
            index0, index1, segment0, segment1, t0, t1, p = intersection
            path0, path1, path2, path3, p = self.splitIntersectionWithPath(other, index0, index1, segment0, segment1, t0, t1, p)
            return path0, path1, path2, path3, p
        return None

    def simpleSplit(self, t):
        if len(self.segments) != 1:
            raise Exception("Isn't a simple path")
        segment0, segment1 = self.segments[0].split(t)
        return TFSPath(False, segment0), TFSPath(False, segment1)

    def simpleEvaluate(self, t):
        if len(self.segments) != 1:
            raise Exception("Isn't a simple path")
        return self.segments[0].evaluate(t)

    def simpleEvaluateWithTangent(self, t):
        if len(self.segments) != 1:
            raise Exception("Isn't a simple path")
        return self.segments[0].evaluateWithTangent(t)

    def simpleTangentToPath(self, other):
        if len(self.segments) != 1:
            raise Exception("Isn't a simple path")
        if len(other.segments) != 1:
            raise Exception("Isn't a simple path")
        return self.segments[0].tangentToSegment(other.segments[0])

    def sliceSimpleBezierAtT(self, t):
        if t <= 0 or t >= 1:
            raise Exception("Invalid t: " + str(t))
        if len(self.segments) != 1:
            raise Exception("Isn't a simple path")
        if len(self.segments[0].points) == 3:
            raise Exception("Isn't a cubic bezier")
        elif len(self.segments[0].points) == 4:
            segment = self.segments[0]
            midpoint, tangent, cp0, cp1 = evaluateCubicSpline2D_pointAndTangent(segment.points[0],
                                                                      segment.points[1],
                                                                      segment.points[2],
                                                                      segment.points[3],
                                                                      t)
            subpath0 = TFSPath(False, TFSSegment(segment.points[0],
                                                 segment.points[0].plus(segment.points[1].minus(segment.points[0]).scale(t)),
#                                             segment.points[1],
                                             cp0,
                                             midpoint))
            subpath1 = TFSPath(False, TFSSegment(midpoint,
                                                 cp1,
#                                                 segment.points[2],
                                                 segment.points[3].plus(segment.points[2].minus(segment.points[3]).scale(1.0 - t)),
                                                 segment.points[3]))
            return subpath0, subpath1
        else:
            raise Exception("Isn't a straight line")
        pass

    def sliceSimpleBezierAtY(self, value):
        if len(self.segments) != 1:
            raise Exception("Isn't a simple path")
        if len(self.segments[0].points) != 4:
            raise Exception("Isn't a cubic bezier")

        segment = self.segments[0]
        cp0, cp1, cp2, cp3 = segment.points
        p0 = evaluateCubicSpline2D_point(cp0, cp1, cp2, cp3, 0)
        p1 = evaluateCubicSpline2D_point(cp0, cp1, cp2, cp3, 1)
        if p0.y < value and p1.y < value:
            raise Exception("both bezier endPoints below y value")
        if p0.y > value and p1.y > value:
            raise Exception("both bezier endPoints above y value")

        if p0.y < p1.y:
            minY = p0.y
            maxY = p1.y
            minT = 0
            maxT = 1
        else:
            minY = p1.y
            maxY = p0.y
            minT = 1
            maxT = 0


        while True:
            t = minT + (maxT - minT) * (value - minY) / (maxY - minY)
            p = evaluateCubicSpline2D_point(cp0, cp1, cp2, cp3, t)
            print 'minT', minT, 'maxY', maxY, 'minY', minY, 'maxY', maxY, 't', t, 'value', value, 'p.y', p.y

            diff = abs(p.y - value)
            SLICE_BEZIER_TOLERANCE = getFloatRoundingTolerance()
            if diff < SLICE_BEZIER_TOLERANCE:
                break

            if value > p.y:
                minY = p.y
                minT = t
            else:
                maxY = p.y
                maxT = t

        midpoint, tangent, cp0, cp1 = evaluateCubicSpline2D_pointAndTangent(segment.points[0],
                                                                  segment.points[1],
                                                                  segment.points[2],
                                                                  segment.points[3],
                                                                  t)
        subpath0 = TFSPath(False, TFSSegment(segment.points[0],
                                             segment.points[0].plus(segment.points[1].minus(segment.points[0]).scale(t)),
#                                             segment.points[1],
                                         cp0,
                                         midpoint))
        subpath1 = TFSPath(False, TFSSegment(midpoint,
                                             cp1,
#                                                 segment.points[2],
                                             segment.points[3].plus(segment.points[2].minus(segment.points[3]).scale(1.0 - t)),
                                             segment.points[3]))
        return subpath0, subpath1


    def splitWithPath(self, other):
        for index0 in xrange(len(self.segments)):
            segment0 = self.segments[index0]
            for index1 in xrange(len(other.segments)):
                segment1 = other.segments[index1]
#        for segment0 in self.segments:
#            for segment1 in other.segments:

                split = segment0.findIntersection_raw(segment1)
#                split = segment0.findIntersection_recursiveClipping(segment1)
                if split:
                    t0, t1, point = split

                    split00, split01 = segment0.split(t0)
                    segments00 = self.segments[:index0] + (split00,)
                    segments01 = (split01,) + self.segments[index0+1:]

                    split10, split11 = segment1.split(t1)
                    segments10 = other.segments[:index1] + (split10,)
                    segments11 = (split11,) + other.segments[index1+1:]

                    return ( TFSPath(False, *segments00),
                             TFSPath(False, *segments01),
                             TFSPath(False, *segments10),
                             TFSPath(False, *segments11), point )
#                    return point
        return None

    def startTangent(self):
        return self.segments[0].startTangent()

    def endTangent(self):
        return self.segments[-1].endTangent()

    def pop(self, count=1):
        if len(self.segments) < 1 + count:
            raise Exception('Cannot pop() from path')
        newSegments = [segment.copy() for segment in self.segments[:-count]]
        return TFSPath(self.closed, *newSegments)

    def popHead(self, count=1):
        if len(self.segments) < 1 + count:
            raise Exception('Cannot popHead() from path')
        newSegments = [segment.copy() for segment in self.segments[count:]]
        return TFSPath(self.closed, *newSegments)

    def evaluateWithMaxPrecision(self, precision):
        result = []
        for segment in self:
            result.extend(segment.evaluateWithMaxPrecision(precision)[:-1])
        return result


def minmaxPaths(paths):
    result = None
    for path in paths:
        result = minmaxMerge(result, path.minmax())
    return result


def minmaxPathsEvaluated(paths, precision):
    result = None
    for path in paths:
        result = minmaxMerge(result, path.minmaxEvaluated(precision))
    return result


def polygonWithPoints(*points):
    lastPoint = points[-1]
    segments = []
    for point in points:
        segments.append(TFSSegment(lastPoint, point))
        lastPoint = point
#    print 'segments', len(segments), segments
    return TFSPath(True, *segments)
#    items = [TFSPathItem(point) for point in points]
#    return pathWithItems(True, *items)


def openPathWithPoints(*points):
    lastPoint = None
    segments = []
    for point in points:
        if lastPoint is not None:
            segments.append(TFSSegment(lastPoint, point))
        lastPoint = point
    return TFSPath(False, *segments)
#    items = [TFSPathItem(point) for point in points]
#    return pathWithItems(True, *items)


DEFAULT_MERGE_TOLERANCE = getFloatRoundingTolerance()

def connectSegments(segments, closed, mergeTolerance=None):
    if mergeTolerance is None:
        mergeTolerance = DEFAULT_MERGE_TOLERANCE

#    print 'path', type(path), path
    newSegments = []
    lastSegment = None
    if closed:
        lastSegment = segments[-1]
#    print 'lastSegment', type(lastSegment), lastSegment
    for segment in segments:
#        print 'segment', type(segment), segment
        if lastSegment is not None:
            if lastSegment.endPoint() == segment.startPoint():
                midpoint = lastSegment.endPoint().midpoint(segment.startPoint())
                lastSegment.setEndPoint(midpoint)
                segment.setStartPoint(midpoint)
            else:
                distance = lastSegment.endPoint().distanceTo(segment.startPoint())
                if distance < mergeTolerance:
                    # merge
                    midpoint = lastSegment.endPoint().midpoint(segment.startPoint())
                    lastSegment.setEndPoint(midpoint)
                    segment.setStartPoint(midpoint)
                else:
                    newSegments.append(TFSSegment(lastSegment.endPoint(), segment.startPoint()))
#            newSegments.append(segment)
        newSegments.append(segment)
        lastSegment = segment
    return TFSPath(closed, *newSegments)

def connectPathSegments(path, mergeTolerance=None):
    return connectSegments(path.copy().segments,
                           path.closed, mergeTolerance=mergeTolerance)


def returnArgs(*argv):
    return argv

def returnArg(arg):
    return arg

def concatenatePath(closed, *objs):
    segments = []
    def appendSegmentPoints(*points):
        if len(points) == 2:
            startPoint = points[0]
            endPoint = points[-1]
            if startPoint == endPoint:
                return
        segments.append(TFSSegment(*points))

    lastPoint = None
    for index in xrange(len(objs)):
        obj = objs[index]
        if isinstance(obj, TFSPath):
            if lastPoint is not None:
                appendSegmentPoints(lastPoint, obj.startPoint())
                lastPoint = None
            segments.extend(obj.copy().segments)
        elif isinstance(obj, TFSSegment):
            if lastPoint is not None:
                appendSegmentPoints(lastPoint, obj.startPoint())
                lastPoint = None
            segments.append(obj.copy())
        elif isinstance(obj, TFSPoint):
            if lastPoint is not None:
                appendSegmentPoints(lastPoint, obj)
                lastPoint = None
            if len(segments) > 0:
                lastSegment = segments[-1]
                appendSegmentPoints(lastSegment.endPoint(), obj)
            else:
                lastPoint = obj
        else:
            raise Exception('Unknown argument: ' + str(type(obj)))

    return connectSegments(segments, closed)


def splitLineWithLine(l0, l1):
    if not l0.isStraightLine():
        raise Exception('Not a straight line')
    if not l1.isStraightLine():
        raise Exception('Not a straight line')
    p00 = l0.startPoint()
    p01 = l0.endPoint()
    p10 = l1.startPoint()
    p11 = l1.endPoint()

    intersect = TFSIntersection.calculateIntersectPoint(p00, p01, p10, p11)
    if intersect is None:
        raise Exception('lines do not intersect')
    return openPathWithPoints(p00, intersect), openPathWithPoints(intersect, p01)


def isClosedPathClockwise(path, debug=False):
    '''
    Reverse the path if necessary so that it is clockwise.
    '''
    angleSum = 0
    lastPoint = path.segments[-1].startPoint()
    for index, segment in enumerate(path.segments):
        p0 = segment.startPoint()
        p1 = segment.endPoint()
        angle0 = p0.minus(lastPoint).atan2()
        angle1 = p1.minus(p0).atan2()
        angleDiff = normalizeRadiansDiff(angle1 - angle0)
        angleSum += angleDiff
        if debug:
            print index + 1, 'angleDiff', angleDiff, 'angle0', angle0, 'angle1', angle1, 'angleSum', angleSum

        lastPoint = p0

    if debug:
        print 'angleSum', angleSum
    return angleSum < 0

def orientClosedPathClockwise(path):
    '''
    Reverse the path if necessary so that it is clockwise.
    '''
    if not isClosedPathClockwise(path):
        return path.reverse()
    else:
        return path

def debugPath(name, path):
    print
    print name, path.description()
#        print repr(path)
    for index1, segment in enumerate(path):
        print '\t', 'segment', index1, segment.description()
    print

def debugPaths(name, paths):
    print
    print name, len(paths)
    for index0, path in enumerate(paths):
        print '\t', 'path', index0, path.description()
#        print repr(path)
        for index1, segment in enumerate(path):
            print '\t\t', 'segment', index1, segment.description()
    print
