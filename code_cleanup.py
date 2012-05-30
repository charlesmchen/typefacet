'''
robofont-extensions-and-scripts
code_cleanup.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''


import datetime
import os
import sys


MAX_LINE_WIDTH = 80

def splitLine(line, maxwidth):
    line = line.strip()

    result = []
    while len(line) > maxwidth:
        index = maxwidth
        if line[index] != ' ':
            if line.rfind(' ', 0, maxwidth) > 0:
                index = line.rfind(' ', 0, maxwidth)
        result.append(line[:index].strip())
        line = line[index:].strip()
    result.append(line)
    return result


def commentText(text):
    result = []
    for line in text.split('\n'):
        line = line.strip()
        line = line.replace('\r', '')
        result.extend(splitLine(line, MAX_LINE_WIDTH - len(HEADER_PREFIX)))
    result = [HEADER_PREFIX + line for line in result]
    return '\n'.join(result)

HEADER_PREFIX_TEMPLATE = '''
robofont-extensions-and-scripts
%s

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) %s Charles Matthew Chen
charlesmchen@gmail.com
'''

def headerPrefix(filepath):
    filename = os.path.basename(filepath)
    return HEADER_PREFIX_TEMPLATE % ( filename,
    	str(datetime.date.today().year), )


def addHeader(text, license, filepath):

    header = '\n'.join(( headerPrefix(filepath),
                         license.strip(), ))

    text = '\n\n\n'.join((("'''" + header + "\n'''"),
                      text, ))

    return text


def removeHeader(text):
	temp = text.strip()
	if not temp.startswith("'''"):
		return text
	text = temp[temp.index("'''", 3)+3:].strip()
	return text


def cleanupFile(filepath, license):
    print 'cleanupFile', filepath

    with open(filepath, 'rt') as f:
        text = f.read()

    text = removeHeader(text)

    text = addHeader(text, license, filepath)

	# Remove trailing whitespace.
    text = '\n'.join([line.rstrip() for line in text.split('\n')]) + '\n'

    with open(filepath, 'wt') as f:
        f.write(text)


def walkCallback(license, dirname, names):
#    print 'walkCallback', dirname, names

    # Make sure we don't visit any source control directories.
    if '.git' in names:
        names.remove('.git')

    for filename in names:
        if filename.endswith('.py'):
            filepath = os.path.join(dirname, filename)
            if os.path.isfile(filepath):
                cleanupFile(filepath, license)


def main():
    path = os.path.abspath(os.curdir)
    print 'path', path

    licenseFilepath = os.path.join(path, 'License.txt')
    if os.path.exists(licenseFilepath) and os.path.isfile(licenseFilepath):
        with open(licenseFilepath, 'rt') as f:
            license = f.read()
    else:
        print 'License missing: ', licenseFilepath
        return


    print sys.argv, type(sys.argv)
    if '--nolicense' in sys.argv[1:]:
        # Remove license
        license = ''

    os.path.walk(path, walkCallback, license)


if __name__ == "__main__":
    main()

    print
    print 'complete.'
