'''
robofont-extensions-and-scripts
TFSCompoundsList.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''


import os
import sys


def parseHexCode(value):
    return int('0x' + value, 16)


def getDiacriticalHexByName(glyphNameMap, diacriticalName):
    altPattern = 'MODITFSER LETTER %s ACCENT'
    altName = altPattern % diacriticalName
    if altName in glyphNameMap:
        diacriticalHexCode = glyphNameMap[altName]
        return diacriticalHexCode

    if diacriticalName in glyphNameMap:
        diacriticalHexCode = glyphNameMap[diacriticalName]
        return diacriticalHexCode
    else:
        diacriticalHexCode = None
        altPatterns = (
                       'MODITFSER LETTER %s ACCENT',
                       '%s ACCENT',
                       )
        for altPattern in altPatterns:
            altName = altPattern % diacriticalName
            if altName in glyphNameMap:
                diacriticalHexCode = glyphNameMap[altName]
                return diacriticalHexCode
    return None

DIACRITICAL_ALIGN_TOP = 'top'
DIACRITICAL_ALIGN_TAIL = 'tail'
DIACRITICAL_ALIGN_TAIL_FLOAT = 'tail float'
DIACRITICAL_ALIGN_MIDDLE = 'middle'
DIACRITICAL_ALIGN_TOP_ROTATE_FLOAT = 'DIACRITICAL_ALIGN_TOP_ROTATE_FLOAT'
DIACRITICAL_ALIGN_TAIL_H_FLIP = 'DIACRITICAL_ALIGN_TAIL_H_FLIP'

def getCompounds(log_dst=None):
    srcFile = os.path.abspath(os.path.join('..', '..', 'data', 'Adobe Glyph List', 'aglfn13.txt'))
    print 'srcFile', srcFile
    if not os.path.exists(srcFile) and os.path.isfile(srcFile):
        raise Exception ('Missing srcFile: ' + srcFile)

    with open(srcFile, 'rt') as f:
        csvData = f.read()

    glyphInfos = []
    glyphNameMap = {}
    for line in csvData.split('\n'):
        line = line.strip()
        if line.startswith('#'):
            continue
        if not line:
            continue
        hexCode, shortName, longName = line.split(';')
        shortName = shortName.strip()
        longName = longName.strip()
        glyphInfos.append( (hexCode, shortName, longName,) )
        glyphNameMap[longName] = hexCode

    # Hack
#    glyphNameMap['MODITFSER LETTER MACRON ACCENT'] = '02C9'
    glyphNameMap['MODITFSER LETTER TILDE ACCENT'] = '02DC'

    yamlMaps = []
    unknownBaseNames = set()
    unknownDiacriticalNames = set()
    knownDiacriticalNames = set()
    for hexCode, shortName, longName in glyphInfos:
        DELIMITER = ' WITH '
        if DELIMITER not in longName:
            continue
        index = longName.index(DELIMITER)
        baseName = longName[:index]
        diacriticalName = longName[index + len(DELIMITER):]
    #    print 'longName "%s", baseName "%s", diacriticalName "%s", ' % ( longName, baseName, diacriticalName, )

        if baseName in glyphNameMap:
            baseHexCode = glyphNameMap[baseName]
        else:
            unknownBaseNames.add(baseName)
            continue

        diacriticalHexCode = getDiacriticalHexByName(glyphNameMap, diacriticalName)
        if diacriticalHexCode is None:
            unknownDiacriticalNames.add(diacriticalName)
            continue
        knownDiacriticalNames.add(diacriticalName)


        diacriticalMap = { 'glyph': parseHexCode(diacriticalHexCode), }
        if parseHexCode(diacriticalHexCode) in ( 0xb7, # Middle dot
                                                 ):
            diacriticalMap['align'] = DIACRITICAL_ALIGN_MIDDLE
        elif parseHexCode(diacriticalHexCode) in ( 0x2DB, # ogonek
                                                 ):
            diacriticalMap['align'] = DIACRITICAL_ALIGN_TAIL
        elif parseHexCode(diacriticalHexCode) in ( 0xB8, # cedilla
                                                 ):
            diacriticalMap['align'] = DIACRITICAL_ALIGN_TAIL_FLOAT
        else:
            diacriticalMap['align'] = DIACRITICAL_ALIGN_TOP

        # An exception
        if parseHexCode(hexCode) in ( 0x123, # g cedilla
                                                 ):
            diacriticalMap['align'] = DIACRITICAL_ALIGN_TOP_ROTATE_FLOAT
        elif parseHexCode(hexCode) in ( 0x162, # T cedilla
                                        0x163, # t cedilla
                                        ):
            diacriticalMap['align'] = DIACRITICAL_ALIGN_TAIL_H_FLIP
            diacriticalMap['glyph'] = 0x2DB # ogonek

        yamlMap = {
                   'glyph': parseHexCode(hexCode),
                   'baseGlyph': parseHexCode(baseHexCode),
                   'diacriticals': ( diacriticalMap, ),
                   }
        yamlMaps.append(yamlMap)
    #- glyph: 220
    #  baseGlyph: 'U'
    #  diacriticals:
    #    - glyph: 168

        pass

    print
    print 'Compound glyph schema results:'
    print 'unknownBaseNames', sorted(unknownBaseNames)
    print 'unknownBaseNames', sorted(unknownDiacriticalNames)
    print 'knownDiacriticalNames', sorted(knownDiacriticalNames)
    print 'unknownBaseNames', len(unknownBaseNames)
    print 'unknownBaseNames', len(unknownDiacriticalNames)
    print 'knownDiacriticalNames', len(knownDiacriticalNames)
    print

#    print 'yamlMaps', yamlMaps

    yamlMaps = sorted(yamlMaps, lambda yamlMap0, yamlMap1: cmp(yamlMap0['glyph'], yamlMap1['glyph']))

    if log_dst is not None:
        import yaml
        dstFile = os.path.abspath(os.path.join(log_dst, 'compounds.yaml'))
        print 'dstFile', dstFile
        yamlData = yaml.safe_dump(yamlMaps)
        with open(dstFile, 'wt') as f:
            f.write(yamlData)

    return yamlMaps



if __name__ == "__main__":
    yamlMaps = getCompounds()
    for yamlMap in yamlMaps:
        print 'yamlMap', yamlMap

    print
    print 'complete.'
