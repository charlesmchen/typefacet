from dialogKit import *

class ButtonDemo(object):
    
    def __init__(self):
        self.w = ModalDialog((200, 120), 'Button Demo')
        self.w.button1 = Button((10, 10, 180, 20), 'Button 1', callback=self.button1Callback)
        self.w.button2 = Button((10, 40, 180, 20), 'Button 2', callback=self.button2Callback)
        self.w.open()
    
    def button1Callback(self, sender):
        print 'Button 1 pressed!'
    
    def button2Callback(self, sender):
        print 'Button 2 pressed!'

ButtonDemo()
