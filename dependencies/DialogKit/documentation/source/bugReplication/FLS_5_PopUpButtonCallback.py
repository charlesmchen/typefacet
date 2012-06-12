# environment: FontLab
# version: Studio 5.0+
# platform: Mac (untested in Windows)
# dialogKit object: PopUpButton
# status: Reported to FontLab developers on December 17, 2005
# description: The callback assigned to a PopUpButton is called when the value is set prgrammatically.
# cause: This is the result of a bug in the FontLab Dialog object.

from FL import *

class ChoiceHitTest(object):
    
    def __init__(self):
        self.d = Dialog(self)
        self.d.size = Point(200, 100)
        self.options = ['a', 'b', 'c']
        self.options_index = 0
        self.d.AddControl(CHOICECONTROL, Rect(10, 10, 180, 57), 'options', STYLE_CHOICE)
        self.d.Run()
    
    def on_options(self, code):
        self.d.GetValue('options')
        index = self.options_index
        print 'selected:', self.options[index]

ChoiceHitTest()