"""
File: TFSPointTest.py
Project: LivelyType1

@author: Charles Matthew Chen (felasold@gmail.com)
Copyright 2012 FelaSold Inc. All rights reserved.
"""


import math
from TFSTest import TFSTest
from tfs.common.TFSPoint import TFSPoint


class TFSPointTest(TFSTest):

    def setUp(self):
        pass

    def test_invert(self):
        self.assertPointEquals(TFSPoint(1, 0).invert(), TFSPoint(-1, 0))
        self.assertPointEquals(TFSPoint(3, 2).invert(), TFSPoint(-3, -2))

    def test_length(self):
        self.assertClose(TFSPoint(3, 4).length(), 5)
        self.assertClose(TFSPoint(0, 0).length(), 0)

    def test_distanceTo(self):
        self.assertClose(TFSPoint(0, 0).distanceTo(TFSPoint(0, 0)), 0)
        self.assertClose(TFSPoint(0, 0).distanceTo(TFSPoint(3, 4)), 5)
        self.assertClose(TFSPoint(3, 4).distanceTo(TFSPoint(0, 0)), 5)
        self.assertClose(TFSPoint(3, 4).distanceTo(TFSPoint(3, 4)), 0)
        self.assertClose(TFSPoint(3, 4).distanceTo(TFSPoint(6, 8)), 5)

    def test_midpoint(self):
        self.assertPointClose(TFSPoint(0, 0).midpoint(TFSPoint(0, 0)), TFSPoint(0, 0))
        self.assertPointClose(TFSPoint(0, 0).midpoint(TFSPoint(3, 4)), TFSPoint(1.5, 2))
        self.assertPointClose(TFSPoint(0, 0).midpoint(TFSPoint(-3, -4)), TFSPoint(-1.5, -2))

    def test_normalize(self):
        try:
            self.assertPointClose(TFSPoint(0, 0).normalize(), TFSPoint(0, 0))
            self.fail('Missing ZeroDivisionError')
        except ZeroDivisionError, e:
            pass

        self.assertPointClose(TFSPoint(2, 0).normalize(), TFSPoint(1, 0))
        self.assertPointClose(TFSPoint(-3, -4).normalize(), TFSPoint(-3 / 5.0, -4 / 5.0))

    def test_dotProduct(self):
        self.assertEquals(TFSPoint(3, 4).dotProduct(TFSPoint(5, 7)), 43)
        self.assertEquals(TFSPoint(3, 4).dotProduct(TFSPoint(0, 0)), 0)

    def test_rightAngleRight(self):
        self.assertPointClose(TFSPoint(0, 0).rightAngleRight(), TFSPoint(0, 0))
        self.assertPointClose(TFSPoint(1, 0).rightAngleRight(), TFSPoint(0, -1))
        self.assertPointClose(TFSPoint(3, 0).rightAngleRight(), TFSPoint(0, -3))
        self.assertPointClose(TFSPoint(-3, 0).rightAngleRight(), TFSPoint(0, 3))
        self.assertPointClose(TFSPoint(0, 5).rightAngleRight(), TFSPoint(5, 0))

    def test_rotate(self):
        self.assertPointClose(TFSPoint(3, 0).rotate(math.pi * 0.0), TFSPoint(3, 0))
        self.assertPointClose(TFSPoint(3, 0).rotate(math.pi * 0.5), TFSPoint(0, 3))
        self.assertPointClose(TFSPoint(3, 0).rotate(math.pi * 1.0), TFSPoint(-3, 0))
        self.assertPointClose(TFSPoint(3, 0).rotate(math.pi * 1.5), TFSPoint(0, -3))

    def test_hash(self):
        testset = set()
        self.assertEqual(len(testset), 0)
        testset.add(TFSPoint(0, 0))
        self.assertEqual(len(testset), 1)
        testset.add(TFSPoint(0, 0))
        self.assertEqual(len(testset), 1)
        testset.add(TFSPoint(0, 1))
        self.assertEqual(len(testset), 2)
        testset.add(TFSPoint(0, 1.0))
        self.assertEqual(len(testset), 2)
