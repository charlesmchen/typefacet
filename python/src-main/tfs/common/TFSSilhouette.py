'''
robofont-extensions-and-scripts
TFSSilhouette.py

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

from TFSPoint import scaleVectorHV
from TFSPath import *
import TFSIntersection as TFSntersection
from TFSTesselation import TFSTesselation as FTesselation
from TFSMath import *
from TFSOval import TFSOval as TFSOval
from TFSContoursException import TFSContoursException
from TFSValidationException import TFSValidationException


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


def _flateSegmentLeft(segment, hDistance, vDistance=None):
    '''
    '''
    if vDistance is None:
        vDistance = hDistance

    if (segment.startVector().length() == 0 or
        segment.endVector().length() == 0):
        raise Exception('Cannot flate a segment without valid tangents: ' + segment.description())


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
        result = TFSSegment(*newPoints).roundWithDefaultPrecision()

        '''
        Segments can be turned "inside out" when deflating.
        For example, deflating an arc by more than its "radius".
        We want to discard these segments.
        We can detect them by checking whether the naive endpoint tangent has reversed.
        '''
        affinity = result.naiveEndpointTangent().dotProduct(segment.naiveEndpointTangent())
        if affinity < 0:
            return None

        return result
    except TFSValidationException, e:
        '''
        flating a segment can result in an empty or otherwise invalid segment.
        In fact, this will happen often since we'll be deflating previously
        inflated rounding curves.
        That's fine; ignore them.
        '''
        return None


def _flatePathLeft(path, hDistance, vDistance=None, debugMode=False):
    '''
    Input paths may be clockwise (fill) or counter-clockwise (hole) if we are inflating.
    And they are reversed if we are deflating.

    Edge case: What happens if we inflate an oval curve beyond it's center?
    Edge case: What happens if segment has a start or end vector of zero length?
        Should be fine.
    '''

    for segment in path:
        if (segment.startVector().length() == 0 or
            segment.endVector().length() == 0):
            raise Exception('Cannot flate a segment without valid tangents: ' + segment.description())

    if vDistance is None:
        vDistance = hDistance
    if hDistance <= 0 or vDistance <= 0:
        raise Exception('Invalid flate distances, hDistance: %f, vDistance: %f ' % ( hDistance, vDistance, ) )

    TIME_INFLATE_DEFLATE_PATHS = False
#    debugMode = True

    if TIME_INFLATE_DEFLATE_PATHS:
        import time
        time0 = time.time()

#    raise TFSContoursException('argh', [path,])

    if debugMode:
        print 'flatePathLeft input'
        for index, segment in enumerate(path):
            print '\t', 'segment', index, segment.description()
        print

    '''
    Phase 1: Naively "flate" segments left.
    '''
    offsetSegments = []
    for index, segment in enumerate(path):
        newSegment = _flateSegmentLeft(segment, hDistance, vDistance)
        '''
        Inflating a segment can result in an empty or otherwise invalid segment.
        In fact, this will happen often since we'll be deflating previously
        inflated rounding curves.
        That's fine; ignore them.
        '''
        if newSegment is not None:
            if debugMode:
                print 'inflating segment'
                print '\t', 'from', index, segment.description()
                print '\t', 'to', index, newSegment.description()

        offsetSegments.append(newSegment)
    del segment

#    print 'hDistance', hDistance
#    print 'vDistance', vDistance

    debugSegments('offsetSegments', offsetSegments)

#    if debugMode:
#        raise TFSContoursException('argh', [TFSPath(False, segment) for segment in offsetSegments if segment is not None])

    '''
    Phase 2: Add rounding segments as necessary.
    '''
    roundingPaths = [None,] * len(path)
    lastSegmentInvalid = False
#    for index, segment in enumerate(offsetSegments):
    for index, srcSegment in enumerate(path):
        lastSrcSegment = path[(index + len(path) - 1) % len(path)]
        offsetSegment = offsetSegments[index]
        lastOffsetSegment = offsetSegments[(index + len(path) - 1) % len(path)]

        if debugMode:
            print 'checking join'
            print '\t', 'offsetSegment', index, offsetSegment.description() if offsetSegment is not None else ''
            print '\t', 'lastOffsetSegment', index, lastOffsetSegment.description() if lastOffsetSegment is not None else ''
            print '\t', 'srcSegment', index, srcSegment.description() if srcSegment is not None else ''
            print '\t', 'srcSegment', index, srcSegment.description() if srcSegment is not None else ''
#            print '\t', 'to', index, segment.description()

        if ((offsetSegment is not None) and
            (lastOffsetSegment is not None) and
            offsetSegment.startPoint().roundedEquals(lastOffsetSegment.endPoint())):
#            (offsetSegment.startPoint() == lastOffsetSegment.endPoint())):
            '''
            No join necessary if inflated segments that align perfectly.
            '''
            if debugMode:
                print 'No join necessary (segments aligned)'

            '''
            Heal the join.
            '''
            endpoint = offsetSegment.startPoint().midpoint(lastOffsetSegment.endPoint())
            offsetSegment.setStartPoint(endpoint)
            lastOffsetSegment.setEndPoint(endpoint)

            continue

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

                try:
                    roundingPath = roundingc.createArc(roundingStartAngle, roundingEndAngle).reverse()
                except TFSValidationException, e:
                    '''
                    If its too short to round, just use a straight segment.
                    '''
                    continue

                # Make sure the rounding endpoints exactly align.
                if lastOffsetSegment is not None:
                    roundingPath[0].setStartPoint(lastOffsetSegment.endPoint())
                if offsetSegment is not None:
                    roundingPath[-1].setEndPoint(offsetSegment.startPoint())
#                    if debugMode:
#                        rounding = openPathWithPoints(rounding.startPoint(), roundingCenter, rounding.endPoint())
                if debugMode:
                    debugPath('roundingPath', roundingPath)

                roundingPaths[index] = roundingPath
                if debugMode:
                    print 'inserting join'
                    for value in roundingPath.segments:
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

        lastSegmentInvalid = False

#    if debugMode:
#        raise TFSContoursException('argh', [TFSPath(False, segment) for segment in newSegments])

    if not(len(offsetSegments) ==
           len(roundingPaths) ==
           len(path)):
        print 'offsetSegments, roundingPaths, path', len(offsetSegments), len(roundingPaths), len(path)
        raise Exception('Unexpected segments')
    newSegments = []
    for offsetSegment, roundingPath in zip(offsetSegments, roundingPaths):
        if roundingPath is not None:
            newSegments.extend(roundingPath.segments)
        if offsetSegment is not None:
            newSegments.append(offsetSegment)
    newSegments = [segment.roundWithDefaultPrecision() for segment in newSegments]
    newPaths = [TFSPath(False, segment) for segment in newSegments]

    if debugMode:
        debugPaths('newPaths', newPaths)

    debugPaths('_flatePathLeft midpoint newPaths', newPaths)
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
    tesselatedPaths, intersections = FTesselation().tesselateContours(newPaths, reorientPaths=False, ignoreStrayEdges=True, debugMode=debugMode)
#    newPaths, intersections = FTesselation().tesselateContours(newPaths, reorientPaths=False, ignoreStrayEdges=True, debugMode=debugMode)
#    newPaths, intersections = FTesselation().tesselateContours(newPaths, reorientPaths=False, debugMode=True)

    debugPaths('_flatePathLeft tesselatedPaths', tesselatedPaths)

    if TIME_INFLATE_DEFLATE_PATHS:
        time1 = time.time()
        print '\t', 'TFSSilhouette.deflatePaths.tesselateContours', time1 - time0

#    raise TFSContoursException('argh', newPaths)

    if TIME_INFLATE_DEFLATE_PATHS:
        time1 = time.time()
        print '\t', 'TFSSilhouette.deflatePaths.cleanup', time1 - time0

    return tesselatedPaths


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

    allFlatedPaths = []
    for path in paths:
        print 'reversePaths', reversePaths
        debugPath('path', path)
        if reversePaths:
            srcPath = path.reverse()
        else:
            srcPath = path
        debugPath('srcPath', srcPath)
        flatedPaths = _flatePathLeft(srcPath, hDistance, vDistance, debugMode)
        debugPaths('flatedPaths', flatedPaths)
        if reversePaths:
            flatedPaths = [flatedPath.reverse() for flatedPath in flatedPaths]
        debugPaths('flatedPaths.1', flatedPaths)

        for flatedPath in flatedPaths:
            if isClosedPathClockwise(flatedPath) == isClosedPathClockwise(path):
                '''
                If deflating path has reversed its orientation, discard it.
                It is a hole that has collapsed on itself.
                '''
                allFlatedPaths.append(flatedPath)

    debugPaths('all flatedPaths', allFlatedPaths)

#        newPaths.extend(inflatedPaths)

#    raise TFSContoursException('argh', newPaths)

    TIME_INFLATE_DEFLATE_PATHS = False

    if TIME_INFLATE_DEFLATE_PATHS:
        import time
        time0 = time.time()
    tesselatePaths, intersections = FTesselation().tesselateContours(allFlatedPaths, reorientPaths=False, debugMode=debugMode)
    if TIME_INFLATE_DEFLATE_PATHS:
        time1 = time.time()
        print '\t', 'TFSSilhouette.inflateDeflatePaths.tesselateContours', time1 - time0

    return tesselatePaths


def inflatePaths(paths, hDistance, vDistance=None, debugMode=False):
    return inflateDeflatePaths(paths, reversePaths=False, hDistance=hDistance, vDistance=vDistance, debugMode=debugMode)

inflatePathsLeft = inflatePaths

def deflatePaths(paths, hDistance, vDistance=None, debugMode=False):
    return inflateDeflatePaths(paths, reversePaths=True, hDistance=hDistance, vDistance=vDistance, debugMode=debugMode)


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
