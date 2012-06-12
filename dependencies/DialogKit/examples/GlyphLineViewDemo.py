import os
from FL import *
from dialogKit import *

def _allFonts():
    return [fl[i] for i in xrange(len(fl))]

class GlyphLineViewDemo(object):
    
    def __init__(self):
        self.allFonts = [(os.path.basename(font.file_name), font) for font in _allFonts()]
        self.allFontNames = [name for name, font in self.allFonts]
        self.w = ModalDialog((500, 230), 'GlyphLineView Demo')
        #
        self.w.textEntry = EditText((10, 10, 480, 27), 'HELLO!', callback=self.textEntryCallback)
        #
        self.w.glyphLineView = GlyphLineView((10, 50, 480, 120))
        #
        self.w.fontOption = PopUpButton((10, -37, 150, 22), items=self.allFontNames, callback=self.fontOptionCallback)
        #
        self.w.open()
    
    def textEntryCallback(self, sender):
        text = sender.get()
        self.w.glyphLineView.set(text)
    
    def fontOptionCallback(self, sender):
        index = sender.getSelection()
        font = self.allFonts[index][1]
        self.w.glyphLineView.setFont(font)

GlyphLineViewDemo()
