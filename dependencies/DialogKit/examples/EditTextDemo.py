from dialogKit import *

class EditTextTest(object):
    
    def __init__(self):
        self.w = ModalDialog((200, 95), 'EditText Demo', okCallback=self.okCallback)
        self.w.editText = EditText((10, 10, 180, 27), 'Hello', callback=self.editTextCallback)
        self.w.open()
    
    def editTextCallback(self, sender):
        print 'text entry:', sender.get()
    
    def okCallback(self, sender):
        print 'finished:', self.w.editText.get()

EditTextTest()