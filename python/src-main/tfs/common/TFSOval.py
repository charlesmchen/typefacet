'''
robofont-extensions-and-scripts
TFSOval.py

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

#        print 'self.hRadius', self.hRadius, 'self.vRadius', self.vRadius
#        print 'self.center', self.center
#        print 'ps', ps
#        print 'check1', self.center.distanceTo(ps.lc)

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
