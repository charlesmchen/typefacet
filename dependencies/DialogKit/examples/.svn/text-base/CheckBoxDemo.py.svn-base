from dialogKit import *

class CheckBoxDemo(object):
    
    def __init__(self):
        self.w = ModalDialog((200, 120), 'CheckBox Demo')
        self.w.checkBox1 = CheckBox((10, 10, 180, 20), 'CheckBox 1', callback=self.checkBox1Callback, value=True)
        self.w.checkBox2 = CheckBox((10, 40, 180, 20), 'CheckBox 2', callback=self.checkBox2Callback)
        self.w.open()
    
    def checkBox1Callback(self, sender):
        print 'CheckBox 1:', sender.get()
    
    def checkBox2Callback(self, sender):
        print 'CheckBox 2:', sender.get()

CheckBoxDemo()
