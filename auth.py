import re
import functools

from datetime import datetime

from .base import RegexLogfileReader

from .utils import asUTC, get_file_date


def parse_auth_timestamp(year, datestring):
    """Converts the date and time in auth logs to a `datetime` instance."""
    return asUTC(datetime.strptime('{} {}'.format(year, datestring), "%Y %b %d %H:%M:%S"))


class AuthLogfileReader(RegexLogfileReader):
    """Parses logfiles generated by the Auth server.

    Returns a dictionary with the following keys:
    - timestamp
    - server
    - process
    - process_id
    - message
    """

    FIELD_NAMES = ['timestamp', 'server', 'process',
                   'process_id', 'message']

    REGEX = [
        re.compile(
            r"""
            ^(?P<timestamp>[A-Za-z]{3}[ ]+[\d]{1,2}\ \d\d:\d\d:\d\d)
            \ (?P<server>[a-z0-9]+)
            \ (?P<process>[a-zA-Z]+)\[?(?P<process_id>[\d]+)?\]?:
            \ (?P<message>.+)$
            """,
            re.VERBOSE
        )
    ]

    def __init__(self, filenameOrFile):
        super(AuthLogfileReader, self).__init__(
            filenameOrFile, type_mapper={
                # we need a year part to get a date time, but auth doesn't output the year.
                # so instead we guess the year part from the time the file was created
                'timestamp': functools.partial(parse_auth_timestamp, get_file_date(filenameOrFile).year),
                'process_id': lambda s: s and int(s) or None,
                'process': lambda s: s.lower()
            })
