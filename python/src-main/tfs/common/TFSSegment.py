'''
robofont-extensions-and-scripts
TFSSegment.py

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
from TFSValidationException import TFSValidationException

onJython = sys.platform.startswith('java')


def inferTValue(minValue, maxValue, value):
    if value == minValue:
        return 0.0
    if value == maxValue:
        return 1.0
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
            if startVector is None:
                raise TFSValidationException('Empty start vector')
            if endVector is None:
                raise TFSValidationException('Empty end vector')
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
                    if ((startIntersectionLength <= startVectorLength * 0.5) and
                        (endIntersectionLength <= endVectorLength * 0.5)):
                        # this curve will cross itself.

#                        print 'cpIntersection', cpIntersection.description()
#                        print 'startVectorLength', startVectorLength
#                        print 'endVectorLength', endVectorLength
#                        print 'startIntersectionLength', startIntersectionLength
#                        print 'endIntersectionLength', endIntersectionLength
#                        print 'hmm', startIntersectionLength, startVectorLength * 0.5, startIntersectionLength > startVectorLength * 0.5

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
            return self.startVector().normalize()
#            return self.points[1].minus(self.points[0]).normalize()
        except ZeroDivisionError, e:
            print 'Segment.normalize() ZeroDivisionError', self.description()
            raise e

    def endTangent(self):
        try:
            return self.endVector().normalize()
#            return self.points[1].minus(self.points[0]).normalize()
        except ZeroDivisionError, e:
            print 'Segment.normalize() ZeroDivisionError', self.description()
            raise e
#        return self.points[-1].minus(self.points[-2]).normalize()

#    def inferredEndTangent(self):
#        '''
#        Tangent derived simply by subtracting the endpoints.
#        Does not reflect the actual endpoint tangents.
#        '''
#        try:
#            return self.endPoint().minus(self.startPoint()).normalize()
#        except ZeroDivisionError, e:
#            print 'Segment.normalize() ZeroDivisionError', self.description()
#            raise e

    def naiveEndpointTangent(self):
        '''
        Tangent derived simply by subtracting the endpoints.
        Does not reflect the actual endpoint tangents.
        '''
        try:
            return self.endPoint().minus(self.startPoint()).normalize()
        except ZeroDivisionError, e:
            print 'Segment.normalize() ZeroDivisionError', self.description()
            raise e

    def naiveStartVector(self):
        return self.points[1].minus(self.points[0])

    def startVector(self):
#        return self.points[1].minus(self.points[0])

        '''
        Normally, we can derive the start vector by subtracting the first
        point from the second point, regardless of whether this segment
        is a straight line, quadratic or bezier curve.
        '''
        naiveResult = self.points[1].minus(self.points[0])
        if naiveResult.x != 0 or naiveResult.y != 0:
            return naiveResult

        '''
        Try to derive start vector using other means.
        '''
        if len(self.points) == 4:
            '''
            For quadratic bezier curves, if the first control point is same
            as the startPoint, try to use the other control point.
            '''
            otherControlpointResult = self.points[-2].minus(self.points[0])
            if otherControlpointResult.x != 0 or otherControlpointResult.y != 0:
                return otherControlpointResult
            '''
            If both control points are the same as the startPoint,
            curve is a straight line, try using the endpoints.
            '''

        '''
        Default to returning the endpoint result, which may have zero length.
        '''
        endpointResult = self.points[-1].minus(self.points[0])
        if endpointResult.x != 0 or endpointResult.y != 0:
            return endpointResult
#        return None
        raise Exception('Invalid start vector')
#        return naiveResult

    def naiveEndVector(self):
        return self.points[-1].minus(self.points[-2])

    def endVector(self):
#        return self.points[-1].minus(self.points[-2])

        '''
        Normally, we can derive the end vector by subtracting the second-to-last
        point from the last point, regardless of whether this segment
        is a straight line, quadratic or bezier curve.
        '''
        naiveResult = self.points[-1].minus(self.points[-2])
        if naiveResult.x != 0 or naiveResult.y != 0:
            return naiveResult

        '''
        Try to derive end vector using other means.
        '''
        if len(self.points) == 4:
            '''
            For quadratic bezier curves, if the second control point is same
            as the endPoint, try to use the other control point.
            '''
            otherControlpointResult = self.points[-1].minus(self.points[-3])
            if otherControlpointResult.x != 0 or otherControlpointResult.y != 0:
                return otherControlpointResult
            '''
            If both control points are the same as the endPoint,
            curve is a straight line, try using the endpoints.
            '''

        '''
        Default to returning the endpoint result, which may have zero length.
        '''
        endpointResult = self.points[-1].minus(self.points[0])
        if endpointResult.x != 0 or endpointResult.y != 0:
            return endpointResult
#        return None
        raise Exception('Invalid end vector')
#        return naiveResult


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


    def isColinear2_linear(self, p):
        '''
        returns t if colinear, None otherwise.
        '''

        '''
        Trivial discard case.
        '''
        minmax = self.minmax()
        if ((p.x < minmax.minX) or
            (minmax.maxX < p.x) or
            (p.y < minmax.minY) or
            (minmax.maxY < p.y)):
            return None

        p0 = self.startPoint()
        p1 = self.endPoint()

        '''
        Trivial endpoint cases.
        '''
        if p.roundedEquals(p0):
            return 0.0
        if p.roundedEquals(p1):
            return 1.0

        if p0.x == p1.x:
            '''
            Vertical case.
            '''
            if p0.x == p.x:
                t = inferTValue(p0.y, p1.y, p.y)
                return t
            else:
                return None
        if p0.y == p1.y:
            '''
            Horizontal case.
            '''
            if p0.y == p.y:
                t = inferTValue(p0.x, p1.x, p.x)
                return t
            else:
                return None

        '''
        General case
        '''
        tx = inferTValue(p0.x, p1.x, p.x)
        ty = inferTValue(p0.y, p1.y, p.y)
        if abs(tx - ty) > getFloatRoundingTolerance():
            return None
        t = (tx + ty) * 0.5
        return t


    def isColinear2_recursiveClipping(self, p):
        '''
        Trivial endpoint cases.
        '''
        if p.roundedEquals(self.startPoint()):
            return self.startT
        if p.roundedEquals(self.endPoint()):
            return self.endT

        '''
        Trivial discard case.
        '''
        bbox = self.boundingBox()
        if not bbox.containsPoint(p):
            return None

        try:
            scaleFactor = max(bbox.width, bbox.height)
            SCALE_FACTOR_THRESHOLD = getFloatRoundingTolerance() * 2
            if scaleFactor > SCALE_FACTOR_THRESHOLD:
                left, right = self.split(0.5)
                left.startT = self.startT
                left.endT = right.startT = self.startT + (self.endT - self.startT) * 0.5
                right.endT = self.endT
                for subsegment in (left, right,):
                    t = subsegment.isColinear2_recursiveClipping(p)
                    if t is not None:
                        return t
                return None
        except TFSValidationException, e:
            '''
            Due to rounding error, we may get validation errors
            when slicing bezier curves very finely.
            '''
            pass

        # Default to not splitting
        t = self.isColinear2_linear(p)
        if t is None:
            return None
        return self.startT + (self.endT - self.startT) * t


    def isColinear2(self, p):
        '''
        returns t if colinear, None otherwise.
        '''
        if len(self.points) == 2:
            return self.isColinear2_linear(p)
        elif len(self.points) in (3, 4,):
            return self.isColinear2_recursiveClipping(p)
        else:
            raise Exception('evaluatePointsWithT(): Invalid segment point count: %d' % len(self.points))


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
            elif p0.y == p1.y:
                return inferTValue(p0.x, p1.x, p.x)
            else:
                tx = inferTValue(p0.x, p1.x, p.x)
                ty = inferTValue(p0.y, p1.y, p.y)
                return (tx + ty) * 0.5

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

    def findIntersection2_raw(self, other_segment, debugMode=False):
        '''
        Given two segments, return _any_ intersection, including endpoint and co-linear intersections.

        returns selfT, otherT, point of intersection
            or None.
        '''
        debugMode = False
        if debugMode:
            print 'findIntersection considering', self.description(), other_segment.description()

#        '''
#        Trivial endpoint case.
#        '''
#        if self.startPoint() == other_segment.startPoint():
#            return 0.0, 0.0, self.startPoint()
#        if self.startPoint() == other_segment.endPoint():
#            return 0.0, 1.0, self.startPoint()
#        if self.endPoint() == other_segment.startPoint():
#            return 1.0, 0.0, self.endPoint()
#        if self.endPoint() == other_segment.endPoint():
#            return 1.0, 1.0, self.endPoint()

        '''
        Trivial bounding-box case.
        '''
        minmax0 = self.minmax()
        minmax1 = other_segment.minmax()
        if ((minmax0.maxX < minmax1.minX) or
            (minmax1.maxX < minmax0.minX) or
            (minmax0.maxY < minmax1.minY) or
            (minmax1.maxY < minmax0.minY)):
            if debugMode:
                print 'findIntersection2_raw.0'
            return None

        selfT = self.isColinear2(other_segment.startPoint())
        if selfT is not None:
            if debugMode:
                print 'colinear1', selfT
            if debugMode:
                print 'findIntersection2_raw.1'
            return selfT, 0.0, other_segment.startPoint()
        selfT = self.isColinear2(other_segment.endPoint())
        if selfT is not None:
            if debugMode:
                print 'colinear2', selfT
            if debugMode:
                print 'findIntersection2_raw.2'
            return selfT, 1.0, other_segment.endPoint()

        otherT = other_segment.isColinear2(self.startPoint())
        if otherT is not None:
            if debugMode:
                print 'colinear3', otherT
            if debugMode:
                print 'findIntersection2_raw.3'
            return 0.0, otherT, self.startPoint()
        otherT = other_segment.isColinear2(self.endPoint())
        if otherT is not None:
            if debugMode:
                print 'colinear4', otherT
            if debugMode:
                print 'findIntersection2_raw.4'
            return 1.0, otherT, self.endPoint()

        if self.isStraight() and other_segment.isStraight():
#        if self.isStraight() and other_segment.isStraight() and False:
            intersection = self.findIntersection_naive(other_segment, debugMode=debugMode)
        else:
            intersection = self.findIntersection_recursiveClipping(other_segment)

        if intersection:
            selfT, otherT, point = intersection
            if debugMode:
                print 'findIntersection2_raw.7'
            return selfT, otherT, point
        if debugMode:
            print 'findIntersection2_raw.8'
        return None


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

    def findIntersection2(self, other_segment, maxEndpoints):
        '''
        maxEndpoints == 0 means no endpoints may be involved in the intersection.
        maxEndpoints == 1 means only endpoints may be involved in the intersection.
        maxEndpoints == 2 means endpoints of both segments may be involved in the intersection.
        '''
        if maxEndpoints < 0 or maxEndpoints > 2:
            raise Exception('Invalid maxEndpoints value: %d' % maxEndpoints)

        intersection = self.findIntersection2_raw(other_segment)
        if intersection:
            selfT, otherT, point = intersection
            if maxEndpoints == 0:
                if ( point.roundedEquals(self.startPoint()) or
                     point.roundedEquals(self.endPoint()) or
                     point.roundedEquals(other_segment.startPoint()) or
                     point.roundedEquals(other_segment.endPoint())):
                    return None
            elif maxEndpoints == 1:
                if ( ( point.roundedEquals(self.startPoint()) or
                       point.roundedEquals(self.endPoint())) and
                     ( point.roundedEquals(other_segment.startPoint()) or
                       point.roundedEquals(other_segment.endPoint()))):
                    return None
            return selfT, otherT, point
#            return self, other_segment, selfT, otherT, point
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


def debugSegments(name, segments):
    print
    print name, len(segments)
    for index, segment in enumerate(segments):
        print '\t', index, segment.description() if segment is not None else 'None'
