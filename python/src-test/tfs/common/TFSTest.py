"""
File: FTest.py
Project: LivelyType1

@author: Charles Matthew Chen (felasold@gmail.com)
Copyright 2012 FelaSold Inc. All rights reserved.
"""


import unittest
import tfs.common.TFSPoint


class TFSTest(unittest.TestCase):

    def setUp(self):
        pass

    def assertPointEquals(self, point0, point1, msg=None):
        self.assertEqual(point0.x, point1.x, msg=msg)
        self.assertEqual(point0.y, point1.y, msg=msg)

    def assertPointClose(self, point0, point1, msg=None):
        self.assertClose(point0.distanceTo(point1), msg=msg)

    def assertClose(self, value, expected=0, msg=None):
        CLOSE_TOLERANCE = 0.0001
        self.assertLess(abs(value - expected), CLOSE_TOLERANCE, msg=msg)

#    def assertDistanceClose(self, distance, msg=None):
#        CLOSE_TOLERANCE = 0.0001
#        self.assertLess(distance, CLOSE_TOLERANCE, msg=msg)
