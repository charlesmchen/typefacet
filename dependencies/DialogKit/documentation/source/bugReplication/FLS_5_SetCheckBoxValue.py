# environment: FontLab
# version: Studio 5.0+
# platform: Mac (untested in Windows)
# dialogKit object: CheckBox
# status: Reported to FontLab developers on December 17, 2005
# description: The callback assigned to a CheckBox is called when the value is set programmatically.
# cause: This is the result of a bug in the FontLab Dialog object.

from FL import *

class CheckBoxTest(object):
    
    def __init__(self):
        self.d = Dialog(self)
        self.d.size = Point(200, 130)
        self.checkbox1 = 0
        self.checkbox2 = 0
        self.d.AddControl(CHECKBOXCONTROL, Rect(10, 10, 190, 37), 'checkbox1', STYLE_CHECKBOX, 'checkbox1')
        self.d.AddControl(CHECKBOXCONTROL, Rect(10, 47, 190, 74), 'checkbox2', STYLE_CHECKBOX, 'checkbox2')
        self.d.Run()
    
    def on_checkbox1(self, code):
        self.d.GetValue('checkbox1')
        self.checkbox2 = self.checkbox1
        self.d.PutValue('checkbox2')
    
    def on_checkbox2(self, code):
        print 'checkbox2 hit!'

CheckBoxTest()