from dateutil.parser import parse as dateutil_parse


class MsgPackDecoder(object):

    def default(self, obj):
        if '__class__' in obj:
            func = getattr(self, 'parse_%s' % obj['__class__'], None)
            if func:
                return func(obj['v'])
        return obj

    def parse_datetime(self, v):
        return dateutil_parse(v)

    def parse_date(self, v):
        return dateutil_parse(v).date()

    def parse_time(self, v):
        return dateutil_parse(v).time()
