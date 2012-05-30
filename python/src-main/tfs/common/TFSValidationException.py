'''
robofont-extensions-and-scripts
TFSValidationException.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''




class TFSValidationException(Exception):

    def __init__(self, *argv, **argm):
        Exception.__init__(self, *argv, **argm)
