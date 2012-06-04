'''
robofont-extensions-and-scripts
TFFreetypeFont.py

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


import freetype
import freetype.ft_enums as ft_enums

from tfs.common.TFSPoint import TFSPoint
from tfs.common.TFSPath import TFSPath
from tfs.common.TFSSegment import TFSSegment
from tfs.common.TFSMap import TFSMap
from tfs.common.UnicodeCharacterNames import getUnicodeCharacterName


class TFFreetypeFont(object):

    def __init__(self, src_file, ttx_index=0):
        if src_file.lower().endswith('.otf'):
            self.isTrueType = False
            self.ftFont = freetype.Face(src_file)
        elif src_file.lower().endswith('.ttf'):
            self.isTrueType = True
            self.ftFont = freetype.Face(src_file)
        elif src_file.lower().endswith('.ttx'):
            self.isTrueType = True
            if self.ttx_index is None:
                raise Exception('.ttx missing --ttx-index.')
            self.ftFont = freetype.Face(src_file, index=ttx_index)
        else:
            raise Exception('Unrecognized file extension: %s' % self.src_file)

    postscriptName = property(lambda self: self.ftFont.postscript_name)
    familyName = property(lambda self: self.ftFont.family_name)
    styleName = property(lambda self: self.ftFont.style_name)

    ascender = property(lambda self: self.ftFont.ascender)
    descender = property(lambda self: self.ftFont.descender)
    unitsPerEm = property(lambda self: self.ftFont.units_per_EM)

    has_kerning = property(lambda self: self.ftFont.has_kerning)


#        ufoFont.info.xHeight = metadata.xHeight
#        ufoFont.info.capHeight = metadata.capHeight
#        ufoFont.info.versionMajor = metadata.versionMajor
#        ufoFont.info.versionMinor = metadata.versionMinor
#
#        ufoFont.info.italicAngle = metadata.italicAngle
#        #ufoFont.info.openTypeHeadFlags = metadata.openTypeHeadFlags
#        ufoFont.info.openTypeHheaAscender = ufoFont.info.ascender
#        ufoFont.info.openTypeHheaDescender = ufoFont.info.descender
#        ufoFont.info.openTypeHheaCaretSlopeRise = metadata.caretSlopeRise
#        ufoFont.info.openTypeHheaCaretSlopeRun = metadata.caretSlopeRun
#        ufoFont.info.openTypeHheaCaretOffset = 0
#
#        ufoFont.update()
#
#
#        ufoFont.info.styleMapFamilyName = ufoFont.info.familyName
#        ufoFont.info.styleMapStyleName = ufoFont.info.styleName

#        ufoFont.info.openTypeNamePreferredFamilyName = ufoFont.info.familyName
#        ufoFont.info.openTypeNamePreferredSubfamilyName = ufoFont.info.styleName
#        ufoFont.info.fullName = ufoFont.info.familyName + '-' + ufoFont.info.styleName
#        ufoFont.info.ufoFontName = ufoFont.info.fullName.replace(' ', '')
#        #ufoFont.info.postscriptUniqueID = ufoFont.info.ufoFontName
#        ufoFont.info.postscriptFontName = ufoFont.info.ufoFontName
#        ufoFont.info.postscriptFullName = ufoFont.info.fullName
#        #ufoFont.info.weightName = ufoFont.info.fullName
#        #ufoFont.info.postscriptFullName = ufoFont.info.fullName
#        # TODO: remove
#        ufoFont.info.menuName = ufoFont.info.fullName
#        # TODO: remove
#        ufoFont.info.fondName = ufoFont.info.familyName
#        ufoFont.info.macintoshFONDName = ufoFont.info.familyName
#
#        ufoFont.info.otFamilyName = ufoFont.info.familyName
#        ufoFont.info.otStyleName = ufoFont.info.styleName
#        ufoFont.info.otMacName = ufoFont.info.fullName
#        ufoFont.info.openTypeNameCompatibleFullName = ufoFont.info.fullName
#
#        ufoFont.info.designer = metadata.designer
#        ufoFont.info.openTypeNameDesigner = metadata.designer
#        ufoFont.info.createdBy = metadata.designer
#        ufoFont.info.year = metadata.year
#        # TODO: openTypeNameLicense
#        # TODO: openTypeNameLicenseURL
#
#        ufoFont.update()
#        ufoFont.autoUnicodes()
#        ufoFont.update()
#        ufoFont.save(dstFile)
#
#        ufoFont.close()


    def getGlyphContours(self, glyphIndex):

        IRRELEVANT_CHAR_SIZE = 48*64
        self.ftFont.set_char_size( IRRELEVANT_CHAR_SIZE )

        FT_LOAD_NO_SCALE = ( 1 << 0 )
        self.ftFont.load_glyph(glyphIndex, FT_LOAD_NO_SCALE)

        ftGlyph = self.ftFont.glyph

        outline = ftGlyph.outline

#        print 'outline.points', outline.points
        def convertPoint(x, y):
            return TFSPoint(float(x),
                            float(y))
        points = [convertPoint(*point) for point in outline.points]
#        print 'points', points
#        x = [point.x for point in points]
#        y = [point.y for point in points]

        start, end = 0, 0
#
        paths = []
        for i in range(len(outline.contours)):
            end    = outline.contours[i]
            points = outline.points[start:end+1]
            points.append(points[0])
            tags   = outline.tags[start:end+1]
            tags.append(tags[0])

#            print 'points', points
#            print 'tags', tags

            segments = [ [points[0],], ]
            for j in range(1, len(points) ):
                segments[-1].append(points[j])
                if tags[j] & (1 << 0) and j < (len(points)-1):
                    segments.append( [points[j],] )

#            print 'contour'
#            for segment in segments:
#                print 'segment', segment

            def convertPoint(x, y):
                return TFSPoint(float(x),
                                float(y))

            def addSegment(points, segments):
                '''
                Ignore empty segments
                '''
                if 2 == len(points):
                    if points[0] == points[-1]:
                        return
                elif len(points) == 3:
                    if points[0] == points[1] == points[2]:
                        return
                elif len(points) == 4:
                    if points[0] == points[1] == points[2] == points[3]:
                        return
                else:
                    raise Exception('Invalid segment!')
                segment = TFSSegment(*points)
#                print 'segment', segment.description()
                segments.append(segment)


            def parseSegments(points):
                points = [convertPoint(*point) for point in points]
                if 2 <= len(points) <= 3:
                    result = []
                    addSegment(points, result)
                    return result
                endpoint0 = points[0]
                remainder = points[1:]
                result = []
                while True:
                    if len(remainder) == 2:
                        controlPoint, endpoint1 = remainder
                        addSegment((endpoint0, controlPoint, endpoint1), result)
                        break
                    else:
                        controlPoint = remainder[0]
                        nextControlPoint = remainder[1]
                        endpoint1 = controlPoint.midpoint(nextControlPoint)
                        addSegment((endpoint0, controlPoint, endpoint1), result)
                        endpoint0 = endpoint1
                        remainder.pop(0)
                return result

            tfsSegments = []
            for segment in segments:
                tfsSegments += parseSegments(segment)
#            tfsSegments = [TFSSegment(*[convertPoint(*point) for point in segment]) for segment in segments]
            if len(tfsSegments) > 0:
                '''
                Why are there so many empty contours?
                '''
                if tfsSegments[-1].endPoint() != tfsSegments[0].startPoint():
                    tfsSegments.append(TFSSegment(tfsSegments[-1].endPoint(),
                                                  tfsSegments[0].startPoint()))
                paths.append(TFSPath(True, *tfsSegments))

            start = end+1

#        debugPaths('paths', paths)
#        raise Exception('...')

        return paths, ftGlyph.advance.x


    def getKerning(self, glyphIndex0, glyphIndex1):

        kerning = freetype.FT_Vector(0,0)
        error = freetype.FT_Get_Kerning( self.ftFont._FT_Face,
                                         glyphIndex0, glyphIndex1,
                                         ft_enums.FT_KERNING_UNSCALED,
                                         freetype.byref(kerning) )
        if error: raise freetype.FT_Exception( error )
        return kerning.x


    def getGlyphIndices(self):
        return [glyphIndex for glyphIndex in xrange(self.ftFont.num_glyphs)]


    def getGlyphIndexToCharacterMap(self):
        glyphIndexToCharacterMap = {}
#        self.ftFont.select_charmap(ft_enums.FT_ENCODING_UNICODE)
        characterCode, glyphIndex = self.ftFont.get_first_char();
        while glyphIndex > 0:
            glyphIndexToCharacterMap[glyphIndex] = characterCode
            characterCode, glyphIndex = self.ftFont.get_next_char(characterCode, 0)
        return glyphIndexToCharacterMap


    def getCharacterToGlyphIndexMap(self):
        result = {}
        for glyphIndex, characterCode in self.getGlyphIndexToCharacterMap().items():
            result[characterCode] = glyphIndex
        return result


    def getGlyphInfos(self):
        result = []
#        glyphIndexToNameMap = {}
        glyphToCharacterMap = self.getGlyphIndexToCharacterMap()
        if self.ftFont.has_glyph_names:
            for glyphIndex in self.getGlyphIndices():
                glyphNameBuffer = ' '*256
                error = freetype.FT_Get_Glyph_Name(self.ftFont._FT_Face,
                                                   glyphIndex,
                                                   glyphNameBuffer,
                                                   len(glyphNameBuffer) - 1)
                if error:
                    raise freetype.FT_Exception(error)

                glyphInfo = TFSMap()
                glyphInfo.glyphIndex = glyphIndex
                glyphInfo.glyphName = glyphNameBuffer.strip()[:-1]
#                print 'glyphName', glyphIndex, glyphName, len(glyphName)
                glyphInfo.characterCode = None
                if glyphIndex in glyphToCharacterMap:
                    glyphInfo.characterCode = glyphToCharacterMap[glyphIndex]
                result.append(glyphInfo)

        else:
            for glyphIndex, characterCode in glyphToCharacterMap.items():
                glyphInfo = TFSMap()
                glyphInfo.glyphIndex = glyphIndex
                glyphInfo.glyphName = getUnicodeCharacterName(characterCode)
                glyphInfo.characterCode = characterCode
#                glyphInfoMap[glyphIndex] = glyphInfo
                result.append(glyphInfo)

        return result
