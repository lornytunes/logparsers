"""This file contains code for testing the base web log reader

Running:
- `python3 -m logparsers.tests.weblog_test`
"""

import unittest

from ..web import parse_weblog_timestamp


class WebogfileReaderTest(unittest.TestCase):

    def testTimestamp(self):
        s = '08/Nov/2017:06:23:57 +0100'
        d = parse_weblog_timestamp(s)
        self.assertEqual(d.hour, 5)


unittest.main()
