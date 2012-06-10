'''
robofont-extensions-and-scripts
Autokern.py

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


import os
import shutil
import math
import time
import locale
import itertools
import yaml

locale.setlocale(locale.LC_ALL, 'en_US')

from tfs.common.TFSFont import *
from AutokernSettings import AutokernSettings
#from tfs.common.TFSSilhouette import *
from tfs.common.TFTiming import TFTiming
from tfs.common.TFSMap import TFSMap
import tfs.common.TFSMath as TFSMath
from tfs.common.TFSPath import minmaxPaths, minmaxMerge, openPathWithPoints, debugPaths, concatenatePath, orientClosedPathClockwise
from tfs.common.TFSPoint import TFSPoint, scaleVectorHV
from tfs.common.TFSSegment import TFSSegment
from tfs.common.TFSOval import TFSOval
from tfs.common.TFSValidationException import TFSValidationException
import tfs.common.TFSIntersection as TFSIntersection
import tfs.common.UnicodeCharacterNames as UnicodeCharacterNames
#from collections import defaultdict


TFSMath.setFloatRoundingTolerance(0.1)
TFSMath.setDefaultPrecisionDigits(1)

AUTOKERN_SEGMENT_PRECISION = 16

USE_CACHED_KERNING_MAP = False
#USE_CACHED_KERNING_MAP = True


def formatGlyphUnicode(glyph):
    if glyph.unicode is None:
        return 'None'
    else:
        return u'%d %s' % ( glyph.unicode,
                            hex(glyph.unicode), )

def formatUnicode(value):
    if value is None:
        return 'None'
    else:
        return '0x%X' % ( value, )

def formatGlyphName(glyph):
    if glyph.unicode is None:
        name = glyph.name
    elif glyph.name == unichr(glyph.unicode):
        name = glyph.name
    else:
        name = u'%s &#%d;' % ( glyph.name,
                               glyph.unicode, )
    return u'%s (%s)' % ( name,
                          formatGlyphUnicode(glyph), )

def getCachedMinmax(contours):
    return minmaxPaths(contours)

class Autokern(TFSMap):

    def __init__(self):
        TFSMap.__init__(self)

    def isCombiningGlyph(self, glyph):
        names = ('dieresis_acutecomb',
                 'dieresis_gravecomb',
                 'hungarumlaut',
                'ring',
                'dotaccent',

                 'dieresistonos',

                'acutecomb',
                'dotbelowcomb',
                'gravecomb',
                'hookabovecomb',
                'tildecomb',

                'acute',
                'base',
                'breve',
                'caron',
                'cedilla',
                'circumflex',
                'comma below',
                'corner leftwards',
                'diaeresis',
                'dialytika',
                'dialytika and tonos',
                'dot above',
                'double acute',
                'grave',
                'hamza above',
                'hamza below',
                'hook',
                'hook symbol',
                'horn',
                'macron',
                'madda above',
                'middle dot',
                'ogonek',
                'rays',
                'ring above',
                'ring above and acute',
                'stroke',
                'stroke and acute',
                'tilde',
                'tonos',
                'upturn',

                 )
        if glyph.name in names:
            return True
        '''
        Look for variations like 'breve.cap' or 'breve.cyr'.
        '''
        if '.' in glyph.name[1:]:
            shortName = glyph.name[:glyph.name.index('.')]
            if shortName in names:
                return True
        return False

    def subrenderGlyphContours(self, tfsSvg, contours, strokeColor, addPoints=True):
        from tfs.common.TFSSvg import TFSSvgPath
        ON_POINT_COLOR = 0x7f7f7f7f
        CONTROL_POINT_COLOR = 0x7fafafaf
        for contour in contours:
#            tfsSvg.addItem(TFSSvgPath(contour).addStroke(strokeColor, 2).addPointHighlights(ON_POINT_COLOR, CONTROL_POINT_COLOR))

            svgPath = TFSSvgPath(contour).addStroke(strokeColor, 2)
            if addPoints:
                svgPath.addPointHighlights(ON_POINT_COLOR, CONTROL_POINT_COLOR)
            tfsSvg.addItem(svgPath)


    def renderSvgScene(self,
                       filename,
                       pathTuples,
                       rawPathTuples = None,
                       hGuidelines=None):
        from tfs.common.TFSSvg import TFSSvg, TFSSvgPath
        if filename is None:
            dstFile = filename
        else:
            filename = '%s.svg' % ( filename, )
            dstFile = os.path.abspath(os.path.join(self.svg_folder, filename))

        CANVAS_BACKGROUND_COLOR = 0xffffffff
        CANVAS_BORDER_COLOR = 0x07fbfbfbf
        tfsSvg = TFSSvg().withBackground(CANVAS_BACKGROUND_COLOR).withBorder(CANVAS_BORDER_COLOR)

    #    if pathTuples:
        for color, contours in pathTuples:
            self.subrenderGlyphContours(tfsSvg, contours, color)
        if rawPathTuples is not None:
            for color, contours in rawPathTuples:
                self.subrenderGlyphContours(tfsSvg, contours, color, addPoints=False)

        if hGuidelines:
            for hGuideline in hGuidelines:
                p0 = TFSPoint(hGuideline, self.dstUfoFont.info.descender)
                p1 = TFSPoint(hGuideline, self.dstUfoFont.info.ascender)
                GUIDELINE_COLOR = 0x7fdfdfdf
                tfsSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

        vGuidelines = ( 0,
                        self.dstUfoFont.info.ascender,
                        self.dstUfoFont.info.descender,
                        )
        if vGuidelines:
            minmax = None
            allPathTuples = pathTuples
            if rawPathTuples is not None:
                allPathTuples = allPathTuples + rawPathTuples
            for color, contours in allPathTuples:
                minmax = minmaxMerge(minmax, minmaxPaths(contours))

            for vGuideline in vGuidelines:
                p0 = TFSPoint(0, vGuideline)
                p1 = TFSPoint(minmax.maxX, vGuideline)
                GUIDELINE_COLOR = 0x7fdfdfdf
                tfsSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

        SVG_HEIGHT = 400
        SVG_MAX_WIDTH = 800
        self.timing.mark('renderSvgScene.0')
        svgdata = tfsSvg.renderToFile(dstFile, margin=10, height=SVG_HEIGHT, maxWidth=SVG_MAX_WIDTH, timing=self.timing)
        self.timing.mark('renderSvgScene.1')
        if filename is not None:
            return filename
        else:
            return svgdata


    def getSrcGlyphContours(self, ufoglyph):
#        ufoglyph = self.srcUfoFont.getGlyphByName(ufoglyph.name)
#        if ufoglyph is None:
#            return None
        if ufoglyph.name in self.srcContoursCache:
            return self.srcContoursCache[ufoglyph.name]
        contours = ufoglyph.getContours()
        self.srcContoursCache[ufoglyph.name] = contours
        return contours


    def getGlyphContours(self, ufoglyph):
        if ufoglyph.name in self.dstContoursCache:
            return self.dstContoursCache[ufoglyph.name]
        contours = ufoglyph.getContours()
        self.dstContoursCache[ufoglyph.name] = contours
        return contours


    def getGlyphPixels(self, ufoglyph):
        if ufoglyph.name in self.pixelsCache:
            return self.pixelsCache[ufoglyph.name]
        RASTERIZE_CELL_SIZE = self.precision
        pixels = self.rasterizeGlyph(ufoglyph, RASTERIZE_CELL_SIZE)
        if pixels is not None:
            pixels = self.padPixels(pixels, self.convertToPixelUnits(self.max_distance, RASTERIZE_CELL_SIZE))
        self.pixelsCache[ufoglyph.name] = pixels
        return pixels


    def dumpPixelBlock(self, name, pixels):
        if not pixels:
            print name, '[No pixels]'
            return
        print name, len(pixels), 'pixel rows'
        for row in pixels:
            buffer = []
            for pixel in row:
                buffer.append('1' if pixel else '0')
            print '\t', ''.join(buffer)
        print


    def padPixels(self, pixels, padding):
        hPadding = (False,) * padding
        rowLength = len(pixels[0]) + 2 * padding
        vPadding = (False,) * rowLength
        result = []
        for _ in xrange(padding):
            result.append(vPadding)
        for row in pixels:
            result.append(hPadding + tuple(row) + hPadding)
        for _ in xrange(padding):
            result.append(vPadding)
        return result

    def convertToPixelUnits(self, value, RASTERIZE_CELL_SIZE):
        return int(math.ceil(value / float(RASTERIZE_CELL_SIZE)))

    def inflatePixelBlock(self, pixels, radius, RASTERIZE_CELL_SIZE):
#        radius = 100

        maskScale = self.convertToPixelUnits(radius, RASTERIZE_CELL_SIZE)
        maskSize = 1 + 2 * maskScale
        mask = []
        for y in xrange(maskSize):
            maskRow = []
            for x in xrange(maskSize):
                xOffset = x - maskScale
                yOffset = y - maskScale
                xDiff = xOffset * RASTERIZE_CELL_SIZE
                yDiff = yOffset * RASTERIZE_CELL_SIZE
                maskValue = (radius * radius) > (xDiff * xDiff) + (yDiff * yDiff)
#                xDiff = x * RASTERIZE_CELL_SIZE - radius
#                yDiff = y * RASTERIZE_CELL_SIZE - radius
#                maskValue = (radius * radius) > (xDiff * xDiff) + (yDiff * yDiff)
#                print 'x', x, 'y', y, 'radius', radius, 'xDiff', xDiff, 'yDiff', yDiff, 'maskValue', maskValue
                maskRow.append(maskValue)
            mask.append(maskRow)



        result = []
        for row in pixels:
            result.append(list(row))

#        result = []
        for y1, row1 in enumerate(pixels):
            for x1, pixel1 in enumerate(row1):
                if not pixel1:
                    continue
                # Inflate pixel
                for y2, row2 in enumerate(mask):
                    for x2, pixel2 in enumerate(row2):
                        if not pixel2:
                            continue
                        x = x1 + x2 - maskScale
                        y = y1 + y2 - maskScale
                        if 0 <= y < len(result):
                            if 0 <= x < len(result[y]):
                                result[y][x] = True

        return result


    def rasterizeGlyph(self, ufoglyph, RASTERIZE_CELL_SIZE):
        if ufoglyph.name in self.rasterCache:
            return self.rasterCache[ufoglyph.name]
        pixels = ufoglyph.rasterize(cellSize=RASTERIZE_CELL_SIZE,
                                   xMin=self.minmax.minX,
                                   yMin=self.minmax.minY,
                                   xMax=self.minmax.maxX,
                                   yMax=self.minmax.maxY)
        self.rasterCache[ufoglyph.name] = pixels
        return pixels

#    def findMinAdvance(self, pixels0, pixels1, tolerancePixels=0):
    def findMinAdvance(self, pixels0, pixels1, intrusionTolerancePixels=0, minNonIntrusionCount=0):
        if len(pixels0) != len(pixels1):
            raise Exception('pixel heights do not match. %d != %d', len(pixels0), len(pixels1))

        def leftRowProfile(row):
            for index, pixel in enumerate(row):
                if pixel:
                    return index
            return None

        def rightRowProfile(row):
            for index, pixel in enumerate(reversed(row)):
                if pixel:
                    return len(row) - (1 + index)
            return None

        def makePixelProfile(pixels, func):
            result = []
            for row in pixels:
                result.append(func(row))
            return result

        profile0 = makePixelProfile(pixels0, rightRowProfile)
        profile1 = makePixelProfile(pixels1, leftRowProfile)

#        def makeRowProfile(row, func):
#            result = None
#            for index, pixel in enumerate(row):
#                if pixel:
#                    if result is not None:
#                        result = func(result, index)
#                    else:
#                        result = index
#            return result
#
#        def makePixelProfile(pixels, func):
#            result = []
#            for row in pixels:
#                result.append(makeRowProfile(row, func))
#            return result
#
#        profile0 = makePixelProfile(pixels0, max)
#        profile1 = makePixelProfile(pixels1, min)
#        print 'profile0', profile0
#        print 'profile1', profile1
        contactAdvance = None
        for edge0, edge1 in zip(profile0, profile1):
            if edge0 is None or edge1 is None:
                continue
            diff = 1 + edge0 - edge1
#            print 'diff', diff
#            print 'edge0, edge1', edge0, edge1, 'diff', diff
            if contactAdvance is None:
                contactAdvance = diff
            else:
                contactAdvance = max(contactAdvance, diff)

#        print 'contactAdvance', contactAdvance

        if contactAdvance is None or intrusionTolerancePixels == 0:
            return contactAdvance

        def getProfileOverlap(advance):
#            print
#            print 'getProfileOverlap'
            intrusionTotal = 0
            extrusionTotal = 0
            nonIntrusionCount = 0
            for edge0, edge1 in zip(profile0, profile1):
                if edge0 is None or edge1 is None:
                    continue
                diff = 1 + edge0 - edge1
                rowIntrusion = max(0, diff - advance)
                rowExtrusion = max(0, advance - diff)
#                print 'edge0, edge1', edge0, edge1, 'diff', diff, 'advance', advance, 'rowIntrusion', rowIntrusion, 'rowExtrusion', rowExtrusion
                intrusionTotal += rowIntrusion
                extrusionTotal += rowExtrusion
                if rowIntrusion <= 0:
                    nonIntrusionCount += 1
            return intrusionTotal, extrusionTotal, nonIntrusionCount


#        width0 = len(pixels0[0])
#        width1 = len(pixels1[0])
#        print 'contactAdvance', contactAdvance
#        print 'tolerancePixels', tolerancePixels
        offsetAdvance = contactAdvance
#        for offset in xrange(1, min(width0, width1)):
        for offset in xrange(1, contactAdvance + 1):
            advance = contactAdvance - offset
            intrusionTotal, extrusionTotal, nonIntrusionCount = getProfileOverlap(advance)
#            print 'intrusionTotal, extrusionTotal, nonIntrusionCount', intrusionTotal, extrusionTotal, nonIntrusionCount, 'intrusionTolerancePixels', intrusionTolerancePixels, 'minNonIntrusionCount', minNonIntrusionCount
            if intrusionTotal > extrusionTotal:
                return offsetAdvance
            if intrusionTotal > intrusionTolerancePixels:
                return offsetAdvance
            minNonIntrusionCount
            if nonIntrusionCount < minNonIntrusionCount:
                return offsetAdvance

#            overlapPixels = getProfileOverlap(advance)
##            print 'overlapPixels', overlapPixels
#            if overlapPixels > tolerancePixels:
#                return offsetAdvance

#            return offsetAdvance

            offsetAdvance = advance

        return offsetAdvance


    def findDisparities(self):

        disparities = []
        glyphs = self.dstUfoFont.getGlyphs()
#        total = len(glyphs) * len(glyphs)
#        count = 0
#        startTime = time.time()
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))
        for ufoglyph0 in glyphs:
            for ufoglyph1 in glyphs:
                key = (ufoglyph0.name,
                       ufoglyph1.name,)
                if key not in self.advanceMap:
                    continue

                disparity = TFSMap()
                disparity.dstUfoGlyph0 = ufoglyph0
                disparity.dstUfoGlyph1 = ufoglyph1

#                disparity.srcXAdvance = disparity.srcUfoGlyph0.xAdvance
                disparity.dstAdvance = int(round(self.advanceMap[key]))
                disparity.dstXAdvance = disparity.dstUfoGlyph0.xAdvance
                disparity.dstKerning = disparity.dstAdvance - disparity.dstXAdvance


                disparity.srcUfoGlyph0 = self.srcUfoFont.getGlyphByName(ufoglyph0.name)
                if disparity.srcUfoGlyph0 is None:
                    raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph0.name),
                                                                             str(ufoglyph0.unicode)))
                disparity.srcUfoGlyph1 = self.srcUfoFont.getGlyphByName(ufoglyph1.name)
                if disparity.srcUfoGlyph1 is None:
                    raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph1.name),
                                                                             str(ufoglyph1.unicode)))

                disparity.srcKerning = self.srcUfoFont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
                if disparity.srcKerning is None:
                    disparity.srcKerning = 0
                disparity.srcXAdvance = disparity.srcUfoGlyph0.xAdvance
                disparity.srcAdvance = disparity.srcUfoGlyph0.xAdvance + disparity.srcKerning


                disparity.srcContours0 = self.getSrcGlyphContours(disparity.srcUfoGlyph0)
                disparity.srcContours1 = self.getSrcGlyphContours(disparity.srcUfoGlyph1)

                disparity.srcMinmax0 = self.getSrcCachedValue('getCachedMinmax %s' % ufoglyph0.name, getCachedMinmax, disparity.srcContours0)
                disparity.srcMinmax1 = self.getSrcCachedValue('getCachedMinmax %s' % ufoglyph1.name, getCachedMinmax, disparity.srcContours1)
                disparity.srcOffset = disparity.srcAdvance + (-disparity.srcMinmax0.maxX) + (disparity.srcMinmax1.minX)

                disparity.dstContours0 = self.getGlyphContours(ufoglyph0)
                disparity.dstContours1 = self.getGlyphContours(ufoglyph1)
                disparity.dstMinmax0 = self.getDstCachedValue('getCachedMinmax %s' % ufoglyph0.name, getCachedMinmax, disparity.dstContours0)
                disparity.dstMinmax1 = self.getDstCachedValue('getCachedMinmax %s' % ufoglyph1.name, getCachedMinmax, disparity.dstContours1)
                disparity.dstOffset = disparity.dstAdvance + (-disparity.dstMinmax0.maxX) + (disparity.dstMinmax1.minX)

                disparity.offsetDifference = abs(disparity.srcOffset - disparity.dstOffset)
                disparity.advanceDifference = abs(disparity.dstAdvance - disparity.srcAdvance)

                if disparity.offsetDifference != 0:
                    disparities.append(disparity)

        def compareDisparities(disparity0, disparity1):
            return cmp(disparity0.offsetDifference, disparity1.offsetDifference)

        disparities.sort(compareDisparities, reverse=True)
        return disparities


    def logDisparities(self):

        renderLog = self.log_dst is not None
        if not renderLog:
            return

        disparities = self.findDisparities()

        '''
        We're only interested in the top 100 disparities.
        '''
        disparities = disparities[:100]

        def getDisparityFilename(index):
            return 'disparity-%d.html' % index

        disparityLinkMaps = []
        for index, disparity in enumerate(disparities):
            disparityLinkMaps.append({ 'filename': getDisparityFilename(index),
                                      'name': str(index + 1),
                                      })

        for index, disparity in enumerate(disparities):

            filenamePrefix = 'disparity-%d' % index
            phase = 0
            oldAdvanceSvg = self.renderSvgScene(None,
                                             pathTuples = (
                                                           ( 0x7f7faf7f, disparity.srcContours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(disparity.srcAdvance, 0)) for contour in disparity.srcContours1], ),
                                                           ),
                                             hGuidelines = ( disparity.srcAdvance, ) )
            phase += 1

            newAdvanceSvg = self.renderSvgScene(None,
                                             pathTuples = (
                                                           ( 0x7f7faf7f, disparity.dstContours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(disparity.dstAdvance, 0)) for contour in disparity.dstContours1], ),
                                                           ),
                                             hGuidelines = ( disparity.dstAdvance, ) )
            phase += 1

            import tfs.common.TFSProject as TFSProject
            mustache_template_file = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'autokern_disparity_template.txt'))
            with open(mustache_template_file, 'rt') as f:
                mustache_template = f.read()

            pageTitle = u'Autokern Disparity: %s vs. %s' % ( formatGlyphName(disparity.dstUfoGlyph0),
                                                                   formatGlyphName(disparity.dstUfoGlyph1), )

            def formatEmScalar(value):
                return '%0.3f em' % (value / float(self.units_per_em))

            def formatGlyphMap(glyph, srcMinmax, dstMinmax):
                return {
                           'glyphName': formatGlyphName(glyph),
                           'srcMinX': formatEmScalar(srcMinmax.minX),
                           'srcMaxX': formatEmScalar(srcMinmax.maxX),
                           'dstMinX': formatEmScalar(dstMinmax.minX),
                           'dstMaxX': formatEmScalar(dstMinmax.maxX),
                        }

            mustacheMap = {
                           'kerningLogFilename': self.getKerningPairHtmlFilename(disparity.dstUfoGlyph0,
                                                                                 disparity.dstUfoGlyph1),
                           'pageTitle': pageTitle,
                           'minmax0': disparity.dstMinmax0,
                           'minmax1': disparity.dstMinmax1,
                           'dstAdvance': formatEmScalar(disparity.dstAdvance),
                           'srcAdvance': formatEmScalar(disparity.srcAdvance),
                           'advanceDifference': formatEmScalar(disparity.advanceDifference),
                           'srcOffset': formatEmScalar(disparity.srcOffset),
                           'dstOffset': formatEmScalar(disparity.dstOffset),
                           'offsetDifference': formatEmScalar(disparity.offsetDifference),
                           'srcKerning': formatEmScalar(disparity.srcKerning),
                           'srcXAdvance': formatEmScalar(disparity.srcXAdvance),
                           'dstXAdvance': formatEmScalar(disparity.dstXAdvance),
                           'dstKerning': formatEmScalar(disparity.dstKerning),

                           'min_distance': formatEmScalar(self.min_distance),
                           'max_distance': formatEmScalar(self.max_distance),

                           'oldAdvanceSvg': oldAdvanceSvg,
                           'newAdvanceSvg': newAdvanceSvg,

                           'glyph0': formatGlyphName(disparity.dstUfoGlyph0),
                           'glyph1': formatGlyphName(disparity.dstUfoGlyph1),

                           'glyphMaps': ( formatGlyphMap(disparity.dstUfoGlyph0, disparity.srcMinmax0, disparity.dstMinmax0),
                                          formatGlyphMap(disparity.dstUfoGlyph1, disparity.srcMinmax1, disparity.dstMinmax1),
                                          ),
                           'disparityLinkMaps': disparityLinkMaps,
                           'firstDisparityLink': getDisparityFilename(0),
                           'lastDisparityLink': getDisparityFilename(len(disparities) - 1),
                           }
            if index > 0:
                mustacheMap['prevDisparityLink'] = {'filename': getDisparityFilename(index - 1), }
            if index + 1 < len(disparities):
                mustacheMap['nextDisparityLink'] = {'filename': getDisparityFilename(index + 1), }

            for key in ( 'ascender',
                         'descender',
                        ):
                mustacheMap[key] = formatEmScalar(getattr(self.dstUfoFont.info, key))

            for key in (
                         'unitsPerEm',
                         'familyName',
                         'styleName',
                         'fullName',
                         'fontName',
                        ):
                mustacheMap[key] = getattr(self.dstUfoFont.info, key)

            import pystache
            logHtml = pystache.render(mustache_template, mustacheMap)

            logFilename = getDisparityFilename(index)
            logFile = os.path.abspath(os.path.join(self.html_folder, logFilename))
            with open(logFile, 'wt') as f:
                # TODO: explicitly encode unicode
                f.write(logHtml)

#    def convertToPixelUnits(self, value):
#        RASTERIZE_CELL_SIZE = self.precision
#        return int(math.ceil(value / float(RASTERIZE_CELL_SIZE)))

    def getDstCachedValue(self, key, func, *argv):
        if key in self.dstValueCache:
            return self.dstValueCache[key]
        result = func(*argv)
        self.dstValueCache[key] = result
        return result

    def getSrcCachedValue(self, key, func, *argv):
        if key in self.srcValueCache:
            return self.srcValueCache[key]
        result = func(*argv)
        self.srcValueCache[key] = result
        return result


    def getFilenamePrefixPair(self, prefix, ufoglyph0, ufoglyph1):
        return '%s-%s-%s' % ( prefix,
                              formatUnicode(ufoglyph0.unicode),
                              formatUnicode(ufoglyph1.unicode), )

    def getKerningPairFilenamePrefix(self, ufoglyph0, ufoglyph1):
        return self.getFilenamePrefixPair('autokern', ufoglyph0, ufoglyph1)

    def getKerningPairHtmlFilename(self, ufoglyph0, ufoglyph1):
        return self.getKerningPairFilenamePrefix(ufoglyph0, ufoglyph1) + '.html'


    def convertProfileToLogPaths(self, profile, isLeft, offset=None):
        minYunits = int(math.floor((self.allGlyphsMinY - self.max_distance) / float(self.precision)))

        result = []

        def addPath(points):
            firstPoint = points[0]
            lastPoint = points[-1]
            if isLeft:
                extraX = min(firstPoint.x, lastPoint.x)
                extraX += -10
            else:
                extraX = max(firstPoint.x, lastPoint.x)
                extraX += +10

            points.append(TFSPoint(extraX, lastPoint.y))
            points.append(TFSPoint(extraX, firstPoint.y))

            if offset is not None:
                points = [point.plus(offset) for point in points]

            result.append(concatenatePath(True, *points))

        currentPoints = []
        for index, xValue in enumerate(profile):
            if xValue is None:
                if len(currentPoints) > 0:
                    '''
                    Tie off path
                    '''
                    addPath(currentPoints)
                    currentPoints = []
            else:
                yValue = self.precision * (index + minYunits)
#                print 'convertProfileToLogPaths point', 'yValue', yValue, 'precision', self.precision, 'index', index, 'minYunits', minYunits, 'xValue', xValue
                currentPoints.append(TFSPoint(xValue, yValue))

        if len(currentPoints) > 0:
            '''
            Tie off path
            '''
            addPath(currentPoints)

        return result


    def makeProfile(self, func, paths=None, segments=None, debug=False):
        maxYunits = int(math.ceil((self.allGlyphsMaxY + self.max_distance) / float(self.precision)))
        minYunits = int(math.floor((self.allGlyphsMinY - self.max_distance) / float(self.precision)))
        yHeightUnits = 1 + maxYunits - minYunits

#        print 'maxYunits', maxYunits
#        print 'minYunits', minYunits
#        print 'self.allGlyphsMinY', self.allGlyphsMinY
#        print 'self.allGlyphsMaxY', self.allGlyphsMaxY
#        print 'self.precision', self.precision
#        print 'yHeightUnits', yHeightUnits

        profile = list((None,) * yHeightUnits)

        # combine paths and segments parameters
        allSegments = []
        if segments is not None:
            allSegments.extend(segments)
        if paths is not None:
            for path in paths:
                allSegments.extend(path.segments)

        def addProfilePoint(yIndex, xValue):
            if yIndex < 0 or yIndex >= len(profile):
                raise Exception('Invalid yIndex: %d' % yIndex)
#                print 'yIndex', yIndex, 'len(profile)', len(profile)
            if profile[yIndex] is None:
                profile[yIndex] = xValue
            else:
                profile[yIndex] = func(profile[yIndex], xValue)

        def addSegmentSection(point0, point1):
            '''
            Given two endpoints of a straight segment, interpolate x values along the y-axis.

            Not very precise; rounds y value of endpoint locations.
            Acceptable; as precise as "precision".
            '''
            y0u = int(round(point0.y / float(self.precision)))
            y1u = int(round(point1.y / float(self.precision)))
#            y0u = int(round((point0.y - self.max_distance) / float(self.precision)))
#            y1u = int(round((point1.y - self.max_distance) / float(self.precision)))

            if debug:
                print 'addSegmentSection', point0.description(), point1.description(), 'y0u', y0u, 'y1u', y1u

            if y0u == y1u:
                yIndex = y0u - minYunits
                addProfilePoint(yIndex, func(point0.x, point1.x))
                return

            if y0u < y1u:
                minYIndex = y0u - minYunits
                maxYIndex = y1u - minYunits
                minXValue = point0.x
                maxXValue = point1.x
            else:
                minYIndex = y1u - minYunits
                maxYIndex = y0u - minYunits
                minXValue = point1.x
                maxXValue = point0.x

            for yIndexOffset in xrange(1 + maxYIndex - minYIndex):
                yIndex = minYIndex + yIndexOffset
                xValue = minXValue + (maxXValue - minXValue) * yIndexOffset / float(maxYIndex - minYIndex)
                addProfilePoint(yIndex, xValue)

        for segment in allSegments:
            if debug:
                print 'segment', segment.description()
            if segment.isStraight():
                addSegmentSection(segment.startPoint(), segment.endPoint())
            else:
                segmentPoints = segment.evaluateRangeWithPrecision(AUTOKERN_SEGMENT_PRECISION)
                lastPoint = None
                for point in segmentPoints:
                    if lastPoint is not None:
                        addSegmentSection(lastPoint, point)
                    lastPoint = point

        return profile


    def findMinProfileAdvance(self, profile0, profile1, intrusionToleranceArea=0, minNonIntrusionRowCount=0):
        if len(profile0) != len(profile1):
            raise Exception('profile heights do not match. %d != %d', len(profile0), len(profile1))

        contactAdvance = None
        for edge0, edge1 in itertools.izip(profile0, profile1):
            if edge0 is None or edge1 is None:
                continue
            diff = 1 + edge0 - edge1
            if contactAdvance is None:
                contactAdvance = diff
            else:
                contactAdvance = max(contactAdvance, diff)

        if contactAdvance is None or intrusionToleranceArea == 0:
            return contactAdvance

        def getProfileOverlap(advance):
#            print
#            print 'getProfileOverlap'
            intrusionTotal = 0
            extrusionTotal = 0
            nonIntrusionRowCount = 0
            for edge0, edge1 in itertools.izip(profile0, profile1):
                if edge0 is None or edge1 is None:
                    continue
                diff = 1 + edge0 - edge1
                rowIntrusion = max(0, diff - advance)
                rowExtrusion = max(0, advance - diff)
#                print 'edge0, edge1', edge0, edge1, 'diff', diff, 'advance', advance, 'rowIntrusion', rowIntrusion, 'rowExtrusion', rowExtrusion
                intrusionTotal += rowIntrusion
                extrusionTotal += rowExtrusion
                if rowIntrusion <= 0:
                    nonIntrusionRowCount += 1
            return intrusionTotal, extrusionTotal, nonIntrusionRowCount


#        print 'contactAdvance', contactAdvance, type(contactAdvance)
        contactAdvance = int(round(contactAdvance))
#        print 'tolerancePixels', tolerancePixels
        offsetAdvance = contactAdvance
        for offset in xrange(1, contactAdvance + 1):
            advance = contactAdvance - offset
            intrusionTotal, extrusionTotal, nonIntrusionRowCount = getProfileOverlap(advance)
#            print 'intrusionTotal, extrusionTotal, nonIntrusionCount', intrusionTotal, extrusionTotal, nonIntrusionCount, 'intrusionTolerancePixels', intrusionTolerancePixels, 'minNonIntrusionCount', minNonIntrusionCount
            if intrusionTotal > extrusionTotal:
                return offsetAdvance
            if intrusionTotal > intrusionToleranceArea:
                return offsetAdvance
            if nonIntrusionRowCount < minNonIntrusionRowCount:
                return offsetAdvance

            offsetAdvance = advance

        return offsetAdvance


    def inflateSegmentLeft(self, segment, hDistance, vDistance=None):
        '''
        '''
        if vDistance is None:
            vDistance = hDistance

        if segment.startVector().length() == 0:
            startTangent = segment.naiveEndpointTangent()
        else:
            startTangent = segment.startTangent()

        if segment.endVector().length() == 0:
            endTangent = segment.naiveEndpointTangent()
        else:
            endTangent = segment.endTangent()

#        if (segment.startVector().length() == 0 or
#            segment.endVector().length() == 0):
#            raise Exception('Cannot flate a segment without valid tangents: ' + segment.description())


        p0 = segment.startPoint()
        p1 = segment.endPoint()
#        startTangent = segment.startTangent()

        if len(segment) == 2:
            offset = scaleVectorHV(startTangent.rotate(math.pi * 0.5), hDistance, vDistance)
            p0 = p0.plus(offset)
            p1 = p1.plus(offset)
            newPoints = (p0, p1)
        elif len(segment) == 3:
#            endTangent = segment.endTangent()
            startOffset = scaleVectorHV(startTangent.rotate(math.pi * 0.5), hDistance, vDistance)
            endOffset = scaleVectorHV(endTangent.rotate(math.pi * 0.5), hDistance, vDistance)
            p0 = p0.plus(startOffset)
            p1 = p1.plus(endOffset)
            cp0 = TFSIntersection.intersectionWithTangents(p0, startTangent, p1, endTangent.invert())
            newPoints = (p0, cp0, p1)
        elif len(segment) == 4:
#            endTangent = segment.endTangent()
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
#            print e.message, e
            '''
            flating a segment can result in an empty or otherwise invalid segment.
            In fact, this will happen often since we'll be deflating previously
            inflated rounding curves.
            That's fine; ignore them.
            '''
            return None


    def makeInflatedProfile(self, func, contours, radius):
        segments = []

        def addEndpointRounding(point):
            circle = TFSOval(point, hRadius=radius, vRadius=radius)
            segments.extend(circle.createPath().segments)

        for contour in contours:
            contour = orientClosedPathClockwise(contour)
            for segment in contour:
                addEndpointRounding(segment.startPoint())
                addEndpointRounding(segment.endPoint())
                inflatedSegment = self.inflateSegmentLeft(segment, radius)
                if inflatedSegment is not None:
                    segments.append(inflatedSegment)

        return self.makeProfile(func, segments=segments)


    def processKerningPair(self, ufoglyph0, ufoglyph1):
        '''
        returns True iff pair is kerned.

        TODO: handle empty glyphs with no contours
        '''

        self.timing.mark('processKerningPair.0.')
#        print 'processKerningPair', ufoglyph0.name, ufoglyph1.name

        if self.pairsToKern is not None:
            if (ufoglyph0.name, ufoglyph1.name) not in self.pairsToKern:
                return False
        elif self.glyphsToKern is not None:
            if ufoglyph0.name not in self.glyphsToKern:
                return False
            if ufoglyph1.name not in self.glyphsToKern:
                return False
        elif self.isCombiningGlyph(ufoglyph0) or self.isCombiningGlyph(ufoglyph1):
            return False

#        print 'processKerningPair'

        debugKerning = True
        debugKerning = False

        renderLog = self.log_dst is not None

        RASTERIZE_CELL_SIZE = self.precision

        contours0 = self.getGlyphContours(ufoglyph0)
        contours1 = self.getGlyphContours(ufoglyph1)
        if (not contours0) or (not contours1):
            return False

        self.timing.mark('processKerningPair.01')

        def getRightContour():
#            return self.makeProfile(func=max, paths=contours0, debug=True)
            return self.makeProfile(func=max, paths=contours0)
        profile0 = self.getDstCachedValue('getRightContour %s' % ufoglyph0.name, getRightContour)

        self.timing.mark('processKerningPair.011')

        def getLeftContour():
            return self.makeProfile(func=min, paths=contours1)
        profile1 = self.getDstCachedValue('getLeftContour %s' % ufoglyph1.name, getLeftContour)

        self.timing.mark('processKerningPair.012')

        def getLeftContourInflateMin():
            return self.makeInflatedProfile(func=min, contours=contours1, radius=self.min_distance)
        profileMin1 = self.getDstCachedValue('getLeftContourInflateMin %s' % ufoglyph1.name, getLeftContourInflateMin)

        self.timing.mark('processKerningPair.013')

        def getLeftContourInflateMax():
            return self.makeInflatedProfile(func=min, contours=contours1, radius=self.max_distance)
        profileMax1 = self.getDstCachedValue('getLeftContourInflateMax %s' % ufoglyph1.name, getLeftContourInflateMax)

        self.timing.mark('processKerningPair.014')

        minDistanceAdvance = self.findMinProfileAdvance(profile0, profileMin1)
        self.timing.mark('processKerningPair.021')
        if debugKerning:
            print 'minDistanceAdvance', minDistanceAdvance

        intrusion_tolerance_area = int(round((self.intrusion_tolerance * self.units_per_em) / float(RASTERIZE_CELL_SIZE * RASTERIZE_CELL_SIZE)))
        if debugKerning:
            print 'intrusion_tolerance', self.intrusion_tolerance, 'intrusion_tolerance_area', intrusion_tolerance_area

        min_non_intrusion_row_count = int(round(float(self.min_non_intrusion) / self.precision))
        if debugKerning:
            print 'min_non_intrusion', self.min_non_intrusion, 'min_non_intrusion_row_count', min_non_intrusion_row_count

        intrudingAdvance = self.findMinProfileAdvance(profile0, profileMax1,
                                                      intrusionToleranceArea=intrusion_tolerance_area,
                                                      minNonIntrusionRowCount=min_non_intrusion_row_count)
        self.timing.mark('processKerningPair.023')
        if debugKerning:
            print 'intrudingAdvance', intrudingAdvance

        minmax0 = self.getDstCachedValue('getCachedMinmax %s' % ufoglyph0.name, getCachedMinmax, contours0)
        minmax1 = self.getDstCachedValue('getCachedMinmax %s' % ufoglyph1.name, getCachedMinmax, contours1)

        self.timing.mark('processKerningPair.02')

        '''
        Now combine results into the final advance value.
        1. Start with the "intruding advance."
        2. Make sure advance is at least the "minimum advance."
        '''

#        if minDistanceAdvance is None:
#            advance = minmax0.maxX + self.min_distance - minmax1.minX
#            advance = minDistanceAdvance

        if minDistanceAdvance is None and intrudingAdvance is None:
            '''
            If no collisions between the glyph profiles, use x-extrema
            plus the min_distance argument.

            TODO: should we use the max_distance instead?
            '''
            advance = minmax0.maxX + self.min_distance - minmax1.minX
#            print '!!!', '.1', minmax0.maxX, self.min_distance, minmax1.minX
#            print '!!!', '.1', advance, minDistanceAdvance, intrudingAdvance
        elif minDistanceAdvance is None:
            advance = intrudingAdvance
#            print '!!!', '.2', advance, minDistanceAdvance, intrudingAdvance
        elif intrudingAdvance is None:
            advance = minDistanceAdvance
#            print '!!!', '.3', advance, minDistanceAdvance, intrudingAdvance
        else:
            advance = max(minDistanceAdvance, intrudingAdvance)
#            print '!!!', '.4', advance, minDistanceAdvance, intrudingAdvance

#        advance = max(minDistanceAdvance, intrudingAdvance)

        '''
        3. Make sure the "x-extrema overlap" is not greater than the "max x-extrema overlap".
        '''
#        print '!!!', 'minDistanceAdvance, intrudingAdvance', minDistanceAdvance, intrudingAdvance
#        print '!!!', 'minmax0.maxX, minmax1.minX, advance', minmax0.maxX, minmax1.minX, advance
        x_extrema_overlap = minmax0.maxX - (minmax1.minX + advance)
        if x_extrema_overlap > self.max_x_extrema_overlap:
#            print
#            print 'overlap', ufoglyph0.name, ufoglyph1.name
#            print 'minmax0.maxX, minmax1.minX', minmax0.maxX, minmax1.minX, 'advance', advance
#            print 'x_extrema_overlap, self.max_x_extrema_overlap', x_extrema_overlap, self.max_x_extrema_overlap
#            print 'advance.0', advance
            advance += x_extrema_overlap - self.max_x_extrema_overlap
#            print 'advance.1', advance

#        print 'advanceLimit', advanceLimit, 'advance', advance


        self.advanceMap[(ufoglyph0.name,
                         ufoglyph1.name,)] = advance

#        if ufoglyph0.name == 'A' or ufoglyph1.name == 'A':
#            print '\t', 'result', ufoglyph0.name, ufoglyph1.name, advance, 'spacing', advance - ufoglyph0.xAdvance
#        print '\t', 'result', ufoglyph0.name, ufoglyph1.name, advance, 'spacing', advance - ufoglyph0.xAdvance

        if debugKerning:
            print '\t', ufoglyph0.unicode, ufoglyph1.unicode, advance
#        import sys
#        sys.exit(0)

        self.timing.mark('processKerningPair.5')

        if renderLog:
#            from tfs.common.TFSSvg import *
#            filenamePrefix = self.getKerningPairFilenamePrefix(ufoglyph0, ufoglyph1)
#            phase = 1

            srcufoglyph0 = self.srcUfoFont.getGlyphByName(ufoglyph0.name)
            if srcufoglyph0 is None:
                raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph0.name),
                                                                         str(ufoglyph0.unicode)))
            srcufoglyph1 = self.srcUfoFont.getGlyphByName(ufoglyph1.name)
            if srcufoglyph1 is None:
                raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph1.name),
                                                                         str(ufoglyph1.unicode)))

            srcContours0 = self.getSrcGlyphContours(srcufoglyph0)
            srcContours1 = self.getSrcGlyphContours(srcufoglyph1)
            srcKerning = self.dstUfoFont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
            if srcKerning is None:
                srcKerning = 0
            srcAdvance = srcufoglyph0.xAdvance + srcKerning

            srcminmax0 = self.getSrcCachedValue('getCachedMinmax %s' % ufoglyph0.name, getCachedMinmax, srcContours0)
            srcminmax1 = self.getSrcCachedValue('getCachedMinmax %s' % ufoglyph1.name, getCachedMinmax, srcContours1)

            srcAdvanceAdjusted = srcAdvance + (-srcminmax0.minX) + srcminmax1.minX
            advanceAdjusted = advance + (-minmax0.minX) + minmax1.minX

            srcSpacingSvg = self.renderSvgScene(None,
#                                                filenamePrefix + '-src-spacing',
                                             pathTuples = (
                                                           ( 0x7f7faf7f, srcContours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(srcAdvance, 0)) for contour in srcContours1], ),
                                                           ),
                                             hGuidelines = ( srcAdvance, ) )
#            phase += 1

            self.timing.mark('processKerningPair.6')

            # -----------

            profilePaths0 = self.convertProfileToLogPaths(profile0, isLeft=True)
#            profilePaths1 = self.convertProfileToLogPaths(profile1, isLeft=False, offset=TFSPoint(advance, 0))
#            profileMinPaths1 = self.convertProfileToLogPaths(profileMin1, isLeft=False, offset=TFSPoint(advance, 0))
            profileMaxPaths1 = self.convertProfileToLogPaths(profileMax1, isLeft=False)

            # -----------

            contactAdvance = self.findMinProfileAdvance(profile0, profile1)
            self.timing.mark('processKerningPair.020')
            if debugKerning:
                print 'contactAdvance', contactAdvance

            contactAdvanceSvg = self.renderSvgScene(None,
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(contactAdvance, 0)) for contour in contours1], ),
                                                           ),
                                             rawPathTuples = (
                                                           ( 0xafff7faf, profilePaths0, ),
                                                           ( 0xafaf7fff, self.convertProfileToLogPaths(profile1, isLeft=False, offset=TFSPoint(contactAdvance, 0)), ),
                                                           ),
                                             hGuidelines = ( contactAdvance, ) )

            # -----------

            minDistanceAdvanceSvg = self.renderSvgScene(None,
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(minDistanceAdvance, 0)) for contour in contours1], ),
                                                           ),
                                             rawPathTuples = (
                                                           ( 0xafff7faf, profilePaths0, ),
                                                           ( 0xafaf7fff, self.convertProfileToLogPaths(profileMin1, isLeft=False, offset=TFSPoint(minDistanceAdvance, 0)), ),
                                                           ),
                                             hGuidelines = ( minDistanceAdvance, ) )

            # -----------

            maxDistanceAdvance = self.findMinProfileAdvance(profile0, profileMax1)
            self.timing.mark('processKerningPair.022')
            if debugKerning:
                print 'maxDistanceAdvance', maxDistanceAdvance

            maxDistanceAdvanceSvg = self.renderSvgScene(None,
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(maxDistanceAdvance, 0)) for contour in contours1], ),
                                                           ),
                                             rawPathTuples = (
                                                           ( 0xafff7faf, profilePaths0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(maxDistanceAdvance, 0)) for contour in profileMaxPaths1], ),
                                                           ),
                                             hGuidelines = ( maxDistanceAdvance, ) )

            # -----------

            intrudingAdvanceSvg = self.renderSvgScene(None,
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(intrudingAdvance, 0)) for contour in contours1], ),
                                                           ),
                                             rawPathTuples = (
                                                           ( 0xafff7faf, profilePaths0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(intrudingAdvance, 0)) for contour in profileMaxPaths1], ),
                                                           ),
                                             hGuidelines = ( intrudingAdvance, ) )

            # -----------

            finalAdvanceSvg = self.renderSvgScene(None,
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(advance, 0)) for contour in contours1], ),
                                                           ),
                                             rawPathTuples = (
                                                           ( 0xafff7faf, profilePaths0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(advance, 0)) for contour in profileMaxPaths1], ),
                                                           ),
                                             hGuidelines = ( advance, ) )

            # -----------


            self.timing.mark('processKerningPair.8')

            import tfs.common.TFSProject as TFSProject
            mustache_template_file = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'autokern_pair_pixel_template.txt'))
            with open(mustache_template_file, 'rt') as f:
                mustache_template = f.read()

            pageTitle = u'Autokern Log: %s vs. %s' % ( formatGlyphName(ufoglyph0),
                                                         formatGlyphName(ufoglyph1), )

            def formatEmScalar(value):
                return '%0.3f em' % (value / float(self.units_per_em))

            def formatGlyphMap(glyph, glyphMinmax):
                return {
                           'glyphName': formatGlyphName(glyph),
                           'minX': formatEmScalar(glyphMinmax.minX),
                           'maxX': formatEmScalar(glyphMinmax.maxX),
                           'minY': formatEmScalar(glyphMinmax.minY),
                           'maxY': formatEmScalar(glyphMinmax.maxY),
                        }

            x_extrema_overlap = minmax0.maxX - (minmax1.minX + advance)

            mustacheMap = {
                           'pageTitle': pageTitle,
                           'minmax0': minmax0,
                           'minmax1': minmax1,
#                           'naiveSpacing': formatEmScalar(naiveSpacing),
#                           'minDistanceSpacing': formatEmScalar(minDistanceSpacing),
#                           'roundingSpacing': formatEmScalar(roundingSpacing),
                           'contactAdvance': formatEmScalar(contactAdvance),
#                           'naiveAdvance': formatEmScalar(naiveAdvance),
                           'minDistanceAdvance': formatEmScalar(minDistanceAdvance),
                           'maxDistanceAdvance': formatEmScalar(maxDistanceAdvance),
                           'intrudingAdvance': formatEmScalar(intrudingAdvance),
                           'advance': formatEmScalar(advance),
                           'srcAdvance': formatEmScalar(srcAdvance),
                           'srcAdvanceAdjusted': formatEmScalar(srcAdvanceAdjusted),
                           'advanceAdjusted': formatEmScalar(advanceAdjusted),
                           'x_extrema_overlap': formatEmScalar(x_extrema_overlap),
                           'max_x_extrema_overlap': formatEmScalar(self.max_x_extrema_overlap),

#                           'maxAdvance': formatEmScalar(maxAdvance),
                           'min_distance': formatEmScalar(self.min_distance),
                           'max_distance': formatEmScalar(self.max_distance),
#                           'intrusion_tolerance': formatEmScalar(self.intrusion_tolerance),
                           'min_non_intrusion': formatEmScalar(self.min_non_intrusion),
#                           'rounding': formatEmScalar(self.rounding),

                           'srcSpacingSvg': srcSpacingSvg,

                           'contactAdvanceSvg': contactAdvanceSvg,
#                           'minAdvanceSvg': minAdvanceSvg,
#                           'maxAdvanceSvg': maxAdvanceSvg,
                           'minDistanceAdvanceSvg': minDistanceAdvanceSvg,
                           'maxDistanceAdvanceSvg': maxDistanceAdvanceSvg,
                           'intrudingAdvanceSvg': intrudingAdvanceSvg,
                           'finalAdvanceSvg': finalAdvanceSvg,

#                           'naiveSpacingSvg': naiveSpacingSvg,
#                           'minDistanceSpacingSvg': minDistanceSpacingSvg,
#                           'maxDistanceSpacingSvg': maxDistanceSpacingSvg,
#                           'intrudingAdvanceSpacingSvg': intrudingAdvanceSpacingSvg,
#                           'finalAdvanceSpacingSvg': finalAdvanceSpacingSvg,
#                           'profileDebugSvg': profileDebugSvg,

#                           'roundingSpacingSvg': roundingSpacingSvg,

                           'glyph0': formatGlyphName(ufoglyph0),
                           'glyph1': formatGlyphName(ufoglyph1),

                           'glyphMaps': ( formatGlyphMap(ufoglyph0, minmax0),
                                          formatGlyphMap(ufoglyph1, minmax1),
                                          )
                           }

            for key in ( 'ascender',
                         'descender',
                        ):
                mustacheMap[key] = formatEmScalar(getattr(self.dstUfoFont.info, key))

            for key in (
                         'unitsPerEm',
                         'familyName',
                         'styleName',
                         'fullName',
                         'fontName',
                        ):
                mustacheMap[key] = getattr(self.dstUfoFont.info, key)

            import pystache
            logHtml = pystache.render(mustache_template, mustacheMap)

            logFilename = self.getKerningPairHtmlFilename(ufoglyph0, ufoglyph1)
            logFile = os.path.abspath(os.path.join(self.html_folder, logFilename))
            with open(logFile, 'wt') as f:
                # TODO: explicitly encode unicode
                f.write(logHtml)

#            import sys
#            sys.exit(0)

        self.timing.mark('processKerningPair.9')

        return True


    def processAllKerningPairs(self):

        if USE_CACHED_KERNING_MAP:
            import tfs.common.TFSProject as TFSProject
            tmpFolder = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'tmp'))
            advanceMapYamlFile = os.path.abspath(os.path.join(tmpFolder, 'advanceMap.yaml'))
            if os.path.exists(advanceMapYamlFile):
                with open(advanceMapYamlFile, 'rt') as f:
                    yamldata = f.read()
                    self.advanceMap = yaml.load(yamldata)
                    return

        glyphs = self.dstUfoFont.getGlyphs()
        total = len(glyphs) * len(glyphs)
        count = 0
        startTime = time.time()
        lastLog = None
        firstKernedName = None
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))
        for ufoglyph0 in glyphs:
            for ufoglyph1 in glyphs:

                pairKerned = self.processKerningPair(ufoglyph0, ufoglyph1)

                count += 1

                if not pairKerned:
                    continue

                if firstKernedName is None:
                    firstKernedName = ufoglyph0.name
                    continue
                elif firstKernedName == ufoglyph0.name:
                    '''
                    Do not log until we have completed a first successful pass.
                    '''
                    if count % 10 == 0:
                        print '.',
                    continue

                now = time.time()
                if (lastLog is not None) and (now - lastLog < 1.0):
                    '''
                    Do not log more than once per second.
                    '''
                    continue
                lastLog = now

                elapsedTime = time.time() - startTime
#                    print 'elapsedTime', elapsedTime, 'total', total
                averageTime = elapsedTime / float(count)
#                    print 'averageTime', averageTime
                totalTime = averageTime * total
                remainingTime = totalTime - elapsedTime
                remaining = '%s remaining, %0.2f seconds average' % ( time.strftime('%H:%M:%S', time.gmtime(remainingTime)),
#                                                                                     locale.format("%d", remainingTime, grouping=True),
                                                                                 averageTime,)

                def formatUnicode(value):
                    if value is None:
                        return 'None'
                    else:
                        return '0x%X' % ( value, )
#                print 'ufoglyph0', ufoglyph0.unicode, ufoglyph0.name, 'ufoglyph1', ufoglyph1.unicode, ufoglyph1.name
                print '\t', '%s %s vs. %s %s (%0.2f%%)' % ( ufoglyph0.name,
                                                      formatUnicode(ufoglyph0.unicode),
                                                      ufoglyph1.name,
                                                      formatUnicode(ufoglyph1.unicode),
                                                      100 * count / float(total),), '\t', remaining

#        print
#        print 'self.advanceMap =', repr(self.advanceMap)
        print

        if USE_CACHED_KERNING_MAP:
            yamldata = yaml.dump(self.advanceMap)
            import tfs.common.TFSProject as TFSProject
            tmpFolder = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'tmp'))
            if not os.path.exists(tmpFolder):
                os.mkdir(tmpFolder)
            advanceMapYamlFile = os.path.abspath(os.path.join(tmpFolder, 'advanceMap.yaml'))
            with open(advanceMapYamlFile, 'wt') as f:
                f.write(yamldata)


    def parseCodePoint(self, argName, glyphNames, value):
        '''
        Parses a glyph value in one of three forms and returns to glyph's name.
        1. Glyph name in font, ie. A = A.
        2. Hexidecimal, ie. 0x41 = A.
        3. Decimal, ie. 65 = A.
        '''
        if value in glyphNames:
            return value

        if value.startswith('0x'):
            try:
                codePoint = int(value, 16)
            except ValueError, e:
                raise Exception('Invalid hexidecimal value in %s: %s' % (argName, value,) )
        else:
            try:
                codePoint = int(value)
            except ValueError, e:
                raise Exception('Invalid value in %s: %s' % (argName, value,) )

        try:
#            print 'codePoint', codePoint
            name = UnicodeCharacterNames.getUnicodeCharacterName(codePoint)
            return name
        except ValueError, e:
            raise Exception('Unknown value in %s: %s' % (argName, value,) )


    def configure(self):

        ufo_src = self.ufo_src
        if ufo_src is None:
            raise Exception('Missing ufo_src')
        if not (os.path.exists(ufo_src) and os.path.isdir(ufo_src) and os.path.basename(ufo_src).lower().endswith('.ufo')):
            raise Exception('Invalid ufo_src: %s' % ufo_src)

    #    testFont = os.path.abspath(os.path.join('..', '..', 'data', 'TFSTest Plain.ufo'))
#        self.dstUfoFont = TFSFontFromFile(ufo_src)
        self.srcUfoFont = TFSFontFromFile(ufo_src)
        self.dstUfoFont = TFSFontFromFile(ufo_src)
#        self.dstUfoFont = TFSFontFromFile(ufo_src)


        if self.ufo_dst is None:
            raise Exception('Missing ufo_dst')
        if os.path.exists(self.ufo_dst):
            if os.path.isdir(self.ufo_dst):
                shutil.rmtree(self.ufo_dst)
            elif os.path.isfile(self.ufo_dst):
                os.unlink(self.ufo_dst)
            if os.path.exists(self.ufo_dst):
                raise Exception('Could not overwrite: %s' % (self.ufo_dst,))


        log_dst = self.log_dst
        if log_dst is None:
            self.log_dst = None
    #        raise Exception('Missing log_dst')
            pass
        else:
            OVERWRITE_LOGS = True
#            OVERWRITE_LOGS = False

            if OVERWRITE_LOGS:
                if os.path.exists(log_dst):
                    shutil.rmtree(log_dst)
                if os.path.exists(log_dst):
                    raise Exception('Could not clear log_dst: %s' % log_dst)

            if not os.path.exists(log_dst):
                os.mkdir(log_dst)
            if not (os.path.exists(log_dst) and os.path.isdir(log_dst)):
                raise Exception('Invalid log_dst: %s' % log_dst)
            self.log_dst = log_dst

            if OVERWRITE_LOGS:
                def makeLogSubfolder(parent, name):
                    subfolder = os.path.abspath(os.path.join(parent, name))
                    os.mkdir(subfolder)
                    if not (os.path.exists(subfolder) and os.path.isdir(subfolder)):
                        raise Exception('Invalid log_dst: %s' % log_dst)
                    return subfolder

                self.html_folder = makeLogSubfolder(log_dst, 'html')
                self.css_folder = makeLogSubfolder(self.html_folder, 'stylesheets')
                self.svg_folder = makeLogSubfolder(self.html_folder, 'svg')

                import tfs.common.TFSProject as TFSProject
                srcCssFile = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'styles.css'))
                dstCssFile = os.path.abspath(os.path.join(self.css_folder, os.path.basename(srcCssFile)))
                shutil.copy(srcCssFile, dstCssFile)
            else:
                self.html_folder = os.path.join(log_dst, 'html')
                self.css_folder = os.path.join(self.html_folder, 'stylesheets')
                self.svg_folder = os.path.join(self.html_folder, 'svg')

        self.units_per_em = float(self.dstUfoFont.units_per_em)
        self.precision = int(round(self.precision_ems * self.units_per_em))
        self.min_distance = self.min_distance_ems * self.units_per_em
        self.max_distance = self.max_distance_ems * self.units_per_em
        self.min_non_intrusion  = self.min_non_intrusion_ems * self.units_per_em
        self.kerning_threshold  = self.kerning_threshold_ems * self.units_per_em
        self.max_x_extrema_overlap  = self.max_x_extrema_overlap_ems * self.units_per_em
        self.intrusion_tolerance  = self.intrusion_tolerance_ems * self.units_per_em

#        self.rounding = self.rounding_ems * self.dstUfoFont.units_per_em
        print 'units_per_em', self.units_per_em
        print 'precision', self.precision
        print 'min_distance', self.min_distance
        print 'max_distance', self.max_distance
        print 'intrusion_tolerance', self.intrusion_tolerance
        print 'min_non_intrusion', self.min_non_intrusion
        print 'kerning_threshold', self.kerning_threshold
        print 'max_x_extrema_overlap', self.max_x_extrema_overlap
#        print 'self.rounding', self.rounding
    #    kerning.fontMetadata = kerning.ufofont.info

        self.timing = TFTiming()
        self.advanceMap = {}
#        self.minAdvanceMap = defaultdict(0)
        self.rasterCache = {}
        self.srcContoursCache = {}
        self.dstContoursCache = {}
#        self.dstContoursInflateMinDistanceCache = {}
#        self.dstContoursInflateMaxDistanceCache = {}
        self.dstValueCache = {}
        self.srcValueCache = {}
        self.pixelsCache = {}
        self.pairsToKern = None
        self.glyphsToKern = None

        glyphNames = self.srcUfoFont.glyphNames()

        if self.glyph_pairs_to_kern is not None:
            if len(self.glyph_pairs_to_kern) < 1:
                raise Exception('Missing --glyph-pairs-to-kern value')
            if len(self.glyph_pairs_to_kern) % 2 != 0:
                raise Exception('Uneven number of  --glyph-pairs-to-kern values')
            self.pairsToKern = set()
            for index in xrange(len(self.glyph_pairs_to_kern) / 2):
                value0 = self.glyph_pairs_to_kern[index * 2 + 0]
                value1 = self.glyph_pairs_to_kern[index * 2 + 1]
                self.pairsToKern.add(( self.parseCodePoint('-glyph-pairs-to-kern', glyphNames, value0),
                                       self.parseCodePoint('-glyph-pairs-to-kern', glyphNames, value1),
                                       ))
        elif self.glyphs_to_kern is not None:
            if len(self.glyphs_to_kern) < 1:
                raise Exception('Missing --glyphs-to-kern value')
            self.glyphsToKern = set()
#            print 'self.glyphs_to_kern', self.glyphs_to_kern
            for value in self.glyphs_to_kern:
                self.glyphsToKern.add(self.parseCodePoint('--glyphs-to-kern', glyphNames, value))
        else:
            pass

        # TODO: self.minmax this should not be a class property.
        minmax = None
        for ufoglyph in self.dstUfoFont.getGlyphs():
#            print 'ufoglyph', ufoglyph.unicode

#            if ufoglyph.name in ('Ccedilla.c2', 'f_hcircumflex',):
#                print 'minmax', ufoglyph.name

            contours = self.getGlyphContours(ufoglyph)
            if len(contours) < 1:
                continue
#            if ufoglyph.name in ('Ccedilla.c2', 'f_hcircumflex',):
#                debugPaths('contours', contours)
            glyphMinmax = minmaxPaths(contours)
#            if ufoglyph.name in ('Ccedilla.c2', 'f_hcircumflex',):
#                print 'glyphMinmax', glyphMinmax
#            print 'glyphMinmax', glyphMinmax
            minmax = minmaxMerge(minmax, glyphMinmax)
#            if ufoglyph.name in ('Ccedilla.c2', 'f_hcircumflex',):
#                print 'minmax', minmax
#        print 'minmax', minmax
        self.minmax = minmax
        self.allGlyphsMinY = minmax.minY
        self.allGlyphsMaxY = minmax.maxY


#            return [TFSGlyph(glyph) for glyph in self.rffont]

    def updateKerning(self):
        self.dstUfoFont.clearKerning()

        glyphs = self.dstUfoFont.getGlyphs()
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))
        for ufoglyph0 in glyphs:
            for ufoglyph1 in glyphs:
                key = (ufoglyph0.name,
                       ufoglyph1.name,)
                if key not in self.advanceMap:
                    continue
                advance = self.advanceMap[key]
                advance = int(round(advance))

#                contours0 = self.getGlyphContours(ufoglyph0)
#                contours1 = self.getGlyphContours(ufoglyph1)
#                minmax0 = minmaxPaths(contours0)
#                minmax1 = minmaxPaths(contours1)

                '''
                TODO: add support for re-aligning glyph contours (ie. adjusting side bearings).
                TODO: add support for "max kerning items" argument to limit the number of total kerning values.
                TODO: add support for "min kerning value" argument to ignore small kerning values.
                TODO: add support for controlling what glyphs are kerned (with pairs).
                '''
                kerningValue = advance - ufoglyph0.xAdvance

                if abs(kerningValue) >= self.kerning_threshold:
#                if kerningValue != 0:
                    self.dstUfoFont.setKerningPair(ufoglyph0.name,
                                                ufoglyph1.name, kerningValue)
#                    print 'kerning', ufoglyph0.name, ufoglyph1.name, kerningValue, 'advance, ufoglyph0.xAdvance', advance, ufoglyph0.xAdvance


    def clearSideBearings(self):

        if self.pairsToKern is not None:
            return

        '''
        Removes the left and right side bearings from the glyph.
        '''
        glyphs = self.dstUfoFont.getGlyphs()
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))
        for ufoglyph in glyphs:
            if self.glyphsToKern is not None:
                if ufoglyph.name not in self.glyphsToKern:
                    continue
            elif self.isCombiningGlyph(ufoglyph):
                '''
                TODO: Should we normalize the side bearings of these glyphs to perhaps half of max_distance?
                '''
                continue

            contours = self.getGlyphContours(ufoglyph)
#            contours = ufoglyph.getContours()
            if len(contours) == 0:
                '''
                Do not modify width of space and other empty glyphs.
                '''
                continue
            minmax = minmaxPaths(contours)
            contours = [contour.applyPlus(TFSPoint(-minmax.minX, 0)) for contour in contours]
            ufoglyph.setContours(contours, correctDirection=False)
            ufoglyph.setXAdvance(minmax.maxX - minmax.minX)

        # Clear the contours cache.
        self.dstContoursCache = {}
        self.dstValueCache = {}


    def updateSideBearings(self):
        '''
        Rewrite the left and right side bearings of every glyph to be half of the average spacing
        with other glyphs.
        '''

        if self.pairsToKern is not None:
            return

        modifiedAdvanceMap = {}
        modifiedAdvanceMap.update(self.advanceMap)

        '''
        Removes the left and right side bearings from the glyph.
        '''
        glyphs = self.dstUfoFont.getGlyphs()
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))

        glyphWidthMap = {}
        for ufoglyph in glyphs:
            glyphWidthMap[ufoglyph.name] = ufoglyph.xAdvance

#        print 'updateSideBearings self.dstContoursCache', self.dstContoursCache.keys()

        if USE_CACHED_KERNING_MAP:
            for ufoglyph in glyphs:
                contours = self.getGlyphContours(ufoglyph)
            print

#        for key in self.advanceMap:
#            if key in ( ('A','A',),
#                        ('A','F',),
#                        ):
#                print 'self.advanceMap', key, self.advanceMap[key]

        for ufoglyph in glyphs:
            if self.glyphsToKern is not None:
                if ufoglyph.name not in self.glyphsToKern:
                    continue
            elif self.isCombiningGlyph(ufoglyph):
                continue
#            print 'updateSideBearings getGlyphContours', ufoglyph.name
            contours = self.getGlyphContours(ufoglyph)
#            contours = ufoglyph.getContours()
            if len(contours) == 0:
                '''
                Do not modify width of space and other empty glyphs.
                '''
                continue

            rightSpacings = []
            rightKeys = []
            leftSpacings = []
            leftKeys = []
            for key in self.advanceMap:
                advance = self.advanceMap[key]
                name0, name1 = key
                '''
                The RIGHT side bearing is effected by pairs when he is on the LEFT,
                and vice versa.
                '''
                if ufoglyph.name == name0:
                    '''
                    To get the spacing, subtract the unmodified width of the glyph on the left.
                    '''
                    spacing = advance - glyphWidthMap[name0]
                    rightSpacings.append(spacing)
                    rightKeys.append(key)
                if ufoglyph.name == name1:
                    '''
                    To get the spacing, subtract the unmodified width of the glyph on the left.
                    '''
                    spacing = advance - glyphWidthMap[name0]
                    leftSpacings.append(spacing)
                    leftKeys.append(key)

            '''
            Default sidebearings to half of the "max distance" parameter.
            '''
            leftSideBearing = rightSideBearing = 0.5 * self.max_distance_ems * self.units_per_em
            '''
            If we have kerning values for left or right side, use half of the average as the side bearing.
            '''
            if len(rightSpacings) > 0:
                rightSideBearing = 0.5 * reduce(float.__add__, [float(value) for value in rightSpacings]) / len(rightSpacings)
            if len(leftSpacings) > 0:
                leftSideBearing = 0.5 * reduce(float.__add__, [float(value) for value in leftSpacings]) / len(leftSpacings)
            '''
            Use round numbers
            '''
            rightSideBearing = int(round(rightSideBearing))
            leftSideBearing = int(round(leftSideBearing))
            if self.allow_negative_side_bearings:
                '''
                Check that the side bearings are not "negative", ie. do not
                intrude within the glyph bounds.
                '''
                leftSideBearing = max(0, leftSideBearing)
                rightSideBearing = max(0, rightSideBearing)

#            if ufoglyph.name in ( 'A',
#                                  'F', ):
#                print
#                print 'ufoglyph.name', ufoglyph.name
#                print 'glyphWidthMap[]', glyphWidthMap[ufoglyph.name]
#                print 'ufoglyph.xAdvance', ufoglyph.xAdvance
#                print 'leftKeys', len(leftKeys), leftKeys
#                print 'rightKeys', len(rightKeys), rightKeys
#                print 'rightSpacings', len(rightSpacings), rightSpacings
#                print 'leftSpacings', len(leftSpacings), leftSpacings
#                print 'updateSideBearings', 'leftSideBearing', leftSideBearing, 'rightSideBearing', rightSideBearing, 'ufoglyph.xAdvance', ufoglyph.xAdvance

            '''
            Apply the LSB to the contours.
            '''
            contours = [contour.applyPlus(TFSPoint(+leftSideBearing, 0)) for contour in contours]
            ufoglyph.setContours(contours, correctDirection=False)
            '''
            Update the glyph x advance to reflect the LSB and RSB.
            '''
            ufoglyph.setXAdvance(ufoglyph.xAdvance + leftSideBearing + rightSideBearing)

#            if ufoglyph.name in ( 'A',
#                                  'F', ):
#                print 'updateSideBearings.1', 'leftSideBearing', leftSideBearing, 'rightSideBearing', rightSideBearing, 'ufoglyph.xAdvance', ufoglyph.xAdvance

            '''
            Lastly, update the kerning values in the advance map.
            '''
            for key in leftKeys:
                modifiedAdvanceMap[key] = modifiedAdvanceMap[key] - leftSideBearing
            for key in rightKeys:
                modifiedAdvanceMap[key] = modifiedAdvanceMap[key] - rightSideBearing


#        for key in self.advanceMap:
#            if key in ( ('A','A',),
#                        ('A','F',),
#                        ):
#                print 'self.advanceMap', key, self.advanceMap[key]
#        for key in modifiedAdvanceMap:
#            if key in ( ('A','A',),
#                        ('A','F',),
#                        ):
#                print 'modifiedAdvanceMap', key, modifiedAdvanceMap[key]

        '''
        Replace the advance map.
        '''
        self.advanceMap = modifiedAdvanceMap


    def assessKerningPair(self, ufoglyph0, ufoglyph1):
        RASTERIZE_CELL_SIZE = self.precision

        contours0 = self.getGlyphContours(ufoglyph0)
        contours1 = self.getGlyphContours(ufoglyph1)
        if (not contours0) or (not contours1):
            return None
#        minmax0 = minmaxPaths(contours0)
#        minmax1 = minmaxPaths(contours1)

        kerning = self.dstUfoFont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
        if kerning is None:
            kerning = 0
        advance = ufoglyph0.xAdvance + kerning

        pixels0 = self.rasterizeGlyph(ufoglyph0, RASTERIZE_CELL_SIZE)
        pixels1 = self.rasterizeGlyph(ufoglyph1, RASTERIZE_CELL_SIZE)

        if (pixels0 is None) or (pixels1 is None):
            return

        def convertToPixelUnits(value):
            return int(math.ceil(value / float(RASTERIZE_CELL_SIZE)))

        '''
        Find the closest pair of pixels.
        '''
        minDistanceSqrd = None
        for y0, row0 in enumerate(pixels0):
            for x0, pixel0 in enumerate(row0):
                for y1, row1 in enumerate(pixels1):
                    for x1, pixel1 in enumerate(row1):
                        if (not pixel0) or (not pixel1):
                            continue
                        diffX = x0 - (x1 + advance / float(RASTERIZE_CELL_SIZE))
                        diffY = y0 - y1
                        distanceSqrd = (diffX * diffX) + (diffY * diffY)
                        if (minDistanceSqrd is None) or (distanceSqrd < minDistanceSqrd):
                            minDistanceSqrd = distanceSqrd

        if minDistanceSqrd is None:
            return None
        else:
            minDistance = math.sqrt(float(minDistanceSqrd))
            return minDistance * RASTERIZE_CELL_SIZE


    def assessKerning(self):

        glyphs = self.dstUfoFont.getGlyphs()
#        glyphNameMap = {}
#        for ufoglyph in glyphs:
#            glyphNameMap[ufoglyph.name] = ufoglyph
        unicodeGlyphMap = {}
        for ufoglyph in glyphs:
            if ufoglyph.unicode:
                unicodeGlyphMap[ufoglyph.unicode] = ufoglyph


        pairGroups = (
                      ( min, 'Minimum Distance Pairs',
                         ( ('A', 'A'),
                           ('T', 'T'),
                           ('A', 'V'),
                           ('M', 'M'),
                           ('W', 'W'),
                           ('V', 'V'),
                           ('L', 'L'),
                           ('L', 'J'),
                           ('Y', 'Y'),
                           ('W', 'A'),
                           ('V', 'A'),
                           ('A', 'V'),
                           ('A', 'W'),
                           ),
                         ),
                      ( max, 'Maximum Distance Pairs',
                         ( ('J', 'L'),
                           ('H', 'H'),
                           ('H', 'L'),
                           ('J', 'H'),
                           ('H', 'F'),
                           ('V', 'V'),
                           ('I', 'I'),
                           ('N', 'F'),
                           ('N', 'B'),
                           ('N', 'H'),
                           ('N', 'L'),
                           ('H', 'B'),
                           ('W', 'A'),
                           ('V', 'A'),
                           ('A', 'V'),
                           ('A', 'W'),
                           ),
                         ),
                      )

        def formatEmScalar(value):
            return '%0.3f em' % (value / float(self.units_per_em))

        for reduceFunc, pairGroupName, pairs in pairGroups:
            print
            print pairGroupName
            values = []
            for char0, char1 in pairs:
                unicode0 = ord(char0)
                unicode1 = ord(char1)
#                print 'pair', char0, char1, unicode0, unicode1
                ufoglyph0 = unicodeGlyphMap[unicode0]
                ufoglyph1 = unicodeGlyphMap[unicode1]
                pairDistance = self.assessKerningPair(ufoglyph0, ufoglyph1)
                print 'pair', char0, hex(unicode0), 'vs.', char1, hex(unicode1), 'pairDistance:', pairDistance, ('(%s)' % ( formatEmScalar(pairDistance), ) )
                values.append(pairDistance)
            print pairGroupName, formatEmScalar(reduce(reduceFunc, values))
        print


    def process(self):
        self.configure()

        if self.assess_only:
            print 'Entering assessment mode...'
            self.assessKerning()
            return

        self.timing.mark('configure.')

        if not self.do_not_modify_side_bearings:
            self.clearSideBearings()
            self.timing.mark('clearSideBearings.')

        self.processAllKerningPairs()
        self.timing.mark('processAllKerningPairs.')

#        print 'logDisparities'
        self.logDisparities()
        self.timing.mark('logDisparities.')

        if not self.do_not_modify_side_bearings:
#            print 'updateSideBearings'
            self.updateSideBearings()
            self.timing.mark('updateSideBearings.')

#        print 'updateKerning'
        self.updateKerning()
        self.timing.mark('updateKerning.')

        self.dstUfoFont.update()
        self.dstUfoFont.save(self.ufo_dst)
        self.dstUfoFont.close()

        self.timing.mark('finished.')
        if True:
            self.timing.dump()


if __name__ == "__main__":
    autokern = Autokern()
    AutokernSettings(autokern).getCommandLineSettings()
    autokern.process()

    print
    print 'complete.'
