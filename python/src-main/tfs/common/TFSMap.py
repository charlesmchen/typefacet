'''
robofont-extensions-and-scripts
TFSMap.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''




class TFSMap(dict):

    def __init__(self):
        pass

    def __setattr__(self, key, value):
        self[key] = value

    def __hasattr__(self, key):
        return key in self

    def __getattr__(self, key):
        return self[key]
