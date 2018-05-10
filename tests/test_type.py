import collections
import datetime
import decimal

from io import BytesIO

from django.test import TestCase

from rest_framework_msgpack.parsers import MsgPackParser
from rest_framework_msgpack.renderers import MsgPackRenderer


class MsgPackTypeTestCase(TestCase):

    """
    As msgpack does not keep the orders of the keys in dictionnary, the simpliest way to test
    is to render then parse the encoded data to compare the result from the original.
    """

    def setUp(self):
        self.renderer = MsgPackRenderer()
        self.parser = MsgPackParser()

    def test_datetime(self):
        data = {'date': datetime.datetime.now()}

        output = self.renderer.render(data)
        parsed_data = self.parser.parse(BytesIO(output))

        self.assertDictEqual(parsed_data, data)

    def test_date(self):
        data = {'date': datetime.date.today()}

        output = self.renderer.render(data)
        parsed_data = self.parser.parse(BytesIO(output))

        self.assertDictEqual(parsed_data, data)

    def test_time(self):
        data = {'date': datetime.time.max}

        output = self.renderer.render(data)
        parsed_data = self.parser.parse(BytesIO(output))

        self.assertDictEqual(parsed_data, data)

    def test_timedelta(self):
        data = {'delta': datetime.timedelta(hours=1, milliseconds=1)}

        output = self.renderer.render(data)
        parsed_data = self.parser.parse(BytesIO(output))

        self.assertDictEqual(parsed_data, {'delta': 3600.001})

    def test_decimal(self):
        data = {'decimal': decimal.Decimal(7)}

        output = self.renderer.render(data)
        parsed_data = self.parser.parse(BytesIO(output))

        self.assertDictEqual(parsed_data, {'decimal': 7.0})

    def test_getitem(self):
        data = {'dict': collections.OrderedDict(key='value')}

        output = self.renderer.render(data)
        parsed_data = self.parser.parse(BytesIO(output))

        self.assertDictEqual(parsed_data, {'dict': {'key': 'value'}})

    def test_iter(self):
        data = {'values': range(0, 10)}

        output = self.renderer.render(data)
        parsed_data = self.parser.parse(BytesIO(output))

        self.assertDictEqual(parsed_data, {'values': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]})
