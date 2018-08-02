import re

from .base import RegexLogfileReader
from .web import parse_weblog_timestamp


class ApacheIPLogfileReader(RegexLogfileReader):
    '''
    Provides lightweight log file parsing for Mastering Postgres Database Application book.

    Returns a dictionary with the following keys:
    - ip
    - ts
    - request
    - status
    '''

    FIELD_NAMES = ['ip', 'ts', 'request', 'status']

    REGEX = [
        re.compile(
            r"""
            ^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
            \ -\ -\ \[(?P<ts>[^\]]+)\]
            \ "(?P<request>.*?)"
            \ (?P<status>\d+)
            """,
            re.VERBOSE
        )
    ]

    def __init__(self, filenameOrFile):
        super(ApacheIPLogfileReader, self).__init__(
            filenameOrFile, type_mapper={
                'ts': parse_weblog_timestamp,
                'status': int
            })
