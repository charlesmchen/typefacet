'''
robofont-extensions-and-scripts
TFSSvg.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''



import svgwrite

from TFSPath import *
from TFSPoint import *


class NotImplementedException(Exception):
    pass


def formatSvgColor(value):
    red = 0xff & (value >> 16)
    green = 0xff & (value >> 8)
    blue = 0xff & (value >> 0)
    return svgwrite.utils.rgb(red, green, blue)
#    return 'rgb(%d,%d,%d)' % (red, green, blue,)

def formatSvgOpacity(value):
    alpha = 0xff & (value >> 24)
    return '%0.3f' % (alpha / 255.0)

def formatSvgPixels(value):
    return '%dpx' % (value,)

def formatSvgPoint(value):
    return '%d,%d' % (int(round(value.x)),
                      int(round(value.y)), )

def fillSvgRect(svg_document, x, y, width, height, color):
        svg_document.add(svg_document.rect(insert = (x, y),
                                           size = (formatSvgPixels(width),
                                                   formatSvgPixels(height), ),
                                           stroke = 'none',
                                           fill = formatSvgColor(color),
                                           fill_opacity = formatSvgOpacity(color)))

def drawSvgRect(svg_document, x, y, width, height, color, strokeWidth=1):
        svg_document.add(svg_document.rect(insert = (x, y),
                                           size = (formatSvgPixels(width),
                                                   formatSvgPixels(height), ),
                                           fill = 'none',
                                           stroke = formatSvgColor(color),
                                           stroke_width = str(strokeWidth),
                                           stroke_opacity = formatSvgOpacity(color)))
#
class TFSSvgItem(object):

    def __init__(self):
        pass

    def resetRenderState(self):
        raise NotImplementedException()

    def minmax(self):
        raise NotImplementedException()

    def translate(self, value):
        raise NotImplementedException()

    def scale(self, value):
        raise NotImplementedException()

    def render(self, svg_document):
        raise NotImplementedException()


class TFSSvgPath(TFSSvgItem):

    def __init__(self, path):
        self.path = path.applyScaleXY(1.0, -1.0)
        self.fillColor = None
        self.strokeColor = None
        self.strokeWidth = None
        self.onPointColor = None
        self.controlPointColor = None

    def addFill(self, fillColor):
        if fillColor is None:
            raise Exception('Missing fillColor')
        self.fillColor = fillColor
        return self

    def addStroke(self, strokeColor, strokeWidth):
        if strokeColor is None:
            raise Exception('Missing strokeColor')
        if strokeWidth is None:
            raise Exception('Missing strokeWidth')
        self.strokeColor = strokeColor
        self.strokeWidth = strokeWidth
        return self

    def addPointHighlights(self, onPointColor, controlPointColor):
        if onPointColor is None:
            raise Exception('Missing onPointColor')
        if controlPointColor is None:
            raise Exception('Missing controlPointColor')
        self.onPointColor = onPointColor
        self.controlPointColor = controlPointColor
        return self

    def resetRenderState(self):
        self.renderPath = self.path.copy()

    def minmax(self):
        PATH_PRECISION = 16
        return self.path.minmaxEvaluated(PATH_PRECISION)

    def translate(self, value):
        self.renderPath = self.renderPath.applyPlus(value)

    def scale(self, value):
        self.renderPath = self.renderPath.applyScale(value)

    def renderStrokeAndFill(self, svg_document):
        d = ''
        d += 'M%s\n' % (formatSvgPoint(self.renderPath[0].startPoint()))
        for segment in self.renderPath:
            if len(segment) == 2:
                d += 'L%s\n' % (formatSvgPoint(segment.endPoint()))
            elif len(segment) == 3:
                d += 'Q%s %s\n' % (formatSvgPoint(segment[1]),
                                   formatSvgPoint(segment[2]), )
            elif len(segment) == 4:
                d += 'C%s %s %s\n' % (formatSvgPoint(segment[1]),
                                      formatSvgPoint(segment[2]),
                                      formatSvgPoint(segment[3]), )
            else:
                raise Exception('Invalid segment')
        d += 'Z'

        pathArgs = {
                    'd': d,
                    'fill': 'none',
                    'stroke': 'none',
                    }
        if self.fillColor is not None:
            pathArgs['fill'] = formatSvgColor(self.fillColor)
            pathArgs['fill_opacity'] = formatSvgOpacity(self.fillColor)
        if self.strokeColor is not None:
            pathArgs['stroke'] = formatSvgColor(self.strokeColor)
            pathArgs['stroke_opacity'] = formatSvgOpacity(self.strokeColor)
            pathArgs['stroke_width'] = str(self.strokeWidth)
#        print 'pathArgs', pathArgs
#            path.fill_opacity = formatSvgOpacity(self.fillColor)
#            path.stroke_opacity = formatSvgOpacity(self.strokeColor)

        svg_document.add(svg_document.path(**pathArgs))


    def renderPoints(self, svg_document):
        POINT_RADIUS = 2
        if self.onPointColor is not None:
            for segment in self.renderPath:
                point = segment.startPoint()
                drawSvgRect(svg_document,
                            point.x - POINT_RADIUS,
                            point.y - POINT_RADIUS,
                            POINT_RADIUS * 2,
                            POINT_RADIUS * 2,
                            self.onPointColor,
                            1)
        if self.controlPointColor is not None:
            for segment in self.renderPath:
                for point in segment.controlPoints():
                    drawSvgRect(svg_document,
                                point.x - POINT_RADIUS,
                                point.y - POINT_RADIUS,
                                POINT_RADIUS * 2,
                                POINT_RADIUS * 2,
                                self.controlPointColor,
                                1)

    def render(self, svg_document):
        self.renderPoints(svg_document)
        self.renderStrokeAndFill(svg_document)


class TFSSvg(object):

    def __init__(self):
        self.items = []
        self.backgroundColor = None
        self.borderColor = None

    def withBackground(self, backgroundColor):
        self.backgroundColor = backgroundColor
        return self

    def withBorder(self, borderColor):
        self.borderColor = borderColor
        return self

    def addItem(self, item):
        self.items.append(item)

    def addFillPath(self, path, color):
        self.addItem(TFSSvgPath(path).addFill(color))

    def addStrokePath(self, path, color, strokeWidth):
        self.addItem(TFSSvgPath(path).addStroke(color, strokeWidth))
#    def addPointHighlights(self, onPointColor, controlPointColor):

    def renderToFile(self, filepath, margin, height, maxWidth):
        margin = round(margin)
        height = round(height)
        maxWidth = round(maxWidth)

#        print 'margin, height, maxWidth', margin, height, maxWidth

        minmax = None
        for item in self.items:
            if minmax is None:
                minmax = item.minmax()
            else:
                minmax = minmaxMerge(minmax, item.minmax())

        scalingY = (height - 2 * margin) / (minmax.maxY - minmax.minY)
        scalingX = (maxWidth - 2 * margin) / (minmax.maxX - minmax.minX)
        scaling = min(scalingX, scalingY)
        contentWidth = math.ceil((minmax.maxX - minmax.minX) * scaling)
        contentHeight = math.ceil((minmax.maxY - minmax.minY) * scaling)
        width = contentWidth + 2 * margin

#        print 'scaling, contentWidth, contentHeight', scaling, contentWidth, contentHeight

        svg_document = svgwrite.Drawing(filename = filepath,
                                        size = ( formatSvgPixels(width),
                                                 formatSvgPixels(height), ) )

        if self.backgroundColor is not None:
            fillSvgRect(svg_document, 0, 0, width, height, self.backgroundColor)

        for item in self.items:
            item.resetRenderState()
            item.translate(TFSPoint(-minmax.minX,
                                  -minmax.minY))
            item.scale(scaling)
            item.translate(TFSPoint(margin,
                                  math.floor((height - contentHeight) / 2)))
            item.render(svg_document)

        if self.borderColor is not None:
            drawSvgRect(svg_document, 0, 0, width, height, self.borderColor)

        svg_document.save()

def test_TFSSvg():
    fiSvg = TFSSvg(backgroundColor=0xffff0000)
    fiSvg.addStrokePath(polygonWithPoints(TFSPoint(4,5),
                                         TFSPoint(4,15),
                                         TFSPoint(14,15),
                                         TFSPoint(14,5)),
                       color=0x7f00ff00,
                       strokeWidth=2)
    fiSvg.renderToFile('test.svg', margin=10, height=400, maxWidth=600)
