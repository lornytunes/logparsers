from logparsers.postfix import PostfixLogfileReader
from logparsers.nginx import NginxLogfileReader
from logparsers.apache import ApacheLogfileReader
from logparsers.auth import AuthLogfileReader
from logparsers.apacheip import ApacheIPLogfileReader


READER_MAP = {
    'postfix': PostfixLogfileReader,
    'apache': ApacheLogfileReader,
    'nginx': NginxLogfileReader,
    'auth': AuthLogfileReader,
    'apacheip': ApacheIPLogfileReader
}

__version__ = '1.0'
