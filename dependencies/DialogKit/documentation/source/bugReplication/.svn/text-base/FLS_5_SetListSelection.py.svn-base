# environment: FontLab
# version: Studio 5.0+
# platform: Mac (untested in Windows)
# dialogKit object: List
# status: Reported to FontLab developers on December 17, 2005
# description: setSelection does not select anything in the list.
# cause: This is the result of a bug in the FontLab Dialog object.

class SetIndexTest(object):
    
    def __init__(self):
        self.d = Dialog(self)
        self.d.size = Point(200, 300)
        self.list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.list_index = 0
        self.indexOptions = range(len(self.list))
        self.indexOptions_index = 0
        self.d.AddControl(LISTCONTROL, Rect(10, 10, 180, 210), 'list', STYLE_LIST)
        self.d.AddControl(CHOICECONTROL, Rect(10, 220, 180, 247), 'indexOptions', STYLE_CHOICE)
        self.d.Run()
    
    def on_indexOptions(self, code):
        self.d.GetValue('indexOptions')
        index = self.indexOptions_index
        if index in self.indexOptions:
            self.list_index = index
            self.d.PutValue('list')
            print 'attempted to set index:', index

SetIndexTest()