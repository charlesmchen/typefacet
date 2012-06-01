Type Facet Convert From .otf, .ttf or .ttx to .ufo
============================================

A Python script to convert OpenType and TrueType fonts to UFO format.

Project Pages: http://charlesmchen.github.com/typefacet/

### Usage

usage: ConvertToUfo.py [-h] --src-file SRC_FILE --dst-file DST_FILE
                       [--ttx-index TTX_INDEX]

...

optional arguments:
  -h, --help            show this help message and exit
  --src-file SRC_FILE   The .otf, .ttf or .ttx file to convert to .ufo.
  --dst-file DST_FILE   The .ufo output file.
  --ttx-index TTX_INDEX
                        The index of the face to convert. Required for .ttx
                        src files; otherwise irrelevant. Default is 0.                       

### Details

Supports:

.otf
.ttf
.ttx 

Writes:

.ufo version 2

### Notes

Doesn't yet support much font metadata, but this would be easy to add.

## TODO:

