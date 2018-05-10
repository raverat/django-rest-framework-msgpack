from django.test import TestCase

from rest_framework_msgpack.renderers import MsgPackRenderer


class MsgPackRendererTestCase(TestCase):

    def setUp(self):
        self.renderer = MsgPackRenderer()

    def test_render_dict(self):
        data = {'foo': ['bar', 'baz']}

        result = self.renderer.render(data)

        self.assertEqual(result, b'\x81\xa3foo\x92\xa3bar\xa3baz')

    def test_render_list(self):
        data = ['value1', {'foo': 'bar'}]

        result = self.renderer.render(data)

        self.assertEqual(result, b'\x92\xa6value1\x81\xa3foo\xa3bar')
