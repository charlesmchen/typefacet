'''
robofont-extensions-and-scripts
TFSGlyph.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''


from TFSPoint import *
from TFSPath import *


class TFSGlyph(object):

    def __init__(self, rfglyph):
        self.rfglyph = rfglyph

    unicode = property(lambda self: self.rfglyph.unicode)


    def getContours(self, setSelected=False):

        def rfPointToTFSPoint(rfpoint):
            fiPoint = TFSPoint(rfpoint.x, rfpoint.y)
            if setSelected:
                fiPoint.selected = rfpoint.selected
            return fiPoint

        paths = []
        for rfcontour in self.rfglyph:
#            print 'rfcontour', rfcontour
            segments = []
            lastPoint = rfPointToTFSPoint(rfcontour[-1].points[-1])
            for rfsegment in rfcontour:
#                print 'rfsegment', rfsegment.points
                fiPoints = [lastPoint,] + [rfPointToTFSPoint(rfpoint) for rfpoint in rfsegment.points]
                lastPoint = fiPoints[-1]
                if (len(fiPoints) == 2) and fiPoints[0] == fiPoints[-1]:
                    print 'ignoring empty contour segment in: ' + hex(self.rfglyph.unicode)
                    continue

                rfendpoint = rfsegment.points[-1]
                if rfendpoint.type == 'qcurve':
                    # TrueType "implied on-curve points"
                    lastOnPoint = fiPoints[0]
                    offPoints = fiPoints[1:-1]
                    for index in xrange(len(offPoints) - 1):
                        offPoint0 = offPoints[index + 0]
                        offPoint1 = offPoints[index + 1]
                        impliedPoint = offPoint0.midpoint(offPoint1)
                        segments.append(TFSSegment(lastOnPoint, offPoint0, impliedPoint))
                        lastOnPoint = impliedPoint
                    segments.append(TFSSegment(lastOnPoint, offPoints[-1], fiPoints[-1]))
                else:
                    segments.append(TFSSegment(*fiPoints))

#                segments.append(TFSSegment(*fiPoints))
#                for rfpoint in rfsegment.points:
#                    fiPoint = rfPointToTFSPoint(rfpoint)
#                    print '\t', 'fiPoint', fiPoint
#                print '\t', 'fiPoints', fiPoints
            paths.append(TFSPath(True, *segments))

        return paths


#    def glyphNames(self):
#        return self.rffont.keys()
#
#    def glyphCodePoints(self):
#        result = [glyph.unicode for glyph in self.rffont]
#        return result
#
#    def getGlyphByName(self, key):
#        rfglyph = self.rffont.getGlyph(key)
#        return PAGlyph(rfglyph)


    def setContours(self, paths):
        self.rfglyph.clearContours()

        glyphPen = self.rfglyph.getPen()

        def formatScalar(value):
            return int(round(value))

        def formatPoint(value):
            result = ( formatScalar(value.x),
                        formatScalar(value.y), )
        #    print 'result', result
            return result

        for path in paths:
            firstPoint = path.segments[0].points[0]
        #    print 'writing move to'
            glyphPen.moveTo(formatPoint(firstPoint))
            for segment in path.segments:
                if len(segment.points) == 4:
        #            print 'writing 4-point segment'
                    p1 = segment.points[1]
                    p2 = segment.points[2]
                    p3 = segment.points[3]
                    glyphPen.curveTo(formatPoint(p1),
                                     formatPoint(p2),
                                     formatPoint(p3))
        #            glyphPen.lineTo(formatPoint(p3))
                elif len(segment.points) == 3:
        #            print 'writing 3-point segment'
                    p1 = segment.points[1]
                    p2 = segment.points[2]
                    glyphPen.curveTo(formatPoint(p1),
                                     formatPoint(p2))
        #            glyphPen.moveTo(formatPoint(p))
        #            glyphPen.lineTo(formatPoint(p2))
        #            raise Exception(
        #                            )
                elif len(segment.points) == 2:
        #            print 'writing 2-point segment'
                    p1 = segment.points[1]
                    glyphPen.lineTo(formatPoint(p1))
                else:
                    raise Exception('Invalid contour segment point count: ' + str(len(segment.points)))

            glyphPen.closePath()

        self.rfglyph.update()
#        self.rfglyph.correctDirection()
#        self.rfglyph.update()



    def updateDerivedFromGlyph(self, codePoint, contours, srcGlyph):
        opentype_multiplier = 1
        def formatOpentypeScalar(value):
            return int(round(opentype_multiplier * value))

        self.rfglyph.unicode = codePoint
#        #        glyph.leftMargin = 0
#        #        glyph.rightMargin = 900
        # TODO:
        self.rfglyph.width = formatOpentypeScalar(srcGlyph.rfglyph.width)
        #glyph.advance = formatOpentypeScalar(glyphAdvance)
#        self.rfglyph.rightMargin = formatOpentypeScalar(srcGlyph.rfglyph.rightMargin)

#        print 'self.rfglyph.rightMargin', self.rfglyph.rightMargin, type(self.rfglyph.rightMargin)
#        print 'srcGlyph.rfglyph.rightMargin', srcGlyph.rfglyph.rightMargin, type(srcGlyph.rfglyph.rightMargin)
#        print 'self.rfglyph.width', self.rfglyph.width, type(self.rfglyph.width)
#        print 'srcGlyph.rfglyph.width', srcGlyph.rfglyph.width, type(srcGlyph.rfglyph.width)
        #print 'glyphAdvance', glyphAdvance, formatOpentypeScalar(glyphAdvance)
        #print 'glyphWidth', glyphWidth, formatOpentypeScalar(glyphWidth)
        #print 'glyphWidth', sideBearing, formatOpentypeScalar(sideBearing)
        #print 'glyph.width', glyph.width
        #print 'glyph.advance', glyph.advance
        #print 'glyph.rightMargin', glyph.rightMargin

        self.setContours(contours)
