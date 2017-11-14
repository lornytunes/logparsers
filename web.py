import re
from datetime import datetime

from .base import RegexLogfileReader
from .utils import asUTC

REQUEST_RE = re.compile(r'^(?P<method>[A-Z]+) (?P<path>.+) HTTP/1\.[01]$')


def null_path(s):
    """Converts the missing value indicator in web logs to None"""
    if s == '-':
        return None
    else:
        return s


def null_float(s):
    if s:
        return float(s)
    else:
        return None


def parse_weblog_timestamp(datestring):
    """Converts the date and time in nginx and apache logs to a UTC `datetime` instance"""
    return asUTC(datetime.strptime(datestring, "%d/%b/%Y:%H:%M:%S %z"))


class WebLogfileReader(RegexLogfileReader):
    """Provides unified parsing for apache and nginx log files.

    Returns a dictionary with the following keys:
    - ip
    - timestamp
    - method
    - path
    - status
    - size
    - duration
    - referer
    - useragent
    - host
    """

    FIELD_NAMES = ['ip', 'timestamp', 'method', 'path',
                   'status', 'size', 'duration', 'referer', 'useragent', 'host']

    @staticmethod
    def process_result(d):
        """Breaks the request part into its component parts"""
        request = d.pop('request')
        m = REQUEST_RE.match(request)
        if m:
            d.update(m.groupdict())
        else:
            d.update({'method': None, 'path': request})

    def __init__(self, filenameOrFile):
        super(WebLogfileReader, self).__init__(
            filenameOrFile, type_mapper={
                'timestamp': parse_weblog_timestamp,
                'status': int,
                'size': int,
                'referer': null_path,
                'duration': lambda s: s and float(s) or None
            })
