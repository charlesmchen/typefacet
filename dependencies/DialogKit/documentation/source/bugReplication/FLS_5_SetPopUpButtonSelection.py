# environment: FontLab
# version: Studio 5.0+
# platform: Mac (untested in Windows)
# dialogKit object: PopUpButton
# status: Reported to FontLab developers on December 17, 2005
# description: setSelection does not select anything in the list.
# cause: This is the result of a bug in the FontLab Dialog object.

from FL import *

class ChoiceHitTest(object):
    
    def __init__(self):
        self.d = Dialog(self)
        self.d.size = Point(200, 130)
        self.choices1 = ['select something', 'a', 'b', 'c']
        self.choices1_index = 0
        self.choices2 = ['w', 'x', 'y', 'z']
        self.choices2_index = 0
        self.d.AddControl(CHOICECONTROL, Rect(10, 10, 190, 37), 'choices1', STYLE_CHOICE)
        self.d.AddControl(CHOICECONTROL, Rect(10, 47, 190, 74), 'choices2', STYLE_CHOICE)
        self.d.Run()
    
    def on_choices1(self, code):
        self.d.GetValue('choices1')
        self.choices2_index = self.choices1_index
        self.d.PutValue('choices2')
    
    def on_choices2(self, code):
        print 'choices 2 hit!'

ChoiceHitTest()
