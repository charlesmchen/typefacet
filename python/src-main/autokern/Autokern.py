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
import types
import unicodedata

locale.setlocale(locale.LC_ALL, 'en_US')

#from robofab.world import *
import robofab.world

from tfs.common.TFSFont import *
from AutokernSettings import AutokernSettings
#from tfs.common.TFSSilhouette import *
from tfs.common.TFTiming import TFTiming
from tfs.common.TFSMap import TFSMap
import tfs.common.TFSMath as TFSMath
from tfs.common.TFSPath import *
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
USE_CACHED_KERNING_MAP = True


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


class AutokernCache(TFSMap):

    def __init__(self):
        TFSMap.__init__(self)
        self.valueCache = {}

    def getCachedValue(self, key, func, *argv):
        if key in self.valueCache:
            return self.valueCache[key]
        result = func(*argv)
        self.valueCache[key] = result
        return result

    def getGlyphContours(self, ufoglyph):
        def getCachedContours():
            contours = ufoglyph.getContours(warnings=False)
            return contours
        return self.getCachedValue('getCachedContours %s' % ufoglyph.name, getCachedContours)

    def getContoursMinmax(self, ufoglyph):
        def getCachedMinmax():
            contours = self.getGlyphContours(ufoglyph)
            return minmaxPaths(contours)
        return self.getCachedValue('getCachedMinmax %s' % ufoglyph.name, getCachedMinmax)


class Autokern(TFSMap):

    def __init__(self):
        TFSMap.__init__(self)


    def makeDefaultMustacheMap(self, localsMap=None):

        mustacheMap = {}

        def addToMustacheMap(key, value):
            if type(value) not in ( types.IntType,
                                    types.LongType,
                                    types.FloatType,
                                    types.UnicodeType,
                                    types.StringType, ):
                return

            if type(value) in ( types.IntType,
                                    types.LongType):
                value = locale.format("%d", value, grouping=True)

            if key not in mustacheMap:
                mustacheMap[key] = value

#        for attr in dir(self):
##            print 'attr', attr
#            if attr.startswith('_'):
#                continue
#            value = getattr(self, attr)
#
#            if attr.endswith('_ems'):
#                value = '%0.3f em' % (value, )
#
#            addToMustacheMap(attr, value)

        for key, value in self.items():
            if key.endswith('_ems'):
                value = '%0.3f em' % (value, )
            elif type(value) in ( types.IntType,
                                    types.FloatType,
                                    types.LongType,):
                emsKey = key + '_in_ems'
                emsValue = '%0.3f em' % (value / float(self.units_per_em))
                addToMustacheMap(emsKey, emsValue)
            addToMustacheMap(key, value)

        if localsMap:
            for key, value in localsMap.items():
                if type(value) in ( types.IntType,
                                    types.FloatType,
                                    types.LongType,):
                    emsKey = key + '_in_ems'
                    emsValue = '%0.3f em' % (value / float(self.units_per_em))
                    addToMustacheMap(emsKey, emsValue)
                addToMustacheMap(key, value)

        for key in (
                     'unitsPerEm',
                     'familyName',
                     'styleName',
                     'fullName',
                     'fontName',
                    ):
            mustacheMap[key] = getattr(self.dstUfoFont.info, key)

#        print 'mustacheMap', mustacheMap
#        print 'mustacheMap'
#        for key, value in mustacheMap.items():
#            if type(value) in (types.StringType, types.UnicodeType,) and len(value) > 100:
#                value = value[:100] + '...'
#            print '\t', key, value
#        print

        return mustacheMap

    '''

http://bugs.python.org/file19991/unicodedata-doc.diff

+   +--------------------------------------------------------------------------+
+   | **General Categories**                                                   |
+   +----+-------------+------------------+------------------------------------+
+   |Name|Major        |Minor             |Examples                            |
+   +====+=============+==================+====================================+
+   |Lu  | Letter      | uppercase        |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Ll  | Letter      | lowercase        |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Lt  | Letter      | titlecase        |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Lm  | Letter      | modifier         |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Lo  | Letter      | other            |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Mn  | Mark        | nonspacing       |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Mc  | Mark        | spacing combining|                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Me  | Mark        | enclosing        |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Nd  | Number      | decimal digit    |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Nl  | Number      | letter           |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |No  | Number      | other            |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Pc  | Punctuation | connector        |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Pd  | Punctuation | dash             |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Ps  | Punctuation | open             |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Pe  | Punctuation | close            |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Pi  | Punctuation | initial quote    |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Pf  | Punctuation | final quote      |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Po  | Punctuation | other            |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Sm  | Symbol      | math             |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Sc  | Symbol      | currency         |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Sk  | Symbol      | modifier         |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |So  | Symbol      | other            |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Zs  | Separator   | space            |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Zl  | Separator   | line             |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Zp  | Separator   | paragraph        |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Cc  | Other       | control          |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Cf  | Other       | format           |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Cs  | Other       | surrogate        |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Co  | Other       | private use      |                                    |
+   +----+-------------+------------------+------------------------------------+
+   |Cn  | Other       | not assigned     |                                    |
+   +----+-------------+------------------+------------------------------------+
    '''

    def hasUnicodeCategoryPrefix(self, glyph, *prefixes):
        '''
        The unicodedata glyph categories are:
        L Letter
        M Mark
        N Number
        P Punctuation
        Z Separator
        S Symbol
        C Other
        '''
        if glyph.unicode is None:
            return False
        uc = unichr(glyph.unicode)
        if uc is not None:
            unicode_category = unicodedata.category(uc)
            if unicode_category is not None:
                if unicode_category[0] in prefixes:
                    return True
        return False


    def isLetterGlyph(self, glyph):
        return self.hasUnicodeCategoryPrefix(glyph, 'L')

    def isPunctuationGlyph(self, glyph):
        return self.hasUnicodeCategoryPrefix(glyph, 'P')

    def isSymbolGlyph(self, glyph):
        return self.hasUnicodeCategoryPrefix(glyph, 'S')


    def isPunctuationOrSymbolGlyph(self, glyph):
        if glyph.unicode is None:
            return False

        uc = unichr(glyph.unicode)
        if uc is not None:
            unicode_category = unicodedata.category(uc)
            if unicode_category is not None:
                if (unicode_category.startswith('P') or
                    unicode_category.startswith('N')):
                    return True

        # Latin
        if 0x21 <= glyph.unicode <= 0x2f:
            return True
        if 0x3a <= glyph.unicode <= 0x40:
            return True
        if 0x5b <= glyph.unicode <= 0x60:
            return True
        if 0x7b <= glyph.unicode <= 0x7e:
            return True
        # Latin 1 supplement
        if 0xa1 <= glyph.unicode <= 0xbf:
            return True
        if glyph.unicode in ( 0xf7, ):
            return True
        # 0xf7
        if 0x1c0 <= glyph.unicode <= 0x1c3:
            return True
        # Halfwidth and Fullwidth Forms
        if 0xff01 <= glyph.unicode <= 0xff0f:
            return True
        if 0xff1a <= glyph.unicode <= 0xff20:
            return True
        if 0xff3b <= glyph.unicode <= 0xff40:
            return True
        if 0xff5b <= glyph.unicode <= 0xff65:
            return True
        # Vertical Forms
        if 0xfe10 <= glyph.unicode <= 0xfe1f:
            return True
        # General Punctuation
        if 0x2000 <= glyph.unicode <= 0x206f:
            return True
        # Small Form Variants
        if 0xfe50 <= glyph.unicode <= 0xfe6f:
            return True
        # Supplemental Punctuation
        if 0x2e00 <= glyph.unicode <= 0x2e7f:
            return True
        # CJK Symbols and Punctuation
        if 0x3000 <= glyph.unicode <= 0x303f:
            return True
        # CJK Compatibility Forms
        if 0xfe30 <= glyph.unicode <= 0xfe4f:
            return True
        # Letterlike Symbols
        if 0x2100 <= glyph.unicode <= 0x214f:
            return True
        # Ancient Symbols
        if 0x10190 <= glyph.unicode <= 0x101cf:
            return True

        # TODO: there are more unicode blocks for symbols and punctuation...

        return False

    def isIgnoredGlyph(self, glyph):
        '''
        L Letter
        M Mark
        N Number
        P Punctuation
        Z Separator
        S Symbol
        C Other
        '''
        if self.hasUnicodeCategoryPrefix(glyph, 'S', 'C', 'Z', 'M'):
            return True

        if glyph.unicode is not None:
            if 0xfe20 <= glyph.unicode <= 0xfe2f:
                return True
            if 0x1dc0 <= glyph.unicode <= 0x1dff:
                return True
            if 0x300 <= glyph.unicode <= 0x36f:
                return True

        if not hasattr(self, 'ignore_names_set'):
            self.ignore_names_set = set( (
                      'underscore',
                 'dieresis_acutecomb',
                 'dieresis_gravecomb',
                 'hungarumlaut',
                'ring',
                'dotaccent',
                'dieresis',
                 'dieresistonos',

                'asciitilde',
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
                 ) )

        if glyph.name in self.ignore_names_set:
            return True
        '''
        Look for variations like 'breve.cap' or 'breve.cyr'.
        '''
        if '.' in glyph.name[1:]:
            shortName = glyph.name[:glyph.name.index('.')]
            if shortName in self.ignore_names_set:
                return True

        '''
        We can't count on glyphs having their "standard" names,
        so we'll compare by unicode as well.
        '''
        if not hasattr(self, 'ignore_unicodes_set'):
            self.ignore_unicodes_set = set()
            for name in self.ignore_names_set:
                codePoint = UnicodeCharacterNames.getUnicodeForShortName(name)
                if codePoint is not None:
                    self.ignore_unicodes_set.add(codePoint)
                else:
                    print 'Unknown glyph short name', name

        if glyph.unicode is not None:
            if glyph.unicode in self.ignore_unicodes_set:
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
                       pathTuples = (),
                       strokePathTuples = None,
                       fillPathTuples = None,
                       hGuidelines=None,
                       hRanges=None,
                       textTuples=None,
                       bottomPadding=0):

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
        if strokePathTuples is not None:
            for color, contours in strokePathTuples:
                self.subrenderGlyphContours(tfsSvg, contours, color, addPoints=False)
        if fillPathTuples is not None:
            for color, contours in fillPathTuples:
                for contour in contours:
                    tfsSvg.addItem(TFSSvgPath(contour).addFill(color))
        if textTuples is not None:
            for textMap in textTuples:
                tfsSvg.addText(textMap.text, textMap.origin, textMap.fillColor, **textMap.params)

        if hGuidelines:
            for hGuideline in hGuidelines:
                p0 = TFSPoint(hGuideline, self.dstUfoFont.info.descender)
                p1 = TFSPoint(hGuideline, self.dstUfoFont.info.ascender)
                GUIDELINE_COLOR = 0x7fdfdfdf
                tfsSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

        if hRanges:
            for hRange in hRanges:
                rangeName, rangeLeft, rangeRight = hRange
                p0 = TFSPoint(rangeLeft, int(round(self.max_distance * -1.3)))
                p1 = TFSPoint(rangeRight, int(round(self.max_distance * -1.3)))
                H_RANGE_COLOR = 0xaf3f3faf
                tfsSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(H_RANGE_COLOR, 3))

        vGuidelines = ( 0,
                        self.dstUfoFont.info.ascender,
                        self.dstUfoFont.info.descender,
                        )
        if vGuidelines:
            minmax = None
            allPathTuples = pathTuples
            if strokePathTuples is not None:
                allPathTuples = allPathTuples + strokePathTuples
            if fillPathTuples is not None:
                allPathTuples = allPathTuples + fillPathTuples
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
        svgdata = tfsSvg.renderToFile(dstFile, margin=10, height=SVG_HEIGHT, maxWidth=SVG_MAX_WIDTH,
                                      timing=self.timing,
                                      bottomPadding=bottomPadding)
        self.timing.mark('renderSvgScene.1')
        if filename is not None:
            return filename
        else:
            return svgdata


    def buildKerningInfoMap(self, ufofont, ufoglyph0, ufoglyph1, cache):
        if (ufoglyph0.name is None) or (ufoglyph1.name is None):
            return None
        kerningInfo = TFSMap()
        kerningInfo.ufoglyph0 = ufoglyph0
        kerningInfo.ufoglyph1 = ufoglyph1
        kerningInfo.name0 = ufoglyph0.name
        kerningInfo.name1 = ufoglyph1.name
        kerningInfo.kerningValue = ufofont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
        if kerningInfo.kerningValue is None:
            kerningInfo.kerningValue = 0
        kerningInfo.contours0 = cache.getGlyphContours(ufoglyph0)
        if (kerningInfo.contours0 is None) or (len(kerningInfo.contours0) < 1):
            return None
        kerningInfo.contours1 = cache.getGlyphContours(ufoglyph1)
        if (kerningInfo.contours1 is None) or (len(kerningInfo.contours1) < 1):
            return None
        kerningInfo.minmax0 = cache.getContoursMinmax(ufoglyph0)
        kerningInfo.minmax1 = cache.getContoursMinmax(ufoglyph1)
        kerningInfo.xAdvance = ufoglyph0.xAdvance
        kerningInfo.kernedAdvance = kerningInfo.xAdvance + kerningInfo.kerningValue
        kerningInfo.x_extrema_overlap = kerningInfo.minmax0.maxX - (kerningInfo.minmax1.minX + kerningInfo.kernedAdvance)
        return kerningInfo


    def buildKerningInfoMaps(self, ufofont, ufoglyphs, cache):
        result = {}
        for ufoglyph0 in ufoglyphs:
            for ufoglyph1 in ufoglyphs:
                kerningInfo = self.buildKerningInfoMap(ufofont, ufoglyph0, ufoglyph1, cache)
                if kerningInfo is not None:
                    result[(ufoglyph0.name, ufoglyph1.name,)] = kerningInfo
        return result


    def findDisparities(self):

        srcGlyphs = self.srcUfoFont.getGlyphs()
        dstGlyphs = self.dstUfoFont.getGlyphs()

        srcKerningInfoMap = self.buildKerningInfoMaps(self.srcUfoFont, srcGlyphs, self.srcCache)
        dstKerningInfoMap = self.buildKerningInfoMaps(self.dstUfoFont, dstGlyphs, self.dstCache)

        disparities = []
        for key, srcKerning in srcKerningInfoMap.items():
            if key not in dstKerningInfoMap:
                print 'Missing output kerning info for pair:', key
                continue
            dstKerning = dstKerningInfoMap[key]
            disparity = TFSMap()
            disparity.key = key
            disparity.srcKerning = srcKerning
            disparity.dstKerning = dstKerning
            disparity.disparity = abs(srcKerning.x_extrema_overlap - dstKerning.x_extrema_overlap)
            disparities.append(disparity)

        def cmpDisparities(d0, d1):
            return cmp(d0.disparity, d1.disparity)
        disparities.sort(cmpDisparities, reverse=True)
        return disparities


    def logDisparities(self):

        renderLog = self.log_dst is not None
        if not renderLog:
            return
        if self.disparity_log_count < 1:
            return

        print 'Logging disparities...'

        disparities = self.findDisparities()

        '''
        We're only interested in the top 100 disparities.
        '''
        self.disparity_log_count = max(0, self.disparity_log_count)
        disparities = disparities[:self.disparity_log_count]

        def getDisparityFilename(index):
            return 'disparity-%d.html' % index

        disparityLinkMaps = []
        for index, disparity in enumerate(disparities):
            disparityLinkMaps.append({ 'filename': getDisparityFilename(index),
                                      'name': str(index + 1),
                                      })

        for index, disparity in enumerate(disparities):
            filenamePrefix = 'disparity-%d' % index
            srcAdvanceSvg = self.renderSvgScene(None,
                                             pathTuples = (
                                                           ( 0x7f7faf7f, disparity.srcKerning.contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(disparity.srcKerning.kernedAdvance, 0)) for contour in disparity.srcKerning.contours1], ),
                                                           ),
                                             hGuidelines = ( disparity.srcKerning.kernedAdvance, ) )

            dstAdvanceSvg = self.renderSvgScene(None,
                                             pathTuples = (
                                                           ( 0x7f7faf7f, disparity.dstKerning.contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(disparity.dstKerning.kernedAdvance, 0)) for contour in disparity.dstKerning.contours1], ),
                                                           ),
                                             hGuidelines = ( disparity.dstKerning.kernedAdvance, ) )

            import tfs.common.TFSProject as TFSProject
            mustache_template_file = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'autokern_disparity_template.txt'))
            with open(mustache_template_file, 'rt') as f:
                mustache_template = f.read()

            pageTitle0 = u'Autokern Disparity:'
            pageTitle1 = u'%s vs. %s' % ( formatGlyphName(disparity.srcKerning.ufoglyph0),
                                          formatGlyphName(disparity.srcKerning.ufoglyph1), )

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

            localsMap = {}
            localsMap.update(locals())
            localsMap.update(disparity)

            def mergeMapsItems(srcMap, dstMap, prefix):
                for key, value in srcMap.items():
                    dstMap[prefix + key] = value

            mergeMapsItems(disparity.srcKerning, localsMap, 'src_')
            mergeMapsItems(disparity.srcKerning.minmax0, localsMap, 'src0_')
            mergeMapsItems(disparity.srcKerning.minmax1, localsMap, 'src1_')
            mergeMapsItems(disparity.dstKerning, localsMap, 'dst_')
            mergeMapsItems(disparity.dstKerning.minmax0, localsMap, 'dst0_')
            mergeMapsItems(disparity.dstKerning.minmax1, localsMap, 'dst1_')

            mustacheMap = self.makeDefaultMustacheMap(localsMap=localsMap)

            mustacheMap.update({
                           'pageTitle0': pageTitle0,
                           'pageTitle1': pageTitle1,

                           'disparityLinkMaps': disparityLinkMaps,
                           'firstDisparityLink': getDisparityFilename(0),
                           'lastDisparityLink': getDisparityFilename(len(disparities) - 1),
                           })
            if index > 0:
                mustacheMap['prevDisparityLink'] = {'filename': getDisparityFilename(index - 1), }
            if index + 1 < len(disparities):
                mustacheMap['nextDisparityLink'] = {'filename': getDisparityFilename(index + 1), }

            kerningLogFilename = self.getKerningPairHtmlFilename(disparity.srcKerning.ufoglyph0,
                                                                 disparity.srcKerning.ufoglyph1),
            if kerningLogFilename in self.kerningPairLogFilenames:
                mustacheMap['kerningLogFilename'] = kerningLogFilename

            import pystache
            logHtml = pystache.render(mustache_template, mustacheMap)

            logFilename = getDisparityFilename(index)
            logFile = os.path.abspath(os.path.join(self.html_folder, logFilename))
            with open(logFile, 'wt') as f:
                # TODO: explicitly encode unicode
                f.write(logHtml)


    def findDisparities_old(self):

        disparities = []
        glyphs = self.dstUfoFont.getGlyphs()
#        total = len(glyphs) * len(glyphs)
#        count = 0
#        startTime = time.time()
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))
        for ufoglyph0 in glyphs:
            for ufoglyph1 in glyphs:

                disparity = TFSMap()
                disparity.dstUfoGlyph0 = ufoglyph0
                disparity.dstUfoGlyph1 = ufoglyph1


                disparity.srcUfoGlyph0 = self.srcUfoFont.getGlyphByName(ufoglyph0.name)
                if disparity.srcUfoGlyph0 is None:
                    raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph0.name),
                                                                             str(ufoglyph0.unicode)))
                disparity.srcUfoGlyph1 = self.srcUfoFont.getGlyphByName(ufoglyph1.name)
                if disparity.srcUfoGlyph1 is None:
                    raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph1.name),
                                                                             str(ufoglyph1.unicode)))


                disparity.srcMinmax0 = self.srcCache.getContoursMinmax(disparity.srcUfoGlyph0)
                disparity.srcMinmax1 = self.srcCache.getContoursMinmax(disparity.srcUfoGlyph1)

                disparity.dstMinmax0 = self.dstCache.getContoursMinmax(ufoglyph0)
                disparity.dstMinmax1 = self.dstCache.getContoursMinmax(ufoglyph1)

#                key = (ufoglyph0.name,
#                       ufoglyph1.name,)
#                if key not in self.advanceMap:
#                    continue

#                disparity.srcXAdvance = disparity.srcUfoGlyph0.xAdvance
                disparity.dstAdvance = int(round(self.advanceMap[key]))
                disparity.dstXAdvance = disparity.dstUfoGlyph0.xAdvance
                disparity.dstKerning = disparity.dstAdvance - disparity.dstXAdvance

                disparity.srcKerning = self.srcUfoFont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
                if disparity.srcKerning is None:
                    disparity.srcKerning = 0
                disparity.srcXAdvance = disparity.srcUfoGlyph0.xAdvance
                disparity.srcAdvance = disparity.srcUfoGlyph0.xAdvance + disparity.srcKerning

                disparity.srcContours0 = self.srcCache.getGlyphContours(disparity.srcUfoGlyph0)
                disparity.srcContours1 = self.srcCache.getGlyphContours(disparity.srcUfoGlyph1)

                disparity.srcOffset = disparity.srcAdvance + (-disparity.srcMinmax0.maxX) + (disparity.srcMinmax1.minX)

                disparity.dstContours0 = self.dstCache.getGlyphContours(ufoglyph0)
                disparity.dstContours1 = self.dstCache.getGlyphContours(ufoglyph1)

                disparity.dstOffset = disparity.dstAdvance + (-disparity.dstMinmax0.maxX) + (disparity.dstMinmax1.minX)

                disparity.offsetDifference = abs(disparity.srcOffset - disparity.dstOffset)
                disparity.advanceDifference = abs(disparity.dstAdvance - disparity.srcAdvance)

                if disparity.offsetDifference != 0:
                    disparities.append(disparity)

        def compareDisparities(disparity0, disparity1):
            return cmp(disparity0.offsetDifference, disparity1.offsetDifference)

        disparities.sort(compareDisparities, reverse=True)
        return disparities


    def logDisparities_old(self):

        renderLog = self.log_dst is not None
        if not renderLog:
            return
        if self.disparity_log_count < 1:
            return

        print 'Logging disparities...'

        disparities = self.findDisparities()

        '''
        We're only interested in the top 100 disparities.
        '''
        self.disparity_log_count = max(0, self.disparity_log_count)
        disparities = disparities[:self.disparity_log_count]

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

            pageTitle0 = u'Autokern Disparity:'
            pageTitle1 = u'%s vs. %s' % ( formatGlyphName(disparity.dstUfoGlyph0),
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

            mustacheMap = self.makeDefaultMustacheMap(localsMap=locals())

            mustacheMap.update({
                           'pageTitle0': pageTitle0,
                           'pageTitle1': pageTitle1,
                           'disparityCount': self.disparity_log_count,
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
                           })
            if index > 0:
                mustacheMap['prevDisparityLink'] = {'filename': getDisparityFilename(index - 1), }
            if index + 1 < len(disparities):
                mustacheMap['nextDisparityLink'] = {'filename': getDisparityFilename(index + 1), }

            kerningLogFilename = self.getKerningPairHtmlFilename(disparity.dstUfoGlyph0,
                                                                 disparity.dstUfoGlyph1),
            if kerningLogFilename in self.kerningPairLogFilenames:
                mustacheMap['kerningLogFilename'] = kerningLogFilename

            import pystache
            logHtml = pystache.render(mustache_template, mustacheMap)

            logFilename = getDisparityFilename(index)
            logFile = os.path.abspath(os.path.join(self.html_folder, logFilename))
            with open(logFile, 'wt') as f:
                # TODO: explicitly encode unicode
                f.write(logHtml)


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
                extraX = reduce(min, [point.x for point in points])
#                extraX = min(firstPoint.x, lastPoint.x)
                extraX += -10
            else:
                extraX = reduce(max, [point.x for point in points])
#                extraX = max(firstPoint.x, lastPoint.x)
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


    def isValidProfileIntrusion(self, profile0, profile1, advance):

#        print 'isValidProfileIntrusion', 'advance', advance

        '''
        Step 1
        Split the profiles into sections of continuous values which are no more
        than --max-distance apart.
        '''
        sections = []
        sectionRowSpacings = []
        for edge0, edge1 in itertools.izip(profile0, profile1):
            rowSpacing = None
            if (edge0 is not None) and (edge1 is not None):
                rowSpacing = advance + edge1 - edge0
#                print 'rowSpacing.0', rowSpacing, 'self.max_distance', self.max_distance, 'advance, edge1, edge0', advance, edge1, edge0
#                if rowSpacing >= self.max_distance:
#                    '''
#                    Treat gaps of more than --max-distance to be section breaks.
#                    '''
#                    rowSpacing = None

#            print 'rowSpacing', rowSpacing

            if rowSpacing is None:
                if len(sectionRowSpacings) > 0:
                    sections.append(sectionRowSpacings)
                    sectionRowSpacings = []
                continue

#            print 'rowSpacing.0', rowSpacing, 'self.max_distance', self.max_distance, 'advance, edge1, edge0', advance, edge1, edge0

            sectionRowSpacings.append(rowSpacing)

        if len(sectionRowSpacings) > 0:
            sections.append(sectionRowSpacings)

#        print 'sections', sections

        if len(sections) < 1:
            '''
            No collision found.
            '''
            return True

#        '''
#        Step 2
#        Determine the intrusion tolerance area.
#        '''
#        totalSectionRowCount = reduce(int.__add__, [len(sectionRowSpacings) for sectionRowSpacings in sections])
#        intrusionToleranceArea = self.intrusion_tolerance * totalSectionRowCount

        '''
        Step 3
        Now consider each section separately.
        '''
#        intrusionTotal = 0
#        extrusionTotal = 0
        for sectionRowSpacings in sections:
#            '''
#            Ignore extrusion within section greater than the max intrusion of section.
#            '''
            intrusionTotal = 0
            extrusionTotal = 0
#            maxIntrusion = reduce(min, sectionRowSpacings)
#            extrusionLimit = abs(maxIntrusion)
#            print 'maxIntrusion', maxIntrusion, 'extrusionLimit', extrusionLimit
            for rowSpacing in sectionRowSpacings:
                rowIntrusion = max(0, -rowSpacing)
                '''
                Ignore extrusion greater than --max-distance argument.
                '''
                rowExtrusion = min(self.max_distance, max(0, +rowSpacing))

#                rowExtrusion = min(extrusionLimit, max(0, rowSpacing))
#                print 'edge0, edge1', edge0, edge1, 'diff', diff, 'advance', advance, 'rowIntrusion', rowIntrusion, 'rowExtrusion', rowExtrusion
                intrusionTotal += rowIntrusion
                extrusionTotal += rowExtrusion

            '''
            Enforce
            '''

#            print 'advance', advance
#            print 'intrusionTotal', intrusionTotal, 'extrusionTotal', extrusionTotal
#            INTRUSION_EXTRUSION_MIN_RATIO = 1.5
            INTRUSION_EXTRUSION_MIN_RATIO = 1.0
            if intrusionTotal > extrusionTotal * INTRUSION_EXTRUSION_MIN_RATIO:
                return False

            intrusionToleranceArea = self.intrusion_tolerance * len(sectionRowSpacings)
#            print 'intrusionToleranceArea', intrusionToleranceArea
            if intrusionTotal > intrusionToleranceArea:
                return False

#        print 'totalSectionRowCount', totalSectionRowCount, 'advance', advance
#        print 'intrusionTotal', intrusionTotal, 'extrusionTotal', extrusionTotal, 'intrusionToleranceArea', intrusionToleranceArea

#        if intrusionTotal > extrusionTotal:
#            return False
#        if intrusionTotal > intrusionToleranceArea:
#            return False
        return True


    def findMinProfileAdvance(self, profile0, profile1):
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

        return contactAdvance


    def findMinProfileAdvance_withIntrusion(self, profile0, profile1):
        contactAdvance = self.findMinProfileAdvance(profile0, profile1)

        if contactAdvance is None:
            return None

        '''
        Binary search for best intrusion offset.
        '''
        lowValidIntrusionOffset = 0
        highInvalidIntrusionOffset = int(math.ceil(self.intrusion_tolerance))
        while True:
            intrusionOffset = int(round((lowValidIntrusionOffset + highInvalidIntrusionOffset) / 2))
#            print 'intrusionOffset', intrusionOffset, 'lowValidIntrusionOffset', lowValidIntrusionOffset, 'highInvalidIntrusionOffset', highInvalidIntrusionOffset

            if intrusionOffset in ( lowValidIntrusionOffset,
                                    highInvalidIntrusionOffset, ):
                return contactAdvance - lowValidIntrusionOffset

            if self.isValidProfileIntrusion(profile0, profile1, contactAdvance - intrusionOffset):
                lowValidIntrusionOffset = intrusionOffset
            else:
                highInvalidIntrusionOffset = intrusionOffset


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

        if (ufoglyph0.name is None) or (ufoglyph1.name is None):
            return
        if self.pairsToKern is not None:
            if (ufoglyph0.name, ufoglyph1.name) not in self.pairsToKern:
                return False
        elif self.glyphsToKern is not None:
            if ufoglyph0.name not in self.glyphsToKern:
                return False
            if ufoglyph1.name not in self.glyphsToKern:
                return False

        if self.isIgnoredGlyph(ufoglyph0) or self.isIgnoredGlyph(ufoglyph1):
            return False

#        print 'processKerningPair'

        debugKerning = True
        debugKerning = False

        renderLog = (self.log_dst is not None) and not self.skip_kerning_pair_logs

        contours0 = self.dstCache.getGlyphContours(ufoglyph0)
        contours1 = self.dstCache.getGlyphContours(ufoglyph1)
        if (not contours0) or (not contours1):
            return False

        self.timing.mark('processKerningPair.01')

        minmax0 = self.dstCache.getContoursMinmax(ufoglyph0)
        minmax1 = self.dstCache.getContoursMinmax(ufoglyph1)

        self.timing.mark('processKerningPair.010')

#        if (self.isPunctuationGlyph(ufoglyph0) and
#            self.isPunctuationGlyph(ufoglyph1)):
#            '''
#            Do not kern punctuation against each other.
#            '''
#
#            advance = minmax0.maxX + self.max_distance - minmax1.minX
#            self.advanceMap[(ufoglyph0.name,
#                             ufoglyph1.name,)] = advance
#
#            self.timing.mark('processKerningPair.010a')
#            return

        def getRightContour():
#            return self.makeProfile(func=max, paths=contours0, debug=True)
            return self.makeProfile(func=max, paths=contours0)
        profile0 = self.dstCache.getCachedValue('getRightContour %s' % ufoglyph0.name, getRightContour)

        self.timing.mark('processKerningPair.011')

        def getLeftContour():
            return self.makeProfile(func=min, paths=contours1)
        profile1 = self.dstCache.getCachedValue('getLeftContour %s' % ufoglyph1.name, getLeftContour)

        self.timing.mark('processKerningPair.012')

        def getLeftContourInflateMin():
            return self.makeInflatedProfile(func=min, contours=contours1, radius=self.min_distance)
        profileMin1 = self.dstCache.getCachedValue('getLeftContourInflateMin %s' % ufoglyph1.name, getLeftContourInflateMin)

        self.timing.mark('processKerningPair.013')

        def getLeftContourInflateMax():
            return self.makeInflatedProfile(func=min, contours=contours1, radius=self.max_distance)
        profileMax1 = self.dstCache.getCachedValue('getLeftContourInflateMax %s' % ufoglyph1.name, getLeftContourInflateMax)

        self.timing.mark('processKerningPair.014')

        minDistanceAdvance = self.findMinProfileAdvance(profile0, profileMin1)
        self.timing.mark('processKerningPair.021')
        if debugKerning:
            print 'minDistanceAdvance', minDistanceAdvance

        intrudingAdvance = self.findMinProfileAdvance_withIntrusion(profile0, profileMax1)
#        print 'intrudingAdvance.1', intrudingAdvance

        self.timing.mark('processKerningPair.023')
        if debugKerning:
            print 'intrudingAdvance', intrudingAdvance

#        intruding_x_extrema_overlap = minmax0.maxX - (minmax1.minX + intrudingAdvance)
#        print 'intruding_x_extrema_overlap', intruding_x_extrema_overlap


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

        pair_max_x_extrema_overlap = self.max_x_extrema_overlap

        if (self.isPunctuationGlyph(ufoglyph0) or
            self.isPunctuationGlyph(ufoglyph1)):
            '''
            Punctuation should keep x-extrema at least --min-distance apart.
            '''
            pair_max_x_extrema_overlap = -self.min_distance

        if x_extrema_overlap > pair_max_x_extrema_overlap:
#            print
#            print 'overlap', ufoglyph0.name, ufoglyph1.name
#            print 'minmax0.maxX, minmax1.minX', minmax0.maxX, minmax1.minX, 'advance', advance
#            print 'x_extrema_overlap, self.max_x_extrema_overlap', x_extrema_overlap, self.max_x_extrema_overlap
#            print 'advance.0', advance
            advance += x_extrema_overlap - pair_max_x_extrema_overlap
#            print 'advance.1', advance

#        print 'advanceLimit', advanceLimit, 'advance', advance


        self.advanceMap[(ufoglyph0.name,
                         ufoglyph1.name,)] = advance

#        if ufoglyph0.name == 'A' or ufoglyph1.name == 'A':
#            print '\t', 'result', ufoglyph0.name, ufoglyph1.name, advance, 'spacing', advance - ufoglyph0.xAdvance
#        print '\t', 'result', ufoglyph0.name, ufoglyph1.name, advance, 'spacing', advance - ufoglyph0.xAdvance, 'x-extrema offset', advance + minmax1.minX - minmax0.maxX

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

            srcContours0 = self.srcCache.getGlyphContours(srcufoglyph0)
            srcContours1 = self.srcCache.getGlyphContours(srcufoglyph1)
            srcKerning = self.dstUfoFont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
            if srcKerning is None:
                srcKerning = 0
            srcAdvance = srcufoglyph0.xAdvance + srcKerning

            srcminmax0 = self.srcCache.getContoursMinmax(srcufoglyph0)
            srcminmax1 = self.srcCache.getContoursMinmax(srcufoglyph1)

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

            if contactAdvance is None:
                '''
                If no collisions between the glyph profiles, use x-extrema.
                '''
                contactAdvance = minmax0.maxX - minmax1.minX

            contactAdvanceSvg = self.renderSvgScene(None,
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(contactAdvance, 0)) for contour in contours1], ),
                                                           ),
                                             strokePathTuples = (
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
                                             strokePathTuples = (
                                                           ( 0xafff7faf, profilePaths0, ),
                                                           ( 0xafaf7fff, self.convertProfileToLogPaths(profileMin1, isLeft=False, offset=TFSPoint(minDistanceAdvance, 0)), ),
                                                           ),
                                             hGuidelines = ( minDistanceAdvance, ) )

            # -----------

            maxDistanceAdvance = self.findMinProfileAdvance(profile0, profileMax1)
            self.timing.mark('processKerningPair.022')
            if debugKerning:
                print 'maxDistanceAdvance', maxDistanceAdvance

            if maxDistanceAdvance is None:
                '''
                If no collisions between the glyph profiles, use x-extrema
                plus the max_distance argument.
                '''
                maxDistanceAdvance = minmax0.maxX + self.max_distance - minmax1.minX

            maxDistanceAdvanceSvg = self.renderSvgScene(None,
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(maxDistanceAdvance, 0)) for contour in contours1], ),
                                                           ),
                                             strokePathTuples = (
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
                                             strokePathTuples = (
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
                                             strokePathTuples = (
                                                           ( 0xafff7faf, profilePaths0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(advance, 0)) for contour in profileMaxPaths1], ),
                                                           ),
                                             hGuidelines = ( advance, ),
                                             hRanges = ( ('x_extrema_overlap',
                                                          min(minmax0.maxX, minmax1.minX + advance),
                                                          max(minmax0.maxX, minmax1.minX + advance),
                                                           ), ) )

            # -----------


            self.timing.mark('processKerningPair.8')

            import tfs.common.TFSProject as TFSProject
            mustache_template_file = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'autokern_pair_pixel_template.txt'))
            with open(mustache_template_file, 'rt') as f:
                mustache_template = f.read()

            pageTitle0 = u'Autokern Log:'
            pageTitle1 = u'%s vs. %s' % ( formatGlyphName(ufoglyph0),
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

            mustacheMap = self.makeDefaultMustacheMap(localsMap=locals())

            mustacheMap.update({
                           'pageTitle0': pageTitle0,
                           'pageTitle1': pageTitle1,
                           'minmax0': minmax0,
                           'minmax1': minmax1,

                           'srcSpacingSvg': srcSpacingSvg,
                           'contactAdvanceSvg': contactAdvanceSvg,
                           'minDistanceAdvanceSvg': minDistanceAdvanceSvg,
                           'maxDistanceAdvanceSvg': maxDistanceAdvanceSvg,
                           'intrudingAdvanceSvg': intrudingAdvanceSvg,
                           'finalAdvanceSvg': finalAdvanceSvg,

                           'glyph0': formatGlyphName(ufoglyph0),
                           'glyph1': formatGlyphName(ufoglyph1),

                           'glyphMaps': ( formatGlyphMap(ufoglyph0, minmax0),
                                          formatGlyphMap(ufoglyph1, minmax1),
                                          )
                           })

            import pystache
            logHtml = pystache.render(mustache_template, mustacheMap)

            logFilename = self.getKerningPairHtmlFilename(ufoglyph0, ufoglyph1)
            logFile = os.path.abspath(os.path.join(self.html_folder, logFilename))
            with open(logFile, 'wt') as f:
                # TODO: explicitly encode unicode
                f.write(logHtml)

            self.kerningPairLogFilenames.add(logFilename)

#            import sys
#            sys.exit(0)

        self.timing.mark('processKerningPair.9')

        return True


    def processAllKerningPairs(self):

        print
        print 'Processing kerning pairs...'

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
#                    print
                    continue
                elif firstKernedName == ufoglyph0.name:
                    '''
                    Do not log until we have completed a first successful pass.
                    '''
                    if count % 10 == 0:
                        print '.',
                    continue

                now = time.time()
                if (lastLog is not None) and (now - lastLog < 3.0):
                    '''
                    Do not log more than once per second.
                    '''
                    continue
                if lastLog is None:
                    print
                lastLog = now

                elapsedTime = time.time() - startTime
#                    print 'elapsedTime', elapsedTime, 'total', total
                averageTime = elapsedTime / float(count)
#                    print 'averageTime', averageTime
                totalTime = averageTime * total
                remainingTime = totalTime - elapsedTime

                def formatTimeDuration(value):
                    if value < 60:
                        return '%d seconds' % int(round(value))
                    if value < 60 * 60:
                        return time.strftime('%M:%S', time.gmtime(value))
                    if value < 60 * 60 * 24:
                        return time.strftime('%H:%M:%S', time.gmtime(value))
                    hmsValue = value % (60 * 60 * 24)
                    daysValue = int(round((value - hmsValue) / (60 * 60 * 24)))
                    return '%d days, %s' % ( daysValue,
                                             time.strftime('%H:%M:%S', time.gmtime(hmsValue)), )

                remaining = '%s remaining' % ( formatTimeDuration(remainingTime), )

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

        self.dstCache = AutokernCache()
        self.srcCache = AutokernCache()


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

            self.kerningPairLogFilenames = set()

        self.units_per_em = int(round(self.dstUfoFont.units_per_em))
        self.precision = int(round(self.precision_ems * self.units_per_em))
        self.min_distance = self.min_distance_ems * self.units_per_em
        self.max_distance = self.max_distance_ems * self.units_per_em
#        self.min_non_intrusion  = self.min_non_intrusion_ems * self.units_per_em
        self.kerning_threshold  = self.kerning_threshold_ems * self.units_per_em
        self.max_x_extrema_overlap  = self.max_x_extrema_overlap_ems * self.units_per_em
        self.intrusion_tolerance  = self.intrusion_tolerance_ems * self.units_per_em

        self.ascender = self.srcUfoFont.ascender
        self.descender = self.srcUfoFont.descender
        self.ascender_ems = self.srcUfoFont.ascender / float(self.units_per_em)
        self.descender_ems = self.srcUfoFont.descender / float(self.units_per_em)

#        self.rounding = self.rounding_ems * self.dstUfoFont.units_per_em
        print 'units_per_em', self.units_per_em
        print 'precision', self.precision
        print 'min_distance', self.min_distance
        print 'max_distance', self.max_distance
        print 'intrusion_tolerance', self.intrusion_tolerance
#        print 'min_non_intrusion', self.min_non_intrusion
        print 'kerning_threshold', self.kerning_threshold
        print 'max_x_extrema_overlap', self.max_x_extrema_overlap
#        print 'self.rounding', self.rounding
    #    kerning.fontMetadata = kerning.ufofont.info

        self.timing = TFTiming()
        self.advanceMap = {}
#        self.minAdvanceMap = defaultdict(0)
        self.rasterCache = {}
#        self.dstContoursInflateMinDistanceCache = {}
#        self.dstContoursInflateMaxDistanceCache = {}
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

        minmax = None
        for ufoglyph in self.dstUfoFont.getGlyphs():
            contours = self.dstCache.getGlyphContours(ufoglyph)
            if len(contours) < 1:
                continue
            glyphMinmax = minmaxPaths(contours)
            minmax = minmaxMerge(minmax, glyphMinmax)
        self.allGlyphsMinY = minmax.minY
        self.allGlyphsMaxY = minmax.maxY


    def updateKerning(self):
        print 'Updating kerning...'
        self.dstUfoFont.clearKerning()

        glyphs = self.dstUfoFont.getGlyphs()
        glyphWidthMap = {}
        for ufoglyph in glyphs:
            if ufoglyph.name is None:
                continue
            glyphWidthMap[ufoglyph.name] = ufoglyph.xAdvance

        kerningTuples = []
        for key in self.advanceMap:
            advance = self.advanceMap[key]
            name0, name1 = key
            kerningValue = advance - glyphWidthMap[name0]
            if abs(kerningValue) < self.kerning_threshold:
                continue
            kerningTuples.append( ( name0, name1, kerningValue, ) )

        def cmpKerningTuples(value0, value1):
            return cmp(abs(value0[-1]), abs(value1[-1]))
        kerningTuples.sort(cmpKerningTuples, reverse=True)

#        print 'kerningTuples', kerningTuples[0]
#        print 'kerningTuples[-1]', kerningTuples[-1]

        self.glyph_count = len(glyphs)
        self.kerned_pairs_count = len(self.advanceMap)
        self.valid_kerned_pairs_count = len(kerningTuples)

#        for i in xrange(len(kerningTuples) / 1000):
#            index = i * 1000
#            print 'kerningTuples[%d]' % index, kerningTuples[index]

        if self.max_kerning_pairs:
            self.max_kerning_pairs = max(0, self.max_kerning_pairs)
            kerningTuples = kerningTuples[:self.max_kerning_pairs]

        self.final_kerned_pairs_count = len(kerningTuples)

        for name0, name1, kerningValue in kerningTuples:
            self.dstUfoFont.setKerningPair(name0, name1, kerningValue)


    def clearSideBearings(self):

        if self.pairsToKern is not None:
            return
        if self.glyphsToKern is not None:
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
#            elif self.isIgnoredGlyph(ufoglyph):
#                '''
#                TODO: Should we normalize the side bearings of these glyphs to perhaps half of max_distance?
#                '''
#                continue

            contours = self.dstCache.getGlyphContours(ufoglyph)
#            contours = ufoglyph.getContours()
            if len(contours) == 0:
                '''
                Do not modify width of space and other empty glyphs.
                '''
                continue
            minmax = minmaxPaths(contours)

            if self.isIgnoredGlyph(ufoglyph):
                '''
                TODO: Should we normalize the side bearings of these glyphs to perhaps half of max_distance?
                '''
                defaultSideBearing = self.max_distance * 0.5
                contours = [contour.applyPlus(TFSPoint(defaultSideBearing + -minmax.minX, 0)) for contour in contours]
                ufoglyph.setContours(contours, correctDirection=False)
                ufoglyph.setXAdvance(2 * defaultSideBearing + minmax.maxX - minmax.minX)
                continue

            contours = [contour.applyPlus(TFSPoint(-minmax.minX, 0)) for contour in contours]
            ufoglyph.setContours(contours, correctDirection=False)
            ufoglyph.setXAdvance(minmax.maxX - minmax.minX)

        # Clear the dst cache.
        self.dstCache = AutokernCache()


    def updateSideBearings(self):
        '''
        Rewrite the left and right side bearings of every glyph to be half of the average spacing
        with other glyphs.
        '''

        if self.pairsToKern is not None:
            return
        if self.glyphsToKern is not None:
            return

        print 'Updating side-bearings...'

        modifiedAdvanceMap = {}
        modifiedAdvanceMap.update(self.advanceMap)

        '''
        Removes the left and right side bearings from the glyph.
        '''
        glyphs = self.dstUfoFont.getGlyphs()
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))

        glyphWidthMap = {}
        for ufoglyph in glyphs:
            if ufoglyph.name is None:
                continue
            glyphWidthMap[ufoglyph.name] = ufoglyph.xAdvance

        #

        leftKeyMap = {}
        rightKeyMap = {}
        for key in self.advanceMap:
            advance = self.advanceMap[key]
            name0, name1 = key
            spacing = advance - glyphWidthMap[name0]

            leftKeyList = leftKeyMap.get(name1, [])
            leftKeyList.append( ( key, advance, spacing, ) )
            leftKeyMap[name1] = leftKeyList

            rightKeyList = rightKeyMap.get(name0, [])
            rightKeyList.append( ( key, advance, spacing, ) )
            rightKeyMap[name0] = rightKeyList

        #

        if USE_CACHED_KERNING_MAP:
            for ufoglyph in glyphs:
                contours = self.dstCache.getGlyphContours(ufoglyph)
#            print

#        for key in self.advanceMap:
#            if key in (
#                       ('N','N',),
##                       ('A','A',),
##                        ('A','F',),
#                        ):
#                print 'self.advanceMap', key, self.advanceMap[key]

        for ufoglyph in glyphs:
            if self.glyphsToKern is not None:
                if ufoglyph.name not in self.glyphsToKern:
                    continue
            elif self.isIgnoredGlyph(ufoglyph):
                continue

            contours = self.dstCache.getGlyphContours(ufoglyph)

            if len(contours) == 0:
                '''
                Do not modify width of space and other empty glyphs.
                '''
                continue

            rightSpacings = []
            rightKeys = []
            leftSpacings = []
            leftKeys = []

            for key, advance, spacing in leftKeyMap[ufoglyph.name]:
                leftSpacings.append(spacing)
                leftKeys.append(key)
            for key, advance, spacing in rightKeyMap[ufoglyph.name]:
                rightSpacings.append(spacing)
                rightKeys.append(key)

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

#            if ufoglyph.name in (
#                                 'N',
##                                  'A',
##                                  'F',
#                                   ):
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

#            if ufoglyph.name in (
#                                 'N',
##                                  'A',
##                                  'F',
#                                   ):
#                print 'updateSideBearings.1', 'leftSideBearing', leftSideBearing, 'rightSideBearing', rightSideBearing, 'ufoglyph.xAdvance', ufoglyph.xAdvance

            '''
            Lastly, update the kerning values in the advance map.

            The LSBs effect the advance maps, but the RSBs don't, because the
            advance map represents the kerned advance, not the kerning value itself.
            '''
            for key in leftKeys:
                modifiedAdvanceMap[key] = modifiedAdvanceMap[key] - leftSideBearing
            for key in rightKeys:
#                modifiedAdvanceMap[key] = modifiedAdvanceMap[key] + leftSideBearing - rightSideBearing
                modifiedAdvanceMap[key] = modifiedAdvanceMap[key] + leftSideBearing


#        for key in self.advanceMap:
#            if key in (
#                       ('N','N',),
##                       ('A','A',),
##                        ('A','F',),
#                        ):
#                print 'self.advanceMap', key, self.advanceMap[key]
#        for key in modifiedAdvanceMap:
#            if key in (
#                       ('N','N',),
##                       ('A','A',),
##                        ('A','F',),
#                        ):
#                print 'modifiedAdvanceMap', key, modifiedAdvanceMap[key]

        '''
        Replace the advance map.
        '''
        self.advanceMap = modifiedAdvanceMap

        # Clear the dst cache.
        self.dstCache = AutokernCache()


    def assessKerningPair(self, ufoglyph0, ufoglyph1):

        contours0 = self.dstCache.getGlyphContours(ufoglyph0)
        contours1 = self.dstCache.getGlyphContours(ufoglyph1)

        if (not contours0) or (not contours1):
            return None

        kerning = self.dstUfoFont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
        if kerning is None:
            kerning = 0
        advance = ufoglyph0.xAdvance + kerning

        profile0 = self.makeProfile(func=max, paths=contours0)
        profile1 = self.makeProfile(func=min, paths=contours1)

        def convertToPixelUnits(value):
            return int(math.ceil(value / float(self.precision)))

        '''
        Find the closest pair of pixels.
        '''
        minDistanceSqrd = None
        for y0, x0 in enumerate(profile0):
            for y1, x1 in enumerate(profile1):
                if x0 is None or x1 is None:
                    continue
                diffX = x0 - (x1 + advance / float(self.precision))
                diffY = y0 - y1
                distanceSqrd = (diffX * diffX) + (diffY * diffY)
                if (minDistanceSqrd is None) or (distanceSqrd < minDistanceSqrd):
                    minDistanceSqrd = distanceSqrd

        if minDistanceSqrd is None:
            return None
        else:
            minDistance = math.sqrt(float(minDistanceSqrd))
            return minDistance * self.precision


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


    def convertTextToContours(self, text, ufoFont, lastKerningValues=None):
        outsideContours = []
        insideContours = []
        labels = []
        kerningValues = []
        xOffset = 0
        lastUfoGlyph = None
        lastMinmax = None
        for index, textGlyph in enumerate(text):
            codePoint = ord(textGlyph)
            ufoglyph = ufoFont.getGlyphByCodePoint(codePoint)
            if ufoglyph is None:
                print 'Unknown glyph in sample text: %s %s' % (textGlyph, formatUnicode(codePoint),)
                return None
#                if len(contours) < 1:
#                    continue

            contours = self.dstCache.getGlyphContours(ufoglyph)
#            contours = ufoglyph.getContours(warnings=False)
#                contours = self.getGlyphContours(ufoglyph)

            '''
            We use robofab's correctDirection() method to correctly orient the
            inside and outside contours in truetype orientation.

            We don't want to effect the output, so we do this in a temporary font.
            '''
            tempUfoFont = robofab.world.NewFont(familyName='ignore', styleName='ignore')
            tempUfoGlyph = tempUfoFont.newGlyph('ignore')
            tempTFSGlyph = TFSGlyph(tempUfoGlyph)
            tempTFSGlyph.setContours(contours, correctDirection=True)
            contours = tempTFSGlyph.getContours(warnings=False)

            kerningValue = None
            if lastUfoGlyph is None:
                minmax = minmaxPaths(contours)
                xOffset = -minmax.minX
            else:
#                if lastUfoGlyph is not None:
                kerningValue = ufoFont.getKerningPair(lastUfoGlyph.name, ufoglyph.name, )
                if kerningValue is not None:
                    xOffset += kerningValue
                else:
                    kerningValue = 0


            contours = [contour.applyPlus(TFSPoint(xOffset, 0)) for contour in contours]
            minmax = minmaxPaths(contours)

            if kerningValue is not None:
                xExtremaOverlap = minmax.minX - lastMinmax.maxX
#                    text = '%0.0f/%s%0.0f' % (
#                                                 float(kerningValue),
#                                                 '+' if xExtremaOverlap > 0 else '-',
#                                                 float(abs(xExtremaOverlap)),
#                                                 )
                text = '%d' % ( int(xExtremaOverlap), )

                KERNING_LABEL_COLOR = 0xdf000000
                if lastKerningValues is not None:
                    lastXExtremaOverlap = lastKerningValues[index - 1]
                    xExtremaOverlapDelta = xExtremaOverlap - lastXExtremaOverlap
                    KERNING_HIGHLIGHT_LOW_THRESHOLD = 10
                    KERNING_HIGHLIGHT_HIGH_THRESHOLD = 20
                    if abs(xExtremaOverlapDelta) >= KERNING_HIGHLIGHT_HIGH_THRESHOLD:
                        KERNING_LABEL_COLOR = 0xdfa70000
                    elif abs(xExtremaOverlapDelta) >= KERNING_HIGHLIGHT_LOW_THRESHOLD:
                        KERNING_LABEL_COLOR = 0xdf530000

                    text += ' (%s%0.0f)' % (
                                           '' if xExtremaOverlapDelta == 0 else ('+' if xExtremaOverlapDelta > 0 else '-'),
                                           float(abs(xExtremaOverlapDelta)),
                                           )


                label = TFSMap()
                label.text = text
                label.origin = TFSPoint(xOffset, -abs(self.descender * 1.1))
                label.fillColor = KERNING_LABEL_COLOR
                label.params = {
                                       'text-anchor': 'middle',
                                       'dominant-baseline': 'text-before-edge',
                                       'font-family': "Lato, Helvetica, Arial, sans-serif;",
#                                           'font-size': "14px",
#                                           'font-weight': "bold",
                                       }
                labels.append(label)
                kerningValues.append( xExtremaOverlap )

            lastMinmax = minmax

            for contour in contours:
                if isClosedPathClockwise(contour):
                    outsideContours.append(contour)
                else:
                    insideContours.append(contour)

            xOffset += ufoglyph.xAdvance
            lastUfoGlyph = ufoglyph

        return outsideContours, insideContours, labels, kerningValues


    def renderTextWithFont(self, text, ufoFont, source, fillColor, lastKerningValues=None):
        converted = self.convertTextToContours(text, ufoFont, lastKerningValues=lastKerningValues)
        if converted is None:
            return {'errorMap': {'text': text,
                                 'source': source,
                                 'message': 'error'},
                    }, None
        else:
            outsideContours, insideContours, labels, kerningValues = converted

            sampleSvg = self.renderSvgScene(None,
                                            fillPathTuples = ( ( fillColor, outsideContours, ),
                                                               ( 0xffffffff, insideContours, ),
                                                               ),
                                            textTuples = labels,
                                            bottomPadding = 20,
                                            )
            return {'renderMap': {'text': text,
                   'source': source,
                   'svg': sampleSvg},
                   }, kerningValues


    def writeSamples(self):
        '''
        hh vs. nn
        '''

        renderLog = self.log_dst is not None
        if not renderLog:
            return
        print 'Writing samples...'


        sampleTexts = (
                       'Typography',
                       'WAVE',
                       'COLT',
                       'Style',
                       'enjoying',
                       'hamburgerfont',
                       'NNOOoo',
                       'pqpiitt',
                       'ijiJn.',
                       'N-N=NtN',
                       )
        sampleTextsMaps = []
        for sampleText in sampleTexts:
            sampleTextMap, kerningValues = self.renderTextWithFont(sampleText, self.srcUfoFont, 'Original', 0x7f7f7faf)
            sampleTextsMaps.append(sampleTextMap)
            sampleTextMap, _ = self.renderTextWithFont(sampleText, self.dstUfoFont, 'Autokern', 0x7f7faf7f,
                                                       lastKerningValues=kerningValues)
            sampleTextsMaps.append(sampleTextMap)


        pageTitle = u'Autokern Sample Texts'

        mustacheMap = self.makeDefaultMustacheMap(localsMap=locals())
        mustacheMap.update({
                   'pageTitle': pageTitle,
                   'sampleTextsMaps': sampleTextsMaps,
                   })

        import tfs.common.TFSProject as TFSProject
        mustache_template_file = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'autokern_samples_template.txt'))
        with open(mustache_template_file, 'rt') as f:
            mustache_template = f.read()

        import pystache
        logHtml = pystache.render(mustache_template, mustacheMap)

        logFilename = 'sample_texts.html'
        logFile = os.path.abspath(os.path.join(self.html_folder, logFilename))
        with open(logFile, 'wt') as f:
            # TODO: explicitly encode unicode
            f.write(logHtml)


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

        if not self.do_not_modify_side_bearings:
#            print 'updateSideBearings'
            self.updateSideBearings()
            self.timing.mark('updateSideBearings.')

#        print 'updateKerning'
        self.updateKerning()
        self.timing.mark('updateKerning.')

        self.logDisparities()
        self.timing.mark('logDisparities.')

        self.writeSamples()
        self.timing.mark('writeSamples.')

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
