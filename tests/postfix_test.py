"""This file contains code for testing the postfix logfile reader

Running:
- `python3 -m logparsers.tests.postfix_test`
"""

import os
import unittest

from ..postfix import PostfixLogfileReader


class PostfixLogfileReaderTest(unittest.TestCase):

    def setUp(self):
        self.logfile = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'fixtures', 'postfix.log')
        self.field_names = set(PostfixLogfileReader.FIELD_NAMES)

    def testParse(self):
        with open(self.logfile, 'r', encoding='utf-8') as fp:
            for d in PostfixLogfileReader(fp):
                self.assertEqual(set(d.keys()), self.field_names)
                self.assertIsInstance(d['process_id'], int)

    def testProcess(self):
        d = {'message': 'to=<notify@dstbusinesssystems.com>, relay=none, delay=365798'}
        PostfixLogfileReader.process_result(d)
        self.assertIsInstance(d, dict)


unittest.main()
