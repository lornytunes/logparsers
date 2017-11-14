"""This file contains code for testing the auth logfile reader

Running:
- `python3 -m logparsers.tests.auth_test`
"""

import os
import unittest

from ..auth import AuthLogfileReader


class AuthLogfileReaderTest(unittest.TestCase):

    def setUp(self):
        self.logfile = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'fixtures', 'auth.log')
        self.field_names = set(AuthLogfileReader.FIELD_NAMES)

    def testParse(self):
        with open(self.logfile, 'r', encoding='utf-8') as fp:
            for d in AuthLogfileReader(fp):
                self.assertEqual(set(d.keys()), self.field_names)
                if d['process_id']:
                    self.assertIsInstance(d['process_id'], int)


unittest.main()
