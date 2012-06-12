# environment: FontLab
# version: Studio 5.0+
# platform: Mac (untested in Windows)
# dialogKit object: List
# status: Reported to FontLab developers on December 17, 2005
# description: The callback assigned to a List is called twice.
# cause: This is the result of a bug in the FontLab Dialog object.

from FL import *

class ListHitTest(object):
    
    def __init__(self):
        self.d = Dialog(self)
        self.d.size = Point(200, 300)
        self.list = ['a', 'b', 'c']
        self.d.AddControl(LISTCONTROL, Rect(10, 10, 180, 240), 'list', STYLE_LIST)
        self.d.Run()
    
    def on_list(self, code):
        print 'list hit!'

ListHitTest()