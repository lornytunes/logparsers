def map_types(data, mapper):
    """
    Returns a copy of data with values coerced into the types specified in the mapper
    """
    d = {}
    for k, v in data.items():
        if k in mapper:
            d[k] = mapper[k](v)
        else:
            d[k] = v
    return d


class RegexLogfileReader(object):
    """Base class for logfile readers that use regular expressions to parse logfiles."""

    # List of regular expressions used to parse log file
    REGEX = []
    # List of keys that will be present in the dictionary returned
    FIELD_NAMES = []

    @classmethod
    def process_result(cls, d):
        """Hook for subclasses to process the dictionary of values prior to yielding"""
        pass

    def __init__(self, filenameOrFile, type_mapper=None):
        if isinstance(filenameOrFile, str):
            self.filename = filenameOrFile
            self.file = None
        else:
            self.file = filenameOrFile
            self.filename = None
        self.type_mapper = type_mapper
        self.data = None

    def __iter__(self):
        try:
            if self.file is None:
                self.file = open(self.filename, "r", encoding="utf-8")
            for line in self.file:
                self.data = line.rstrip()
                m = None
                for reg in self.__class__.REGEX:
                    m = reg.match(self.data)
                    if m:
                        break
                if m is None:
                    yield {}
                else:
                    d = m.groupdict()
                    # ensure all field names are present
                    for field_name in self.__class__.FIELD_NAMES:
                        if field_name not in d:
                            d[field_name] = None
                    # perform any data conversions
                    if self.type_mapper:
                        d = map_types(d, self.type_mapper)
                    # perform any post processing
                    self.__class__.process_result(d)
                    # return data to caller
                    yield d
        finally:
            if isinstance(self.filename, str) and self.file is not None:
                self.file.close()
