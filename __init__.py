from logparsers.postfix import PostfixLogfileReader
from logparsers.nginx import NginxLogfileReader
from logparsers.apache import ApacheLogfileReader
from logparsers.auth import AuthLogfileReader


READER_MAP = {
    'postfix': PostfixLogfileReader,
    'apache': ApacheLogfileReader,
    'nginx': NginxLogfileReader,
    'auth': AuthLogfileReader
}

__version__ = '1.0'
