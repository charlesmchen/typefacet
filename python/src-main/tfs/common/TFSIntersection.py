'''
robofont-extensions-and-scripts
TFSIntersection.py

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


from TFSPoint import *


def getIntersectPoint(p1, p2, p3, p4):
    try:
        denom = float((p1.x - p2.x) * (p3.y - p4.y) - (p1.y - p2.y) * (p3.x - p4.x))
        x = ((p1.x * p2.y - p1.y * p2.x) * (p3.x - p4.x) - (p1.x - p2.x) * (p3.x * p4.y - p3.y * p4.x)) / denom
        y = ((p1.x * p2.y - p1.y * p2.x) * (p3.y - p4.y) - (p1.y - p2.y) * (p3.x * p4.y - p3.y * p4.x)) / denom
    except ZeroDivisionError:
        return
    return TFSPoint(x, y).roundWithDefaultPrecision()


# For line segments (ie not infinitely long lines) the intersect point
# may not lay on both lines.
#
# If the point where two lines intersect is inside both line's bounding
# rectangles then the lines intersect. Returns intersect point if the line
# intesect o None if not
def calculateIntersectPoint(p1, p2, p3, p4, debugMode=False):
    '''
    We need to be very careful with rounding error.
    '''

    p = getIntersectPoint(p1, p2, p3, p4)
    if debugMode:
        print 'calculateIntersectPoint', 'p', p
    #   print 'p', p
    #   print 'p1', p1
    #   print 'p2', p2
    #   print 'p3', p3
    #   print 'p4', p4
    if not p:
        if debugMode:
            print 'calculateIntersectPoint.0'
        return None

    '''
    Check to make sure that the point of intersection is on both segments.
    We use rounded values for the sake of comparison t avoid rounding error.
    '''
    _p = p.roundWithDefaultPrecision()
    _p1 = p1.roundWithDefaultPrecision()
    _p2 = p2.roundWithDefaultPrecision()
    _p3 = p3.roundWithDefaultPrecision()
    _p4 = p4.roundWithDefaultPrecision()
    if ((_p.x < min(_p1.x, _p2.x) or _p.x < min(_p3.x, _p4.x)) or
        (_p.x > max(_p1.x, _p2.x) or _p.x > max(_p3.x, _p4.x)) or
        (_p.y < min(_p1.y, _p2.y) or _p.y < min(_p3.y, _p4.y)) or
        (_p.y > max(_p1.y, _p2.y) or _p.y > max(_p3.y, _p4.y))):
        if debugMode:
            print '_p', _p.x, _p.y
            print '_p1', _p1.x, _p1.y
            print '_p2', _p2.x, _p2.y
            print '_p3', _p3.x, _p3.y
            print '_p4', _p4.x, _p4.y
            print '1', (_p.x < min(_p1.x, _p2.x) or _p.x < min(_p3.x, _p4.x))
            print '2', (_p.x > max(_p1.x, _p2.x) or _p.x > max(_p3.x, _p4.x))
            print '3', (_p.y < min(_p1.y, _p2.y) or _p.y < min(_p3.y, _p4.y))
            print '4', (_p.y > max(_p1.y, _p2.y) or _p.y > max(_p3.y, _p4.y))
            print '1', (_p.x < min(_p1.x, _p2.x), _p.x < min(_p3.x, _p4.x))
            print '2', (_p.x > max(_p1.x, _p2.x), _p.x > max(_p3.x, _p4.x))
            print '3', (_p.y < min(_p1.y, _p2.y), _p.y < min(_p3.y, _p4.y))
            print '4', (_p.y > max(_p1.y, _p2.y), _p.y > max(_p3.y, _p4.y))
            print 'calculateIntersectPoint.1'
        return None

    '''
    To avoid rounding error, make sure endpoint values don't exceed the segment endpoints.
    '''
    p.x = max(p.x, min(p1.x, p2.x, p3.x, p4.x))
    p.x = min(p.x, max(p1.x, p2.x, p3.x, p4.x))
    p.y = max(p.y, min(p1.y, p2.y, p3.y, p4.y))
    p.y = min(p.y, max(p1.y, p2.y, p3.y, p4.y))

#    if ((p.x < min(p1.x, p2.x) or p.x < min(p3.x, p4.x)) or
#        (p.x > max(p1.x, p2.x) or p.x > max(p3.x, p4.x)) or
#        (p.y < min(p1.y, p2.y) or p.y < min(p3.y, p4.y)) or
#        (p.y > max(p1.y, p2.y) or p.y > max(p3.y, p4.y))):
#        if debugMode:
#            print 'p', p.x, p.y
#            print 'p1', p1.x, p1.y
#            print 'p2', p2.x, p2.y
#            print 'p3', p3.x, p3.y
#            print 'p4', p4.x, p4.y
#            print '1', (p.x < min(p1.x, p2.x) or p.x < min(p3.x, p4.x))
#            print '2', (p.x > max(p1.x, p2.x) or p.x > max(p3.x, p4.x))
#            print '3', (p.y < min(p1.y, p2.y) or p.y < min(p3.y, p4.y))
#            print '4', (p.y > max(p1.y, p2.y) or p.y > max(p3.y, p4.y))
#            print '1', (p.x < min(p1.x, p2.x), p.x < min(p3.x, p4.x))
#            print '2', (p.x > max(p1.x, p2.x), p.x > max(p3.x, p4.x))
#            print '3', (p.y < min(p1.y, p2.y), p.y < min(p3.y, p4.y))
#            print '4', (p.y > max(p1.y, p2.y), p.y > max(p3.y, p4.y))
#            print 'calculateIntersectPoint.1'
#        return None
    #   if ((p.x < min(p1.x, p2.x, p3.x, p4.x)) or
    #       (p.x > max(p1.x, p2.x, p3.x, p4.x)) or
    #       (p.y < min(p1.y, p2.y, p3.y, p4.y)) or
    #       (p.y > max(p1.y, p2.y, p3.y, p4.y))):
    #       return None
    if debugMode:
        print 'calculateIntersectPoint.2'
    return p

def intersectionWithTangents(p0, tangent0, p1, tangent1):
    p = getIntersectPoint(p0, p0.plus(tangent0),
                          p1, p1.plus(tangent1))
    return p


# Test script below...
if __name__ == "__main__":

    # line 1 and 2 cross, 1 and 3 don't but would if extended, 2 and 3 are parallel
    # line 5 is horizontal, line 4 is vertical
    p1 = TFSPoint(1,5)
    p2 = TFSPoint(4,7)

    p3 = TFSPoint(4,5)
    p4 = TFSPoint(3,7)

    p5 = TFSPoint(4,1)
    p6 = TFSPoint(3,3)

    p7 = TFSPoint(3,1)
    p8 = TFSPoint(3,10)

    p9 =  TFSPoint(0,6)
    p10 = TFSPoint(5,6)

    p11 = (472.0, 116.0)
    p12 = (542.0, 116.0)

    assert None != calculateIntersectPoint(p1, p2, p3, p4), "line 1 line 2 should intersect"
    assert None != calculateIntersectPoint(p3, p4, p1, p2), "line 2 line 1 should intersect"
    assert None == calculateIntersectPoint(p1, p2, p5, p6), "line 1 line 3 shouldn't intersect"
    assert None == calculateIntersectPoint(p3, p4, p5, p6), "line 2 line 3 shouldn't intersect"
    assert None != calculateIntersectPoint(p1, p2, p7, p8), "line 1 line 4 should intersect"
    assert None != calculateIntersectPoint(p7, p8, p1, p2), "line 4 line 1 should intersect"
    assert None != calculateIntersectPoint(p1, p2, p9, p10), "line 1 line 5 should intersect"
    assert None != calculateIntersectPoint(p9, p10, p1, p2), "line 5 line 1 should intersect"
    assert None != calculateIntersectPoint(p7, p8, p9, p10), "line 4 line 5 should intersect"
    assert None != calculateIntersectPoint(p9, p10, p7, p8), "line 5 line 4 should intersect"

    print "\nSUCCESS! All asserts passed for doLinesIntersect"
