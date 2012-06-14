'''
robofont-extensions-and-scripts
TFSFont.py

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
import robofab.world
from TFSGlyph import TFSGlyph


class TFSFont(object):

    def __init__(self, rffont):
        self.rffont = rffont

    ascender = property(lambda self: self.rffont.info.ascender)
    descender = property(lambda self: self.rffont.info.descender)

    def clearKerning(self):
        self.rffont.kerning.clear()

    def update(self):
        self.rffont.update()

    def save(self, filepath):
        self.rffont.save(filepath)

    def close(self):
        self.rffont.close()

    def glyphNames(self):
        return self.rffont.keys()

    def glyphCodePoints(self):
        result = [glyph.unicode for glyph in self.rffont if glyph.unicode is not None]
        return result

    def getGlyphByName(self, key):
        rfglyph = self.rffont.getGlyph(key)
        return TFSGlyph(rfglyph)

    def getGlyphByCodePoint(self, value):
        for glyph in self.rffont:
            if glyph.unicode == value:
                return TFSGlyph(glyph)
        return None
#        raise Exception('Unknown code point: ' + str(value))
#        return None

    def getGlyphs(self):
        return [TFSGlyph(glyph) for glyph in self.rffont]

    units_per_em = property(lambda self: self.rffont.info.unitsPerEm)
    info = property(lambda self: self.rffont.info)
#    ascender = property(lambda self: self.rffont.info.ascender)
#    descender = property(lambda self: self.rffont.info.descender)
#    xHeight = property(lambda self: self.rffont.info.xHeight)
#    capHeight = property(lambda self: self.rffont.info.capHeight)
#    versionMajor = property(lambda self: self.rffont.info.versionMajor)
#    versionMinor = property(lambda self: self.rffont.info.versionMinor)

    def writeToFile(self, dstFile):
        self.rffont.update()
        self.rffont.autoUnicodes()
        self.rffont.update()
        self.rffont.save(dstFile)
#        font.close()

    def getGlyphName(self, codePoint):
#        if codePoint is None:
#            return  '.notdef'

        import UnicodeCharacterNames
        name = UnicodeCharacterNames.getUnicodeCharacterName(codePoint)
        return name

    def insertGlyph(self, codePoint, contours, xAdvance,
                    glyphName=None, correctDirection=True):
        if glyphName is None:
            glyphName = self.getGlyphName(codePoint)
        glyph = TFSGlyph(self.rffont.newGlyph(glyphName))
        if codePoint is not None:
            glyph.setUnicode(codePoint)
        glyph.setContours(contours, correctDirection=correctDirection)
        glyph.setXAdvance(xAdvance)
        glyph.update()
#        glyph.correctDirection()
        return glyph


    def insertGlyphDerivedFromGlyph(self, codePoint, contours, srcGlyph):
        self.insertGlyph(codePoint, contours, srcGlyph.rfglyph.width)

    def setKerningPair(self, glyphName0, glyphName1, value):
        self.rffont.kerning[(glyphName0, glyphName1, )] = value

    def getKerningPair(self, glyphName0, glyphName1):
        '''
        returns None if pair does not exist.
        '''
        return self.rffont.kerning[(glyphName0, glyphName1, )]

    def getKerningPairCount(self):
        return len(self.rffont.kerning)


#font.info.ascender = formatOpentypeScalar(metadata.ascender)
#font.info.descender = formatOpentypeScalar(metadata.descender)
#font.info.unitsPerEm = formatOpentypeScalar(metadata.unitsPerEm)
#font.info.xHeight = formatOpentypeScalar(metadata.xHeight)
#font.info.capHeight = formatOpentypeScalar(metadata.capHeight)
#font.info.versionMajor = metadata.versionMajor
#font.info.versionMinor = metadata.versionMinor
#
#font.info.italicAngle = metadata.italicAngle
##font.info.openTypeHeadFlags = metadata.openTypeHeadFlags
#font.info.openTypeHheaAscender = font.info.ascender
#font.info.openTypeHheaDescender = font.info.descender
#font.info.openTypeHheaCaretSlopeRise = formatOpentypeScalar(metadata.caretSlopeRise)
#font.info.openTypeHheaCaretSlopeRun = formatOpentypeScalar(metadata.caretSlopeRun)
#font.info.openTypeHheaCaretOffset = 0
#
#font.update()
#
#
#font.info.styleMapFamilyName = font.info.familyName
#font.info.openTypeNamePreferredFamilyName = font.info.familyName
#font.info.openTypeNamePreferredSubfamilyName = font.info.styleName
#font.info.fullName = font.info.familyName + '-' + font.info.styleName
#font.info.fontName = font.info.fullName.replace(' ', '')
##font.info.postscriptUniqueID = font.info.fontName
#font.info.postscriptFontName = font.info.fontName
#font.info.postscriptFullName = font.info.fullName
##font.info.weightName = font.info.fullName
##font.info.postscriptFullName = font.info.fullName
## TODO: remove
#font.info.menuName = font.info.fullName
## TODO: remove
#font.info.fondName = font.info.familyName
#font.info.macintoshFONDName = font.info.familyName
#
#font.info.otFamilyName = font.info.familyName
#font.info.otStyleName = font.info.styleName
#font.info.otMacName = font.info.fullName
#font.info.openTypeNameCompatibleFullName = font.info.fullName
#
#font.info.designer = metadata.designer
#font.info.openTypeNameDesigner = metadata.designer
#font.info.createdBy = metadata.designer
#font.info.year = metadata.year

def TFSFontFromFile(filepath):
#    filepath = os.path.abspath(filepath)
    if not (os.path.exists(filepath) and
            os.path.isdir(filepath) and
            os.path.basename(filepath).lower().endswith('.ufo')):
        raise Exception('Invalid .ufo file: ' + filepath)

#    print 'filepath', filepath
    rffont = robofab.world.OpenFont(filepath)
    return TFSFont(rffont)
