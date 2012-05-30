'''
robofont-extensions-and-scripts
TFSFont.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''


import os
import robofab.world
from TFSGlyph import TFSGlyph


class TFSFont(object):

    def __init__(self, rffont):
        self.rffont = rffont

    def glyphNames(self):
        return self.rffont.keys()

    def glyphCodePoints(self):
        result = [glyph.unicode for glyph in self.rffont]
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

    def insertGlyphDerivedFromGlyph(self, codePoint, contours, srcGlyph):
        import UnicodeCharacterNames
        name = UnicodeCharacterNames.getUnicodeCharacterName(codePoint)
        glyph = TFSGlyph(self.rffont.newGlyph(name))
        glyph.updateDerivedFromGlyph(codePoint, contours, srcGlyph)













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
