"""This file contains code for testing the nginx logfile reader

Running:
- `python3 -m logparsers.tests.nginx_test`
"""

import os
import unittest

from ..nginx import NginxLogfileReader


class NginxLogfileReaderTest(unittest.TestCase):

    def setUp(self):
        self.logfile = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'fixtures', 'nginx.log')
        self.field_names = set(NginxLogfileReader.FIELD_NAMES)

    def testParse(self):
        for d in NginxLogfileReader(self.logfile):
            self.assertEqual(set(d.keys()), self.field_names)
            if d['duration']:
                self.assertIsInstance(d['duration'], float)


unittest.main()
