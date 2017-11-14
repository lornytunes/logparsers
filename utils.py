import os
import pytz

from datetime import datetime


def asUTC(dt):
    """Normalizes a datetime instance to UTC"""
    if dt.tzinfo is None:
        # no timezone component - create one
        return pytz.utc.localize(dt)
    else:
        return pytz.utc.normalize(dt.astimezone(pytz.utc))


def get_file_date(filenameOrFile):
    """Returns a the date and time a file was created."""
    ts = isinstance(filenameOrFile, str) and os.stat(filenameOrFile) or os.stat(filenameOrFile.name)
    return datetime.fromtimestamp(ts.st_ctime)
