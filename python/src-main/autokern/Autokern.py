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
import traceback

try:
    locale.setlocale(locale.LC_ALL, 'en_US')
except locale.Error, e:
    print 'Could not set locale:', str(e)

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
#USE_CACHED_KERNING_MAP = True

DEBUG_h_n_ISSUE = False
#DEBUG_h_n_ISSUE = True


DEFAULT_SAMPLE_TEXTS = (
               'Typography',
               'WAVE',
               'COLT',
               'Style',
               'enjoying',
               'hamburgerfont',
               'tragedy',
               'success',
               'lavas',
               'TTttrf', # min distance
               '||NNnnOOoo', # max distance
               'rtryvjj',
               'pqpiitt',
               'ijiJn.',
               'N-N=NtN',
               'TaLTLYPJ', # x-extrema overlap
               'VAWML4TO',
               'hhnnhn',
               'JFrf',
               'WaToYaVa',
#                'Alphabet',
                
'MOUNTAIN',
'LAKE',
'heyboy',
'1234567890',
'L7L4',
'+5-3=74%',
'8*7/6^2',
'a@b.com',
'(ok)[4]<4>{4}',
'1' + unichr(194) + unichr(162) + '2' + unichr(194) + unichr(163) + '3' + unichr(194) + unichr(165) + '4$5' + unichr(226) + unichr(130) + unichr(172),
'#7+&>>?',
'//\+_T' + unichr(195) + unichr(134),
unichr(208) + unichr(148) + unichr(208) + unichr(160) + unichr(208) + unichr(163) + unichr(208) + unichr(147) + unichr(208) + unichr(144) + unichr(208) + unichr(160) + unichr(208) + unichr(152),
unichr(208) + unichr(147) + '-' + unichr(208) + unichr(150) + unichr(208) + unichr(138) + '7' + unichr(208) + unichr(147) + unichr(208) + unichr(136),
unichr(206) + unichr(147) + '-' + unichr(206) + unichr(148) + unichr(206) + unichr(154) + '-' + unichr(206) + unichr(167),
unichr(206) + unichr(182) + '*' + unichr(206) + unichr(187) + unichr(207) + unichr(130) + unichr(206) + unichr(155) + unichr(206) + unichr(168),
                                
               'O!O?O.O;O;O,',
               'o!o?o.o;o;o,',
               'r!r?r.r;r;r,',
               'N!N?N.N;N;N,',
               )

def formatUnicodeStringLiteral(value):
    result = []
    for c in value:
        if ord(c) < 127:
            result.append('\'' + c + '\'')
        else:
            result.append('unichr(%d)' % ord(c))
    return ' + '.join(result)

def formatUnicodeForHtml(value):
    result = []
    for c in value:
        result.append(u'&#%d;' % ord(c) )
    return ''.join(result)

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

def formatGlyphNameShort(glyph):
    if glyph.unicode is None:
        return glyph.name
    else:
        return u'&#%d;' % ( glyph.unicode, )

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

def mergeMustacheMaps(srcMap, dstMap, prefix):
    for key, value in srcMap.items():
        dstMap[prefix + key] = value

def formatEms(value):
    return '%0.3f em' % (value,)

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

def xTranslateContours(contours, value):
    if value == 0:
        return contours
    return [contour.applyPlus(TFSPoint(value, 0)) for contour in contours]


def minmaxPathsEvaluatedWithinYRange(paths, precision, minY, maxY):
    allPoints = []
    for path in paths:
        for segment in path:
            if segment.isStraight():
                startPoint = segment.startPoint()
                allPoints.append(startPoint)
                endPoint = segment.endPoint()
                allPoints.append(endPoint)

                minYPoint = TFSIntersection.calculateIntersectPoint(startPoint, endPoint,
                                                                        TFSPoint(min(startPoint.x, endPoint.x) - 1, minY),
                                                                        TFSPoint(max(startPoint.x, endPoint.x) + 1, minY))
                if minYPoint:
                    allPoints.append(minYPoint)
                maxYPoint = TFSIntersection.calculateIntersectPoint(startPoint, endPoint,
                                                                        TFSPoint(min(startPoint.x, endPoint.x) - 1, maxY),
                                                                        TFSPoint(max(startPoint.x, endPoint.x) + 1, maxY))
                if maxYPoint:
                    allPoints.append(maxYPoint)
            else:
                allPoints.extend(segment.evaluateRangeWithPrecision(precision))
    validPoints = [point for point in allPoints if minY <= point.y <= maxY]
    return minmaxPoints(validPoints)
    return minmaxPoints(validPoints)


class AutokernCache(TFSMap):

    def __init__(self):
        TFSMap.__init__(self)

    def getCachedValue(self, key, func, *argv):
        if key in self:
#            print 'cache hit'
            return self[key]
        result = func(*argv)
        self[key] = result
#        print 'cache miss'
        return result

    def getGlyphContours(self, ufoglyph):
        def getCachedContours():
            contours = ufoglyph.getContours(warnings=False)
            return contours
        return self.getCachedValue('getCachedContours %s' % ufoglyph.name, getCachedContours)

    def getContoursMinmax(self, ufoglyph):
        def getCachedMinmax():
            contours = self.getGlyphContours(ufoglyph)
            return minmaxPathsEvaluated(contours, AUTOKERN_SEGMENT_PRECISION)
        return self.getCachedValue('getCachedMinmax %s' % ufoglyph.name, getCachedMinmax)

    def getAdjMinmax(self, ufoglyph, context):
        if not context.ignore_x_extrema_overlap_outside_ascender:
            return self.getContoursMinmax(ufoglyph)

        def getCachedAdjMinmax():
            contours = self.getGlyphContours(ufoglyph)
            return minmaxPathsEvaluatedWithinYRange(contours, AUTOKERN_SEGMENT_PRECISION, 0, context.ascender)
        return self.getCachedValue('getCachedAdjMinmax %s' % ufoglyph.name, getCachedAdjMinmax)


class Autokern(TFSMap):

    def __init__(self, argumentsMap):
        TFSMap.__init__(self)
        self.argumentsMap = argumentsMap
        for key, value in argumentsMap.items():
            setattr(self, key, value)


    def configureLogging(self):

        if self.log_path is None:
            return

        if os.path.exists(self.log_path):
            for index in xrange(1, 100000):
                oldLogsPath = os.path.join(os.path.dirname(self.log_path),
                                           os.path.basename(self.log_path) + '.' + str(index))
                if not os.path.exists(oldLogsPath):
                    break
            os.rename(self.log_path, oldLogsPath)
            if os.path.exists(self.log_path):
                raise Exception('Could not rename exists logs folder: ' + self.log_path)
            print 'Renaming old logs folder to:', oldLogsPath

        os.mkdir(self.log_path)
        if not (os.path.exists(self.log_path) and os.path.isdir(self.log_path)):
            raise Exception('Could not create logs folder: %s' % self.log_path)

        self.html_folder = self.log_path

        def makeLogSubfolder(parent, name):
            subfolder = os.path.abspath(os.path.join(parent, name))
            os.mkdir(subfolder)
            if not (os.path.exists(subfolder) and os.path.isdir(subfolder)):
                raise Exception('Invalid log_path: %s' % self.log_path)
            return subfolder

        self.css_folder = makeLogSubfolder(self.html_folder, 'stylesheets')

        import tfs.common.TFSProject as TFSProject
        srcCssFile = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'styles.css'))
        dstCssFile = os.path.abspath(os.path.join(self.css_folder, os.path.basename(srcCssFile)))
        shutil.copy(srcCssFile, dstCssFile)

        self.logFileTuples = []


    def configure(self):

        print 'Processing configuration...'

        self.dstCache = AutokernCache()
        self.srcCache = AutokernCache()

        ufo_src_path = self.ufo_src_path
        if ufo_src_path is None:
            raise Exception('Missing ufo_src_path')
        if not (os.path.exists(ufo_src_path) and os.path.isdir(ufo_src_path) and os.path.basename(ufo_src_path).lower().endswith('.ufo')):
            raise Exception('Invalid ufo_src_path: %s' % ufo_src_path)

        self.srcUfoFont = TFSFontFromFile(ufo_src_path)
        self.dstUfoFont = TFSFontFromFile(ufo_src_path)
        self.srcFilename = os.path.basename(ufo_src_path)
        self.src_kerning_value_count = self.srcUfoFont.getKerningPairCount()
        self.glyph_count = len(self.srcUfoFont.getGlyphs())


        if self.ufo_dst_path is None:
            raise Exception('Missing ufo_dst_path')
        if os.path.exists(self.ufo_dst_path):
            if os.path.isdir(self.ufo_dst_path):
                shutil.rmtree(self.ufo_dst_path)
            elif os.path.isfile(self.ufo_dst_path):
                os.unlink(self.ufo_dst_path)
            if os.path.exists(self.ufo_dst_path):
                raise Exception('Could not overwrite: %s' % (self.ufo_dst_path,))


        self.configureLogging()


        self.units_per_em = int(round(self.dstUfoFont.units_per_em))
        for key, value in self.argumentsMap.items():
            if key.endswith('_ems'):
                setattr(self, key[:-len('_ems')], value * self.units_per_em)
        self.precision = int(round(self.precision))

        if self.min_distance > self.max_distance:
            raise Exception('--min-distance-ems value (%0.3f) cannot be greater than --max-distance-ems value (%0.3f)' % (self.min_distance_ems,
                                                                                                                          self.max_distance_ems,
                                                                                                                          ) )
        if self.only_modify_side_bearings and self.do_not_modify_side_bearings:
            raise Exception('--only-modify-side-bearings and --do-not-modify-side-bearings arguments cannot be used together.')

        self.ascender = self.srcUfoFont.ascender
        self.descender = self.srcUfoFont.descender
        self.ascender_ems = self.srcUfoFont.ascender / float(self.units_per_em)
        self.descender_ems = self.srcUfoFont.descender / float(self.units_per_em)

        self.timing = TFTiming()
        self.advanceMap = {}
        self.rasterCache = {}
        self.pixelsCache = {}
        self.pairsToKern = None
        self.glyphsToKern = None
        self.sampleTexts = list(DEFAULT_SAMPLE_TEXTS)

        #

        glyphs = self.srcUfoFont.getGlyphs()
        glyphCodePoints = set()
        glyphNames = set()
        glyphCodePointToNameMap = {}
        self.ignoredGlyphNames = set()
        for glyph in glyphs:
            if glyph.unicode is not None:
                glyphCodePoints.add(glyph.unicode)
            if glyph.name is None:
                raise Exception('Glyph missing name')
            if glyph.name in glyphNames:
                raise Exception('Duplicate glyph name: ' + glyph.name)
            glyphNames.add(glyph.name)
            if glyph.unicode is not None:
                glyphCodePointToNameMap[glyph.unicode] = glyph.name
#            if self.isIgnoredGlyph(glyph):
#                self.ignoredGlyphNames.add(glyph.name)

        '''
        Parse glyph categories, Step 1: parse the --glyph-categories argument.
        '''

        import AutokernGlyphClasses
        allGlyphCategories = AutokernGlyphClasses.unicodedataCategoryMap.keys()
        allGlyphWildcardCategories = set()
        for category in allGlyphCategories:
            categoryMajorWildcard = category[:-1] + '*'
            allGlyphWildcardCategories.add(categoryMajorWildcard)

        self.glyphNameToCategoryMap = {}
        self.missingCategoryGlyphNames = []
        self.defaultGlyphCategory = None

        if self.glyph_categories is not None:
#            if len(self.glyph_categories) < 1:
#                raise Exception('Missing --glyph-categories value')
            if len(self.glyph_categories) % 2 != 0:
                raise Exception('Uneven number of  --glyph-categories values')
            for index in xrange(len(self.glyph_categories) / 2):
                value0 = self.glyph_categories[index * 2 + 0]
                value1 = self.glyph_categories[index * 2 + 1]

                category = value1
                if category not in allGlyphCategories:
#                if ((category not in allGlyphCategories) and
#                    (category not in allGlyphWildcardCategories)):
                    raise Exception('Unknown glyph category: ' + category)

                glyphName = value0
                if glyphName == '*':
                    self.defaultGlyphCategory = category
                else:
                    glyphName = self.parseCodePoint('-glyph-categories', glyphNames, glyphName)
                    if glyphName in self.ignoredGlyphNames:
                        continue
                    self.glyphNameToCategoryMap[glyphName] = category


        '''
        Parse glyph categories, Step 2: Verify that all glyphs are associated with a valid category.
        '''
        for glyph in glyphs:
            category = self.getUnicodeCategory(glyph)
            if glyph.name in self.glyphNameToCategoryMap:
                '''
                Category already set by --glyph-categories argument.
                '''
                continue
            if glyph.name == '.notdef':
                '''
                An exception: it is okay if .notdef has no category.
                '''
                continue
            elif category is None:
                if self.defaultGlyphCategory is not None:
                    category = self.defaultGlyphCategory
                else:
                    #                print 'Missing glyph category:', glyph.name
                    self.missingCategoryGlyphNames.append(glyph.name)
            self.glyphNameToCategoryMap[glyph.name] = category

        if len(self.missingCategoryGlyphNames) > 0:
            print 'Glyphs with unknown unicode category:', ', '.join(sorted(self.missingCategoryGlyphNames))
            raise Exception('%d Glyph%s with unknown unicode category. Use the --glyph-categories argument to specify a category for each glyph.' %
                            ( len(self.missingCategoryGlyphNames),
                              's' if len(self.missingCategoryGlyphNames) > 1 else '', ))

        #

        if self.sample_texts is not None:
            if len(self.sample_texts) < 1:
                raise Exception('Missing --sample-texts value')
            for sampleText in self.sample_texts:
                if len(sampleText) < 1:
                    raise Exception('Invalid --sample-texts value: %s' % sampleText)
                for glyph in sampleText:
                    if ord(glyph) not in glyphCodePoints:
                        raise Exception('--sample-texts value: %s has unknown glyph: %s' % (sampleText, glyph,))

            # Use sample texts.
            self.sampleTexts = self.sample_texts

        #

        self.ignoredGlyphNames.add('.notdef')
        if self.glyphs_to_ignore is not None:
#            ignoreArguments.append('--glyphs-to-ignore')
            if len(self.glyphs_to_ignore) < 1:
                raise Exception('Missing --glyphs-to-ignore value')
            for value in self.glyphs_to_ignore:
                self.ignoredGlyphNames.add(self.parseCodePoint('--glyphs-to-ignore', glyphNames, value))
        if self.glyph_categories_to_ignore is not None:
#            ignoreArguments.append('--glyph-categories-to-ignore')
#            if len(self.glyph_categories_to_ignore) < 1:
#                raise Exception('Missing --glyph-categories-to-ignore value')
            for category in self.glyph_categories_to_ignore:
                categoryWildcard = category[:-1] + '*'
                if ((category not in allGlyphCategories) and
                    (categoryWildcard not in allGlyphWildcardCategories)):
                    print 'Unknown glyph category:', category

            for glyph in glyphs:
                if glyph.name == '.notdef':
                    continue
                category = self.glyphNameToCategoryMap[glyph.name]
                if category is None:
                    print 'Missing glyph category:', glyph.name
                else:
                    categoryWildcard = category[:-1] + '*'
                    if ((category in self.glyph_categories_to_ignore) or
                        (categoryWildcard in self.glyph_categories_to_ignore)):
                        self.ignoredGlyphNames.add(glyph.name)
#                    else:
#                        if self.isIgnoredGlyph(glyph):
#                            print '\t', 'ignored Glyph?', glyph.name, 'category', category

        print 'ignoring %s / %s glyphs' %  ( locale.format("%d", len(self.ignoredGlyphNames), grouping=True),
                                             locale.format("%d", len(glyphs), grouping=True), )

        #

        scopeArguments = []
        if self.glyph_pairs_to_kern is not None:
            scopeArguments.append('--glyph-pairs-to-kern')
            if len(self.glyph_pairs_to_kern) < 1:
                raise Exception('Missing --glyph-pairs-to-kern value')
            if len(self.glyph_pairs_to_kern) % 2 != 0:
                raise Exception('Uneven number of  --glyph-pairs-to-kern values')
            self.pairsToKern = set()
            for index in xrange(len(self.glyph_pairs_to_kern) / 2):
                value0 = self.glyph_pairs_to_kern[index * 2 + 0]
                value1 = self.glyph_pairs_to_kern[index * 2 + 1]
                name0 = self.parseCodePoint('-glyph-pairs-to-kern', glyphNames, value0)
                name1 = self.parseCodePoint('-glyph-pairs-to-kern', glyphNames, value1)
                if name0 in self.ignoredGlyphNames or name1 in self.ignoredGlyphNames:
                    print 'ignoring --pairs-to-kern value:', value
                else:
                    self.pairsToKern.add(( name0, name1, ))
        if self.glyphs_to_kern is not None:
            scopeArguments.append('--glyphs-to-kern')
            if len(self.glyphs_to_kern) < 1:
                raise Exception('Missing --glyphs-to-kern value')
            self.glyphsToKern = set()
#            print 'self.glyphs_to_kern', self.glyphs_to_kern
            for value in self.glyphs_to_kern:
                name = self.parseCodePoint('--glyphs-to-kern', glyphNames, value)
                if name in self.ignoredGlyphNames:
                    print 'ignoring --glyphs-to-kern value:', value
                else:
                    self.glyphsToKern.add(name)
        if self.kern_samples_only:
            scopeArguments.append('--kern-samples-only')
            self.pairsToKern = set()
            for sampleText in self.sampleTexts:
                lastGlyphName = None
                for glyph in sampleText:
                    if ord(glyph) not in glyphCodePointToNameMap:
                        '''
                        We've already validated the sample texts.
                        Ignore missing characters in the default sample texts.
                        '''
                        continue
                    glyphName = glyphCodePointToNameMap.get(ord(glyph))
                    if glyphName is not None and lastGlyphName is not None:
                        self.pairsToKern.add( (lastGlyphName, glyphName,) )
                    lastGlyphName = glyphName

        notIgnoredGlyphs = len(glyphs) - len(self.ignoredGlyphNames)
        if self.pairsToKern is not None:
            print 'kerning %s / %s pairs' % ( locale.format("%d", len(self.pairsToKern), grouping=True),
                                              locale.format("%d", notIgnoredGlyphs * notIgnoredGlyphs, grouping=True), )
        elif self.glyphsToKern is not None:
            print 'kerning %s / %s glyphs' % ( locale.format("%d", len(self.glyphsToKern), grouping=True),
                                               locale.format("%d", len(glyphs), grouping=True), )
        else:
            print 'kerning %s glyphs, %s pairs' % ( locale.format("%d", notIgnoredGlyphs, grouping=True),
                                                    locale.format("%d", notIgnoredGlyphs * notIgnoredGlyphs, grouping=True), )

        if len(scopeArguments) > 1:
            raise Exception('Do not use more than one of the %s arguments.' % (' '.join(scopeArguments),))

        #

        def isValidGlyphCategories(key, value):
            if type(value) not in ( types.StringType,
                                    types.UnicodeType, ):
                raise Exception('Invalid %s value: %s' % (key, value,))
            if value in allGlyphCategories:
                return value
            if value[-1] == '*':
                valueMajor = value[:-1]
                categoriesMajor = set([category[0] for category in allGlyphCategories])
                if valueMajor in categoriesMajor:
                    return value
            raise Exception('Invalid unicodedata category value: ' + value)

        def parseFloatPerCategoryMap(key, values, minValue, maxValue):
            resultMap = {}
            resultKeys = []
            if values is not None:
                if len(values) < 1:
                    raise Exception('Missing %s value' % key)
                if len(values) % 2 != 0:
                    raise Exception('Uneven number of  %s values' % key)
                for index in xrange(len(values) / 2):
                    value0 = values[index * 2 + 0]
                    value1 = values[index * 2 + 1]
                    isValidGlyphCategories('%s' % key, value0)
                    try:
                        value1 = float(value1)
                        if not (minValue <= value1 <= maxValue):
                            raise Exception('Invalid %s value: %s' % (key, str(value1),))
                        value1 *= self.units_per_em
                    except ValueError, e:
                        raise Exception('Invalid %s value: %s' % (key, str(value1),))

                    resultMap[value0] = value1
                    resultKeys.append(value0)
            return resultMap, resultKeys

        def getGlyphCategoryValue(categoryMap, categoryKeys, glyph):
            result = []
            if glyph.name not in self.glyphNameToCategoryMap:
                return result
            category = self.glyphNameToCategoryMap[glyph.name]
            if category is None:
                return result
            if category in categoryMap:
                result.append( ( categoryMap[category],
                                 categoryKeys.index(category), ) )
            categoryMajor = category[:-1] + '*'
            if categoryMajor in categoryMap:
                result.append( ( categoryMap[categoryMajor],
                                 categoryKeys.index(categoryMajor), ) )
            return result

        def getGlyphPairCategoryValue(categoryMap, categoryKeys,
                                      defaultValue, glyph0, glyph1):
            '''
            The LAST category rule has precedence.
            '''
            values = []
            values.extend(getGlyphCategoryValue(categoryMap, categoryKeys, glyph0))
            values.extend(getGlyphCategoryValue(categoryMap, categoryKeys, glyph1))
#            print 'values', values
            if len(values) < 1:
                return defaultValue
            bestValue, bestIndex = values[0]
            for value, index in values[1:]:
                if index > bestIndex:
                    bestValue, bestIndex = value, index

            return bestValue


        def parseFloatPerCategoryProperty(name, minValue, maxValue):
            '''
            self.max_x_extrema_overlap_categoryMap = parseFloatPerCategoryMap('--max-x-extrema-overlap-ems-per-category',
                                                                              self.max_x_extrema_overlap_ems_per_category,
                                                                              -1.0, 1.0)
            '''
            valuesName = name.replace('-', '_')[2:]
            values = getattr(self, valuesName)
            defaultValueName = valuesName[:-len('-ems-per-category')]
            defaultValue = getattr(self, defaultValueName)
            valueMap, valueKeys = parseFloatPerCategoryMap(name, values,
                                                           -1.0, 1.0)
            '''
            We want the LAST rules to have precedence, so we reverse order.
            '''
            valueKeys.reverse()
            setattr(self, defaultValueName + '_valueMap', valueMap)
            setattr(self, defaultValueName + '_valueKeys', valueKeys)
            def getterFunc(glyph0, glyph1):
#                print 'defaultValueName', defaultValueName
#                print 'valuesName', valuesName
#                print 'valueMap', valueMap
#                print 'valueKeys', valueKeys
                return getGlyphPairCategoryValue(valueMap,
                                                 valueKeys,
                                                 defaultValue,
                                                 glyph0, glyph1)
            getterFuncName = 'getGlyphPair_' + defaultValueName
            setattr(self, getterFuncName, getterFunc)


        self.max_x_extrema_overlap_categoryMap = parseFloatPerCategoryProperty('--max-x-extrema-overlap-ems-per-category',
                                                                               -1.0, 1.0)
        self.min_distance_categoryMap = parseFloatPerCategoryProperty('--min-distance-ems-per-category',
                                                                      0.0, 1.0)
        self.max_distance_categoryMap = parseFloatPerCategoryProperty('--max-distance-ems-per-category',
                                                                      0.0, 1.0)
        self.intrusion_tolerance_categoryMap = parseFloatPerCategoryProperty('--intrusion-tolerance-ems-per-category',
                                                                             0.0, 1.0)
        self.tracking_categoryMap = parseFloatPerCategoryProperty('--tracking-ems-per-category',
                                                                  0.0, 1.0)

        #

        minmax = None
        for ufoglyph in self.dstUfoFont.getGlyphs():
            contours = self.dstCache.getGlyphContours(ufoglyph)
            if len(contours) < 1:
                continue
            glyphMinmax = self.dstCache.getContoursMinmax(ufoglyph)
            minmax = minmaxMerge(minmax, glyphMinmax)
        allGlyphsMinY = minmax.minY
        allGlyphsMaxY = minmax.maxY
        #
        if self.max_distance_valueMap:
            max_max_distance = max(self.max_distance,
                                   reduce(max, self.max_distance_valueMap.values()))
        else:
            max_max_distance = self.max_distance
        self.profileMaxYunits = int(math.ceil((allGlyphsMaxY + max_max_distance) / float(self.precision)))
        self.profileMinYunits = int(math.floor((allGlyphsMinY - max_max_distance) / float(self.precision)))


    def formatUnitsInEms(self, value):
        return formatEms(value / float(self.units_per_em))

    def addSidebarMustacheMap(self, mustacheMap, kerned, complete=False):
        vars = (
                ( 'Filename', 'srcFilename',),
                ( 'Family', 'familyName',),
                ( 'Style', 'styleName',),
                ( 'Units per em', 'units_per_em',),
                ( 'Ascender', 'ascender_ems',),
                ( 'Descender', 'descender_ems',),
                ( 'Precision', 'precision_ems',),
#                ( 'Minimum Distance', 'min_distance_ems',),
#                ( 'Maximum Distance', 'max_distance_ems',),
#                ( 'Tracking', 'tracking_ems',),
#                ( 'Intrusion Tolerance', 'intrusion_tolerance_ems',),
##                ( 'Intrusion Min. Thickness', 'intrusion_min_thickness_ems',),
#                ( 'Max. x-extrema Overlap', 'max_x_extrema_overlap_ems',),
#                ( 'x-extrema Overlap Scaling', 'x_extrema_overlap_scaling',),
                ( 'Total Glyphs', 'glyph_count',),
                )

        if kerned:
            vars += (
                ( 'Original Kerning Values', 'src_kerning_value_count',),
                ( 'Kerned Pairs', 'kerned_pairs_count',),
                ( 'Valid Kerning Values', 'valid_kerned_pairs_count',),
                )
            if self.max_kerning_pairs:
                vars += (
                    ( 'Final Kerning Values', 'final_kerned_pairs_count',),
                    )

        if complete:
            vars += (
                ( 'Elapsed', 'elapsedDatetime',),
                ( 'Completed', 'finishDatetime',),
                )

        varMaps = []
        for name, key in vars:
            varMaps.append({'sidebarVarName': name,
                            'sidebarVarValue': mustacheMap[key],
                            })
        mustacheMap['sidebarVars'] = varMaps

        argMaps = []
        for key in sorted(self.argumentsMap):
            value = self.argumentsMap[key]
            if key.endswith('_path'):
                continue
            if value is None:
                continue
            if type(value) == types.BooleanType:
                if value:
                    argMaps.append({'sidebarVarName': '--' + key.replace('_', '-'),
                                    'sidebarVarValue': '',
                                    })
                continue
            elif type(value) in ( types.ListType, types.TupleType, ):
                value = ', '.join([str(item) for item in value])
            argMaps.append({'sidebarVarName': '--' + key.replace('_', '-'),
                            'sidebarVarValue': value,
                            })
        mustacheMap['sidebarArgs'] = argMaps


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
                value = formatEms(value)
            elif type(value) in ( types.IntType,
                                    types.FloatType,
                                    types.LongType,):
                emsKey = key + '_in_ems'
                emsValue = formatEms(value / float(self.units_per_em))
                addToMustacheMap(emsKey, emsValue)
            addToMustacheMap(key, value)

        if localsMap:
            for key, value in localsMap.items():
                if type(value) in ( types.IntType,
                                    types.FloatType,
                                    types.LongType,):
                    emsKey = key + '_in_ems'
                    emsValue = formatEms(value / float(self.units_per_em))
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


    def getUnicodeCategory(self, glyph):
        def getUnicodeCategory_():
            codePoint = glyph.unicode
            if codePoint is None:
                name = glyph.name
                if '.' in name:
                    name = name[:name.index('.')]
                codePoint = UnicodeCharacterNames.getUnicodeForShortName(name)
            if codePoint is not None:
                try:
                    uc = unichr(codePoint)
                except UnicodeEncodeError:
                    return None
                if uc is not None:
                    unicode_category = unicodedata.category(uc)
                    return unicode_category
            return None
        return self.srcCache.getCachedValue('getUnicodeCategory: %s' % glyph.name, getUnicodeCategory_)


    def hasUnicodeCategoryPrefix(self, glyph, prefixes, exceptions=None):
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
        if glyph.name not in self.glyphNameToCategoryMap:
            return False
        unicode_category = self.glyphNameToCategoryMap[glyph.name]
        if unicode_category is not None:
            if exceptions:
                if unicode_category in exceptions:
                    return False
            if unicode_category[0] in prefixes:
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
                       width=None, height=None, maxWidth=None, maxHeight=None,
                       padding=None):

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
                if rangeLeft == rangeRight:
                    continue
                p0 = TFSPoint(rangeLeft, int(round(self.dstUfoFont.info.descender * 0.2)))
                p1 = TFSPoint(rangeRight, int(round(self.dstUfoFont.info.descender * 0.2)))
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

        if set((width, height, maxWidth, maxHeight,)) == set((None,)):
            SVG_HEIGHT = 400
            SVG_MAX_WIDTH = 800
            height = SVG_HEIGHT
            maxWidth = SVG_MAX_WIDTH

        self.timing.mark('renderSvgScene.0')
        svgdata = tfsSvg.renderToFile(dstFile,
                                      margin=10,
                                      timing=self.timing,
                                      width=width, height=height, maxWidth=maxWidth, maxHeight=maxHeight,
                                      padding=padding)
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
#        kerningInfo.adj_minmax0 = cache.getAdjMinmax(ufoglyph0, self)
#        kerningInfo.adj_minmax1 = cache.getAdjMinmax(ufoglyph1, self)
#        kerningInfo.x_extrema_overlap = kerningInfo.adj_minmax0.maxX - (kerningInfo.adj_minmax1.minX + kerningInfo.kernedAdvance)

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


    def logDisparitiesGroup(self, disparities, groupName, filterFunc=None):

        '''
        We're only interested in the top 100 disparities.
        '''
        self.disparity_log_count = max(0, self.disparity_log_count)

        # Remove empty values.
        disparities = [disparity for disparity in disparities if disparity.disparity != 0]

        if filterFunc is not None:
            filtered_disparities = []
            for disparity in disparities:
                if filterFunc(disparity.srcKerning.ufoglyph0, disparity.srcKerning.ufoglyph1):
                    filtered_disparities.append(disparity)
                    if len(filtered_disparities) >= self.disparity_log_count:
                        break
            disparities = filtered_disparities
        else:
            disparities = disparities[:self.disparity_log_count]

        if len(disparities) < 1:
            return

        def getDisparityFilename(index):
            return 'disparity-%s-%d.html' % ( groupName.lower().replace(' ', '_'),
                                              index, )

        disparityLinkMaps = []
        for index, disparity in enumerate(disparities):
            disparityLinkMaps.append({ 'linkFile': getDisparityFilename(index),
                                      'linkName': str(index + 1),
                                      })

        for index, disparity in enumerate(disparities):
            ufoglyph0 = disparity.dstKerning.ufoglyph0
            ufoglyph1 = disparity.dstKerning.ufoglyph1

#            print 'index', index, 'ufoglyph0', ufoglyph0.name, ufoglyph1.name

            comment = 'The top %d disparities between the original kerning and Autokern\'s kerning, in descending order.' % len(disparities)
            logFilename = getDisparityFilename(index)

            self.writeGenericPairLog(ufoglyph0,
                                     ufoglyph1,
                                     pageTitles=(groupName + ' disparity:',
                                                 '%s vs. %s' % ( formatGlyphName(ufoglyph0),
                                                                 formatGlyphName(ufoglyph1), ), ),
                                     pageComments=(comment,),
                                     logFilename=logFilename,
                                     logGroupName='Disparities: ' + groupName,
                                     logGroupDescription=comment,
                                     logIndexName='%d' % (index + 1),
                                     linkMaps=disparityLinkMaps)


    def logDisparities(self):

        renderLog = self.log_path is not None
        if not renderLog:
            return
        if (self.disparity_log_count is None) or (self.disparity_log_count < 1):
            return

        print 'Logging disparities...'

        disparities = self.findDisparities()

        def isRomanLetter(ufoglyph):
            if len(ufoglyph.name) != 1:
                return False
            return ord('A') <= ord(ufoglyph.name.upper()) <= ord('Z')
        def romanLettersFilter(ufoglyph0, ufoglyph1):
            return isRomanLetter(ufoglyph0) and isRomanLetter(ufoglyph1)
        self.logDisparitiesGroup(disparities, 'Roman Letters', filterFunc=romanLettersFilter)

        def isArabNumeral(ufoglyph):
            if ufoglyph.unicode is None:
                return False
            return ord('0') <= ufoglyph.unicode <= ord('9')
        def arabNumeralsFilter(ufoglyph0, ufoglyph1):
            return isArabNumeral(ufoglyph0) and isArabNumeral(ufoglyph1)
        self.logDisparitiesGroup(disparities, 'Arab Numerals', filterFunc=arabNumeralsFilter)

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
        def lettersAndNumbersFilter(ufoglyph0, ufoglyph1):
            unicodeCategoryPrefixes = ('L','N',)
            unicodeCategoryExceptions = ('Lm',)
            return (self.hasUnicodeCategoryPrefix(ufoglyph0, prefixes=unicodeCategoryPrefixes, exceptions=unicodeCategoryExceptions) and
                    self.hasUnicodeCategoryPrefix(ufoglyph1, prefixes=unicodeCategoryPrefixes, exceptions=unicodeCategoryExceptions))
        self.logDisparitiesGroup(disparities, 'Letters And Numbers', filterFunc=lettersAndNumbersFilter)

        self.logDisparitiesGroup(disparities, 'All')


    def writeGenericPairLog(self,
                            ufoglyph0, ufoglyph1,
                            pageTitles, pageComments,
                            logFilename, logGroupName, logGroupDescription, logIndexName,
                            linkMaps=None,
                            timing=None):

        if timing is not None:
             timing.mark('writeGenericPairLog.0')

        logSections = []

        logSections.append(self.writeSourceLogSectionMap(ufoglyph0, ufoglyph1))

        if timing is not None:
             timing.mark('writeGenericPairLog.1')

        contours0 = self.dstCache.getGlyphContours(ufoglyph0)
        contours1 = self.dstCache.getGlyphContours(ufoglyph1)
        if (not contours0) or (not contours1):
            return False

        kerningValue = self.dstUfoFont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
        if kerningValue is None:
            kerningValue = 0
        rawAdvance = ufoglyph0.xAdvance
        kernedAdvance = rawAdvance + kerningValue

        logSections.append(self.writeLogSectionMap('Autokern',
                                                   self.dstCache,
                                                   ufoglyph0, ufoglyph1,
                                                   kernedAdvance))

        if timing is not None:
             timing.mark('writeGenericPairLog.2')

        self.writeGenericSectionsLog(logSections,
#                            ufoglyph0, ufoglyph1,
                                    pageTitles, pageComments,
                                    logFilename, logGroupName, logGroupDescription, logIndexName,
                                    localVars=locals(),
                                    linkMaps=linkMaps,
                                    timing=timing)


    def writeGenericSectionsLog(self,
                                logSections,
#                            ufoglyph0, ufoglyph1,
                                pageTitles, pageComments,
                                logFilename, logGroupName, logGroupDescription, logIndexName,
                                localVars,
                                linkMaps=None,
                                timing=None):

        localsMap = {}
        localsMap.update(localVars)

        mustacheMap = self.makeDefaultMustacheMap(localsMap=localsMap)
        self.addSidebarMustacheMap(mustacheMap, kerned=False)

        logSectionMaps = []
        for logSection in logSections:
            logSectionMap = {}
            logSectionMap['sectionTitle'] = logSection['title']
            logSectionMap['sectionSvg'] = logSection['svg']
            if logSection['comments']:
                logSectionMap['sectionComments'] = [{'comment': comment,} for comment in logSection['comments']]
            def formatSectionVariable(variableTuple):
                if len(variableTuple) == 2:
                    name, var = variableTuple
                    return {'varName': name, 'varValue':mustacheMap[var],}
                else:
                    return {'varName': variableTuple[0], 'varValue':variableTuple[1],}

            logSectionMap['sectionVariables'] = [formatSectionVariable(variableTuple) for variableTuple in logSection['variables']]
            logSectionMaps.append(logSectionMap)

        def makeStringMaps(key, values):
            result = []
            for value in values:
                result.append({key: value,})
            return result

        mustacheMap.update({
                            'pageTitles': makeStringMaps('pageTitle', pageTitles),
                            'pageComments': makeStringMaps('pageComment', pageComments),
                            'logSectionMaps': logSectionMaps,
                            'linkMaps': linkMaps,
                            })
        if linkMaps is not None:
            if len(linkMaps) > 0:
                mustacheMap['hasLinkMaps'] = True
                mustacheMap['firstLinkMap'] = linkMaps[0]
                mustacheMap['lastLinkMap'] = linkMaps[-1]

                for index, linkMap in enumerate(linkMaps):
                    if linkMap['linkFile'] == logFilename:
                        mustacheMap['hasNextPrevLinkMaps'] = True
                        mustacheMap['prevLinkMap'] = linkMaps[(index + len(linkMaps) - 1) % len(linkMaps)]
                        mustacheMap['nextLinkMap'] = linkMaps[(index + 1) % len(linkMaps)]
                        break


#        self.kerningPairLogFilenames.add(logFilename)

        if timing is not None:
             timing.mark('writeGenericPairLog.4')

        self.writeLogFile('autokern_generic_template.txt',
                          logFilename,
                          logGroupName,
                          logGroupDescription,
                          logIndexName,
                          mustacheMap)

        if timing is not None:
             timing.mark('writeGenericPairLog.5')


    def writeBasicPairsLog(self):

        renderLog = self.log_path is not None
        if not renderLog:
            return
        if not self.log_basic_pairs:
            return

        print 'Logging basic pairs...'


        import tfs.common.TFSProject as TFSProject
#        dataFolder = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data'))
        mustache_template_file = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'ilovetypography kerning pairs.txt'))
        with open(mustache_template_file, 'rt') as f:
            text = f.read().decode('utf8')

        pairs = []
        for line in text.split('\n'):
            line = line.strip()
            if line.startswith('#'):
                continue
            for value in line.split(' '):
                if value:
                    pairs.append(value)

        glyphs = self.dstUfoFont.getGlyphs()

        unicodeToGlyphMap = {}
        for glyph in glyphs:
            if glyph.unicode is None:
                continue
            unicodeToGlyphMap[glyph.unicode] = glyph

        #

        pairTuples = []
        linkMaps = []
        for pair in pairs:
            if len(pair) != 2:
                raise Exception('Invalid pair: ' + pair)
            left, right = pair
            unicode0 = ord(left)
            unicode1 = ord(right)
            if ((unicode0 not in unicodeToGlyphMap) or
                (unicode1 not in unicodeToGlyphMap)):
                continue

            ufoglyph0 = unicodeToGlyphMap[unicode0]
            ufoglyph1 = unicodeToGlyphMap[unicode1]

            logFilename = self.getKerningPairFilename('basic_pair', ufoglyph0, ufoglyph1, '.html')
            pairTuples.append( ( pair, ufoglyph0, ufoglyph1, logFilename, ) )
            linkMaps.append( { 'linkFile': logFilename,
                               'linkName': '%s%s' % ( formatGlyphNameShort(ufoglyph0),
                                                      formatGlyphNameShort(ufoglyph1), ),
                              } )
            if len(pairTuples) > 25:
                break

        #

        timing = None
#        timing = TFTiming()

        startTime = time.time()
        lastLogTime = time.time()
        for index, (pair, ufoglyph0, ufoglyph1, logFilename,) in enumerate(pairTuples):
            now = time.time()
            if lastLogTime is None or now - lastLogTime > 3.0:
                remainingTime = (now - startTime) / float(index) * (len(pairTuples) - index)
                print '\t', ufoglyph0.name, ufoglyph1.name, index, '/', len(pairTuples), '%d%%' % ( 100 * index / len(pairTuples), ), formatTimeDuration(remainingTime), 'remaining'
                lastLogTime = now

            self.writeGenericPairLog(ufoglyph0, ufoglyph1,
                                     pageTitles=('Basic Pair:',
                                                 '%s vs. %s' % ( formatGlyphName(ufoglyph0),
                                                                 formatGlyphName(ufoglyph1), ), ),
                                     pageComments=('''
    Before-and-after comparisons of common kerning pairs.
                              ''',),
                                     logFilename=logFilename,
                                     logGroupName='Basic Pairs',
                                     logGroupDescription='''
    Before-and-after comparisons of common kerning pairs.
                              ''',
                                     logIndexName='%s%s' % ( formatGlyphNameShort(ufoglyph0),
                                                             formatGlyphNameShort(ufoglyph1), ),
                                     linkMaps=linkMaps,
                                     timing=timing)
        if timing is not None:
            timing.dump()

        print


    def getFilenamePrefixPair(self, prefix, ufoglyph0, ufoglyph1):
        return '%s-%s-%s' % ( prefix,
                              ufoglyph0.name,
                              ufoglyph1.name, )

    def getKerningPairFilename(self, prefix, ufoglyph0, ufoglyph1, extension):
        return self.getFilenamePrefixPair(prefix, ufoglyph0, ufoglyph1) + extension

    def getKerningPairHtmlFilename(self, ufoglyph0, ufoglyph1):
        return self.getKerningPairFilename('autokern', ufoglyph0, ufoglyph1, '.html')


    def convertProfileToLogPaths(self, profile, isLeft, offset=None):
        minYunits = self.profileMinYunits

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


    def makeProfile(self, paths=None, segments=None, debug=False):
        minYunits = self.profileMinYunits
        maxYunits = self.profileMaxYunits
        yHeightUnits = 1 + maxYunits - minYunits

#        print 'maxYunits', maxYunits
#        print 'minYunits', minYunits
#        print 'self.allGlyphsMinY', self.allGlyphsMinY
#        print 'self.allGlyphsMaxY', self.allGlyphsMaxY
#        print 'self.precision', self.precision
#        print 'yHeightUnits', yHeightUnits

        maxProfile = list((None,) * yHeightUnits)
        minProfile = list((None,) * yHeightUnits)

        # combine paths and segments parameters
        allSegments = []
        if segments is not None:
            allSegments.extend(segments)
        if paths is not None:
            for path in paths:
                allSegments.extend(path.segments)

        def addProfilePoint(yIndex, xValue):
            if yIndex < 0 or yIndex >= len(maxProfile):
                raise Exception('Invalid yIndex: %d' % yIndex)
#            print 'yIndex', yIndex, 'len(profile)', len(profile)
            if debug:
                print 'yIndex', yIndex, 'xValue', xValue
            if maxProfile[yIndex] is None:
                minProfile[yIndex] = maxProfile[yIndex] = xValue
            else:
                minProfile[yIndex] = min(minProfile[yIndex], xValue)
                maxProfile[yIndex] = max(maxProfile[yIndex], xValue)

        def addSegmentSection(point0, point1):
            '''
            Given two endpoints of a straight segment, interpolate x values along the y-axis.

            Not very precise; rounds y value of endpoint locations.
            Acceptable; as precise as "precision".
            '''
            y0u = int(round(point0.y / float(self.precision)))
            y1u = int(round(point1.y / float(self.precision)))

            if debug:
                print 'addSegmentSection', point0.description(), point1.description(), 'y0u', y0u, 'y1u', y1u

            if y0u == y1u:
                yIndex = y0u - minYunits
                addProfilePoint(yIndex, point0.x)
                addProfilePoint(yIndex, point1.x)
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

        return minProfile, maxProfile


    def isValidProfileIntrusion(self, profile0, profile1, referenceProfiles, advance,
                                pair_max_distance,
                                pair_intrusion_tolerance,
                                withinAscender=False):

#        DEBUG_h_n_ISSUE = True
#        print 'isValidProfileIntrusion', 'advance', advance

#        maxRowProtrusion = pair_max_distance
        maxRowProtrusion = pair_max_distance * 1.5
#        maxRowProtrusion = pair_max_distance * 1.0
#        maxRowProtrusion = pair_max_distance * 2.0
#        maxSectionGapLength = int(round(pair_max_distance * 1.0 / self.precision))
        maxSectionGapLength = int(round(pair_max_distance * 0.5 / self.precision))
#        maxSectionPadding = int(round(pair_max_distance * 0.5 / self.precision))
#        maxSectionPadding = int(round(pair_max_distance * 0.3 / self.precision))
#        maxSectionPadding = int(round(pair_max_distance * 1.5 / self.precision))
        maxSectionPadding = int(round(pair_max_distance * 1.0 / self.precision))
#        maxSectionPadding = int(round(pair_max_distance * 1.15 / self.precision))
        defaultMaxXOffset = maxRowProtrusion


        def isValidRow(x_offset):
#            return (x_offset is not None)
#            return (x_offset is not None) and (x_offset > -maxRowProtrusion)
            return (x_offset is not None) and (x_offset < maxRowProtrusion)

        minYunits = self.profileMinYunits
        ascenderIndex = int(round(self.ascender / float(self.precision))) - minYunits
        baselineIndex = int(round(0 / float(self.precision))) - minYunits

        '''
        Step 1

        Evaluate the x-offset between the profiles for each row.
        '''
        allXOffsets = []
        for index in xrange(len(profile0)):
            edge0 = profile0[index]
            edge1 = profile1[index]

            x_offset = None
            if (edge0 is not None) and (edge1 is not None):
                x_offset = advance + edge1 - edge0
#
            if withinAscender:
                if not (baselineIndex <= index <= ascenderIndex):
                    x_offset = None

            '''
            A row is hollow if it only exists because one of the profiles was inflated,
            ie. the top and bottom spacing around the glyph.
            '''
            hollow = False
            for referenceProfile in referenceProfiles:
                if referenceProfile[index] is None:
                    hollow = True
            if hollow and x_offset >= 0:
                '''
                If a row is hollow and there is no intrusion, ignore it
                so that it does not count towards protrusion.
                '''
                x_offset = None

            allXOffsets.append(x_offset)

#        if DEBUG_h_n_ISSUE:
#            print 'sections.0', len(sections), [len(section) for section in sections]
#            print 'sections.0', len(sections), sections

        def splitSection(section):
            '''
            Step 2

            We need to split sections that have large internal gaps.
            Consider C vs. O.  If the mouth of the C is too large,
            it cases the upper and lower arms of the C to be kerned too
            closely to the next glyph.

            To resolve this, we split sections with large continuous internal gaps.
            The gaps must be entirely deeper and longer than pair_max_distance.

            We leave up to pair_max_distance of the gap around the split which
            will be trimmed by the next phase anyhow.
            '''

            lastValidIndex = None
            for index, x_offset in enumerate(section):
#                print 'index, x_offset', index, x_offset
                if isValidRow(x_offset):
                    if lastValidIndex is not None:
                        gapLength = index - lastValidIndex
#                        if gapLength > 1:
#                            print 'gapLength', gapLength
                        if gapLength >= maxSectionGapLength:
                            left = section[:index]
                            right = section[lastValidIndex + 1:]
#                            print 'maxGapLength', maxGapLength, 'gapLength', gapLength, 'pair_max_distance', pair_max_distance
#                            print 'left', left
#                            print 'right', right
                            return splitSection(left) + splitSection(right)

                    lastValidIndex = index

            return [section,]

#        print 'splitSections.0', len(sections)
#        print 'splitSections.0', len(allXOffsets), allXOffsets
        sections = splitSection(allXOffsets)
#        print 'splitSections.1', len(sections)
#        print 'maxRowProtrusion', maxRowProtrusion
#        print 'maxSectionGapLength', maxSectionGapLength


        def trimSection(section):
            '''
            Step 3

            We need to trim the sections that have huge gaps at the top and/or bottom.
            Consider h vs. h.  The huge space between the top stems distorts the
            profile and causes their bottoms to be kerned too closely.

            To resolve this, we trim large continuous gaps at the top or bottom
            of a section.  The gaps must be entirely greater than pair_max_distance.

            We leave up to pair_max_distance * 0.5 of the gap, so that beaks
            and arms are kerned closer.  For example, t vs. L or r vs. a.

            This isn't an ideal solution.  It might better to add a new argument that
            discards sections below a certain length.
            '''
            headCount = 0
            for index, x_offset in enumerate(section):
#                print 'index, x_offset', index, x_offset
                if isValidRow(x_offset):
                    break
                headCount = index
            tailCount = 0
            for index, x_offset in enumerate(reversed(section)):
#                print 'reversed index, x_offset', index, x_offset
                if isValidRow(x_offset):
                    break
                tailCount = index
#            maxPadding = int(round(pair_max_distance * 0.5 / self.precision))

#            # Pad section if necessary
#            headPaddingCount = max(0, maxSectionPadding - headCount)
#            tailPaddingCount = max(0, maxSectionPadding - tailCount)
#            section = ([defaultMaxXOffset,] * headPaddingCount) + section + ([defaultMaxXOffset,] * tailPaddingCount)

            headTrimCount = max(0, headCount - maxSectionPadding)
            tailTrimCount = max(0, tailCount - maxSectionPadding)
            if headTrimCount + tailTrimCount >= len(section):
                return []
#            print 'section', len(section)
#            print 'maxPadding', maxPadding, 'pair_max_distance', pair_max_distance, 'self.precision', self.precision
#            print 'headCount', headCount, 'headTrimCount', headTrimCount
#            print 'tailCount', tailCount, 'tailTrimCount', tailTrimCount
            if tailTrimCount > 0:
                result = section[headTrimCount:-tailTrimCount]
            else:
                result = section[headTrimCount:]
#            result = section

            # Trim empty space
            while (len(result) > 0) and (result[0] is None):
                result = result[1:]
            while (len(result) > 0) and (result[-1] is None):
                result = result[:-1]

            return result

        trimmedSections = []
        for section in sections:
            section = trimSection(section)
            if len(section) > 0:
                trimmedSections.append(section)
        sections = trimmedSections


        if DEBUG_h_n_ISSUE:
            print 'sections.1', len(sections), [len(section) for section in sections]
            print 'sections.1', len(sections), sections

#        print 'sections', sections

        if len(sections) < 1:
            '''
            No collision found.
            '''
            return True

        '''
        Step 4
        Now consider each section separately.
        '''
        for section in sections:
            intrusionTotal = 0
            protrusionTotal = 0
            intrusionPowTotal = 0
            protrusionPowTotal = 0

            for x_offset in section:
                if x_offset is None:
                    '''
                    Fill in missing gaps with maximum protrusion value.
                    '''
                    x_offset = defaultMaxXOffset
                rowIntrusion = max(0, -x_offset)
                '''
                Ignore protrusion greater than --max-distance argument.
                '''
                rowProtrusion = min(maxRowProtrusion, max(0, +x_offset))
#                print 'edge0, edge1', edge0, edge1, 'diff', diff, 'advance', advance, 'rowIntrusion', rowIntrusion, 'rowProtrusion', rowProtrusion
                intrusionTotal += rowIntrusion
                protrusionTotal += rowProtrusion
#                intrusionPowTotal += pow(rowIntrusion, 2.0)
#                protrusionPowTotal += pow(rowProtrusion, 2.0)
                TRUSION_POWER = 1.15
#                TRUSION_POWER = 1.10
#                intrusionTotal += pow(rowIntrusion, TRUSION_POWER)
#                protrusionTotal += pow(rowProtrusion, 1 / TRUSION_POWER)
                intrusionPowTotal += pow(rowIntrusion, TRUSION_POWER)
#                intrusionPowTotal += self.units_per_em * pow(rowIntrusion / self.units_per_em, TRUSION_POWER)
#                protrusionPowTotal += pow(rowProtrusion, 1 / TRUSION_POWER)
                protrusionPowTotal += rowProtrusion

            '''
            Enforce
            '''

#            print 'advance', advance
#            print 'intrusionTotal', intrusionTotal, 'protrusionTotal', protrusionTotal
#            INTRUSION_EXTRUSION_MIN_RATIO = 1.5
            INTRUSION_EXTRUSION_MIN_RATIO = 1.0
#            if intrusionTotal > protrusionTotal * INTRUSION_EXTRUSION_MIN_RATIO:
#                return False
            if intrusionPowTotal > protrusionPowTotal * INTRUSION_EXTRUSION_MIN_RATIO:
                return False

            intrusionToleranceArea = pair_intrusion_tolerance * len(section)

#            print 'intrusionToleranceArea', intrusionToleranceArea
            if intrusionTotal > intrusionToleranceArea:
                return False

#        print 'totalSectionRowCount', totalSectionRowCount, 'advance', advance
#        print 'intrusionTotal', intrusionTotal, 'protrusionTotal', protrusionTotal, 'intrusionToleranceArea', intrusionToleranceArea

        return True


    def findMinProfileAdvance(self, profile0, profile1):
        if len(profile0) != len(profile1):
            raise Exception('profile heights do not match. %d != %d', len(profile0), len(profile1))

        contactAdvance = None
        for edge0, edge1 in itertools.izip(profile0, profile1):
            if edge0 is None or edge1 is None:
                continue
            diff = edge0 - edge1
            if contactAdvance is None:
                contactAdvance = diff
            else:
                contactAdvance = max(contactAdvance, diff)

        return contactAdvance


    def findMinProfileAdvance_withIntrusion(self, profile0, profile1, referenceProfiles,
                                            pair_max_distance,
                                            pair_intrusion_tolerance):
        contactAdvance = self.findMinProfileAdvance(profile0, profile1)

        if contactAdvance is None:
            return None

        '''
        Binary search for best intrusion offset.
        '''
        lowValidIntrusionOffset = 0
        '''
        I'm not sure what the best way to determine an upper bound on this value is,
        so I've erred on the side of accuracy by chosing a very high upper bound.
        '''
        maximumIntrusionOffset = int(math.ceil(2.0 * max(pair_intrusion_tolerance,
                                                         pair_max_distance)))
        highInvalidIntrusionOffset = maximumIntrusionOffset
        while True:
            intrusionOffset = int(round((lowValidIntrusionOffset + highInvalidIntrusionOffset) / 2))
            if DEBUG_h_n_ISSUE:
                print 'intrusionOffset', intrusionOffset, 'lowValidIntrusionOffset', lowValidIntrusionOffset, 'highInvalidIntrusionOffset', highInvalidIntrusionOffset

            if intrusionOffset in ( lowValidIntrusionOffset,
                                    highInvalidIntrusionOffset, ):
                intrudingAdvance = contactAdvance - lowValidIntrusionOffset
                return intrudingAdvance


            if (self.isValidProfileIntrusion(profile0, profile1, referenceProfiles, contactAdvance - intrusionOffset,
                                             pair_max_distance,
                                             pair_intrusion_tolerance) and
                self.isValidProfileIntrusion(profile0, profile1, referenceProfiles, contactAdvance - intrusionOffset,
                                             pair_max_distance,
                                             pair_intrusion_tolerance, withinAscender=True)):
#            if self.isValidProfileIntrusion(profile0, profile1, referenceProfiles, contactAdvance - intrusionOffset,
#                                            pair_max_distance,
#                                            pair_intrusion_tolerance):
                lowValidIntrusionOffset = intrusionOffset
            else:
                highInvalidIntrusionOffset = intrusionOffset


    def inflateSegmentLeft(self, segment, hDistance, vDistance=None):
        '''
        '''
        if vDistance is None:
            vDistance = hDistance

        startTangent = segment.startTangent()
        endTangent = segment.endTangent()

        p0 = segment.startPoint()
        p1 = segment.endPoint()

        if len(segment) == 2:
            offset = scaleVectorHV(startTangent.rotate(math.pi * 0.5), hDistance, vDistance)
            p0 = p0.plus(offset)
            p1 = p1.plus(offset)
            newPoints = (p0, p1)
        elif len(segment) == 3:
            startOffset = scaleVectorHV(startTangent.rotate(math.pi * 0.5), hDistance, vDistance)
            endOffset = scaleVectorHV(endTangent.rotate(math.pi * 0.5), hDistance, vDistance)
            p0 = p0.plus(startOffset)
            p1 = p1.plus(endOffset)
            cp0 = TFSIntersection.intersectionWithTangents(p0, startTangent, p1, endTangent.invert())
            newPoints = (p0, cp0, p1)
        elif len(segment) == 4:
            startOffset = scaleVectorHV(startTangent.rotate(math.pi * 0.5), hDistance, vDistance)
            endOffset = scaleVectorHV(endTangent.rotate(math.pi * 0.5), hDistance, vDistance)
            oldScale = p0.distanceTo(p1)
            p0 = p0.plus(startOffset)
            p1 = p1.plus(endOffset)
            newScale = p0.distanceTo(p1)
            cp0 = p0.plus(segment.naiveStartVector().scale(newScale / oldScale))
            cp1 = p1.minus(segment.naiveEndVector().scale(newScale / oldScale))
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


    def makeInflatedProfile(self, contours, radius):

        segments = []

        def addEndpointRounding(point):
            if radius <= 0:
                return
#            print
#            print 'addEndpointRounding', point.description(), 'radius', radius
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

        return self.makeProfile(segments=segments)


    def processKerningPair(self, ufoglyph0, ufoglyph1):
        '''
        returns True iff pair is kerned.
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

#        if self.isIgnoredGlyph(ufoglyph0) or self.isIgnoredGlyph(ufoglyph1):
#            return False

#        print 'processKerningPair'

        debugKerning = True
        debugKerning = False

        renderLog = (self.log_path is not None) and self.write_kerning_pair_logs

        contours0 = self.dstCache.getGlyphContours(ufoglyph0)
        contours1 = self.dstCache.getGlyphContours(ufoglyph1)
        if (not contours0) or (not contours1):
            return False

        self.timing.mark('processKerningPair.01')

        minmax0 = self.dstCache.getContoursMinmax(ufoglyph0)
        minmax1 = self.dstCache.getContoursMinmax(ufoglyph1)

        self.timing.mark('processKerningPair.010')

        pair_min_distance = self.getGlyphPair_min_distance(ufoglyph0, ufoglyph1)
        pair_max_distance = self.getGlyphPair_max_distance(ufoglyph0, ufoglyph1)
        pair_tracking = self.getGlyphPair_tracking(ufoglyph0, ufoglyph1)
        pair_max_x_extrema_overlap = self.getGlyphPair_max_x_extrema_overlap(ufoglyph0, ufoglyph1)
        pair_intrusion_tolerance = self.getGlyphPair_intrusion_tolerance(ufoglyph0, ufoglyph1)

#        print 'pair_min_distance', pair_min_distance
#        print 'pair_max_distance', pair_max_distance
#        print 'pair_intrusion_tolerance', pair_intrusion_tolerance

        self.timing.mark('processKerningPair.011')

        def getGlyphProfiles(contours):
            return self.makeProfile(paths=contours)

        def maxAdvance(advance0, advance1, defaultAdvance):
            if advance0 is None and advance1 is None:
                result = defaultAdvance
            elif advance0 is None:
                result = advance1
            elif advance1 is None:
                result = advance0
            else:
                result = max(advance0, advance1)
            result = int(round(result))
            return result

        def getGlyphProfilesInflateMin(contours):
            return self.makeInflatedProfile(contours=contours, radius=pair_min_distance * 0.5)
        def getGlyphProfilesInflateMax(contours):
            return self.makeInflatedProfile(contours=contours, radius=pair_max_distance * 0.5)

        _, profile0 = self.dstCache.getCachedValue('getGlyphProfiles %s' % ufoglyph0.name, getGlyphProfiles, contours0)
        self.timing.mark('processKerningPair.011')

        _, profileMin0 = self.dstCache.getCachedValue('getGlyphProfilesInflateMin %s %f' % (ufoglyph0.name,
                                                                                         pair_min_distance,), getGlyphProfilesInflateMin, contours0)
        self.timing.mark('processKerningPair.012')

        _, profileMax0 = self.dstCache.getCachedValue('getGlyphProfilesInflateMax %s %f' % (ufoglyph0.name,
                                                                                            pair_max_distance,), getGlyphProfilesInflateMax, contours0)
        self.timing.mark('processKerningPair.013')

        profile1, _ = self.dstCache.getCachedValue('getGlyphProfiles %s' % ufoglyph1.name, getGlyphProfiles, contours1)
        self.timing.mark('processKerningPair.014')

        profileMin1, _ = self.dstCache.getCachedValue('getGlyphProfilesInflateMin %s %f' % (ufoglyph1.name,
                                                                                            pair_min_distance,), getGlyphProfilesInflateMin, contours1)
        self.timing.mark('processKerningPair.015')

        profileMax1, _ = self.dstCache.getCachedValue('getGlyphProfilesInflateMax %s %f' % (ufoglyph1.name,
                                                                                            pair_max_distance,), getGlyphProfilesInflateMax, contours1)
        self.timing.mark('processKerningPair.016')

        if DEBUG_h_n_ISSUE:
            print ufoglyph0.name, ufoglyph1.name, 'findMinProfileAdvance(profileMin0, profileMin1)'
        minDistanceAdvance = self.findMinProfileAdvance(profileMin0, profileMin1)
        if minDistanceAdvance is None:
            minDistanceAdvance = minmax0.maxX + pair_min_distance - minmax1.minX
        minDistanceAdvance = int(round(minDistanceAdvance))
        self.timing.mark('processKerningPair.020')
        if debugKerning:
            print 'minDistanceAdvance', minDistanceAdvance



        maxDistanceAdvance = self.findMinProfileAdvance(profileMax0, profileMax1)
        if debugKerning:
            print 'maxDistanceAdvance', maxDistanceAdvance
        if maxDistanceAdvance is None:
            maxDistanceAdvance = minmax0.maxX + pair_max_distance - minmax1.minX
        maxDistanceAdvance = int(round(maxDistanceAdvance))
        self.timing.mark('processKerningPair.021')



        if DEBUG_h_n_ISSUE:
            print ufoglyph0.name, ufoglyph1.name, 'findMinProfileAdvance_withIntrusion(profileMax0, profileMax1)'
        intrudingAdvance = self.findMinProfileAdvance_withIntrusion(profileMax0, profileMax1,
                                                                    referenceProfiles=(profile0, profile1),
                                                                    pair_max_distance=pair_max_distance,
                                                                    pair_intrusion_tolerance=pair_intrusion_tolerance)
        self.timing.mark('processKerningPair.022')
        if intrudingAdvance is None:
            intrudingAdvance = minmax0.maxX + pair_min_distance - minmax1.minX
        intrudingAdvance = int(round(intrudingAdvance))
        if debugKerning:
            print 'intrudingAdvance', intrudingAdvance

        if DEBUG_h_n_ISSUE:
            print 'minDistanceAdvance', minDistanceAdvance
            print 'intrudingAdvance', intrudingAdvance

        '''
        Now combine results into the final advance value.
        1. Start with the "intruding advance."

        All subsequent steps should only serve to increase the advance.
        '''
        advance = intrudingAdvance

#        '''
#        1a. Apply the kerning stretgth.
#        '''
##        print 'kerning_strength', self.kerning_strength
#        naiveAdvance = (minDistanceAdvance + maxDistanceAdvance) * 0.5
#        self.kerning_strength = max(0, min(1.0, self.kerning_strength))
##        print 'advance', advance, 'kerning_strength', self.kerning_strength
##        print 'minDistanceAdvance', minDistanceAdvance, 'maxDistanceAdvance', maxDistanceAdvance, 'naiveAdvance', naiveAdvance
#        advance = (advance * self.kerning_strength) + (naiveAdvance * (1.0 - self.kerning_strength))
##        print 'advance.1', advance


        '''
        2. Make sure advance is at least the "minimum advance."
        '''
        advance = maxAdvance(advance, minDistanceAdvance, minmax0.maxX + pair_min_distance - minmax1.minX)

        '''
        3. Add the "tracking" value.
        '''
        advance += pair_tracking

        '''
        4. Apply --x-extrema-overlap-scaling argument.
        '''

        adj_minmax0 = self.dstCache.getAdjMinmax(ufoglyph0, self)
        adj_minmax1 = self.dstCache.getAdjMinmax(ufoglyph1, self)

        if adj_minmax0 is not None and adj_minmax1 is not None:
            x_extrema_overlap = adj_minmax0.maxX - (adj_minmax1.minX + advance)
            if x_extrema_overlap > 0:
                '''
                If x-extrema are overlapping, adjust advance accordingly.
                '''
                scaled_x_extrema_overlap = x_extrema_overlap * self.x_extrema_overlap_scaling
                advance += x_extrema_overlap - scaled_x_extrema_overlap

        '''
        5. Make sure the "x-extrema overlap" is not greater than the "max x-extrema overlap".
        '''
        if adj_minmax0 is not None and adj_minmax1 is not None:
            x_extrema_overlap = adj_minmax0.maxX - (adj_minmax1.minX + advance)
            if x_extrema_overlap > pair_max_x_extrema_overlap:
                advance += x_extrema_overlap - pair_max_x_extrema_overlap


        advance = int(round(advance))

        self.advanceMap[(ufoglyph0.name,
                         ufoglyph1.name,)] = advance

        if debugKerning:
            print '\t', ufoglyph0.unicode, ufoglyph1.unicode, advance

        self.timing.mark('processKerningPair.5')

        if renderLog:

            logSections = []

            def addLogSection(title,
                              logCache,
                              logufoglyph0, logufoglyph1,
                              glyphProfile0, glyphProfile1,
                              advanceValue,
                              extraVariableTuples=None,
                              comments=None):

                strokePathTuples = ()
                if glyphProfile0 is not None:
                    strokePathTuples = (
                    ( 0xafff7faf, glyphProfile0, ),
                    ( 0xafaf7fff, xTranslateContours(glyphProfile1, advanceValue), ),
                    )

                logSections.append(self.writeLogSectionMap(title,
                                                           logCache,
                                                           logufoglyph0, logufoglyph1,
                                                           advanceValue,
                                                           strokePathTuples=strokePathTuples,
                                                           extraVariableTuples=extraVariableTuples,
                                                           comments=comments))


            logSections.append(self.writeSourceLogSectionMap(ufoglyph0, ufoglyph1))

            self.timing.mark('processKerningPair.61')

            # -----------

            profilePaths0 = self.convertProfileToLogPaths(profile0, isLeft=True)
            profileMinPaths0 = self.convertProfileToLogPaths(profileMin0, isLeft=True)
            profileMaxPaths0 = self.convertProfileToLogPaths(profileMax0, isLeft=True)
            profilePaths1 = self.convertProfileToLogPaths(profile1, isLeft=False)
            profileMinPaths1 = self.convertProfileToLogPaths(profileMin1, isLeft=False)
            profileMaxPaths1 = self.convertProfileToLogPaths(profileMax1, isLeft=False)

            self.timing.mark('processKerningPair.62')

            # -----------

            contactAdvance = self.findMinProfileAdvance(profile0, profile1)
            if contactAdvance is None:
                contactAdvance = minmax0.maxX - minmax1.minX
            contactAdvance = int(round(contactAdvance))

            self.timing.mark('processKerningPair.63')

            addLogSection('Contact',
                          self.dstCache,
                          ufoglyph0, ufoglyph1,
                          profilePaths0, profilePaths1,
                          contactAdvance,
                          comments=('The raw contours brought into contact if possible.',
                                    'From each glyph, a facade profile is constructed from its contours.',))

            self.timing.mark('processKerningPair.64')

            # -----------

            addLogSection('Minimum Distance',
                          self.dstCache,
                          ufoglyph0, ufoglyph1,
                          profileMinPaths0, profileMinPaths1,
                          minDistanceAdvance,
                          (
                              ('--min-distance-ems', 'min_distance_ems',),
                              ('Pair-specific --min-distance-ems', 'pair_min_distance_in_ems',),
                          ),
                          comments=('The minimum distance kerning.',
                                    'From each glyph, a facade profile is constructed from its contours (inflated by half of --min-distance-ems).',))

            self.timing.mark('processKerningPair.65')

            # -----------
#
#            maxDistanceAdvance = self.findMinProfileAdvance(profileMax0, profileMax1)
#            if debugKerning:
#                print 'maxDistanceAdvance', maxDistanceAdvance
#
#            if maxDistanceAdvance is None:
#                '''
#                If no collisions between the glyph profiles, use x-extrema
#                plus the max_distance argument.
#                '''
#                maxDistanceAdvance = minmax0.maxX + pair_max_distance - minmax1.minX
#            maxDistanceAdvance = int(round(maxDistanceAdvance))
#
#            self.timing.mark('processKerningPair.66')

            addLogSection('Maximum Distance',
                          self.dstCache,
                          ufoglyph0, ufoglyph1,
                          profileMaxPaths0, profileMaxPaths1,
                          maxDistanceAdvance,
                          (
                              ('--max-distance-ems', 'max_distance_ems',),
                              ('Pair-specific --max-distance-ems', 'pair_max_distance_in_ems',),
                          ),
                          comments=('The maximum distance kerning.',
                                    'From each glyph, a facade profile is constructed from its contours (inflated by half of --max-distance-ems).',))
            self.timing.mark('processKerningPair.67')

            # -----------

            addLogSection('Intruding',
                          self.dstCache,
                          ufoglyph0, ufoglyph1,
                          profileMaxPaths0, profileMaxPaths1,
                          intrudingAdvance,
                          (
#                              ('intrudingAdvance', 'intrudingAdvance_in_ems',),
#                              ('intrudingAdvance (Right)', 'intrudingAdvance0_in_ems',),
#                              ('intrudingAdvance (Left)', 'intrudingAdvance1_in_ems',),
                              ('--intrusion-tolerance-ems', 'intrusion_tolerance_ems',),
                              ('Pair-specific --intrusion-tolerance-ems', 'pair_intrusion_tolerance_in_ems',),
                          ),
                          comments=('The intrusion kerning.',
                                    'From each glyph, a facade profile is constructed from its contours (inflated by half of --max-distance-ems).',
                                    'The profiles are then drawn towards each other using the intrusion algorithm.'))
            self.timing.mark('processKerningPair.68')

            # -----------

            addLogSection('Autokern Raw',
                          self.dstCache,
                          ufoglyph0, ufoglyph1,
                          profileMaxPaths0, profileMaxPaths1,
                          advance,
                          (
                              ('--max-x-extrema-overlap-ems', 'max_x_extrema_overlap_in_ems',),
                              ('Pair-specific --max-x-extrema-overlap-ems', 'pair_max_x_extrema_overlap_in_ems',),
                              ('--x-extrema-overlap-scaling', 'x_extrema_overlap_scaling',),
                              ('--tracking-ems', 'tracking_ems',),
                              ('Pair-specific --tracking-ems', 'pair_tracking_in_ems',),
                          ),
                          comments=('The raw kerning. Does not represent the final output which is effected by changes to the side bearings.',
                                    'The results of the previous steps are combined, and the effects of various arguments are applied.',
                                    ))

            self.timing.mark('processKerningPair.69')

            # -----------

            comment = 'Logs that document the kerning process for each glyph pair.'
            logFilename = self.getKerningPairHtmlFilename(ufoglyph0, ufoglyph1)
            self.writeGenericSectionsLog(logSections,
                                         pageTitles=('Kerning Pair:'
                                                     '%s vs. %s' % ( formatGlyphName(ufoglyph0),
                                                                     formatGlyphName(ufoglyph1), ), ),
                                         pageComments=(comment,),
                                         logFilename=logFilename,
                                         logGroupName='Kerning Pairs',
                                         logGroupDescription=comment,
                                         logIndexName=('%s vs. %s' % (ufoglyph0.name, ufoglyph1.name,)),
                                         localVars=locals(),
#                                     linkMaps=disparityLinkMaps
                                      )
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
#        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))
        for ufoglyph0 in glyphs:
            if ufoglyph0.name in self.ignoredGlyphNames:
                count += len(glyphs)
                continue

            for ufoglyph1 in glyphs:
                if ufoglyph1.name in self.ignoredGlyphNames:
                    count += 1
                    continue

#                print count, ufoglyph0.name, ufoglyph1.name

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

                remaining = '%s remaining' % ( formatTimeDuration(remainingTime), )

                def formatUnicode(value):
                    if value is None:
                        return 'None'
                    else:
                        return '0x%X' % ( value, )
#                print 'ufoglyph0', ufoglyph0.unicode, ufoglyph0.name, 'ufoglyph1', ufoglyph1.unicode, ufoglyph1.name
                print '\t', '%s vs. %s %d / %d (%0.2f%%)' % ( ufoglyph0.name,
                                                              ufoglyph1.name,
                                                              count,
                                                              total,
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


    def writeSourceLogSectionMap(self, ufoglyph0, ufoglyph1):

        srcufoglyph0 = self.srcUfoFont.getGlyphByName(ufoglyph0.name)
        if srcufoglyph0 is None:
            raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph0.name),
                                                                     str(ufoglyph0.unicode)))
        srcufoglyph1 = self.srcUfoFont.getGlyphByName(ufoglyph1.name)
        if srcufoglyph1 is None:
            raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph1.name),
                                                                     str(ufoglyph1.unicode)))

        srcKerning = self.srcUfoFont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
        if srcKerning is None:
            srcKerning = 0
        srcAdvance = srcufoglyph0.xAdvance
        srcKernedAdvance = srcAdvance + srcKerning

        return self.writeLogSectionMap('Original',
                                       self.srcCache,
                                        srcufoglyph0, srcufoglyph1,
                                        srcKernedAdvance,
                                        comments=('The original kerning from the input.',) )


    def writeLogSectionMap(self,
                           title,
                           cache,
                           ufoglyph0, ufoglyph1,
#                           glyphProfile0, glyphProfile1,
                           advanceValue,
                           strokePathTuples = None,
                           extraVariableTuples=None,
                           comments=None):

        glyphXAdvance0 = ufoglyph0.xAdvance
        glyphXAdvance1 = ufoglyph1.xAdvance

        fillPathTuples = ()

        if strokePathTuples is None:
            strokePathTuples = ()

        glyphMinmax0 = cache.getContoursMinmax(ufoglyph0)
        glyphMinmax1 = cache.getContoursMinmax(ufoglyph1)
        glyphContours0 = cache.getGlyphContours(ufoglyph0)
        glyphContours1 = cache.getGlyphContours(ufoglyph1)
#        glyphMinmax0 = minmaxPaths(glyphContours0)
#        glyphMinmax1 = minmaxPaths(glyphContours1)
        glyphContours1 = xTranslateContours(glyphContours1, advanceValue)
        glyphMinmax1_ = minmaxPaths(glyphContours1)

        avgGlyphWidth = ((glyphMinmax0.maxX - glyphMinmax0.minX) +
                         (glyphMinmax1.maxX - glyphMinmax1.minX)) * 0.5
        fillAdvance = glyphMinmax1_.maxX + avgGlyphWidth / 3.0

        def fillGlyphContours(glyphContours, glyphColor):
            result = ()
            tempUfoFont = robofab.world.NewFont(familyName='ignore', styleName='ignore')
            tempUfoGlyph = tempUfoFont.newGlyph('ignore')
            tempTFSGlyph = TFSGlyph(tempUfoGlyph)
            tempTFSGlyph.setContours(glyphContours, correctDirection=True)
            reorientedContours = tempTFSGlyph.getContours(warnings=False)

            for contour in reorientedContours:
                if isClosedPathClockwise(contour):
                    result += ( ( glyphColor, [contour,] ), )
                else:
                    result += ( ( 0xffffffff, [contour,] ), )
            return result

        fillPathTuples += fillGlyphContours(xTranslateContours(glyphContours0, fillAdvance,), 0x7f7faf7f)
        fillPathTuples += fillGlyphContours(xTranslateContours(glyphContours1, fillAdvance,), 0x7f7f7faf)
#        fillPathTuples += (
#                           ( 0x7f7faf7f, xTranslateContours(glyphContours0, fillAdvance,), ),
#                           ( 0x7f7f7faf, xTranslateContours(glyphContours1, fillAdvance,), ),
#                           )

        variableTuples = (
                          ('%s (%s) lsb' % (ufoglyph0.name, formatUnicode(ufoglyph0.unicode),), (glyphMinmax0.minX), True,),
                          ('%s (%s) rsb' % (ufoglyph0.name, formatUnicode(ufoglyph0.unicode),), (glyphXAdvance0 - glyphMinmax0.maxX), True,),
                          ('%s (%s) right x-extrema' % (ufoglyph0.name, formatUnicode(ufoglyph0.unicode),), (glyphMinmax0.maxX), True,),
                          ('%s (%s) x-advance' % (ufoglyph0.name, formatUnicode(ufoglyph0.unicode),), (glyphXAdvance0), True,),
                          ('%s (%s) lsb' % (ufoglyph1.name, formatUnicode(ufoglyph1.unicode),), (glyphMinmax1.minX), True,),
                          ('%s (%s) rsb' % (ufoglyph1.name, formatUnicode(ufoglyph1.unicode),), (glyphXAdvance1 - glyphMinmax1.maxX), True,),
                          ('%s (%s) right x-extrema' % (ufoglyph0.name, formatUnicode(ufoglyph1.unicode),), (glyphMinmax1.maxX), True,),
#                                  ('%s x-advance' % (title,), self.formatUnitsInEms(glyphXAdvance0), True,),
                          ('%s kerning value' % (title,), self.formatUnitsInEms(advanceValue - glyphXAdvance0), True,),
                          ('%s kerned x-advance' % (title,), self.formatUnitsInEms(advanceValue), True,),
                          )

        section_x_extrema_offset = glyphMinmax1_.minX - glyphMinmax0.maxX
        if section_x_extrema_offset >= 0:
            variableTuples += ( (title + ' x-extrema offset', self.formatUnitsInEms(section_x_extrema_offset), True, ), )
        else:
            variableTuples += ( (title + ' x-extrema overlap', self.formatUnitsInEms(-section_x_extrema_offset), True, ), )

        if self.ignore_x_extrema_overlap_outside_ascender:
            adjGlyphMinmax0 = cache.getAdjMinmax(ufoglyph0, self)
            adjGlyphMinmax1 = minmaxPathsEvaluatedWithinYRange(glyphContours1, AUTOKERN_SEGMENT_PRECISION, 0, self.ascender)
#            print 'ufoglyph0,1', ufoglyph0.name, ufoglyph1.name
#            print 'adjGlyphMinmax0', adjGlyphMinmax0
#            print 'adjGlyphMinmax1', adjGlyphMinmax1
            if adjGlyphMinmax0 is not None and adjGlyphMinmax1 is not None:
                adj_section_x_extrema_offset = adjGlyphMinmax1.minX - adjGlyphMinmax0.maxX
                if adj_section_x_extrema_offset >= 0:
                    variableTuples += ( (title + ' in-ascender x-extrema offset', self.formatUnitsInEms(adj_section_x_extrema_offset), True, ), )
                else:
                    variableTuples += ( (title + ' in-ascender x-extrema overlap', self.formatUnitsInEms(-adj_section_x_extrema_offset), True, ), )
            else:
                variableTuples += ( (title + ' in-ascender x-extrema overlap', 'None', True, ), )

        if extraVariableTuples:
            variableTuples += extraVariableTuples

        hRanges = ( ( 'x-extrema overlap',
                      min(glyphMinmax0.maxX, glyphMinmax1_.minX),
                      max(glyphMinmax0.maxX, glyphMinmax1_.minX), ), )

        return {'title': title,
                'svg': self.renderSvgScene(None,
                                           pathTuples = (
                                                         ( 0x7f7faf7f, glyphContours0, ),
                                                         ( 0x7f7f7faf, glyphContours1, ),
                                                         ),
                                           fillPathTuples = fillPathTuples,
                                           strokePathTuples = strokePathTuples,
                                           hRanges = hRanges,
                                           hGuidelines = ( advanceValue, # RSB
                                                           glyphXAdvance0, # LSB
                                                           min(glyphMinmax0.maxX, glyphMinmax1_.minX),
                                                           max(glyphMinmax0.maxX, glyphMinmax1_.minX),
                                             ) ),
                'variables': variableTuples,
                'comments': comments,
                }


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


    def updateKerning(self):
        if self.only_modify_side_bearings:
            print 'Clearing kerning...'
            self.dstUfoFont.clearKerning()
            return

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
#            print 'name0, name1', name0, name1, 'kerningValue', kerningValue, 'advance', advance, 'glyphWidth', glyphWidthMap[name0]
#            if key in (
#                       ('j', 'o',),
#                        ):
#                print 'updateKerning', key, kerningValue

            if abs(kerningValue) < self.kerning_threshold:
                continue
            kerningTuples.append( ( name0, name1, kerningValue, ) )

        def cmpKerningTuples(value0, value1):
            return cmp(abs(value0[-1]), abs(value1[-1]))
        kerningTuples.sort(cmpKerningTuples, reverse=True)

#        print 'kerningTuples', kerningTuples[0]
#        print 'kerningTuples[-1]', kerningTuples[-1]

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
#            if (name0, name1) in (
#                       ('j', 'o',),
#                        ):
#                print 'updateKerning.1', key, kerningValue

            self.dstUfoFont.setKerningPair(name0, name1, kerningValue)


    def clearSideBearings(self):

        if self.pairsToKern is not None:
            return
        if self.glyphsToKern is not None:
            return

        print 'Clearing Side Bearings...'

        '''
        Removes the left and right side bearings from the glyph.
        '''
        glyphs = self.dstUfoFont.getGlyphs()
#        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))
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

            if ufoglyph.name in self.ignoredGlyphNames:
                '''
                TODO: Should we normalize the side bearings of these glyphs to perhaps half of max_distance?
                '''
#                defaultSideBearing = self.max_distance * 0.5
#                contours = [contour.applyPlus(TFSPoint(defaultSideBearing + -minmax.minX, 0)) for contour in contours]
#                ufoglyph.setContours(contours, correctDirection=False)
#                ufoglyph.setXAdvance(2 * defaultSideBearing + minmax.maxX - minmax.minX)
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
#        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))

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
#                       ('j', 'o',),
##                       ('N','N',),
##                       ('A','A',),
##                        ('A','F',),
#                        ):
#                print 'self.advanceMap', key, self.advanceMap[key]

        for ufoglyph in glyphs:
            if self.glyphsToKern is not None:
                if ufoglyph.name not in self.glyphsToKern:
                    continue
            elif ufoglyph.name in self.ignoredGlyphNames:
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
            leftSideBearing = rightSideBearing = 0.5 * self.max_distance
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
#                       'j', 'o',
##                                 'N',
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
#                       'j', 'o',
##                                 'N',
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
#                       ('j', 'o',),
##                       ('N','N',),
##                       ('A','A',),
##                        ('A','F',),
#                        ):
#                print 'self.advanceMap', key, self.advanceMap[key]
#        for key in modifiedAdvanceMap:
#            if key in (
#                       ('j', 'o',),
##                       ('N','N',),
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


    def convertTextToContours(self, text, ufoFont, cache, lastKerningValues=None):
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
                print u'Unknown glyph in sample text: %s' % (formatUnicode(codePoint),)
#                print u'Unknown glyph in sample text: %s %s' % (textGlyph, formatUnicode(codePoint),)
                raise Exception(u'Unknown glyph in sample text: %s' % (formatUnicode(codePoint),))
#                return None
#                if len(contours) < 1:
#                    continue

            contours = cache.getGlyphContours(ufoglyph)
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
            minmax = None
            kerningValue = 0
            
            if contours:
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
    
    #            print
    #            print 'xOffset', xOffset
    #            print 'ufoglyph.name', ufoglyph.name
    #            print 'ufoglyph.xAdvance', ufoglyph.xAdvance
    #            print 'kerningValue', kerningValue
    #            minmax = minmaxPaths(contours)
    #            print 'minmax.raw', minmax
    
                contours = [contour.applyPlus(TFSPoint(xOffset, 0)) for contour in contours]
                minmax = minmaxPaths(contours)
    
    #            print 'minmax', minmax
    
                if ((kerningValue is not None) and
                    (lastMinmax is not None)):
                    xExtremaOverlap = minmax.minX - lastMinmax.maxX
    #                print 'lastMinmax', lastMinmax
    #                print 'xExtremaOverlap', xExtremaOverlap
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
    
    #                    print 'index', index
    #                    print 'lastXExtremaOverlap', lastXExtremaOverlap
    #                    print 'xExtremaOverlapDelta', xExtremaOverlapDelta
    
                        KERNING_HIGHLIGHT_LOW_THRESHOLD = 10
                        KERNING_HIGHLIGHT_HIGH_THRESHOLD = 20
                        if abs(xExtremaOverlapDelta) >= KERNING_HIGHLIGHT_HIGH_THRESHOLD:
                            KERNING_LABEL_COLOR = 0xdfa70000
                        elif abs(xExtremaOverlapDelta) >= KERNING_HIGHLIGHT_LOW_THRESHOLD:
                            KERNING_LABEL_COLOR = 0xff530000
    
                        text += ' (%s%0.0f)' % (
                                               '' if xExtremaOverlapDelta == 0 else ('+' if xExtremaOverlapDelta > 0 else '-'),
                                               float(abs(xExtremaOverlapDelta)),
                                               )
    
                    if lastUfoGlyph is not None and lastKerningValues is not None:
                        '''
                        For the Autokern kerning values, we want to visually highlight
                        values which were not kerned.
                        '''
                        if ( lastUfoGlyph.name, ufoglyph.name, ) not in self.advanceMap:
                            '''
                            Kerning pair was ignored.
                            '''
                            KERNING_LABEL_COLOR = 0xdf007f7f
    
    
                    label = TFSMap()
                    label.text = text
    #                # Subtract half of the kerning value to center on the ker
    #                labelX = xOffset - kerningValue * 0.5
    #                labelX = xOffset
                    # Center label between the x-extrema of the two glyphs.
                    labelX = (minmax.minX + lastMinmax.maxX) * 0.5
                    label.origin = TFSPoint(labelX, -abs(self.descender * 1.1))
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
    
                for contour in contours:
                    if isClosedPathClockwise(contour):
                        outsideContours.append(contour)
                    else:
                        insideContours.append(contour)

            xOffset += ufoglyph.xAdvance
            lastMinmax = minmax
            lastUfoGlyph = ufoglyph

        return outsideContours, insideContours, labels, kerningValues


    def renderTextWithFont(self, text, ufoFont, cache, source, fillColor, lastKerningValues=None):
        try:
            converted = self.convertTextToContours(text, ufoFont, cache, lastKerningValues=lastKerningValues)
        except Exception, e:
            return {'text': formatUnicodeForHtml(text), 
                    'errorMap': {'text': formatUnicodeForHtml(text), 
                                 'source': source,
                                 'message': e.message,
                                 },
                    }, None
            
        outsideContours, insideContours, labels, kerningValues = converted

        sampleSvg = self.renderSvgScene(None,
                                        fillPathTuples = ( ( fillColor, outsideContours, ),
                                                           ( 0xffffffff, insideContours, ),
                                                           ),
                                        textTuples = labels,
                                        padding=(0,0,20,0),
#                                            maxWidth = 800,
#                                            maxHeight = 300,
                                        maxWidth = 700,
                                        maxHeight = 250,
                                        )
        return {'text': formatUnicodeForHtml(text), 
                'renderMap': {'text': formatUnicodeForHtml(text), 
               'source': source,
               'svg': sampleSvg},
               }, kerningValues


    def writeSamples(self):

        renderLog = self.log_path is not None
        if not renderLog:
            return
        print 'Writing samples...'

        sampleTextsMaps = []
        for index, sampleText in enumerate(self.sampleTexts):
            sampleTextMap, kerningValues = self.renderTextWithFont(sampleText, self.srcUfoFont, self.srcCache, 'Original', 0x7f7f7faf)
            sampleTextMap['indexMap'] = { 'index': index,
                                         'indexName': sampleTextMap['text'],
                                         }
            sampleTextsMaps.append(sampleTextMap)
            sampleTextMap, _ = self.renderTextWithFont(sampleText, self.dstUfoFont, self.dstCache, 'Autokern', 0x7f7faf7f,
                                                       lastKerningValues=kerningValues)
            sampleTextsMaps.append(sampleTextMap)


        pageTitle = u'Autokern Sample Texts'

        mustacheMap = self.makeDefaultMustacheMap(localsMap=locals())
        self.addSidebarMustacheMap(mustacheMap, kerned=True)
        mustacheMap.update({
                   'pageTitle': pageTitle,
                   'sampleTextsMaps': sampleTextsMaps,
                   })

        self.writeLogFile('autokern_samples_template.txt',
                          'sample_texts.html',
                          'Sample Texts',
                              '''
    Side-by-side comparisons of short texts using the original kerning and Autokern's kerning.
                              ''',
                          'Sample Texts',
                          mustacheMap)


    def writeLogIndex(self):

        renderLog = self.log_path is not None
        if not renderLog:
            return
        print 'Writing log index...'

        groupDescriptionMap = {}
        groupNames = []
        groupItemsMap = {}
        for groupName, groupDescription, filename, logIndexName in self.logFileTuples:
            groupDescriptionMap[groupName] = groupDescription
            groupItemsMap[groupName] = groupItemsMap.get(groupName, []) + [(filename, logIndexName,)]
            if groupName not in groupNames:
                groupNames.append(groupName)

        logGroupMaps = []
        for groupName in groupNames:
            logGroupItems = []
            for filename, logIndexName in groupItemsMap[groupName]:
                logGroupItems.append({'groupName': groupName,
                                      'logItemFilename': filename,
                                      'logItemIndexName': logIndexName,
                                      })
            groupSuffix = ''
            if len(logGroupItems) > 100:
                logGroupItems = logGroupItems[:100]
                groupSuffix = '...'
            logGroupMaps.append({'logGroupName': groupName,
                                 'logGroupDescription': groupDescriptionMap[groupName],
                                 'logGroupItems': logGroupItems,
                                 'groupSuffix': groupSuffix,
                                 })


        pageTitle = u'Autokern Results'

        mustacheMap = self.makeDefaultMustacheMap(localsMap=locals())
        self.addSidebarMustacheMap(mustacheMap, kerned=True, complete=True)
        mustacheMap.update({
                   'pageTitle': pageTitle,
                   'logGroupMaps': logGroupMaps,
                   })

        self.writeLogFile('autokern_index_template.txt',
                          'index.html',
                          None,
                          None,
                          None,
                          mustacheMap)


    def writeLogFile(self,
                     templateFilename, logFilename,
                     groupName, groupDescription,
                     logIndexName, mustacheMap):

        import tfs.common.TFSProject as TFSProject
#        dataFolder = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data'))
        mustache_template_file = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', templateFilename))
        with open(mustache_template_file, 'rt') as f:
            mustache_template = f.read()

        import pystache

#        class CustomMustacheRenderer(pystache.renderer.Renderer):
#
#            def __init__(self):
#                pystache.renderer.Renderer.__init__(self, search_dirs=[dataFolder,])
#
#            def load_template(self, template_name):
#                print 'load_template', template_name
#                return pystache.renderer.Renderer.load_template(self, template_name)
#
#
#        renderer = CustomMustacheRenderer()
#        renderer = pystache.renderer.Renderer(search_dirs=[dataFolder,],
#                                              file_extension='.mustache')
##        print 'renderer', renderer
#        logHtml = renderer.render(mustache_template, mustacheMap)

        logHtml = pystache.render(mustache_template, mustacheMap)

        logFile = os.path.abspath(os.path.join(self.html_folder, logFilename))
        with open(logFile, 'wt') as f:
            # TODO: explicitly encode unicode
            f.write(logHtml)

        if groupName is not None:
            self.logFileTuples.append( (groupName, groupDescription, logFilename, logIndexName,) )


    def process(self):
        print
        startTime = time.time()

        self.configure()

#        self.dstUfoFont.save(self.ufo_dst_path + '.1.ufo')

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

#        self.dstUfoFont.save(self.ufo_dst_path + '.3.ufo')

#        print 'updateKerning'
        self.updateKerning()
        self.timing.mark('updateKerning.')

#        self.dstUfoFont.save(self.ufo_dst_path + '.5.ufo')

        self.writeSamples()
        self.timing.mark('writeSamples.')

        self.logDisparities()
        self.timing.mark('logDisparities.')

        self.elapsedDatetime = formatTimeDuration(time.time() - startTime)
        self.finishDatetime = time.strftime('%h. %d, %Y %H:%M:%S', time.localtime())

        self.writeBasicPairsLog()
        self.timing.mark('writeBasicPairsLog.')

        self.writeLogIndex()
        self.timing.mark('writeLogIndex.')

#        self.dstUfoFont.save(self.ufo_dst_path + '.7.ufo')

        self.dstUfoFont.update()
        self.dstUfoFont.save(self.ufo_dst_path)
        self.dstUfoFont.close()

        self.timing.mark('finished.')
        if True:
            self.timing.dump()


if __name__ == "__main__":
    autokernArgs = TFSMap()
    AutokernSettings(autokernArgs).getCommandLineSettings()
    autokern = Autokern(autokernArgs)
    AutokernSettings(autokern).getCommandLineSettings()
    try:
        autokern.process()
        print
        print 'complete.'
    except Exception, e:
        print 'Error:', str(e)
        traceback.print_exc()
