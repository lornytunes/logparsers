"""
Contains the definition of the base parser for web log files
"""

import re

try:
    import GeoIP
    # gi = GeoIP.open("/usr/share/GeoIP/GeoIP.dat", GeoIP.GEOIP_STANDARD)
    GEOIP = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
except ImportError:
    GEOIP = None
from datetime import datetime
from urllib.parse import unquote_plus


from .base import RegexLogfileReader
from .utils import asUTC

REQUEST_RE = re.compile(r'^(?P<method>[A-Z]+) (?P<path>.+) HTTP/1\.[01]$')
SPACE_RE = re.compile(r'\s+')


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


def split_path_qs(url):
    path, qs = url.split('?', 1)
    qs = unquote_plus(qs)
    return (path, qs)


def get_country_for_ip(ip):
    return GEOIP.country_name_by_addr(ip)


def normalize_space(s):
    return s and SPACE_RE.sub(' ', s.strip()) or None


def parse_weblog_timestamp(datestring):
    """Converts the date and time in nginx and apache logs to a UTC `datetime` instance"""
    return asUTC(datetime.strptime(datestring, "%d/%b/%Y:%H:%M:%S %z"))


class WebLogfileReader(RegexLogfileReader):
    """Provides unified parsing for apache and nginx log files.

    Returns a dictionary with the following keys:
    - ip
    - country
    - timestamp
    - method
    - path
    - path_qs
    - status
    - size
    - duration
    - referer,
    - referer_qs,
    - useragent
    - host
    """

    FIELD_NAMES = ['ip', 'country', 'timestamp', 'method', 'path', 'path_qs',
                   'status', 'size', 'duration', 'referer', 'referer_qs', 'useragent', 'host']

    @staticmethod
    def process_result(d):
        """Breaks the request part into its component parts"""
        request = d.pop('request')
        m = REQUEST_RE.match(request)
        if m:
            d.update(m.groupdict())
        else:
            d.update({'method': None, 'path': request})
        if GEOIP:
            d['country'] = get_country_for_ip(d['ip'])
        else:
            d['country'] = None
        # split paths and query strings
        for k in ('referer', 'path',):
            qs_k = '{}_qs'.format(k)
            if d[k] and '?' in d[k]:
                p, qs = split_path_qs(d[k])
                d[k] = p
                d[qs_k] = qs
            else:
                d[qs_k] = None

    def __init__(self, filenameOrFile):
        super(WebLogfileReader, self).__init__(
            filenameOrFile, type_mapper={
                'timestamp': parse_weblog_timestamp,
                'status': int,
                'size': int,
                'referer': null_path,
                'duration': lambda s: s and float(s) or None
            })
