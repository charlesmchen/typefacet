'''
robofont-extensions-and-scripts
FontInterpolator.py

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
import types

from tfs.common.TFSFont import *
from tfs.common.TFSMap import *
#from TFSSvg import *
from tfs.common.TFSPoint import TFSPoint, minmaxMerge, minmaxPoints
from tfs.common.TFSPath import minmaxPaths, openPathWithPoints
import TFSCompoundsList as TFSCompoundsList

from FISettings import getCommandLineSettings


class FontInterpolator(object):

    def __init__(self, settings = None):
        if settings is None:
            self.settings = getCommandLineSettings()
        else:
            self.settings = settings

        self.configure()
        self.initMetrics()


    def configure(self):

        ufo_src_path = self.settings.ufo_src
        if ufo_src_path is None:
            raise Exception('Missing ufo_src_path')
        if not (os.path.exists(ufo_src_path) and os.path.isdir(ufo_src) and os.path.basename(ufo_src).lower().endswith('.ufo')):
            raise Exception('Invalid ufo_src_path: %s' % ufo_src)
        self.ufo_src_path = ufo_src

        ufo_dst_path = self.settings.ufo_dst
        if ufo_dst_path is None:
            raise Exception('Missing ufo_dst_path')
        if os.path.exists(ufo_dst_path):
            shutil.rmtree(ufo_dst_path)
    #    if not (os.path.exists(ufo_dst_path) and os.path.isdir(ufo_dst) and os.path.basename(ufo_dst).lower().endswith('.ufo')):
    #        raise Exception('Invalid ufo_dst_path: %s' % ufo_dst)
        self.ufo_dst_path = ufo_dst

        if os.path.abspath(ufo_src_path) == os.path.abspath(ufo_dst_path):
            raise Exception('ufo_src_path and ufo_dst_path cannot be the same file.')

        otf_dst = self.settings.otf_dst
        if otf_dst is not None:
#        if otf_dst is None:
#            raise Exception('Missing ufo_dst_path')
            if os.path.exists(otf_dst):
                os.unlink(otf_dst)
    #    if not (os.path.exists(ufo_dst_path) and os.path.isdir(ufo_dst) and os.path.basename(ufo_dst).lower().endswith('.ufo')):
    #        raise Exception('Invalid ufo_dst_path: %s' % ufo_dst)
        self.otf_dst = otf_dst



    #    testFont = os.path.abspath(os.path.join('..', '..', 'data', 'FITest Plain.ufo'))
        self.fifont = TFSFontFromFile(ufo_src_path)

    #    interpolation.srcCodePoints = interpolation.fifont.glyphCodePoints()

        log_path = self.settings.log_dst
        if log_path is None:
            self.log_path = None
    #        raise Exception('Missing log_path')
            pass
        else:
            if os.path.exists(log_path):
                shutil.rmtree(log_path)
            os.mkdir(log_path)
            if not (os.path.exists(log_path) and os.path.isdir(log_dst)):
                raise Exception('Invalid log_path: %s' % log_dst)
            self.log_path = log_dst

            def makeLogSubfolder(parent, name):
                subfolder = os.path.abspath(os.path.join(parent, name))
                os.mkdir(subfolder)
                if not (os.path.exists(subfolder) and os.path.isdir(subfolder)):
                    raise Exception('Invalid log_path: %s' % log_dst)
                return subfolder

            self.html_folder = makeLogSubfolder(log_path, 'html')
            self.css_folder = makeLogSubfolder(self.html_folder, 'stylesheets')
            self.svg_folder = makeLogSubfolder(self.html_folder, 'svg')


            import tfs.common.TFSProject as TFSProject
            srcCssFile = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'styles.css'))
            dstCssFile = os.path.abspath(os.path.join(self.css_folder, os.path.basename(srcCssFile)))
            shutil.copy(srcCssFile, dstCssFile)


        self.default_diacritical_distance = self.settings.default_diacritical_distance_ems * self.fifont.units_per_em
        print 'default_diacritical_distance', self.default_diacritical_distance

        self.topJoinCentersMap = {}
        self.populateAlignmentMap('--top-join-centers',
                                  self.topJoinCentersMap,
                                  self.settings.top_join_centers)

        self.tailJoinCentersMap = {}
        self.populateAlignmentMap('--tail-join-centers',
                                  self.tailJoinCentersMap,
                                  self.settings.tail_join_centers)

        self.middleJoinCentersMap = {}
        self.populateAlignmentMap('--middle-join-centers',
                                  self.middleJoinCentersMap,
                                  self.settings.middle_join_centers)

    #    kerning.units_per_em = float(kerning.fifont.units_per_em)
    #    kerning.min_distance = settings.min_distance_ems * kerning.fifont.units_per_em
    #    kerning.max_distance = settings.max_distance_ems * kerning.fifont.units_per_em
    #    kerning.rounding = settings.rounding_ems * kerning.fifont.units_per_em
    #    print 'kerning.units_per_em', kerning.units_per_em
    #    print 'kerning.min_distance', kerning.min_distance
    #    print 'kerning.max_distance', kerning.max_distance
    #    print 'kerning.rounding', kerning.rounding
    #    kerning.fontMetadata = kerning.fifont.info


    def populateAlignmentMap(self, name, map, values):
        if values is None:
            return
        for index in xrange(len(values) / 2):
            codePointRaw = values[index * 2 + 0]
            centerRaw = values[index * 2 + 1]
#            print 'codePointRaw', codePointRaw, 'centerRaw', centerRaw

            def parseCodePoint(value):
                try:
                    if value.startswith('0x'):
                        return int(value, 16)
                    else:
                        return int(value)
                except Exception, e:
                    raise Exception('Invalid %s value: %s' % ( name, str(value),))

            def parseAlignmentValue(value):
                try:
                    return float(value)
                except Exception, e:
                    raise Exception('Invalid %s value: %s' % ( name, str(value),))

            def parseAlignmentPoint(value):
                try:
                    if ',' in value:
                        left, right = value.split(',')
                        result = TFSMap()
                        result.x = parseAlignmentValue(left)
                        result.y = parseAlignmentValue(right)
                        return result
                    else:
                        result = TFSMap()
                        result.x = parseAlignmentValue(value)
                        result.y = None
                        return result
                except ValueError, e:
                    raise Exception('Invalid %s value: %s' % ( name, str(value),))

            codePoint = parseCodePoint(codePointRaw)
            center = parseAlignmentPoint(centerRaw)
            map[codePoint] = center


    def subrenderGlyphContours(self, fiSvg, contours, strokeColor):
        from tfs.common.TFSSvg import TFSSvgPath

        ON_POINT_COLOR = 0x7f7f7f7f
        CONTROL_POINT_COLOR = 0x7fafafaf
        for contour in contours:
            fiSvg.addItem(TFSSvgPath(contour).addStroke(strokeColor, 2).addPointHighlights(ON_POINT_COLOR, CONTROL_POINT_COLOR))


    def renderSvgScene(self,
                       filenamePrefix,
                       pathTuples,
                       hGuidelines=None):
        from tfs.common.TFSSvg import TFSSvg, TFSSvgPath

        filename = '%s.svg' % ( filenamePrefix, )
        dstFile = os.path.abspath(os.path.join(self.svg_folder, filename))

        CANVAS_BACKGROUND_COLOR = 0xffffffff
        CANVAS_BORDER_COLOR = 0x07fbfbfbf
        fiSvg = TFSSvg().withBackground(CANVAS_BACKGROUND_COLOR).withBorder(CANVAS_BORDER_COLOR)

    #    if pathTuples:
        for color, contours in pathTuples:
            self.subrenderGlyphContours(fiSvg, contours, color)

        if hGuidelines:
            for hGuideline in hGuidelines:
                p0 = TFSPoint(hGuideline, self.fifont.info.descender)
                p1 = TFSPoint(hGuideline, self.fifont.info.ascender)
                GUIDELINE_COLOR = 0x7fdfdfdf
                fiSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

        vGuidelines = ( 0,
                        self.fifont.info.ascender,
                        self.fifont.info.descender,
                        )
        if vGuidelines:
            minmax = None
            for color, contours in pathTuples:
                minmax = minmaxMerge(minmax, minmaxPaths(contours))

            for vGuideline in vGuidelines:
                p0 = TFSPoint(0, vGuideline)
                p1 = TFSPoint(minmax.maxX, vGuideline)
                GUIDELINE_COLOR = 0x7fdfdfdf
                fiSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

        SVG_HEIGHT = 400
        SVG_MAX_WIDTH = 800
        fiSvg.renderToFile(dstFile, margin=10, height=SVG_HEIGHT, maxWidth=SVG_MAX_WIDTH)
        return filename


    def convertCodePoint(self, glyph):
        if type(glyph) is types.IntType:
            return glyph
        elif type(glyph) is types.StringType:
            return ord(glyph)
        else:
            raise Exception('Bad glyph: ' + str(glyph))


    def appendDiacriticalContours(self,
                                  alignment,
                                  baseContours,
                                  diacriticalContours,
                                  baseCodePoint,
                                  diacriticalCodePoint):

        baseMinmax = minmaxPaths(baseContours)
        diacriticalMinmax = minmaxPaths(diacriticalContours)

        def minmaxHCenter(minmax):
            return (minmax.minX) + ((minmax.maxX - minmax.minX) * 0.5)

        def minmaxVCenter(minmax):
            return (minmax.minY) + ((minmax.maxY - minmax.minY) * 0.5)

        def minmaxTop(minmax):
            return minmax.maxY

        def minmaxBottom(minmax):
            return minmax.minY

        def getOffsetX(codePoint, joinCentersMap, defaultValue):
            if codePoint in joinCentersMap:
                offset = joinCentersMap[codePoint]
                return offset.x
            else:
                return defaultValue

        def getOffsetY(codePoint, joinCentersMap, defaultValue):
            if codePoint in joinCentersMap:
                offset = joinCentersMap[codePoint]
                if offset.y is None:
                    return defaultValue
                return offset.y
            else:
                return defaultValue

        if alignment == TFSCompoundsList.DIACRITICAL_ALIGN_TOP_ROTATE_FLOAT:
            diacriticalContours = [contour.applyScale(-1.0) for contour in diacriticalContours]
            diacriticalMinmax = minmaxPaths(diacriticalContours)
            alignment = TFSCompoundsList.DIACRITICAL_ALIGN_TOP
        elif alignment == TFSCompoundsList.DIACRITICAL_ALIGN_TAIL_H_FLIP:
            diacriticalContours = [contour.applyScaleXY(-1.0, 1.0) for contour in diacriticalContours]
            diacriticalMinmax = minmaxPaths(diacriticalContours)
            alignment = TFSCompoundsList.DIACRITICAL_ALIGN_TAIL

        if alignment == TFSCompoundsList.DIACRITICAL_ALIGN_TOP:
            offsetX = (getOffsetX(baseCodePoint, self.topJoinCentersMap, minmaxHCenter(baseMinmax)) -
                       getOffsetX(diacriticalCodePoint, self.topJoinCentersMap, minmaxHCenter(diacriticalMinmax)))
            offsetY = (self.default_diacritical_distance +
                       getOffsetY(baseCodePoint, self.topJoinCentersMap, minmaxTop(baseMinmax)) -
                       getOffsetY(diacriticalCodePoint, self.topJoinCentersMap, minmaxBottom(diacriticalMinmax)))
        elif alignment == TFSCompoundsList.DIACRITICAL_ALIGN_TAIL:
            offsetX = (getOffsetX(baseCodePoint, self.tailJoinCentersMap, minmaxHCenter(baseMinmax)) -
                       getOffsetX(diacriticalCodePoint, self.tailJoinCentersMap, minmaxHCenter(diacriticalMinmax)))
            offsetY = (getOffsetY(baseCodePoint, self.tailJoinCentersMap, minmaxBottom(baseMinmax)) -
                       getOffsetY(diacriticalCodePoint, self.tailJoinCentersMap, minmaxTop(diacriticalMinmax)))
        elif alignment == TFSCompoundsList.DIACRITICAL_ALIGN_TAIL_FLOAT:
            offsetX = (getOffsetX(baseCodePoint, self.tailJoinCentersMap, minmaxHCenter(baseMinmax)) -
                       getOffsetX(diacriticalCodePoint, self.tailJoinCentersMap, minmaxHCenter(diacriticalMinmax)))
            offsetY = (getOffsetY(baseCodePoint, self.tailJoinCentersMap, minmaxBottom(baseMinmax)) -
                       getOffsetY(diacriticalCodePoint, self.tailJoinCentersMap, minmaxTop(diacriticalMinmax))) - self.default_diacritical_distance
        elif alignment == TFSCompoundsList.DIACRITICAL_ALIGN_MIDDLE:
            offsetX = (getOffsetX(baseCodePoint, self.middleJoinCentersMap, minmaxHCenter(baseMinmax)) -
                       getOffsetX(diacriticalCodePoint, self.middleJoinCentersMap, minmaxHCenter(diacriticalMinmax)))
            offsetY = (getOffsetY(baseCodePoint, self.middleJoinCentersMap, minmaxVCenter(baseMinmax)) -
                       getOffsetY(diacriticalCodePoint, self.middleJoinCentersMap, minmaxVCenter(diacriticalMinmax)))
        else:
            raise Exception('Unknown diacritical aligment: ' + alignment)

        offsetX = round(offsetX)
        offsetY = round(offsetY)

        diacriticalContours = [contour.applyPlus(TFSPoint(offsetX, offsetY)) for contour in diacriticalContours]

        return baseContours + diacriticalContours


    def createCompoundGlyph(self, dstCodePoint, baseCodePoint, diacriticals):

        dstCodePoint = self.convertCodePoint(dstCodePoint)
        dstGlyph = self.fifont.getGlyphByCodePoint(dstCodePoint)
        if dstGlyph is not None:
            self.existingCompoundGlyphs.add(dstCodePoint)
            return

        baseCodePoint = self.convertCodePoint(baseCodePoint)

        baseExceptionMap = {
                            0x69: # LATIN SMALL LETTER I
                            0x0131, # LATIN SMALL LETTER DOTLESS I
                            }
        if baseCodePoint in baseExceptionMap:
            baseCodePoint = baseExceptionMap[baseCodePoint]

        baseGlyph = self.fifont.getGlyphByCodePoint(baseCodePoint)
        if baseGlyph is None:
            self.unknownBaseGlyphs.add(baseCodePoint)
            self.unknownCompoundGlyphs.add(dstCodePoint)
            return
        else:
            self.knownBaseGlyphs.add(baseCodePoint)

        contours = baseGlyph.getContours()

    ##    diacriticals = [convertGlyph(diacritical) for diacritical in diacriticals]
    #
    #    py_prefix = '''
    #from funt.FuntCommons import *
    #from funt_workaround2.shared import *
    #
    ## Code
    #v_guidelines.append('right')
    #
    #    '''
    #
    #    pytext = py_prefix
    #
    #    if ord('A') <= baseGlyph <= ord('Z'):
    #        diacriticalHeight = 'capHeight'
    #        basePackage = 'block03_uppercase'
    #        baseModule = 'GlyphLetter%s' % (chr(baseGlyph),)
    #        baseFilename = baseModule + '.py'
    #        baseFile = os.path.abspath(os.path.join(basePackage, baseFilename))
    #        if not (os.path.exists(baseFile) and os.path.isfile(baseFile)):
    #            raise Exception('Missing baseFile: ' + baseFile)
    #        knownBaseGlyphs.add(baseGlyph)
    #    elif ord('a') <= baseGlyph <= ord('z'):
    #        diacriticalHeight = 'xHeight'
    #        basePackage = 'block07_lowercase'
    #        baseModule = 'GlyphLetter%s' % (chr(baseGlyph),)
    #        baseFilename = baseModule + '.py'
    #        baseFile = os.path.abspath(os.path.join(basePackage, baseFilename))
    #        if not (os.path.exists(baseFile) and os.path.isfile(baseFile)):
    #            raise Exception('Missing baseFile: ' + baseFile)
    #        knownBaseGlyphs.add(baseGlyph)
    #    else:
    #        unknownBaseGlyphs.add(baseGlyph)
    #        unknownCompoundGlyphs.add(glyph)
    #        return
    #        raise Exception('Unknown base glyph: ' + str(baseGlyph))
    #
    #    pytext += '''
    #import funt_workaround2.%s.%s as %s
    #baseContours = %s.rawContours
    #contours = baseContours
    #
    #diacriticalOffsetX = 0
    #if hasattr(%s, 'diacriticalOffsetX'):
    #    diacriticalOffsetX = %s.diacriticalOffsetX
    #
    #diacriticalMiddleOffsetX = diacriticalOffsetX
    #if hasattr(%s, 'diacriticalMiddleOffsetX'):
    #    diacriticalMiddleOffsetX = %s.diacriticalMiddleOffsetX
    #    ''' % (basePackage, baseModule, baseModule, baseModule, baseModule, baseModule, baseModule, baseModule, )
    #
        diacriticalCodePoints = []
        for diacritical in diacriticals:
            diacriticalCodePoint = self.convertCodePoint(diacritical.glyph)
            diacriticalGlyph = self.fifont.getGlyphByCodePoint(diacriticalCodePoint)
#            print 'diacriticalCodePoint', diacriticalCodePoint
            if diacriticalGlyph is None:
                self.unknownDiacriticalGlyphs.add(diacriticalCodePoint)
                self.unknownCompoundGlyphs.add(dstCodePoint)
                return
            else:
                self.knownDiacriticalGlyphs.add(diacriticalCodePoint)

            contours = self.appendDiacriticalContours(diacritical.align,
                                                      contours,
                                                      diacriticalGlyph.getContours(),
                                                      baseCodePoint,
                                                      diacriticalCodePoint)
            diacriticalCodePoints.append(diacriticalCodePoint)

    #        diacriticalGlyph = convertGlyph(diacritical.glyph)
    #        diacriticalPackage = 'block04_diacriticals'
    #        diacriticalModule = 'GlyphCode%d' % (diacriticalGlyph,)
    #        diacriticalFilename = diacriticalModule + '.py'
    #        diacriticalFile = os.path.abspath(os.path.join(diacriticalPackage, diacriticalFilename))
    #        if not (os.path.exists(diacriticalFile) and os.path.isfile(diacriticalFile)):
    #            unknownDiacriticalGlyphs.add(diacriticalGlyph)
    #            unknownCompoundGlyphs.add(glyph)
    #            return
    #            raise Exception('Missing diacriticalFile: ' + diacriticalFile)
    #        knownDiacriticalGlyphs.add(diacriticalGlyph)
    #
    #        if diacritical.align == 'top':
    #            diacriticalFunction = 'addDiacriticalTop'
    #            diacriticalOffset = 'diacriticalOffsetX'
    #        elif diacritical.align == 'middle':
    #            diacriticalFunction = 'addDiacriticalMiddle'
    #            diacriticalOffset = 'diacriticalMiddleOffsetX'
    #        else:
    #            raise Exception('Unknown diacritical alignment: ' + diacritical.align)
    #
    #        pytext += '''
    #import funt_workaround2.%s.%s as %s
    #diacriticalContours = %s.rawContours
    #diacriticalContours = %s(diacriticalContours, baseContours, %s, %s)
    #contours += diacriticalContours
    #        ''' % (diacriticalPackage, diacriticalModule, diacriticalModule, diacriticalModule, diacriticalFunction, diacriticalOffset, diacriticalHeight)
    #
    #
    #    py_suffix = '''
    #
    #glyphWidth = %s.glyphWidth
    ##rawContours = contours
    ##contours, glyphWidth = postprocessing(contours)
    #
    ## We want to ignore the diacriticals when centering and determining the final glyph width.
    #rawContours = contours
    #contours, glyphWidth = postprocessing(contours, referencePaths=baseContours)
    #
    #right = glyphWidth
    #sideBearing = base_sideBearing
    #glyphAdvance = glyphWidth + sideBearing
    #    ''' % (baseModule, )
    #
    #    pytext += py_suffix
    #    dstFilename = 'GlyphCode%d.py' % (glyph,)
    #    dstFile = os.path.abspath(os.path.join(dstFolder, dstFilename))
    #    print 'dstFile', dstFile
    #    with open(dstFile, 'wt') as f:
    #        f.write(pytext)
    #
        self.fifont.insertGlyphDerivedFromGlyph(dstCodePoint, contours, baseGlyph)

        self.knownCompoundGlyphs.add(dstCodePoint)

        self.logData.append( (dstCodePoint, contours, baseCodePoint, diacriticalCodePoints, ) )


    def writeCompoundHtmlLog(self, dstCodePoint, contours, baseCodePoint, diacriticalCodePoints):

        import pystache

        def getFilenamePrefix(codePoint):
            return u'fi-%s' % ( hex(codePoint), )
#            filenamePrefix = u'fi-%s' % ( unichr(dstCodePoint), )
        filenamePrefix = getFilenamePrefix(dstCodePoint)
        glyphSvg = self.renderSvgScene( filenamePrefix,
                                        pathTuples = (
                                                      ( 0x7f7faf7f, contours, ),
                                                      ),
                                       )

        import tfs.common.TFSProject as TFSProject
        mustache_template_file = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'log_html_mustache.txt'))
        with open(mustache_template_file, 'rt') as f:
            mustache_template = f.read()

        def formatGlyphName(glyph):
            return hex(glyph)
#            return u'%s (%s)' % ( unichr(glyph),
#                                  hex(glyph), )

        pageTitle = u'font-interpolator Log: %s' % ( formatGlyphName(dstCodePoint), )

        linkMaps = []
        currentIndex = 0
        for index, (codePoint, _, _, _,) in enumerate(self.logData):
            if codePoint == dstCodePoint:
                currentIndex = index
            linkMaps.append({
                             'linkFilename': '%s.html' % ( getFilenamePrefix(codePoint), ),
                             'linkHex': '%X' % codePoint,
                             })

        prevCodePoint, _, _, _, = self.logData[(currentIndex + len(self.logData) - 1) % len(self.logData)]
        nextCodePoint, _, _, _, = self.logData[(currentIndex + 1) % len(self.logData)]

        import tfs.common.UnicodeCharacterNames as UnicodeCharacterNames

        def createGlyphMap(codePoint):
            return {
                       'glyphHex': '%X' % codePoint,
                       'glyphName': UnicodeCharacterNames.getUnicodeCharacterName(codePoint),
                    }

        diacriticalGlyphMaps = [createGlyphMap(codePoint) for codePoint in diacriticalCodePoints]
        mustacheMap = {
                       'pageTitle': pageTitle,
                       'glyphSvg': glyphSvg,
#                       'glyph': formatGlyphName(dstCodePoint),
#                       'glyphName': formatGlyphName(dstCodePoint),
                       'glyphHex': '%X' % dstCodePoint,
                       'glyphName': UnicodeCharacterNames.getUnicodeCharacterName(dstCodePoint),
                       'baseGlyphHex': '%X' % baseCodePoint,
                       'baseGlyphName': UnicodeCharacterNames.getUnicodeCharacterName(baseCodePoint),
                       'diacriticalGlyphs': diacriticalGlyphMaps,

                       'linkMaps': linkMaps,

                        'prevLinkFilename': '%s.html' % ( getFilenamePrefix(prevCodePoint), ),
                        'prevCodePoint': '%X' % prevCodePoint,
                        'prevGlyphName': UnicodeCharacterNames.getUnicodeCharacterName(prevCodePoint),
                        'nextLinkFilename': '%s.html' % ( getFilenamePrefix(nextCodePoint), ),
                        'nextCodePoint': '%X' % nextCodePoint,
                        'nextGlyphName': UnicodeCharacterNames.getUnicodeCharacterName(nextCodePoint),
                       }
#baseCodePoint, diacriticalCodePoints
        for key in (
                     'familyName',
                     'styleName',
                     'fullName',
                     'fontName',
                    ):
            mustacheMap[key] = getattr(self.fifont.info, key)

        logHtml = pystache.render(mustache_template, mustacheMap)

        logFilename = '%s.html' % ( filenamePrefix, )
        logFile = os.path.abspath(os.path.join(self.html_folder, logFilename))
        with open(logFile, 'wt') as f:
            # TODO: explicitly encode unicode
            f.write(logHtml)


    def initMetrics(self):
        self.unknownBaseGlyphs = set()
        self.unknownDiacriticalGlyphs = set()
        self.knownBaseGlyphs = set()
        self.knownDiacriticalGlyphs = set()
        self.knownCompoundGlyphs = set()
        self.unknownCompoundGlyphs = set()
        self.existingCompoundGlyphs = set()
        self.logData = []

    def writeOutput(self):
        self.fifont.writeToFile(self.ufo_dst_path)

        if self.otf_dst is not None:
            import tfs.common.TFSWriteOtf as TFSWriteOtf
            TFSWriteOtf.writeOtf(self.fifont.rffont, self.otf_dst)
#

        isLogActive = self.log_path is not None
        if isLogActive:
            for dstCodePoint, contours, baseCodePoint, diacriticalCodePoints in self.logData:
                self.writeCompoundHtmlLog(dstCodePoint, contours, baseCodePoint, diacriticalCodePoints)


    def getCodeRangeScore(self, start, end):
        fontCodePoints = self.fifont.glyphCodePoints()
        count = 0
        missing = []
        total = 0
        for codePoint in xrange(start, end + 1):
            if codePoint in fontCodePoints:
#        for codePoint in self.fifont.glyphCodePoints():
#            if start <= codePoint <= end:
                count += 1
            else:
                missing.append(codePoint)
            total += 1
        return count, total, missing


    def getLatinExtendedAScore(self):
        LATIN_EXTENDED_A_START = 0x0100
        LATIN_EXTENDED_A_END = 0x017F
        score, total, missing = self.getCodeRangeScore(LATIN_EXTENDED_A_START, LATIN_EXTENDED_A_END)
        return '%d / %d' % (
                            score,
                            total,
                            ), missing

    def process(self):
        compoundsList = TFSCompoundsList.getCompounds(self.log_path)

#        print
#        print 'compoundsList', compoundsList

        startScore, _ = self.getLatinExtendedAScore()

        self.initMetrics()

        for compoundMap in compoundsList:
            glyph = compoundMap['glyph']
            baseGlyph = compoundMap['baseGlyph']
            diacriticalMaps = compoundMap['diacriticals']
            diacriticals = []
            for diacriticalMap in diacriticalMaps:
#                print 'diacriticalMap', diacriticalMap
                diacritical = TFSMap()
                diacritical.glyph = diacriticalMap['glyph']
                diacritical.align = diacriticalMap['align']
                diacriticals.append(diacritical)

            self.createCompoundGlyph(glyph, baseGlyph, diacriticals)

        self.writeOutput()

        self.dumpMetrics()

        endScore, endMissing = self.getLatinExtendedAScore()
        print
        print 'startScore', startScore, 'endScore', endScore
        print 'endMissing', [hex(glyph) for glyph in sorted(endMissing)]



    def dumpMetrics(self):

        print
        print 'unknownBaseGlyphs', sorted(self.unknownBaseGlyphs)
        print 'unknownBaseGlyphs', [hex(glyph) for glyph in sorted(self.unknownBaseGlyphs)]
        print 'unknownDiacriticalGlyphs', sorted(self.unknownDiacriticalGlyphs)
        print 'unknownDiacriticalGlyphs', [hex(glyph) for glyph in sorted(self.unknownDiacriticalGlyphs)]

        print 'knownBaseGlyphs', sorted(self.knownBaseGlyphs)
        print 'knownDiacriticalGlyphs', sorted(self.knownDiacriticalGlyphs)

        print 'unknownCompoundGlyphs', sorted(self.unknownCompoundGlyphs)
        print 'knownCompoundGlyphs', sorted(self.knownCompoundGlyphs)

        print 'existingCompoundGlyphs', [hex(glyph) for glyph in sorted(self.existingCompoundGlyphs)]

        print
        print 'unknownBaseGlyphs', len(self.unknownBaseGlyphs)
        print 'unknownDiacriticalGlyphs', len(self.unknownDiacriticalGlyphs)
        print 'knownBaseGlyphs', len(self.knownBaseGlyphs)
        print 'knownDiacriticalGlyphs', len(self.knownDiacriticalGlyphs)

        print 'unknownCompoundGlyphs', len(self.unknownCompoundGlyphs)
        print 'knownCompoundGlyphs', len(self.knownCompoundGlyphs)
        print 'existingCompoundGlyphs', len(self.existingCompoundGlyphs)



if __name__ == "__main__":
    import sys
    print 'sys.argv', sys.argv

    settings = getCommandLineSettings()
    print 'settings', settings
    FontInterpolator(settings).process()

    print
    print 'complete.'
