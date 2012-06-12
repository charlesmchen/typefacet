# environment: FontLab
# version: Studio 5.0+
# platform: Mac (untested in Windows)
# dialogKit object: EditText
# status: Reported to FontLab developers on December 17, 2005
# description: Long strings of text are not wrapping.
# cause: This is the result of a bug in the FontLab Dialog object.

from FL import *

class TextWrapTest(object):
    
    def __init__(self):
        self.d = Dialog(self)
        self.d.size = Point(400, 400)
        self.text = 'foo ' * 500
        self.d.AddControl(EDITCONTROL, Rect(10, 10, 390, 340), 'text', STYLE_CHOICE, self.text)
        self.d.Run()

TextWrapTest()