'''
robofont-extensions-and-scripts
TFSPathTest.py

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


"""
File: TFSPathTest.py
Project: LivelyType1

@author: Charles Matthew Chen (felasold@gmail.com)
Copyright 2012 FelaSold Inc. All rights reserved.
"""


import math
from TFSTest import TFSTest
from tfs.common.TFSPoint import TFSPoint, TFSPoint0
from tfs.common.TFSSegment import TFSSegment
from tfs.common.TFSPath import TFSPath


class TFSPathTest(TFSTest):

    def setUp(self):
        pass

#    def test_init(self):
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
#
#        try:
#            TFSSegment(TFSPoint0(), TFSPoint0(), TFSPoint0(), TFSPoint0(), TFSPoint0())
#            self.fail('Missing exception')
#        except Exception, e:
#            pass
#
#    def test_len(self):
#        self.assertEqual(len(TFSSegment(TFSPoint0(), TFSPoint0())), 2)
#        self.assertEqual(len(TFSSegment(TFSPoint0(), TFSPoint0(), TFSPoint0())), 3)
#        self.assertEqual(len(TFSSegment(TFSPoint0(), TFSPoint0(), TFSPoint0(), TFSPoint0())), 4)
#
#    def test_hash(self):
#        testset = set()
#        self.assertEqual(len(testset), 0)
#        testset.add(TFSSegment(TFSPoint(0, 0), TFSPoint(0, 0)))
#        self.assertEqual(len(testset), 1)
#        testset.add(TFSSegment(TFSPoint(0, 0), TFSPoint(0, 0)))
#        self.assertEqual(len(testset), 1)
#        testset.add(TFSSegment(TFSPoint(0, 0), TFSPoint(0, 0), TFSPoint(0, 0)))
#        self.assertEqual(len(testset), 2)
#        testset.add(TFSSegment(TFSPoint(0, 0), TFSPoint(0, 0), TFSPoint(0, 0)))
#        self.assertEqual(len(testset), 2)
#
#    def test_evaluate(self):
#        segment2 = TFSSegment(TFSPoint(1, 3),
#                                TFSPoint(3, 7))
#        self.assertPointClose(segment2.evaluate(0), TFSPoint(1, 3))
#        self.assertPointClose(segment2.evaluate(-0.5), TFSPoint(1, 3))
#        self.assertPointClose(segment2.evaluate(1), TFSPoint(3, 7))
#        self.assertPointClose(segment2.evaluate(1.1), TFSPoint(3, 7))
#        self.assertPointClose(segment2.evaluate(0.5), TFSPoint(2, 5))
#        # TODO: bezier curves.
#
#    def test_split(self):
#        pass
        # TODO:
#        pass

#    def startTangent(self):
#        try:
#            return self.points[1].minus(self.points[0]).normalize()
#        except ZeroDivisionError, e:
#            print 'Segment.normalize() ZeroDivisionError', self.description()
#            raise e
#
#    def endTangent(self):
#        return self.points[-1].minus(self.points[-2]).normalize()
#
#    def startVector(self):
#        return self.points[1].minus(self.points[0])
#
#    def endVector(self):
#        return self.points[-1].minus(self.points[-2])
#
#    def evaluateWithMaxPrecision(self, precision):
#        if len(self.points) == 2:
#            return list(self.points)
#        elif len(self.points) in (3, 4):
#            result = [self.points[0],]
#            for i in xrange(1, precision):
#                t = i / float(precision)
#                result.append(self.evaluate(t))
#            result.append(self.points[-1])
#            return result
#        else:
#            raise Exception('evaluatePointsWithT(): Invalid segment point count: %d' % len(self.points))
#
#    def isColinear_linear(self, p):
#        bBox = self.boundingBox()
#        if not bBox.containsPoint(p):
#            return None
#        p0 = self.startpoint()
#        p1 = self.endpoint()
#        if p0.x == p1.x:
#            if p0.x == p.x:
#                t = inferTValue(p0.y, p1.y, p.y)
#                print 'isColinear_linear horizontal', p0.description(), p1.description(), p.description(), t
#                return t
#            else:
#                return None
#        if p0.y == p1.y:
#            if p0.y == p.y:
#                t = inferTValue(p0.x, p1.x, p.x)
#                print 'isColinear_linear vertical', p0.description(), p1.description(), p.description(), t
#                return t
#            else:
#                return None
#
#        tx = inferTValue(p0.x, p1.x, p.x)
#        ty = inferTValue(p0.y, p1.y, p.y)
#        if abs(tx - ty) > FLOAT_ROUNDING_TOLERANCE:
#            return None
#        t = (tx + ty) * 0.5
#        print 'isColinear_linear', p0.description(), p1.description(), p.description(), t
#        return t
#
#    def isColinear_recursiveClipping(self, p, level=0):
##        print '\t' * level, 'isColinear_recursiveClipping', self.description(), p.description()
#
#        if p == self.startpoint():
#            return self.startT
#        if p == self.endpoint():
#            return self.endT
#
#        bbox = self.boundingBox()
#        if not bbox.containsPoint(p):
#            return None
#
#        scaleFactor = max(bbox.width, bbox.height)
#        SCALE_FACTOR_THRESHOLD = 0.001
#        if scaleFactor < SCALE_FACTOR_THRESHOLD:
#            selfT = self.isColinear_linear(p)
#            if selfT is None:
#                return None
#            return self.startT + (self.endT - self.startT) * selfT
#
#        left, right = self.split_recursiveClipping(0.5)
##        print '\t' * level, 'left', left
##        print '\t' * level, 'right', right
#
#        for subsegment in (left, right):
##            print '\t' * level, 'dividing into', subsegment.description()
#            selfT = subsegment.isColinear_recursiveClipping(p, level=level+1)
#            if selfT is not None:
#                return selfT
#        return None
#
#
#    def isColinear(self, p):
#        '''
#        If point is colinear, return t
#        else return None
#        '''
#        if p == self.startpoint():
#            return None
#        if p == self.endpoint():
#            return None
#
#        if len(self.points) == 2:
#            return self.isColinear_linear(p)
#        elif len(self.points) == 3:
#            return self.isColinear_recursiveClipping(p)
#        elif len(self.points) == 4:
#            return self.isColinear_recursiveClipping(p)
#        else:
#            raise Exception('evaluatePointsWithT(): Invalid segment point count: %d' % len(self.points))
#
#
#    def split_recursiveClipping(self, t):
#        left, right = self.split(t)
#
#        left.startT = self.startT
#        left.endT = right.startT = self.startT + (self.endT - self.startT) * t
#        right.endT = self.endT
#
##        print 'cutting', self.description(), self.startT, self.endT
##        print '\t', 't', t
##        print '\t', 'left', left.description(), left.startT, left.endT
##        print '\t', 'left', right.description(), right.startT, right.endT
#        return left, right
#
#
#    def findIntersection_naive(self, other_segment):
#        point = LineIntersection.calculateIntersectPoint(self.startpoint(), self.endpoint(), other_segment.startpoint(), other_segment.endpoint())
#        if not point:
#            return None
#
#        point = TFSPoint(point.x, point.y)
#
#        def findT(p0, p1, p):
#            if p0.x == p1.x:
#                return inferTValue(p0.y, p1.y, p.y)
#            else:
#                return inferTValue(p0.x, p1.x, p.x)
#
#        def interpolateT(startT, endT, t):
#            result = startT + (endT - startT) * t
##            print 'interpolateT', startT, endT, 't', t, '->', result
#            return result
#        selfT = findT(self.startpoint(), self.endpoint(), point)
#        selfT = interpolateT(self.startT, self.endT, selfT)
#        otherT = findT(other_segment.startpoint(), other_segment.endpoint(), point)
#        otherT = interpolateT(other_segment.startT, other_segment.endT, otherT)
#
#        return selfT, otherT, point
#
#
#    def findIntersection_recursiveClipping(self, other_segment, level=0):
##        if level > 2:
##            return None
##        print '\t' * level, 'findIntersection_recursiveClipping considering', self.description(), other_segment.description()
#
#        bbox = self.boundingBox()
#        other_bbox = other_segment.boundingBox()
#        if not bbox.intersects(other_bbox):
#            return None
#
#        '''
#        TODO: refactor to only subdivide non-linear bezier curves.
#        Threshold should also only be based on non-linear segments.
#        '''
#
#        scaleFactor = max(bbox.width, bbox.height, other_bbox.width, other_bbox.height)
#        SCALE_FACTOR_THRESHOLD = 0.001
#        if scaleFactor < SCALE_FACTOR_THRESHOLD:
#            intersection = self.findIntersection_naive(other_segment)
#            if not intersection:
#                return None
#
##            selfT, otherT, point = intersection
##            print 'selfT, otherT, point', selfT, otherT, point, point.description()
#            return intersection
#
#        selfCuts = self.split_recursiveClipping(0.5)
#        otherCuts = other_segment.split_recursiveClipping(0.5)
#
#        for subsegment in selfCuts:
#            for other_subsegment in otherCuts:
##                print '\t' * level, 'dividing into', subsegment.description(), other_subsegment.description()
##                intersection = None
#                intersection = subsegment.findIntersection_recursiveClipping(other_subsegment, level=level+1)
#                if intersection:
##                    selfT, otherT, point = intersection
##                    print 'selfT, otherT, point', selfT, otherT, point, point.description()
#                    return intersection
#        return None
#
#    def isStraight(self):
#        return len(self.points) == 2
#
#    def plusOffset(self, offset):
#        newPoints = []
#        for point in self.points:
#            newPoints.append(point.plus(offset))
#        return TFSSegment(*newPoints)
#
#    def findIntersection(self, other_segment):
#        DEBUG = False
#        if DEBUG:
#            print 'findIntersection considering', self.description(), other_segment.description()
#
#        selfT = self.isColinear(other_segment.startpoint())
#        if selfT is not None:
#            if DEBUG:
#                print 'colinear1', selfT
#            return self, other_segment, selfT, 0, other_segment.startpoint()
#        selfT = self.isColinear(other_segment.endpoint())
#        if selfT is not None:
#            if DEBUG:
#                print 'colinear2', selfT
#            return self, other_segment, selfT, 1, other_segment.endpoint()
#
#        otherT = other_segment.isColinear(self.startpoint())
#        if otherT is not None:
#            if DEBUG:
#                print 'colinear3', otherT
#            return self, other_segment, 0, otherT, self.startpoint()
#        otherT = other_segment.isColinear(self.endpoint())
#        if otherT is not None:
#            if DEBUG:
#                print 'colinear4', otherT
#            return self, other_segment, 1, otherT, self.endpoint()
#
#        '''
#        Now that we know the neither segment has an endpoint that is collinear,
#        check endpoints.
#        '''
#        if self.startpoint() in (other_segment.startpoint(),
#                                 other_segment.endpoint()):
#            return None
#        if self.endpoint() in (other_segment.startpoint(),
#                                 other_segment.endpoint()):
#            return None
#
#        if self.isStraight() and other_segment.isStraight():
##        if self.isStraight() and other_segment.isStraight() and False:
#            intersection = self.findIntersection_naive(other_segment)
#        else:
#            intersection = self.findIntersection_recursiveClipping(other_segment)
#
#        if intersection:
#            selfT, otherT, point = intersection
#            return self, other_segment, selfT, otherT, point
#        return None
#
#    def tangentToSegment(self, other):
#
#
#        DEBUG = True
#        DEBUG = False
#
#        if DEBUG:
#            print
#            print 'tangentToSegment', self.description(), other.description()
#
#        def createPoint(segment, t):
#            result = MetaMap()
#            result.t = t
#            result.p, result.tangent, _, _ = segment.evaluateWithTangent(t)
##            result.angle = result.tangent.atan2()
#            result.angle = normalizeRadians(result.tangent.atan2())
#            return result
#
#        def printPoint(name, point):
#            print name,
#            for attr in ('t', 'p', 'tangent', 'angle'):
#                print attr, getattr(point, attr),
#            print
#
#        endpoint00 = createPoint(self, 0)
#        endpoint01 = createPoint(self, 1)
#        endpoint10 = createPoint(other, 0)
#        endpoint11 = createPoint(other, 1)
#
#        if DEBUG:
#            printPoint('endpoint00', endpoint00)
#            printPoint('endpoint01', endpoint01)
#        if DEBUG:
#            printPoint('endpoint10', endpoint10)
#            printPoint('endpoint11', endpoint11)
#
#        # Invert ts if necessary so that angles always increase with t.
#        if normalizeRadiansDiff(endpoint01.angle - endpoint00.angle) < 0:
#            endpoint00, endpoint01 = endpoint01, endpoint00
#        if normalizeRadiansDiff(endpoint11.angle - endpoint10.angle) < 0:
#            endpoint10, endpoint11 = endpoint11, endpoint10
#
#
#        endpoint01.angle = normalizeRadiansAboveAngle(endpoint01.angle, endpoint00.angle)
#        endpoint11.angle = normalizeRadiansAboveAngle(endpoint11.angle, endpoint10.angle)
#
#        # Start at the midpoint of each segment
#        t0 = 0.5
#        t1 = 0.5
#
#        if DEBUG:
#            printPoint('endpoint00\'', endpoint00)
#            printPoint('endpoint01\'', endpoint01)
#            printPoint('endpoint10\'', endpoint10)
#            printPoint('endpoint11\'', endpoint11)
#
#        MAX_ATTEMPTS = 32
#        for _ in xrange(MAX_ATTEMPTS):
##        while True:
#            point0 = createPoint(self, t0)
#            point1 = createPoint(other, t1)
#
#            point0.angle = normalizeRadiansAboveAngle(point0.angle, endpoint00.angle)
#            point1.angle = normalizeRadiansAboveAngle(point1.angle, endpoint10.angle)
#
#            if DEBUG:
#                print
#                printPoint('point0', point0)
#                printPoint('point1', point1)
#
#            angle = point1.p.minus(point0.p).atan2()
#            if DEBUG:
#                print 'angle', angle
#            diff0 = normalizeRadiansDiff(angle - point0.angle)
#            diff1 = normalizeRadiansDiff(angle - point1.angle)
#            if DEBUG:
#                print 'diff0', diff0, 'diff1', diff1
#
#            TANGENT_TO_SEGMENT_PRECISION = 0.0001
#            if abs(diff0) < TANGENT_TO_SEGMENT_PRECISION and abs(diff1) < TANGENT_TO_SEGMENT_PRECISION:
#                # success
#                if DEBUG:
#                    print 'success', 't0, t1, point0.p, point1.p', t0, t1, point0.p, point1.p
#                    print
#                return t0, t1, point0.p, point1.p
#
#            # Select an endpoint to move towards.
#            endpoint0 = endpoint01 if diff0 > 0 else endpoint00
#            endpoint1 = endpoint11 if diff1 > 0 else endpoint10
#            if DEBUG:
#                printPoint('endpoint0', endpoint0)
#                printPoint('endpoint1', endpoint1)
#            factor0 = normalizeRadiansDiff(angle - point0.angle) / normalizeRadiansDiff(endpoint0.angle - point0.angle)
#            factor1 = normalizeRadiansDiff(angle - point1.angle) / normalizeRadiansDiff(endpoint1.angle - point1.angle)
#            BREAKING_FACTOR = 0.85
#            factor0 *= BREAKING_FACTOR
#            factor1 *= BREAKING_FACTOR
#            t0 = t0 + (endpoint0.t - t0) * factor0
#            t1 = t1 + (endpoint1.t - t1) * factor1
#
#            if DEBUG:
#                print 'factor0', factor0, 't0', t0
#                print 'factor1', factor1, 't1', t1
#
#        raise Exception('Algorithm did not converge.')
#
#    def setEndpoint(self, value):
#        self.points = list(self.points)
#        self.points[-1] = value
#
#    def setStartpoint(self, value):
#        self.points = list(self.points)
#        self.points[0] = value
#
#    def tangentToPoint(self, dst):
#        if len(self.points) not in (3, 4):
#            raise Exception('Not a bezier curve')
#
#        t0 = 0
#        t1 = 1
#
#        def radiansDiff(angle0, angle1):
#            result = angle1 - angle0
#            while result < -math.pi:
#                result += 2 * math.pi
#            while result > math.pi:
#                result -= 2 * math.pi
#            return result
#
#        def evaluateTValue(t, dst):
#            p, tangent, _, _ = self.evaluateWithTangent(t)
#            pDiff = dst.minus(p)
#            pAngle = math.atan2(pDiff.y, pDiff.x)
#            tangentAngle = math.atan2(tangent.y, tangent.x)
#            angleDiff = radiansDiff(pAngle, tangentAngle)
#            score = pDiff.normalize().dotProduct(tangent.normalize())
#            return p, tangent, angleDiff, score
#
#        p0, tangent0, angleDiff0, score0 = evaluateTValue(t0, dst)
##        print 't0, p0, tangent0, angleDiff0, score0', t0, p0, tangent0, angleDiff0, score0
#        p1, tangent1, angleDiff1, score1 = evaluateTValue(t1, dst)
##        print 't1, p1, tangent1, angleDiff1, score1', t1, p1, tangent1, angleDiff1, score1
#
#        # We can't interpolate if the tangents of the endpoints of the bezier curve don't
#        # enclose the destination point.
#        if angleDiff0 < 0 and angleDiff1 < 0:
#            raise Exception('Invalid bezier curve')
#        if angleDiff0 > 0 and angleDiff1 > 0:
#            raise Exception('Invalid bezier curve')
#
#        if angleDiff0 < angleDiff1:
#            tmin, pmin, tangentmin, angleDiffmin, scoremin = t0, p0, tangent0, angleDiff0, score0
#            tmax, pmax, tangentmax, angleDiffmax, scoremax = t1, p1, tangent1, angleDiff1, score1
#        else:
#            tmin, pmin, tangentmin, angleDiffmin, scoremin = t1, p1, tangent1, angleDiff1, score1
#            tmax, pmax, tangentmax, angleDiffmax, scoremax = t0, p0, tangent0, angleDiff0, score0
#
#        while True:
#            tm = (tmin + tmax) * 0.5
#            pm, tangentm, angleDiffm, scorem = evaluateTValue(tm, dst)
##            print 'tm, pm, tangentm, angleDiffm, scorem', tm, pm, tangentm, angleDiffm, scorem
#
#            TANGENT_TO_POINT_PRECISION = 0.9999
#
#            if scorem >= TANGENT_TO_POINT_PRECISION:
#                return tm, pm
#            if angleDiffm < 0:
#                tmin, pmin, tangentmin, angleDiffmin, scoremin = tm, pm, tangentm, angleDiffm, scorem
#            else:
#                tmax, pmax, tangentmax, angleDiffmax, scoremax = tm, pm, tangentm, angleDiffm, scorem
#
#
#import sys
#onJython = sys.platform.startswith('java')
#
#
#class TFSPath(object):
#
#    def __init__(self, closed, *segments):
#        if not onJython:
#            import types
#            if type(closed) != types.BooleanType:
#                raise Exception('Unexpected closed type: ' + str(type(closed)))
#            if type(segments) not in (types.ListType, types.TupleType):
#                raise Exception('Unexpected segments type: ' + str(type(segments)))
#        self.closed = closed
#        if len(segments) < 1:
#            raise Exception('Invalid path')
#        self.segments = segments
#
#    def __len__(self):
#        return len(self.segments)
#
#    def __iter__(self):
#        for segment in self.segments:
#            yield segment
#
#    def __getitem__(self, index):
#        return self.segments[index]
#
#    def description(self):
#        return '[Path[%s]: %s]' % ( str(self.closed),
#                                    (''.join((
#                                        str(self.startpoint()),
#                                        '... ',
#                                        str(len(self.segments)),
#                                        ' segments, ',
#                                        '...',
#                                        str(self.endpoint()),
#                                        ))),
#                                      )
##        return '[Path[%s](%d): %s]' % ( str(self.closed),
##                                        len(self.segments),
##                                       ','.join(segment.description() for segment in self.segments)
##                                      )
#
#    def startpoint(self):
#        return self.segments[0].startpoint()
#
#    def endpoint(self):
#        return self.segments[-1].endpoint()
#
#    def plus(self, other, closed=False):
#        newSegments = list(self.segments)
#        if self.endpoint() != other.startpoint():
#            newSegments.append(TFSSegment(self.endpoint(), other.startpoint()))
#        newSegments += list(other.segments)
#        return TFSPath(closed, *newSegments)
#
#    def reverse(self):
#        newSegments = [segment.reverse() for segment in self.segments]
#        newSegments.reverse()
#        return TFSPath(self.closed, *newSegments)
#
#    def copy(self):
#        newSegments = [segment.copy() for segment in self.segments]
#        return TFSPath(self.closed, *newSegments)
#
#    def removeEmptySegments(self):
#        newSegments = []
#        for segment in self:
#            if (segment.endpoint() == segment.startpoint()) and len(segment) == 2:
#                continue
#            newSegments.append(segment.copy())
#        if len(newSegments) == 0:
#            raise Exception('Empty path')
#        return TFSPath(self.closed, *newSegments)
#
#    def asOpen(self):
#        newSegments = [segment.copy() for segment in self.segments]
#        return TFSPath(False, *newSegments)
#
#    def decompose(self):
#        return [TFSPath(False, segment.copy()) for segment in self.segments]
#
#    def minmax(self):
#        points = []
#        for segment in self.segments:
#            points.extend(segment.points)
#
#        result = MetaMap()
#        result.minX = reduce(min, [point.x for point in points])
#        result.maxX = reduce(max, [point.x for point in points])
#        result.minY = reduce(min, [point.y for point in points])
#        result.maxY = reduce(max, [point.y for point in points])
#        return result
#
#    def minmaxEvaluated(self, precision):
#        points = []
#        for segment in self.segments:
#            points.extend(segment.evaluateWithMaxPrecision(precision))
#
#        result = MetaMap()
#        result.minX = reduce(min, [point.x for point in points])
#        result.maxX = reduce(max, [point.x for point in points])
#        result.minY = reduce(min, [point.y for point in points])
#        result.maxY = reduce(max, [point.y for point in points])
#        return result
#
#    def dump(self):
#        print
#        print 'path.dump'
#        for segment in self.segments:
#            print 'segment', segment
#
#    def applyPlus(self, value):
#        newSegments = [segment.applyPlus(value) for segment in self.segments]
#        return TFSPath(self.closed, *newSegments)
#
#    def applyScale(self, value):
#        newSegments = [segment.applyScale(value) for segment in self.segments]
#        return TFSPath(self.closed, *newSegments)
#
#    def applyFunction(self, function):
#        newSegments = [segment.applyFunction(function) for segment in self.segments]
#        return TFSPath(self.closed, *newSegments)
#
#    def applyScaleXY(self, xFactor, yFactor):
#        newSegments = [segment.applyScaleXY(xFactor, yFactor) for segment in self.segments]
#        return TFSPath(self.closed, *newSegments)
#
#    def plusOffset(self, offset):
#        newSegments = []
#        for segment in self.segments:
#            newSegments.append(segment.plusOffset(offset))
#        return TFSPath(self.closed, *newSegments)
#
#    def isStraightLine(self):
#        return (len(self.segments) == 1) and self.segments[0].isStraight()
#
#    def translateStraightLineRight(self, distance):
#        if len(self.segments) != 1 or len(self.segments[0].points) != 2:
#            raise Exception("Isn't a straight line")
#        startpoint = self.startpoint()
#        endpoint = self.endpoint()
#        diff = endpoint.minus(startpoint)
#        vector = diff.normalize()
#        rightVector = vector.rightAngleRight()
#        return TFSPath(False,
#                     TFSSegment(startpoint.plus(rightVector.scale(distance))),
#                     TFSSegment(endpoint.plus(rightVector.scale(distance))))
#
#    def simpleIntersectionWithPath(self, other):
#        if len(self.segments) != 1:
#            raise Exception("Isn't a simple path")
#        if len(other.segments) != 1:
#            raise Exception("Isn't a simple path")
#        return self.segments[0].findIntersection_recursiveClipping(other.segments[0])
#
#    def allIntersections(self, other):
##        newPath0 = self.copy()
#        newPaths0 = [self.copy()]
#        newPaths1 = [other.copy()]
#
#        def allIntersections_iteration(paths0, paths1):
#            for index0 in xrange(len(paths0)):
#                path0 = paths0[index0]
#                for index1 in xrange(len(paths1)):
#                    path1 = paths1[index1]
#                    intersection = path0.intersectionWithPath(path1, ignoreEndpoints=True)
#                    if intersection:
#                        print 'allIntersections', 'intersection!', intersection
#                        path00, path01, path10, path11, _ = intersection
#    #                    if path00.endpoint().distanceTo(path00.startpoint())
#                        print '\t', 'path00', path00.endpoint().distanceTo(path00.startpoint())
#                        print '\t', 'path01', path01.endpoint().distanceTo(path01.startpoint())
#                        print '\t', 'path10', path10.endpoint().distanceTo(path10.startpoint())
#                        print '\t', 'path11', path11.endpoint().distanceTo(path11.startpoint())
#                        paths0 = paths0[:index0] + [path00, path01,] + paths0[index0 + 1:]
#                        paths1 = paths1[:index1] + [path10, path11,] + paths1[index1 + 1:]
#                        return paths0, paths1
#            return None
#
#        while True:
#            print 'allIntersections', 'cycle'
#            intersection = allIntersections_iteration(newPaths0, newPaths1)
#            if not intersection:
#                break
#            newPaths0, newPaths1 = intersection
#
##            for index0 in xrange(len(segments0)):
##                segment0 = segments0[index0]
##            intersectionFound = False
##            for index1 in xrange(len(newPaths1)):
##                print 'allIntersections', 'index1', index1
##                newPath1 = newPaths1[index1]
##                intersection = newPath0.intersectionWithPath(newPath1)
##                if intersection:
##                    print 'allIntersections', 'intersection!', intersection
##                    path00, path01, path10, path11, _ = intersection
###                    if path00.endpoint().distanceTo(path00.startpoint())
##                    print '\t', 'path00', path00.endpoint().distanceTo(path00.startpoint())
##                    print '\t', 'path01', path01.endpoint().distanceTo(path01.startpoint())
##                    print '\t', 'path10', path10.endpoint().distanceTo(path10.startpoint())
##                    print '\t', 'path11', path11.endpoint().distanceTo(path11.startpoint())
##                    newPaths0.append(path00)
##                    newPath0 = path01
##                    newPaths1 = newPaths1[:index1] + [path10, path11,] + newPaths1[index1 + 1:]
##                    intersectionFound = True
##                    break
##            if not intersectionFound:
##                break
##        newPaths0.append(newPath0)
#        print 'newPaths0', len(newPaths0)
#        print 'newPaths1', len(newPaths1)
#        return newPaths0 + newPaths1
#
##        segments0 = [segment.copy() for segment in self.segments]
##        segments1 = [segment.copy() for segment in other.segments]
##        # convert to a stack.
##        segments0.reverse()
##        segments1.reverse()
##        newPaths0 = []
##        newSegments0 = []
##        while len(segments0):
##            segment0 = segments0.pop()
##            newSegments0.push(segment0)
##        if newSegments0:
##            newPaths0.append(TFSPath(False, *newSegments0))
##
###        for segment0 in self.segments:
###            for segment1 in other.segments:
##        for index0 in xrange(len(segments0)):
##            segment0 = segments0[index0]
##            for index1 in xrange(len(segments1)):
##                segment1 = segments1[index1]
##                intersection = segment0.findIntersection_recursiveClipping(segment1)
##                if intersection:
##                    t0, t1, p = intersection
###                    print 't0, t1, p', t0, t1, p
###                    return t0, t1, p
##                    path0 = TFSPath(False, *(self.segments[:index0] + (segment0.split(t0)[0], )))
##                    path1 = TFSPath(False, *((segment0.split(t0)[1], ) + self.segments[index0 + 1:]))
##                    path2 = TFSPath(False, *(other.segments[:index1] + (segment1.split(t1)[0], )))
##                    path3 = TFSPath(False, *((segment1.split(t1)[1], ) + other.segments[index1 + 1:]))
##                    return path0, path1, path2, path3, p
##        return None
#
#    def intersectionWithPath_tOnly(self, other, ignoreEndpoints=False, ignoreEqualSegments=False):
##        for segment0 in self.segments:
##            for segment1 in other.segments:
#        for index0 in xrange(len(self.segments)):
#            segment0 = self.segments[index0]
#            for index1 in xrange(len(other.segments)):
#                segment1 = other.segments[index1]
#
#                if ignoreEqualSegments and segment0 == segment1:
#                    continue
#
#                intersection = segment0.findIntersection_recursiveClipping(segment1)
#                if intersection:
#                    t0, t1, p = intersection
##                    print 't0, t1, p', t0, t1, p
#
#                    '''
#                    When intersecting a path with itself, we want to avoid
#                    false intersection between sequential segments at their endpoints
#                    due to rounding error.
#                    '''
#                    if self is other:
#                        INTERSECTION_ENDPOINT_THRESHOLD = 0.0001
#                        if (index0 + 1) % len(self) == index1:
#                            if segment0.endpoint().distanceTo(p) <= INTERSECTION_ENDPOINT_THRESHOLD:
##                                print '---- ignoring endpoint intersection(0)'
#                                continue
#                        elif index0 == (index1 + 1) % len(self):
#                            if segment1.endpoint().distanceTo(p) <= INTERSECTION_ENDPOINT_THRESHOLD:
##                                print '---- ignoring endpoint intersection(1)'
#                                continue
#
#                    if ignoreEndpoints:
#                        MIN_T = 0.0001
#                        MAX_T = 1.0 - MIN_T
#                        if ((t0 <= MIN_T) or (t0 >= MAX_T)) and ((t1 <= MIN_T) or (t1 >= MAX_T)):
#                            continue
##                        if (t0 <= MIN_T) or (t0 >= MAX_T) or (t1 <= MIN_T) or (t1 >= MAX_T):
##                            continue
##                    print
##                    print 'intersectionWithPath_tOnly'
##                    print 'index0, index1, t0, t1, p', index0, index1, t0, t1, p
##                    print 'segment0', segment0.description()
##                    print 'segment1', segment1.description()
##                    print
#                    return index0, index1, segment0, segment1, t0, t1, p
#        return None
#
#    def singleSplit(self, index, t, p=None):
#        segment = self.segments[index]
#
#        paths0 = self.segments[:index]
#        paths1 = self.segments[index + 1:]
#
#        SPLIT_T_PRECISION = 0.0001
#
#        # do not bother to split if intersection is on an endpoint.
#        if t > 1 - SPLIT_T_PRECISION:
#            paths0 = paths0 + (segment,)
#        elif t < SPLIT_T_PRECISION:
#            paths1 = (segment,) + paths1
#        else:
#            split0, split1 = segment.split(t)
#            if p is not None:
#                # make sure both splits use the exact point of intersection.
#                split0.setEndpoint(p)
#                split1.setStartpoint(p)
#            paths0 = paths0 + (split0,)
#            paths1 = (split1,) + paths1
#
#        result = []
#        for subpaths in (paths0, paths1):
#            if len(subpaths) > 0:
#                result.append(TFSPath(False, *subpaths))
#        return result
#
#    def doubleSplit(self, index0, index1, t0, t1, p0=None, p1=None):
#        segment0 = self.segments[index0]
#        segment1 = self.segments[index1]
#
#        # reverse if necessary.
#        if (index0 > index1) or ((index0 == index1) and (t0 > t1)):
#            index1, index0 = index0, index1
#            segment1, segment0 = segment0, segment1
#            t1, t0 = t0, t1
#            p1, p0 = p0, p1
#
#        paths0 = self.segments[:index0]
#        paths1 = self.segments[index0 + 1:index1]
#        paths2 = self.segments[index1 + 1:]
#
#        SPLIT_T_PRECISION = 0.0001
#
#        # do not bother to split if intersection is on an endpoint.
#        if t0 > 1 - SPLIT_T_PRECISION:
#            paths0 = paths0 + (segment0,)
#        elif t0 < SPLIT_T_PRECISION:
#            paths1 = (segment0,) + paths1
#        else:
#            split00, split01 = segment0.split(t0)
#            if p0 is not None:
#                # make sure both splits use the exact point of intersection.
#                split00.setEndpoint(p0)
#                split01.setStartpoint(p0)
#            paths0 = paths0 + (split00,)
#            paths1 = (split01,) + paths1
#
#
#        # do not bother to split if intersection is on an endpoint.
#        if t1 > 1 - SPLIT_T_PRECISION:
#            paths1 = paths1 + (segment1,)
#        elif t1 < SPLIT_T_PRECISION:
#            paths2 = (segment1,) + paths2
#        else:
#            split10, split11 = segment1.split(t1)
#            if p1 is not None:
#                # make sure both splits use the exact point of intersection.
#                split10.setEndpoint(p1)
#                split11.setStartpoint(p1)
#            paths1 = paths1 + (split10,)
#            paths2 = (split11,) + paths2
#
#
#        if self.closed:
#            subpaths = ( (paths2 + paths0),
#                         paths1, )
#        else:
#            subpaths = ( paths0,
#                         paths1,
#                         paths2, )
#
#        result = []
#        for subpath in subpaths:
#            if len(subpath) > 0:
#                result.append(TFSPath(False, *subpath))
#        return result
#
#    def splitIntersectionWithPath(self, other, index0, index1, segment0, segment1, t0, t1, p):
#        split00, split01 = segment0.split(t0)
#        split10, split11 = segment1.split(t1)
#        # make sure both splits use the exact point of intersection.
#        split00.setEndpoint(p)
#        split01.setStartpoint(p)
#        split10.setEndpoint(p)
#        split11.setStartpoint(p)
#        path0 = TFSPath(False, *(self.segments[:index0] + (split00, )))
#        path1 = TFSPath(False, *((split01, ) + self.segments[index0 + 1:]))
#        path2 = TFSPath(False, *(other.segments[:index1] + (split10, )))
#        path3 = TFSPath(False, *((split11, ) + other.segments[index1 + 1:]))
#        return path0, path1, path2, path3, p
#
#    def intersectionWithPath(self, other, ignoreEndpoints=False, ignoreEqualSegments=False):
#        intersection = self.intersectionWithPath_tOnly(other, ignoreEndpoints=ignoreEndpoints, ignoreEqualSegments=ignoreEqualSegments)
#        if intersection:
#            index0, index1, segment0, segment1, t0, t1, p = intersection
#            path0, path1, path2, path3, p = self.splitIntersectionWithPath(other, index0, index1, segment0, segment1, t0, t1, p)
#            return path0, path1, path2, path3, p
#        return None
#
##
###        for segment0 in self.segments:
###            for segment1 in other.segments:
##        for index0 in xrange(len(self.segments)):
##            segment0 = self.segments[index0]
##            for index1 in xrange(len(other.segments)):
##                segment1 = other.segments[index1]
##
##                if ignoreEqualSegments and segment0 == segment1:
##                    continue
##
##                intersection = segment0.findIntersection_recursiveClipping(segment1)
##                if intersection:
##                    t0, t1, p = intersection
##                    print 't0, t1, p', t0, t1, p
##                    if ignoreEndpoints:
##                        MIN_T = 0.00001
##                        MAX_T = 1.0 - MIN_T
##                        if (t0 <= MIN_T) or (t0 >= MAX_T) or (t1 <= MIN_T) or (t1 >= MAX_T):
##                            continue
###                    return t0, t1, p
##                    split00, split01 = segment0.split(t0)
##                    split10, split11 = segment1.split(t1)
##                    # make sure both splits use the exact point of intersection.
##                    split00.setEndpoint(p)
##                    split01.setStartpoint(p)
##                    split10.setEndpoint(p)
##                    split11.setStartpoint(p)
##                    path0 = TFSPath(False, *(self.segments[:index0] + (split00, )))
##                    path1 = TFSPath(False, *((split01, ) + self.segments[index0 + 1:]))
##                    path2 = TFSPath(False, *(other.segments[:index1] + (split10, )))
##                    path3 = TFSPath(False, *((split11, ) + other.segments[index1 + 1:]))
###                    print 'p', p
###                    print 'p0', segment0.split(t0)[0].endpoint()
###                    print 'p1', segment0.split(t0)[1].startpoint()
###                    print 'p2', segment1.split(t1)[0].endpoint()
###                    print 'p3', segment1.split(t1)[1].startpoint()
##                    return path0, path1, path2, path3, p
##        return None
###        if len(self.segments) != 1:
###            raise Exception("Isn't a simple path")
###        if len(other.segments) != 1:
###            raise Exception("Isn't a simple path")
###        return self.segments[0].findIntersection_recursiveClipping(other.segments[0])
#
#    def simpleSplit(self, t):
#        if len(self.segments) != 1:
#            raise Exception("Isn't a simple path")
#        segment0, segment1 = self.segments[0].split(t)
#        return TFSPath(False, segment0), TFSPath(False, segment1)
#
#    def simpleEvaluate(self, t):
#        if len(self.segments) != 1:
#            raise Exception("Isn't a simple path")
#        return self.segments[0].evaluate(t)
#
#    def simpleEvaluateWithTangent(self, t):
#        if len(self.segments) != 1:
#            raise Exception("Isn't a simple path")
#        return self.segments[0].evaluateWithTangent(t)
#
#    def simpleTangentToPath(self, other):
#        if len(self.segments) != 1:
#            raise Exception("Isn't a simple path")
#        if len(other.segments) != 1:
#            raise Exception("Isn't a simple path")
#        return self.segments[0].tangentToSegment(other.segments[0])
#
#    def sliceSimpleBezierAtT(self, t):
#        if t <= 0 or t >= 1:
#            raise Exception("Invalid t: " + str(t))
#        if len(self.segments) != 1:
#            raise Exception("Isn't a simple path")
#        if len(self.segments[0].points) == 3:
#            raise Exception("Isn't a cubic bezier")
#        elif len(self.segments[0].points) == 4:
#            segment = self.segments[0]
#            midpoint, tangent, cp0, cp1 = evaluateCubicSpline2D_pointAndTangent(segment.points[0],
#                                                                      segment.points[1],
#                                                                      segment.points[2],
#                                                                      segment.points[3],
#                                                                      t)
#            subpath0 = TFSPath(False, TFSSegment(segment.points[0],
#                                                 segment.points[0].plus(segment.points[1].minus(segment.points[0]).scale(t)),
##                                             segment.points[1],
#                                             cp0,
#                                             midpoint))
#            subpath1 = TFSPath(False, TFSSegment(midpoint,
#                                                 cp1,
##                                                 segment.points[2],
#                                                 segment.points[3].plus(segment.points[2].minus(segment.points[3]).scale(1.0 - t)),
#                                                 segment.points[3]))
#            return subpath0, subpath1
#        else:
#            raise Exception("Isn't a straight line")
#        pass
#
#    def sliceSimpleBezierAtY(self, value):
#        if len(self.segments) != 1:
#            raise Exception("Isn't a simple path")
#        if len(self.segments[0].points) != 4:
#            raise Exception("Isn't a cubic bezier")
#
#        segment = self.segments[0]
#        cp0, cp1, cp2, cp3 = segment.points
#        p0 = evaluateCubicSpline2D_point(cp0, cp1, cp2, cp3, 0)
#        p1 = evaluateCubicSpline2D_point(cp0, cp1, cp2, cp3, 1)
#        if p0.y < value and p1.y < value:
#            raise Exception("both bezier endpoints below y value")
#        if p0.y > value and p1.y > value:
#            raise Exception("both bezier endpoints above y value")
#
#        if p0.y < p1.y:
#            minY = p0.y
#            maxY = p1.y
#            minT = 0
#            maxT = 1
#        else:
#            minY = p1.y
#            maxY = p0.y
#            minT = 1
#            maxT = 0
#
#
#        while True:
#            t = minT + (maxT - minT) * (value - minY) / (maxY - minY)
#            p = evaluateCubicSpline2D_point(cp0, cp1, cp2, cp3, t)
#            print 'minT', minT, 'maxY', maxY, 'minY', minY, 'maxY', maxY, 't', t, 'value', value, 'p.y', p.y
#
#            diff = abs(p.y - value)
#            SLICE_BEZIER_TOLERANCE = 0.0001
#            if diff < SLICE_BEZIER_TOLERANCE:
#                break
#
#            if value > p.y:
#                minY = p.y
#                minT = t
#            else:
#                maxY = p.y
#                maxT = t
#
#        midpoint, tangent, cp0, cp1 = evaluateCubicSpline2D_pointAndTangent(segment.points[0],
#                                                                  segment.points[1],
#                                                                  segment.points[2],
#                                                                  segment.points[3],
#                                                                  t)
#        subpath0 = TFSPath(False, TFSSegment(segment.points[0],
#                                             segment.points[0].plus(segment.points[1].minus(segment.points[0]).scale(t)),
##                                             segment.points[1],
#                                         cp0,
#                                         midpoint))
#        subpath1 = TFSPath(False, TFSSegment(midpoint,
#                                             cp1,
##                                                 segment.points[2],
#                                             segment.points[3].plus(segment.points[2].minus(segment.points[3]).scale(1.0 - t)),
#                                             segment.points[3]))
#        return subpath0, subpath1
#
#
#    def splitWithPath(self, other):
#        for index0 in xrange(len(self.segments)):
#            segment0 = self.segments[index0]
#            for index1 in xrange(len(other.segments)):
#                segment1 = other.segments[index1]
##        for segment0 in self.segments:
##            for segment1 in other.segments:
#                split = segment0.findIntersection_recursiveClipping(segment1)
#                if split:
#                    t0, t1, point = split
#
#                    split00, split01 = segment0.split(t0)
#                    segments00 = self.segments[:index0] + (split00,)
#                    segments01 = (split01,) + self.segments[index0+1:]
#
#                    split10, split11 = segment1.split(t1)
#                    segments10 = other.segments[:index1] + (split10,)
#                    segments11 = (split11,) + other.segments[index1+1:]
#
#                    return ( TFSPath(False, *segments00),
#                             TFSPath(False, *segments01),
#                             TFSPath(False, *segments10),
#                             TFSPath(False, *segments11), point )
##                    return point
#        return None
#
#    def startTangent(self):
#        return self.segments[0].startTangent()
#
#    def endTangent(self):
#        return self.segments[-1].endTangent()
#
#    def __add__(self, other):
#        return concatenatePaths(False, self, other)
#
#    def pop(self, count=1):
#        if len(self.segments) < 1 + count:
#            raise Exception('Cannot pop() from path')
#        newSegments = [segment.copy() for segment in self.segments[:-count]]
#        return TFSPath(self.closed, *newSegments)
#
#    def popHead(self, count=1):
#        if len(self.segments) < 1 + count:
#            raise Exception('Cannot popHead() from path')
#        newSegments = [segment.copy() for segment in self.segments[count:]]
#        return TFSPath(self.closed, *newSegments)
#
#    def __eq__(self, other):
#        return self.segments == other.segments
#
#    def __ne__(self, other):
#        return not self.__eq__(other)
#
#    def __hash__(self):
#        return hash(self.segments)
#
#
##def evaluateQuadraticSpline2D_pointAndTangent(self, p0, p1, p2, t):
##def evaluateCubicSpline2D_pointAndTangent(self, p0, p1, p2, p3, t):
#
#def polygonWithPoints(*points):
#    lastPoint = points[-1]
#    segments = []
#    for point in points:
#        segments.append(TFSSegment(lastPoint, point))
#        lastPoint = point
##    print 'segments', len(segments), segments
#    return TFSPath(True, *segments)
##    items = [TFSPathItem(point) for point in points]
##    return pathWithItems(True, *items)
#
#
#def openPathWithPoints(*points):
#    lastPoint = None
#    segments = []
#    for point in points:
#        if lastPoint is not None:
#            segments.append(TFSSegment(lastPoint, point))
#        lastPoint = point
#    return TFSPath(False, *segments)
##    items = [TFSPathItem(point) for point in points]
##    return pathWithItems(True, *items)
#
#DEFAULT_MERGE_TOLERANCE = 0.01
#
#def connectPathSegments(path, mergeTolerance=DEFAULT_MERGE_TOLERANCE):
##def connectPathSegments(path, mergeTolerance=connectPathMergeTolerance):
#    # make a local copy so that we can safely make merge changes.
#    path = path.copy()
#
##    print 'path', type(path), path
#    newSegments = []
#    lastSegment = None
#    if path.closed:
#        lastSegment = path.segments[-1]
##    print 'lastSegment', type(lastSegment), lastSegment
#    for segment in path.segments:
##        print 'segment', type(segment), segment
#        if lastSegment is not None:
#            if lastSegment.endpoint() != segment.startpoint():
#                distance = lastSegment.endpoint().distanceTo(segment.startpoint())
#                if distance < mergeTolerance:
#                    # merge
#                    midpoint = lastSegment.endpoint().midpoint(segment.startpoint())
#                    lastSegment.points = list(lastSegment.points)
#                    segment.points = list(segment.points)
#                    lastSegment.points[-1] = midpoint
#                    segment.points[0] = midpoint
#                else:
#                    newSegments.append(TFSSegment(lastSegment.endpoint(), segment.startpoint()))
##            newSegments.append(segment)
#        newSegments.append(segment)
#        lastSegment = segment
#    return TFSPath(path.closed, *newSegments)
#
##def concatenatePaths(closed, *paths):
##    segments = []
##    for path in paths:
##        segments.extend(path.copy().segments)
##    return TFSPath(closed, *segments)
#
#def concatenatePaths(closed, *objs):
#    segments = []
#    lastPoint = None
#    for index in xrange(len(objs)):
#        obj = objs[index]
#        if isinstance(obj, TFSPath):
#            if lastPoint is not None:
#                segments.append(TFSSegment(lastPoint, obj.startpoint()))
#                lastPoint = None
#            segments.extend(obj.copy().segments)
#        elif isinstance(obj, TFSPoint):
#            if lastPoint is not None:
#                segments.append(TFSSegment(lastPoint, obj))
#                lastPoint = None
#            if len(segments) > 0:
#                lastSegment = segments[-1]
#                segments.append(TFSSegment(lastSegment.endpoint(), obj))
#            else:
#                lastPoint = obj
#        else:
#            raise Exception('Unknown argument: ' + str(type(obj)))
#    return TFSPath(closed, *segments).removeEmptySegments()
#
#def splitLineWithLine(l0, l1):
#    if not l0.isStraightLine():
#        raise Exception('Not a straight line')
#    if not l1.isStraightLine():
#        raise Exception('Not a straight line')
#    p00 = l0.startpoint()
#    p01 = l0.endpoint()
#    p10 = l1.startpoint()
#    p11 = l1.endpoint()
#
#    intersect = LineIntersection.calculateIntersectPoint(p00, p01, p10, p11)
#    if intersect is None:
#        raise Exception('lines do not intersect')
#    return openPathWithPoints(p00, intersect), openPathWithPoints(intersect, p01)
#
##path0 = openPathWithPoints(TFSPoint(1,2), TFSPoint(3,2), TFSPoint(1,5))
##path1 = path0.reverse()
##path2 = path1.reverse()
##print 'path0'
##path0.dump()
##print 'path1'
##path1.dump()
##print 'path2'
##path2.dump()
##print 'path0 == path0', path0 == path0
##print 'path0 == path1', path0 == path1
##print 'path0 == path2', path0 == path2
##pathSet = set((path0,))
##print 'pathSet.contains(path0)', path0 in pathSet
##print 'pathSet.contains(path1)', path1 in pathSet
##print 'pathSet.contains(path2)', path2 in pathSet
#
#
#def isClosedPathClockwise(path, debug=False):
#    '''
#    Reverse the path if necessary so that it is clockwise.
#    '''
#    angleSum = 0
#    lastPoint = path.segments[-1].startpoint()
#    for index, segment in enumerate(path.segments):
#        p0 = segment.startpoint()
#        p1 = segment.endpoint()
#        angle0 = p0.minus(lastPoint).atan2()
#        angle1 = p1.minus(p0).atan2()
#        angleDiff = normalizeRadiansDiff(angle1 - angle0)
#        angleSum += angleDiff
#        if debug:
#            print index + 1, 'angleDiff', angleDiff, 'angle0', angle0, 'angle1', angle1, 'angleSum', angleSum
#
#        lastPoint = p0
#
#    if debug:
#        print 'angleSum', angleSum
#    return angleSum < 0
#
#def orientClosedPathClockwise(path):
#    '''
#    Reverse the path if necessary so that it is clockwise.
#    '''
#    if not isClosedPathClockwise(path):
#        return path.reverse()
#    else:
#        return path
