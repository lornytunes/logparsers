"""This file contains code for testing the apache logfile reader

Running:
- `python3 -m logparsers.tests.apache_test`
"""

import os
import unittest

from ..apache import ApacheLogfileReader


class ApacheLogfileReaderTest(unittest.TestCase):

    def setUp(self):
        self.logfile = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'fixtures', 'apache.log')
        self.field_names = set(ApacheLogfileReader.FIELD_NAMES)

    def testParse(self):
        for d in ApacheLogfileReader(self.logfile):
            self.assertEqual(set(d.keys()), self.field_names)


unittest.main()
