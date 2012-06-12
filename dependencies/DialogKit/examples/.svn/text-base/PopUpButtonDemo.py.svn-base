from dialogKit import *

class PopUpButtonDemo(object):
    
    def __init__(self):
        self.w = ModalDialog((200, 95), 'PopUpButton Demo')
        self.w.popUp = PopUpButton((10, 10, 180, 27), ['hello', 'world'], callback=self.popUpCallback)
        self.w.open()
    
    def popUpCallback(self, sender):
        print 'selected index:', sender.getSelection()

PopUpButtonDemo()