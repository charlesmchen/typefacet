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

from tfs.common.TFSFont import *
from tfs.common.TFSSvg import *
from AutokernSettings import getCommandLineSettings
from tfs.common.TFSSilhouette import *

from tfs.common.TFSMap import TFSMap
import tfs.common.TFSMath as TFSMath


TFSMath.setFloatRoundingTolerance(0.1)
TFSMath.setDefaultPrecisionDigits(1)


class TFSKerning(TFSMap):

    def __init__(self):
        TFSMap.__init__(self)


def subrenderGlyphContours(tfsSvg, contours, strokeColor):
    ON_POINT_COLOR = 0x7f7f7f7f
    CONTROL_POINT_COLOR = 0x7fafafaf
    for contour in contours:
        tfsSvg.addItem(TFSSvgPath(contour).addStroke(strokeColor, 2).addPointHighlights(ON_POINT_COLOR, CONTROL_POINT_COLOR))


def renderSvgScene(kerning,
                   filenamePrefix, phase, phaseName,
                   pathTuples,
                   hGuidelines=None):
    filename = '%s-phase-%d-%s.svg' % ( filenamePrefix,
                                        phase,
                                        phaseName, )
    dstFile = os.path.abspath(os.path.join(kerning.svg_folder, filename))

    CANVAS_BACKGROUND_COLOR = 0xffffffff
    CANVAS_BORDER_COLOR = 0x07fbfbfbf
    tfsSvg = TFSSvg().withBackground(CANVAS_BACKGROUND_COLOR).withBorder(CANVAS_BORDER_COLOR)

#    if pathTuples:
    for color, contours in pathTuples:
        subrenderGlyphContours(tfsSvg, contours, color)

    if hGuidelines:
        for hGuideline in hGuidelines:
            p0 = TFSPoint(hGuideline, kerning.pafont.info.descender)
            p1 = TFSPoint(hGuideline, kerning.pafont.info.ascender)
            GUIDELINE_COLOR = 0x7fdfdfdf
            tfsSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

    vGuidelines = ( 0,
                    kerning.pafont.info.ascender,
                    kerning.pafont.info.descender,
                    )
    if vGuidelines:
        minmax = None
        for color, contours in pathTuples:
            minmax = minmaxMerge(minmax, minmaxPaths(contours))

        for vGuideline in vGuidelines:
            p0 = TFSPoint(0, vGuideline)
            p1 = TFSPoint(minmax.maxX, vGuideline)
            GUIDELINE_COLOR = 0x7fdfdfdf
            tfsSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

    SVG_HEIGHT = 400
    SVG_MAX_WIDTH = 800
    tfsSvg.renderToFile(dstFile, margin=10, height=SVG_HEIGHT, maxWidth=SVG_MAX_WIDTH)
    return filename


def processKerningPair(kerning, paglyph0, paglyph1):

    renderLog = kerning.log_dst is not None

    contours0 = paglyph0.getContours()
    contours1 = paglyph1.getContours()
    minmax0 = minmaxPaths(contours0)
    minmax1 = minmaxPaths(contours1)
    naiveSpacing = minmax0.maxX - minmax1.minX

    minSpacing = 0


#    import time
#    time0 = time.time()
    debugPaths('contours1', contours1)
    contours1_plusMin = inflatePaths(contours1, kerning.min_distance)
    debugPaths('contours1_plusMin', contours1_plusMin)

#    time1 = time.time()
#    print 'inflatePathsLeft', time1 - time0
#    time0 = time1
    SILHOUETTE_RESOLUTION = 2.0
    minDistanceSpacing = findSilhouetteContactSpacing(contours0, contours1_plusMin, SILHOUETTE_RESOLUTION)
#    time1 = time.time()
#    print 'findSilhouetteContactSpacing', time1 - time0
#    time0 = time1
##    minSpacing = kerning.min_distance + findSilhouetteContactSpacing(contours0, contours1_plusMin, SILHOUETTE_RESOLUTION)

    contours0_midRounding = deflatePaths(contours1, kerning.rounding)
    debugPaths('contours0_midRounding', contours0_midRounding)
    contours0_afterRounding = inflatePaths(contours0_midRounding, kerning.rounding)
    debugPaths('contours0_afterRounding', contours0_afterRounding)
    roundingSpacing = findSilhouetteContactSpacing(contours0_afterRounding, contours1_plusMin, SILHOUETTE_RESOLUTION)
#
#    contours1_plusMin = inflatePathsLeft(contours1, kerning.min_distance)
#    contours = FSilhouette.deflatePaths(contours, capHeight * 0.05)
#    time1 = time.time()
#    print ''

    print 'minDistanceSpacing', minDistanceSpacing
    debugPaths('contours0', contours0)
    debugPaths('contours1_plusMin', contours1_plusMin)

    if renderLog:
        filenamePrefix = 'tfs-%s-%s' % ( chr(paglyph0.unicode),
                                         chr(paglyph1.unicode), )
        phase = 1

#        for contour in contours1:
#            print 'contour', type(contour), contour.description()

        naiveSpacingSvg = renderSvgScene(kerning,
                                         filenamePrefix, phase, 'naive-spacing',
                                         pathTuples = (
                                                       ( 0x7f7faf7f, contours0, ),
                                                       ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(naiveSpacing, 0)) for contour in contours1], ),
                                                       ),
                                         hGuidelines = ( naiveSpacing, ) )
        phase += 1
        minDistanceSpacingSvg = renderSvgScene(kerning,
                                         filenamePrefix, phase, 'min-spacing',
                                         pathTuples = (
                                                       ( 0x7f7faf7f, contours0, ),
                                                       ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(minDistanceSpacing, 0)) for contour in contours1], ),
                                                       ( 0x7fafafff, [contour.applyPlus(TFSPoint(minDistanceSpacing, 0)) for contour in contours1_plusMin], ),
                                                       ),
                                         hGuidelines = ( naiveSpacing, ) )
        phase += 1
        roundingSpacingSvg = renderSvgScene(kerning,
                                         filenamePrefix, phase, 'rounding',
                                         pathTuples = (
                                                       ( 0x7f7faf7f, contours0, ),
                                                       ( 0x7fafffaf, contours0_midRounding, ),
                                                       ( 0x7fafffaf, contours0_afterRounding, ),
                                                       ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(roundingSpacing, 0)) for contour in contours1], ),
                                                       ( 0x7fafafff, [contour.applyPlus(TFSPoint(roundingSpacing, 0)) for contour in contours1_plusMin], ),
                                                       ),
                                         hGuidelines = ( naiveSpacing, ) )
        phase += 1

        import tfs.common.TFSProject as TFSProject
        mustache_template_file = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'log_kerning_pair_html_mustache.txt'))
        with open(mustache_template_file, 'rt') as f:
            mustache_template = f.read()

        def formatGlyphName(glyph):
            return u'%s (%s)' % ( unichr(glyph),
                                  hex(glyph), )

        pageTitle = u'pyautokern Log: Kerning %s vs. %s' % ( formatGlyphName(paglyph0.unicode),
                                                             formatGlyphName(paglyph1.unicode), )

        def formatEmScalar(value):
            return '%0.3f em' % (value / float(kerning.units_per_em))

        def formatGlyphMap(glyph, glyphMinmax):
            return {
                       'glyphName': formatGlyphName(glyph),
                       'minX': formatEmScalar(glyphMinmax.minX),
                       'maxX': formatEmScalar(glyphMinmax.maxX),
                       'minY': formatEmScalar(glyphMinmax.minY),
                       'maxY': formatEmScalar(glyphMinmax.maxY),
                    }

        mustacheMap = {
                       'pageTitle': pageTitle,
                       'minmax0': minmax0,
                       'minmax1': minmax1,
                       'naiveSpacing': formatEmScalar(naiveSpacing),
                       'minDistanceSpacing': formatEmScalar(minDistanceSpacing),
                       'roundingSpacing': formatEmScalar(roundingSpacing),
                       'min_distance': formatEmScalar(kerning.min_distance),
                       'max_distance': formatEmScalar(kerning.max_distance),
                       'rounding': formatEmScalar(kerning.rounding),

                       'naiveSpacingSvg': naiveSpacingSvg,
                       'minSpacingSvg': minDistanceSpacingSvg,
                       'roundingSpacingSvg': roundingSpacingSvg,

                       'glyph0': formatGlyphName(paglyph0.unicode),
                       'glyph1': formatGlyphName(paglyph1.unicode),

                       'glyphMaps': ( formatGlyphMap(paglyph0.unicode, minmax0),
                                      formatGlyphMap(paglyph1.unicode, minmax1),
                                      )
                       }

        for key in ( 'ascender',
                     'descender',
                    ):
            mustacheMap[key] = formatEmScalar(getattr(kerning.pafont.info, key))

        for key in (
                     'unitsPerEm',
                     'familyName',
                     'styleName',
                     'fullName',
                     'fontName',
                    ):
            mustacheMap[key] = getattr(kerning.pafont.info, key)

        import pystache
        logHtml = pystache.render(mustache_template, mustacheMap)

        logFilename = '%s.html' % ( filenamePrefix, )
        logFile = os.path.abspath(os.path.join(kerning.html_folder, logFilename))
        with open(logFile, 'wt') as f:
            # TODO: explicitly encode unicode
            f.write(logHtml)


def processAllKerningPairs(kerning):
    for paglyph0 in kerning.pafont.getGlyphs():
        for paglyph1 in kerning.pafont.getGlyphs():
            processKerningPair(kerning, paglyph0, paglyph1)
            return


def configureKerning(kerning, settings):

    ufo_src = settings.ufo_src
    if ufo_src is None:
        raise Exception('Missing ufo_src')
    if not (os.path.exists(ufo_src) and os.path.isdir(ufo_src) and os.path.basename(ufo_src).lower().endswith('.ufo')):
        raise Exception('Invalid ufo_src: %s' % ufo_src)
    kerning.ufo_src = ufo_src

#    testFont = os.path.abspath(os.path.join('..', '..', 'data', 'TFSTest Plain.ufo'))
    kerning.pafont = TFSFontFromFile(ufo_src)

    log_dst = settings.log_dst
    if log_dst is None:
        kerning.log_dst = None
#        raise Exception('Missing log_dst')
        pass
    else:
        if os.path.exists(log_dst):
            shutil.rmtree(log_dst)
        os.mkdir(log_dst)
        if not (os.path.exists(log_dst) and os.path.isdir(log_dst)):
            raise Exception('Invalid log_dst: %s' % log_dst)
        kerning.log_dst = log_dst

        def makeLogSubfolder(parent, name):
            subfolder = os.path.abspath(os.path.join(parent, name))
            os.mkdir(subfolder)
            if not (os.path.exists(subfolder) and os.path.isdir(subfolder)):
                raise Exception('Invalid log_dst: %s' % log_dst)
            return subfolder

        kerning.html_folder = makeLogSubfolder(log_dst, 'html')
        kerning.css_folder = makeLogSubfolder(kerning.html_folder, 'stylesheets')
        kerning.svg_folder = makeLogSubfolder(kerning.html_folder, 'svg')

        import tfs.common.TFSProject as TFSProject
        srcCssFile = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'styles.css'))
        dstCssFile = os.path.abspath(os.path.join(kerning.css_folder, os.path.basename(srcCssFile)))
        shutil.copy(srcCssFile, dstCssFile)

    kerning.units_per_em = float(kerning.pafont.units_per_em)
    kerning.min_distance = settings.min_distance_ems * kerning.pafont.units_per_em
    kerning.max_distance = settings.max_distance_ems * kerning.pafont.units_per_em
    kerning.rounding = settings.rounding_ems * kerning.pafont.units_per_em
    print 'kerning.units_per_em', kerning.units_per_em
    print 'kerning.min_distance', kerning.min_distance
    print 'kerning.max_distance', kerning.max_distance
    print 'kerning.rounding', kerning.rounding
#    kerning.fontMetadata = kerning.pafont.info


def processKerning(settings = None):
    if settings is None:
        settings = getCommandLineSettings()

    kerning = TFSKerning()

    configureKerning(kerning, settings)

    processAllKerningPairs(kerning)


if __name__ == "__main__":
    settings = getCommandLineSettings()
    processKerning(settings)

    print
    print 'complete.'
