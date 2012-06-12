import os
import glob
import shutil
import py2html
from corbon import buildSite
import dialogKit

######################

# some content will be dynamically generated

baseDir = os.path.dirname(os.path.dirname(os.path.dirname(dialogKit.__file__)))
documentationDir = os.path.join(baseDir, 'documentation', 'source')

######################

# auto build the examples into valid xml for corbon

pyDir = os.path.join(baseDir, 'examples')
xmlDir = os.path.join(documentationDir, 'examples')
imagesDir = os.path.join(documentationDir, 'images')
#
templatePath = os.path.join(documentationDir, 'settings', 'example.xml')
templateWithImagePath = os.path.join(documentationDir, 'settings', 'exampleWithImage.xml')
f = open(templatePath, 'r')
template = f.read()
f.close()
f = open(templateWithImagePath, 'r')
templateWithImage = f.read()
f.close()
#
if not os.path.exists(xmlDir):
    os.mkdir(xmlDir)
#
exampleFileNames = []
#
for fullFileName in glob.glob(os.path.join(pyDir, '*.py')):
    print 'converting: %s...' % os.path.basename(fullFileName)
    #
    text = py2html.file2HTML(file_name=fullFileName, format="0", style=py2html.readStyleFile(None), Replace=1)
    text = py2html.makeBlock(text)
    text = text.replace('<br>', '<br/>') # make it valid XHTML so corbon won't choke
    #
    fileName = os.path.basename(fullFileName)
    imageName = os.path.splitext(fileName)[0] + '.png'
    #
    if os.path.exists(os.path.join(imagesDir, imageName)):
        text = templateWithImage % (1, fileName, fileName, text, imageName)
    else:
        text = template % (1, fileName, fileName, text)
    #
    xmlFileName = os.path.join(xmlDir, os.path.splitext(fileName)[0]+'.xml')
    f = open(xmlFileName, 'w')
    f.write(text)
    f.close()
    #
    exampleFileNames.append(fileName)

# add a list of the examples to the main example page

examplesPath = os.path.join(documentationDir, 'examples.xml')
f = open(examplesPath, 'r')
examplesXML = originalExamplesXML = f.read()
f.close()
#
exampleLines = []
for fileName in exampleFileNames:
    line = '<a href="examples/%s.html">%s</a><br />' % (os.path.splitext(fileName)[0], fileName)
    exampleLines.append(line)
exampleLines = '\n'.join(exampleLines)
#
examplesXML = examplesXML % exampleLines
#
f = open(examplesPath, 'w')
f.write(examplesXML)
f.close()

######################

# write the bug reports

bugsDir = os.path.join(documentationDir, 'bugReplication')

bugs = []

for fullFileName in glob.glob(os.path.join(bugsDir, '*.py')):
    f = open(fullFileName, 'rb')
    pyText = f.read()
    f.close()
    #
    # determine if there is example code
    # since some bug files may not contain code.
    exampleText = [line for line in pyText.splitlines() if line.strip() and not line.startswith('#')]
    if exampleText:
        hasCode = True
    else:
        hasCode = False
    #
    data = {'hasCode':hasCode, 'fileName':os.path.basename(fullFileName)}
    for line in pyText.splitlines():
        # finished scanning for data
        if not line.startswith('#'):
            break
        # strip away the #
        line = line[2:]
        if line.startswith('environment: '):
            data['environment'] = line[len('environment :'):]
        elif line.startswith('version: '):
            data['version'] = line[len('version :'):]
        elif line.startswith('platform: '):
            data['platform'] = line[len('platform :'):]
        elif line.startswith('status: '):
            data['status'] = line[len('status :'):]
        elif line.startswith('dialogKit object: '):
            data['object'] = line[len('dialogKit object :'):]
        elif line.startswith('description: '):
            data['description'] = line[len('description :'):]
        elif line.startswith('cause: '):
            data['cause'] = line[len('cause :'):]
    sorter = (data.get('environment'), data.get('version'), data.get('platform'), data.get('dialogKit object'))
    data = (sorter, data)
    bugs.append(data)

bugs.sort()

bugReports = []

bugSourceTemplate = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>%s</title>
<style type="text/css">
    h1 {    color: green;
            position: center;
        }
    .python_code {  font-family: monospace;
                font-size: 10pt;
                }
    .py_key {color: black;}
    .py_num color: black;{}
    .py_str { color: #00AA00;}
    .py_op {color: black; }
    .py_com { color: red;}
    .py_res { color: #FF7700;}
    .py_def { color: blue;}
    .py_brk { color: black;}
</style>
</head>

<body>
%s
</body>
</html>"""

bugHTMLPaths = []

for bug in bugs:
    data = bug[-1]
    #
    xml = []
    xml.append('<div class="bug">')
    #
    xml.append('<div class="bugHeader"><b class="bugSmallCaps">Object:</b> %s</div>' % data['object'])
    xml.append('<div class="bugHeader"><b class="bugSmallCaps">Environment:</b> %s</div>' % data['environment'])
    xml.append('<div class="bugHeader"><b class="bugSmallCaps">Version:</b> %s</div>' % data['version'])
    xml.append('<div class="bugHeader"><b class="bugSmallCaps">Platform:</b> %s</div>' % data['platform'])
    #
    if data['hasCode']:
        fileName = data['fileName']
        xml.append('<div class="bugData"><b class="bugSmallCaps">Demo:</b> <a href="bugReplication/%s.html" class="bugReplication">%s</a></div>' % (os.path.splitext(fileName)[0], fileName))
        # make the html file for the bug demo
        fullFileName = os.path.join(bugsDir, fileName)
        text = py2html.file2HTML(file_name=fullFileName, format="0", style=py2html.readStyleFile(None), Replace=1)
        text = py2html.makeBlock(text)
        text = bugSourceTemplate % (fileName, text)
        htmlPath = os.path.join(bugsDir, os.path.splitext(fileName)[0]+'.html')
        bugHTMLPaths.append(htmlPath)
        f = open(htmlPath, 'w')
        f.write(text)
        f.close()
    #
    status = data.get('status')
    if status:
        xml.append('<div class="bugData"><b class="bugSmallCaps">Status:</b> %s</div>' % status)
    description = data.get('description')
    cause = data.get('cause')
    if description or cause:
        xml.append('<div class="bugText">')
        if description:
            xml.append('<p><b>%s</b></p>' % description)
        if cause:
            xml.append('<p>%s</p>' % cause)
        xml.append('</div>')
    #
    xml.append('</div>')
    xml = '\n'.join(xml)
    #
    bugReports.append(xml)

bugReports = '\n'.join(bugReports)

bugsPath = os.path.join(documentationDir, 'bugs.xml')
f = open(bugsPath, 'r')
bugsXML = originalBugsXML = f.read()
f.close()
#
bugsXML = bugsXML % bugReports
#
f = open(bugsPath, 'w')
f.write(bugsXML)
f.close()

######################

# tell corbon to do its thing

settings = {'generateXMLforMissingLocalLinks': False}
buildSite('source', 'documentation', settings)

######################

# now that corbon is finished, remove
# the auto generated example XML file
shutil.rmtree(xmlDir)

# remove the auto generate bug HTML
for path in bugHTMLPaths:
    os.remove(path)

# reset the examples and bugs xml

f = open(examplesPath, 'w')
f.write(originalExamplesXML)
f.close()

f = open(bugsPath, 'w')
f.write(originalBugsXML)
f.close()
