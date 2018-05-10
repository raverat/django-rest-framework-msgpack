from io import BytesIO

from django.test import TestCase

from rest_framework_msgpack.parsers import MsgPackParser


class MsgPackParserTestCase(TestCase):

    def setUp(self):
        self.parser = MsgPackParser()

    def test_parse_dict(self):
        encoded_data = b'\x81\xa3foo\x92\xa3bar\xa3baz'

        result = self.parser.parse(BytesIO(encoded_data))

        self.assertEqual(result, {'foo': ['bar', 'baz']})

    def test_parse_list(self):
        encoded_data = b'\x92\xa6value1\x81\xa3foo\xa3bar'

        result = self.parser.parse(BytesIO(encoded_data))

        self.assertEqual(result, ['value1', {'foo': 'bar'}])

    def test_invalid_class(self):
        encoded_data = b'\x81\xa1k\x82\xa9__class__\xa7unknown\xa1v\x01'

        result = self.parser.parse(BytesIO(encoded_data))

        self.assertEqual(result, {'k': {'__class__': 'unknown', 'v': 1}})