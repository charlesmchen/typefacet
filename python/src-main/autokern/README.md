Type Facet Autokern
===================

A Python script to convert auto-kern fonts in UFO format.

Project Pages: http://charlesmchen.github.com/typefacet/

### Usage

usage: Autokern.py [-h] --ufo-src UFO_SRC --ufo-dst UFO_DST
                   [--log-dst LOG_DST] [--min-distance-ems MIN_DISTANCE_EMS]
                   [--max-distance-ems MAX_DISTANCE_EMS]
                   [--intrusion-tolerance INTRUSION_TOLERANCE]
                   [--min-non-intrusion-ems MIN_NON_INTRUSION_EMS]

required arguments:
  --ufo-src UFO_SRC     The UFO source file to kern.
  --ufo-dst UFO_DST     The UFO destination file.

optional arguments:
  -h, --help            show this help message and exit
  --log-dst LOG_DST     Optional folder in which to write HTML logs. CAUTION:
                        This folder will be completely overwritten.
  --min-distance-ems MIN_DISTANCE_EMS
                        The absolute minimum distance between glyphs in ems.
                        0.0 <= x <= 1.0. Default: 0.1
  --max-distance-ems MAX_DISTANCE_EMS
                        The absolute maximum distance between glyphs in ems.
                        0.0 <= x <= 1.0. Default: 0.3
  --intrusion-tolerance INTRUSION_TOLERANCE
                        Intrusion tolerance as a fraction of the area defined
                        by the --max-distance-ems value times the greater of
                        the two glyphs' heights. Default: 0.1
  --min-non-intrusion-ems MIN_NON_INTRUSION_EMS
                        The minimum non-intruding height in ems. 0.0 <= x <=
                        1.0. Default: 0.2
     
### Details


### Notes

## TODO:

## License

Distributed under the Apache Software License 2.0.

## Dependencies

* Python 2.7 or later
* [pystache](https://github.com/defunkt/pystache) (only if using --log-dst option to write html logs).
* [svgwrite](http://packages.python.org/svgwrite/) (only if using --log-dst option to write html logs).

## Tested on:

* Mac OS X 10.7 (Lion) with Python 2.7




