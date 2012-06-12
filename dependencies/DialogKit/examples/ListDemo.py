from dialogKit import *

class AddItemDialog(object):
    
    def __init__(self, callback):
        self.callback = callback
        self.w = ModalDialog((300, 130), okCallback=self.okCallback, cancelCallback=self.cancelCallback)
        self.w.titleField = TextBox((10, 10, 280, 20), 'Enter some text')
        self.w.inputField = EditText((10, 35, 280, 27), '')
        self.w.open()
    
    def cancelCallback(self, sender):
        self.callback(None)
    
    def okCallback(self, sender):
        text = self.w.inputField.get()
        if text:
            self.callback(text)
        else:
            self.callback(None)


class ListDemoDialog(object):
    
    def __init__(self):
        self.w = ModalDialog((200, 300), 'List Demo', okCallback=self.okCallback)
        self.w.list = List((10, 40, 180, 200), ['hello', 'there'], callback=self.listHitCallback)
        self.w.addButton = Button((10, 10, 85, 20), 'Add', callback=self.addCallback)
        self.w.removeButton = Button((105, 10, 85, 20), 'Remove', callback=self.removeCallback)
        self.w.open()
    
    def okCallback(self, sender):
        print 'this final list contains:', list(self.w.list)
    
    def listHitCallback(self, sender):
        selection = sender.getSelection()
        if not selection:
            selectedItem = None
        else:
            selectionIndex = selection[0]
            selectedItem = sender[selectionIndex]
        print 'selection:', selectedItem
    
    def addItemDialogCallback(self, result):
        if result is not None:
            self.w.list.append(result)
            self.w.list.setSelection([len(self.w.list)-1])
    
    def addCallback(self, sender):
        AddItemDialog(self.addItemDialogCallback)
    
    def removeCallback(self, sender):
        if len(self.w.list):
            selectionIndex = self.w.list.getSelection()[0]
            selectedItem = self.w.list[selectionIndex]
            print 'removing:', selectedItem
            del self.w.list[selectionIndex]


ListDemoDialog()
