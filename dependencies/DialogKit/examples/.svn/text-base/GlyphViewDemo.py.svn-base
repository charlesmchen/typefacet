from FL import *
from dialogKit import *

class GlyphViewDemo(object):
    
    def __init__(self):
        self.font= fl.font
        self.glyphs = {}
        for glyph in self.font.glyphs:
            self.glyphs[glyph.name] = glyph
        glyphNames = self.glyphs.keys()
        glyphNames.sort()
        #
        self.w = ModalDialog((700, 500), 'GlyphView Demo')
        self.w.glyphList = List((10, 10, 150, -60), glyphNames, callback=self.glyphListCallback)
        self.w.view = GlyphView((170, 10, 400, -60), None, None)
        #
        self.w.fillCheckBox = CheckBox((580, 10, -10, 20), 'Fill', value=True, callback=self.viewOptionsCallback)
        self.w.outlineCheckBox = CheckBox((580, 35, -10, 20), 'Outline', value=False, callback=self.viewOptionsCallback)
        self.w.pointsCheckBox = CheckBox((580, 60, -10, 20), 'Points', value=True, callback=self.viewOptionsCallback)
        self.w.descenderCheckBox = CheckBox((580, 85, -10, 20), 'Descender', value=True, callback=self.viewOptionsCallback)
        self.w.baselineCheckBox = CheckBox((580, 110, -10, 20), 'Baseline', value=True, callback=self.viewOptionsCallback)
        self.w.xHeightCheckBox = CheckBox((580, 135, -10, 20), 'X Height', value=True, callback=self.viewOptionsCallback)
        self.w.ascenderCheckBox = CheckBox((580, 160, -10, 20), 'Ascender', value=True, callback=self.viewOptionsCallback)
        self.w.capHeightCheckBox = CheckBox((580, 185, -10, 20), 'Cap Height', value=True, callback=self.viewOptionsCallback)
        self.w.upmTopCheckBox = CheckBox((580, 210, -10, 20), 'UPM Top', value=False, callback=self.viewOptionsCallback)
        self.w.leftCheckBox = CheckBox((580, 235, -10, 20), 'Left', value=True, callback=self.viewOptionsCallback)
        self.w.rightCheckBox = CheckBox((580, 260, -10, 20), 'Right', value=True, callback=self.viewOptionsCallback)
        #
        self.w.open()
    
    def glyphListCallback(self, sender):
        selection = sender.getSelection()
        if not selection:
            font = glyph = None
        else:
            glyphName = sender[selection[0]]
            glyph = self.glyphs[glyphName]
            font = self.font
        self.w.view.set(font, glyph)
        self.w.view.update()
    
    def viewOptionsCallback(self, sender):
        if self.w.fillCheckBox.get() != self.w.view.getShowFill():
            self.w.view.setShowFill(self.w.fillCheckBox.get())
        if self.w.outlineCheckBox.get() != self.w.view.getShowOutline():
            self.w.view.setShowOutline(self.w.outlineCheckBox.get())
        if self.w.pointsCheckBox.get() != self.w.view.getShowOnCurvePoints():
            self.w.view.setShowOnCurvePoints(self.w.pointsCheckBox.get())
        if self.w.descenderCheckBox.get() != self.w.view.getShowDescender():
            self.w.view.setShowDescender(self.w.descenderCheckBox.get())
        if self.w.baselineCheckBox.get() != self.w.view.getShowBaseline():
            self.w.view.setShowBaseline(self.w.baselineCheckBox.get())
        if self.w.xHeightCheckBox.get() != self.w.view.getShowXHeight():
            self.w.view.setShowXHeight(self.w.xHeightCheckBox.get())
        if self.w.ascenderCheckBox.get() != self.w.view.getShowAscender():
            self.w.view.setShowAscender(self.w.ascenderCheckBox.get())
        if self.w.capHeightCheckBox.get() != self.w.view.getShowCapHeight():
            self.w.view.setShowCapHeight(self.w.capHeightCheckBox.get())
        if self.w.upmTopCheckBox.get() != self.w.view.getShowUPMTop():
            self.w.view.setShowUPMTop(self.w.upmTopCheckBox.get())
        if self.w.leftCheckBox.get() != self.w.view.getShowLeftSidebearing():
            self.w.view.setShowLeftSidebearing(self.w.leftCheckBox.get())
        if self.w.rightCheckBox.get() != self.w.view.getShowRightSidebearing():
            self.w.view.setShowRightSidebearing(self.w.rightCheckBox.get())
        self.w.view.update()

GlyphViewDemo()