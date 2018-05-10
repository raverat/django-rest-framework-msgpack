import datetime
import decimal

from django.utils import timezone


class MsgPackEncoder(object):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            value = obj.isoformat()
            if value.endswith('+00:00'):
                value = value[:-6] + 'Z'
            return {'__class__': 'datetime', 'v': value}
        elif isinstance(obj, datetime.date):
            return {'__class__': 'date', 'v': obj.isoformat()}
        elif isinstance(obj, datetime.time):
            if timezone and timezone.is_aware(obj):
                raise ValueError("MsgPack can't represent timezone-aware times.")
            return {'__class__': 'time', 'v': obj.isoformat()}
        elif isinstance(obj, datetime.timedelta):
            return obj.total_seconds()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif hasattr(obj, '__getitem__'):
            try:
                return dict(obj)
            except Exception:
                pass
        elif hasattr(obj, '__iter__'):
            return tuple(item for item in obj)
        return obj

