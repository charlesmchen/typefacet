'''
robofont-extensions-and-scripts
TFSContoursException.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''





class TFSContoursException(Exception):

    def __init__(self, str, contours):
        Exception.__init__(self, str)
        self.contours = contours
