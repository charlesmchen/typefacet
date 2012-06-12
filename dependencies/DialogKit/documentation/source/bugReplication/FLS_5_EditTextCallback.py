# environment: FontLab
# version: Studio 5.0+
# platform: Mac (untested in Windows)
# dialogKit object: EditText
# status: Reported to FontLab developers on December 17, 2005
# description: The callback assigned to an EditText is called when the value is set prgrammatically.
# cause: This is the result of a bug in the FontLab Dialog object.

class EditTextHitTest(object):
    
    def __init__(self):
        self.d = Dialog(self)
        self.d.size = Point(200, 130)
        self.text1 = 'text 1'
        self.text2 = 'text 2'
        self.d.AddControl(EDITCONTROL, Rect(10, 10, 190, 37), 'text1', STYLE_EDIT)
        self.d.AddControl(EDITCONTROL, Rect(10, 47, 190, 74), 'text2', STYLE_EDIT)
        self.d.Run()
    
    def on_text1(self, code):
        self.d.GetValue('text1')
        self.text2 = self.text1
        self.d.PutValue('text2')
    
    def on_text2(self, code):
        print 'text 2 hit!'

EditTextHitTest()