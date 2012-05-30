'''
robofont-extensions-and-scripts
TFSWriteOtf.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''




import os
import robofab.world


def writeOtf(rffont, otfFile):

    rffont.update()
    rffont.autoUnicodes()
    rffont.update()

    from ufo2fdk import haveFDK
    from ufo2fdk import OTFCompiler

    if haveFDK():
        print "I found the FDK!"
    else:
        print "I'm sorry, I could not find the FDK."

    compiler = OTFCompiler()
    reports = compiler.compile(rffont, otfFile, checkOutlines=True, autohint=True)
    #    reports = compiler.compile(font, dstFile, checkOutlines=True, autohint=False)
    print reports["checkOutlines"]
    print reports["autohint"]
    print reports["makeotf"]
