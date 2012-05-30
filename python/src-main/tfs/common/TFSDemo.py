'''
robofont-extensions-and-scripts
TFSDemo.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''


import os
import shutil

from FontInterpolator import FontInterpolator
from TFSSettings import getCommandLineSettings

#pseudo_argv = ('--ufo-src=' + os.path.abspath(os.path.join('..', '..', 'data-ignore', 'theleagueof-league-gothic-4f9ff8d', 'source', 'League Gothic.ufo')) + '',
pseudo_argv = ('--ufo-src=' + os.path.abspath(os.path.join('..', '..', 'data-ignore', 'League Gothic.modified.ufo')) + '',
               '--ufo-dst=' + os.path.abspath(os.path.join('..', '..', 'out', 'League Gothic.ufo')) + '',
               '--log-dst=' + os.path.abspath(os.path.join('..', '..', 'logs')) + '',
               '--otf-dst=' + os.path.abspath(os.path.join('..', '..', 'out', 'League Gothic.otf')) + '',
               '--top-join-centers',
               '0x60', '261', # Grave
               '0xB4', '239', # Acute
               '0x6A', '87.5', # j
               '0x4A', '118', # J
               '0x67', '157', # g
               '0x47', '177', # G
               '0x2DD', '218', # hungarumlaut
               '0x52', '148', # R
               '0x72', '130', # r
               '0x74', '111.5', # t
               '0x4C', '94.0', # L
               '0x44', '175.0', # D
               '0x64', '140.0', #

               '--tail-join-centers',
               '0xAF', '260.0', # ogonek
               '0x41', '311.5,0', # A
               '0x61', '253.0,0', # a
               '0x45', '230,0', # E
               '0x65', '162,0', # e

#Base Glyph: L (L, 0x4C)

#D, 0x44)
# d (d, 0x64)
 #               '--top-join-centers 0x60 261',

               )
print 'pseudo_argv', ' '.join(pseudo_argv)

# d with caron is super wrong.
# should i use dotless i?

settings = getCommandLineSettings(*pseudo_argv)
#settings = getCommandLineSettings()
#settings.ufo_src = os.path.abspath(os.path.join('..', '..', 'data-ignore', 'theleagueof-league-gothic-4f9ff8d', 'source', 'League Gothic.ufo'))
#settings.ufo_dst = os.path.abspath(os.path.join('..', '..', 'out', 'League Gothic.ufo'))
#settings.log_dst = os.path.abspath(os.path.join('..', '..', 'logs'))
#settings.otf_dst = os.path.abspath(os.path.join('..', '..', 'out', 'League Gothic.otf'))

FontInterpolator(settings).process()

print
print 'complete.'
