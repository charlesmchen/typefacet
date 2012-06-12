import os
import sys
import shutil
import zipfile

def truncatePath(top, path):
    path = path.split(os.sep)
    top = top.split(os.sep)
    truncated = list(path)
    for i in path:
        if not top:
            break
        if i == top[0]:
            truncated = truncated[1:]
            top = top[1:]
        else:
            break
    return os.sep.join(truncated)

def gatherFiles(dir, top=""):
    entries = []
    for fileName in os.listdir(dir):
        if fileName.startswith('.'):
            continue
        if fileName.endswith('.pyc'):
            continue
        fullFileName = os.path.join(dir, fileName)
        if os.path.isdir(fullFileName):
            otherEntries = gatherFiles(fullFileName, top)
            entries.extend(otherEntries)
        else:
            fullFileName = truncatePath(top, fullFileName)
            entries.append(fullFileName)
    return entries

def copyFiles(srcDir, dstDir, entries):
    for entry in entries:
        src = os.path.join(srcDir, entry)
        dst = os.path.join(dstDir, entry)
        dir = os.path.dirname(dst)
        if not os.path.exists(dir):
            os.makedirs(dir)
        try:
            shutil.copy(src, dst)
        except IOError:
            print "#### makeDistro warns: Source missing (copying): ", src
            continue

def addFiles(zipArchive, srcDir, entries):
    """Add files to zip archive."""
    for entry in entries:
        src = os.path.join(srcDir, entry)
        if not os.path.exists(src):
            print "#### makeDistro warns: Source missing (zipping): ", src
            continue
        zipArchive.write(src, entry)

#############

import dialogKit

dkDir = os.path.dirname(os.path.dirname(os.path.dirname(dialogKit.__file__)))

#############

distDir = os.path.join(dkDir, "Distributions")

if os.path.exists(distDir):
    shutil.rmtree(distDir)
os.mkdir(distDir)

#############

print "Gathering files..."

dkFiles = gatherFiles(dkDir, dkDir)
dkFiles.sort()

exclude = ['makeDistro.py']

dkFiles = [i for i in dkFiles if i not in exclude]

#############

print "Copying files to folders..."

dkName = "dialogKit_%s" % dialogKit.version

dkDist = os.path.join(distDir, dkName)

copyFiles(dkDir, dkDist, dkFiles)

dkZip = zipfile.ZipFile(os.path.join(distDir, dkName + ".zip"),
        "w", zipfile.ZIP_DEFLATED)

#############

print "Writing zip file..."

addFiles(dkZip, dkDir, dkFiles)
dkZip.close()

#############

print "Done."
