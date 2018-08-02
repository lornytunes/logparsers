"""This file contains code for testing the ApacheIP logfile reader

Running:
- `python3 -m logparsers.tests.apacheip_test`
"""

import os
import unittest

from ..apacheip import ApacheIPLogfileReader


class ApacheIPLogfileReaderTest(unittest.TestCase):

    def setUp(self):
        self.logfile = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'fixtures', 'apacheip.log')
        self.field_names = set(ApacheIPLogfileReader.FIELD_NAMES)

    def testParse(self):
        for d in ApacheIPLogfileReader(self.logfile):
            self.assertEqual(set(d.keys()), self.field_names)


unittest.main()
