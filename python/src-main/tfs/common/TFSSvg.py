'''
robofont-extensions-and-scripts
TFSSvg.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com

Apache License

Version 2.0, January 2004

http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.

"Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.

"You" (or "Your") shall mean an individual or Legal Entity exercising permissions granted by this License.

"Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.

"Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).

"Derivative Works" shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.

"Contribution" shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.

3. Grant of Patent License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.

4. Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:

You must give any other recipients of the Work or Derivative Works a copy of this License; and

You must cause any modified files to carry prominent notices stating that You changed the files; and

You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and

If the Work includes a "NOTICE" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License. You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.

9. Accepting Warranty or Additional Liability. While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS
'''


import svgwrite

from TFSPath import *
from TFSPoint import *
from TFSMap import TFSMap


class NotImplementedException(Exception):
    pass

def parseArgbColor(value):
    result = TFSMap()
    result.alpha = 0xff & (value >> 24)
    result.red = 0xff & (value >> 16)
    result.green = 0xff & (value >> 8)
    result.blue = 0xff & (value >> 0)
    return result

def parseArgbColor01(value):
    result = parseArgbColor(value)
    result.alpha /= float(255.0)
    result.red /= float(255.0)
    result.green /= float(255.0)
    result.blue /= float(255.0)
    return result

def unparseArgbColor(value):
    result = 0
    result |= (int(value.alpha) & 0xff) << 24
    result |= (int(value.red) & 0xff) << 16
    result |= (int(value.green) & 0xff) << 8
    result |= (int(value.blue) & 0xff) << 0
    return result

def blendArgbColors(argb0, argb1, factor):
    factor = clamp01(factor)
    color0 = parseArgbColor(argb0)
    color1 = parseArgbColor(argb1)
    color = TFSMap()
    color.alpha = int((color0.alpha * (1.0 - factor)) + (color1.alpha * factor))
    color.red = int((color0.red * (1.0 - factor)) + (color1.red * factor))
    color.green = int((color0.green * (1.0 - factor)) + (color1.green * factor))
    color.blue = int((color0.blue * (1.0 - factor)) + (color1.blue * factor))
    return unparseArgbColor(color)


def formatSvgColor(value):
    color = parseArgbColor(value)
    return svgwrite.utils.rgb(color.red, color.green, color.blue)
#    return 'rgb(%d,%d,%d)' % (red, green, blue,)

def formatSvgOpacity(value):
    color = parseArgbColor01(value)
    return '%0.3f' % (color.alpha)

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

    def applyFunction(self, value):
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
        self.renderPath = None

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
#        self.renderPath = self.path.copy()
        self.renderPath = None

    def getRenderPath(self):
        if self.renderPath is None:
            return self.path
        else:
            return self.renderPath

    def minmax(self):
        PATH_PRECISION = 16
        return self.path.minmaxEvaluated(PATH_PRECISION)

    def applyFunction(self, value):
        self.renderPath = self.getRenderPath().applyFunction(value)

    def translate(self, value):
        self.renderPath = self.getRenderPath().applyPlus(value)

    def scale(self, value):
        self.renderPath = self.getRenderPath().applyScale(value)

    def renderStrokeAndFill(self, svg_document):
        rpath = self.getRenderPath()
        d = ''
        d += 'M%s\n' % (formatSvgPoint(rpath[0].startPoint()))
        for segment in rpath:
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
        def drawPointBox(point, color):
            POINT_RADIUS = 2
            drawSvgRect(svg_document,
                        point.x - POINT_RADIUS,
                        point.y - POINT_RADIUS,
                        POINT_RADIUS * 2,
                        POINT_RADIUS * 2,
                        color,
                        1)

        rpath = self.getRenderPath()
        if self.onPointColor is not None:
            for segment in rpath:
                point = segment.startPoint()
                drawPointBox(point, self.onPointColor)
        if self.controlPointColor is not None:
            for segment in rpath:
                for point in segment.controlPoints():
                    drawPointBox(point, self.controlPointColor)

    def render(self, svg_document):
        self.renderPoints(svg_document)
        self.renderStrokeAndFill(svg_document)


class TFSSvgText(TFSSvgItem):

    def __init__(self, text, origin, fillColor, **params):
        self.origin = origin.scaleXY(1.0, -1.0)
        self.text = text
        self.renderOrigin = origin
#        path.applyScaleXY(1.0, -1.0)
        self.fillColor = fillColor
        self.params = params

    def resetRenderState(self):
        self.renderOrigin = self.origin

    def minmax(self):
        return minmaxPoints((self.origin,))

    def applyFunction(self, value):
        self.renderOrigin = value(self.renderOrigin)

    def translate(self, value):
        self.renderOrigin = self.renderOrigin.plus(value)

    def scale(self, value):
        self.renderOrigin = self.renderOrigin.scale(value)

    def render(self, svg_document):
        argm = {
                'insert': (int(round(self.renderOrigin.x)),
                           int(round(self.renderOrigin.y)), ),
                'fill': formatSvgColor(self.fillColor),
                'fill_opacity': formatSvgOpacity(self.fillColor),
                }
        argm.update(self.params)

        svg_document.add(svgwrite.text.Text(self.text,
                                            **argm
                                            ))


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

    def addText(self, text, origin, fillColor, **params):
        item = TFSSvgText(text, origin, fillColor, **params)
        self.items.append(item)
        return item

    def addFillPath(self, path, color):
        self.addItem(TFSSvgPath(path).addFill(color))

    def addStrokePath(self, path, color, strokeWidth):
        self.addItem(TFSSvgPath(path).addStroke(color, strokeWidth))
#    def addPointHighlights(self, onPointColor, controlPointColor):

    def renderRaw(self, filepath, width, height):

        svg_document = svgwrite.Drawing(filename = filepath,
                                        size = ( formatSvgPixels(width),
                                                 formatSvgPixels(height), ) )

        if self.backgroundColor is not None:
            fillSvgRect(svg_document, 0, 0, width, height, self.backgroundColor)

        for item in self.items:
            item.resetRenderState()
            item.render(svg_document)

        if self.borderColor is not None:
            drawSvgRect(svg_document, 0, 0, width, height, self.borderColor)

        if filepath is not None:
            svg_document.save()
        else:
            return svg_document.tostring()


    def renderToFile(self,
                     filepath,
                     margin,
                     width=None, height=None, maxWidth=None, maxHeight=None,
                     padding=None,
                     timing=None):
        '''
        Padding in css order: top, right, bottom, left.
        '''
        if timing is not None:
            timing.mark('TFSSvg.renderToFile.0')


        margin = round(margin)
#        height = round(height)
#        maxWidth = round(maxWidth)
        if padding is None:
            padding = (0,0,0,0,)
        topPadding, rightPadding, bottomPadding, leftPadding = [int(round(value)) for value in padding]
#        print 'margin, height, maxWidth', margin, height, maxWidth

        minmax = None
        for item in self.items:
            if minmax is None:
                minmax = item.minmax()
            else:
                minmax = minmaxMerge(minmax, item.minmax())
        itemsWidth = (minmax.maxX - minmax.minX)
        itemsHeight = (minmax.maxY - minmax.minY)

        hSpacing = (2 * margin + leftPadding + rightPadding)
        vSpacing = (2 * margin + topPadding + bottomPadding)

        if maxWidth is None:
            maxWidth = width
        if maxHeight is None:
            maxHeight = height
        if maxWidth is None or maxHeight is None:
            raise Exception('Unknown combination of arguments: width: %s, height: %s, maxWidth: %s, maxHeight: %s' % ( [str(value) for value in ( width, height, maxWidth, maxHeight, ) ] ) )
        scalingX = (maxWidth - hSpacing) / itemsWidth
        scalingY = (maxHeight - vSpacing) / itemsHeight
        scaling = min(scalingX, scalingY)
        if width is None:
            width = math.ceil(itemsWidth * scaling) + hSpacing
        if height is None:
            height = math.ceil(itemsHeight * scaling) + vSpacing

#        if width is not None and height is not None:
#            pass
##            contentWidth = width - (2 * margin + leftPadding + rightPadding)
##            contentHeight = height - (2 * margin + topPadding + bottomPadding)
#        elif height is not None and maxWidth is not None:
#            scalingX = (maxWidth - hSpacing) / itemsWidth
#            scalingY = (height - vSpacing) / itemsHeight
#            scaling = min(scalingX, scalingY)
#            contentWidth = math.ceil(itemsWidth * scaling)
#            width = contentWidth + hSpacing
#        elif maxWidth is not None and maxHeight is not None:
#            scalingX = (maxWidth - hSpacing) / itemsWidth
#            scalingY = (maxHeight - vSpacing) / itemsHeight
#            scalingX = (maxWidth - vSpacing) / (minmax.maxX - minmax.minX)
#            scalingY = (height - hSpacing) / (minmax.maxY - minmax.minY)
#            scaling = min(scalingX, scalingY)
#            contentWidth = math.ceil((minmax.maxX - minmax.minX) * scaling)
#            contentHeight = math.ceil((minmax.maxY - minmax.minY) * scaling)
#            width = contentWidth + 2 * margin
#        else:
#            raise Exception('Unknown combination of arguments: width: %s, height: %s, maxWidth: %s, maxHeight: %s' % ( [str(value) for value in ( width, height, maxWidth, maxHeight, ) ] ) )

        contentWidth = width - hSpacing
        contentHeight = height - vSpacing

        width = int(round(width))
        height = int(round(height))
        contentWidth = int(round(contentWidth))
        contentHeight = int(round(contentHeight))

        scalingX = contentWidth / itemsWidth
        scalingY = contentHeight / itemsHeight
        scaling = min(scalingX, scalingY)

#        print 'scaling, contentWidth, contentHeight', scaling, contentWidth, contentHeight

        svg_document = svgwrite.Drawing(filename = filepath,
                                        size = ( formatSvgPixels(width),
                                                 formatSvgPixels(height), ) )

        if self.backgroundColor is not None:
            fillSvgRect(svg_document, 0, 0, width, height, self.backgroundColor)

        def pointFunc(point):
            x, y = point.x, point.y
            x -= minmax.minX
            y -= minmax.minY
            x *= scaling
            y *= scaling
            x += math.floor((width - contentWidth) / 2)
            y += math.floor((height - contentHeight) / 2)
            return TFSPoint(x, y)
#            return TFSPoint(margin + scaling * (point.x - minmax.minX),
#                            math.floor((height - contentHeight) / 2) + scaling * (point.y - minmax.minY))

        if timing is not None:
            timing.mark('TFSSvg.renderToFile.6')

        for item in self.items:
            item.resetRenderState()

            item.applyFunction(pointFunc)

#            item.translate(TFSPoint(-minmax.minX,
#                                    -minmax.minY))
#            item.scale(scaling)
#            item.translate(TFSPoint(margin,
#                                  math.floor((height - contentHeight) / 2)))

            item.render(svg_document)

        if timing is not None:
            timing.mark('TFSSvg.renderToFile.7')

        if self.borderColor is not None:
            drawSvgRect(svg_document, 0, 0, width, height, self.borderColor)

        if timing is not None:
            timing.mark('TFSSvg.renderToFile.8')

#        svg_document.save()
#        if timing is not None:
#            timing.mark('TFSSvg.renderToFile.9')
#
#        svg_document.tostring()

        if filepath is not None:
            svg_document.save()
            result = None
        else:
            result = svg_document.tostring()
        if timing is not None:
            timing.mark('TFSSvg.renderToFile.9')
        return result


def test_TFSSvg():
    fiSvg = TFSSvg(backgroundColor=0xffff0000)
    fiSvg.addStrokePath(polygonWithPoints(TFSPoint(4,5),
                                         TFSPoint(4,15),
                                         TFSPoint(14,15),
                                         TFSPoint(14,5)),
                       color=0x7f00ff00,
                       strokeWidth=2)
    fiSvg.renderToFile('test.svg', margin=10, height=400, maxWidth=600)
