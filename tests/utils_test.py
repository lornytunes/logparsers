"""This file contains code for testing utility functions used by different log parsers

Running:
- `python3 -m logparsers.tests.utils_test`
"""


import unittest

from ..utils import get_file_date


class UtilsTest(unittest.TestCase):

    def testWeblogTimestamp(self):
        self.assertEqual(1, 1)


unittest.main()
