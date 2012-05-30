'''
robofont-extensions-and-scripts
TFSSvgUtils.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''


import os
import shutil
import types

from TFSFont import *
from TFSMap import *
#from TFSSvg import *
from TFSSettings import getCommandLineSettings
import TFSCompoundsList
from TFSPoint import TFSPoint, minmaxMerge, minmaxPoints
from TFSPath import minmaxPaths, openPathWithPoints


def svgRenderGlyphContours(fiSvg, contours, strokeColor):
    from TFSSvg import TFSSvgPath

    ON_POINT_COLOR = 0x7f7f7f7f
    CONTROL_POINT_COLOR = 0x7fafafaf
    for contour in contours:
        fiSvg.addItem(TFSSvgPath(contour).addStroke(strokeColor, 2).addPointHighlights(ON_POINT_COLOR, CONTROL_POINT_COLOR))


def renderSvgScene(self,
                   filenamePrefix,
                   pathTuples,
                   hGuidelines=None):
    from TFSSvg import TFSSvg, TFSSvgPath

    filename = '%s.svg' % ( filenamePrefix, )
    dstFile = os.path.abspath(os.path.join(self.svg_folder, filename))

    CANVAS_BACKGROUND_COLOR = 0xffffffff
    CANVAS_BORDER_COLOR = 0x07fbfbfbf
    fiSvg = TFSSvg().withBackground(CANVAS_BACKGROUND_COLOR).withBorder(CANVAS_BORDER_COLOR)

#    if pathTuples:
    for color, contours in pathTuples:
        self.subrenderGlyphContours(fiSvg, contours, color)

    if hGuidelines:
        for hGuideline in hGuidelines:
            p0 = TFSPoint(hGuideline, self.fifont.info.descender)
            p1 = TFSPoint(hGuideline, self.fifont.info.ascender)
            GUIDELINE_COLOR = 0x7fdfdfdf
            fiSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

    vGuidelines = ( 0,
                    self.fifont.info.ascender,
                    self.fifont.info.descender,
                    )
    if vGuidelines:
        minmax = None
        for color, contours in pathTuples:
            minmax = minmaxMerge(minmax, minmaxPaths(contours))

        for vGuideline in vGuidelines:
            p0 = TFSPoint(0, vGuideline)
            p1 = TFSPoint(minmax.maxX, vGuideline)
            GUIDELINE_COLOR = 0x7fdfdfdf
            fiSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

    SVG_HEIGHT = 400
    SVG_MAX_WIDTH = 800
    fiSvg.renderToFile(dstFile, margin=10, height=SVG_HEIGHT, maxWidth=SVG_MAX_WIDTH)
    return filename
