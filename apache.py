import re

from .web import WebLogfileReader


class ApacheLogfileReader(WebLogfileReader):
    """Parses logfiles generated by apache.
    """

    REGEX = [
        re.compile(
            r"""
            ^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
            \ -\ -\ \[(?P<timestamp>[^\]]+)\]
            \ "(?P<request>.*?)"
            \ (?P<status>\d+)
            \ (?P<size>\d+)
            \ "(?P<referer>.*?)"
            \ "(?P<useragent>.*?)"$
            """,
            re.VERBOSE
        )
    ]
