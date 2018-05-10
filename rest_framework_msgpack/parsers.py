import msgpack

from django.utils import six

from rest_framework import parsers
from rest_framework.exceptions import ParseError

from rest_framework_msgpack.settings import settings


class MsgPackParser(parsers.BaseParser):

    media_type = 'application/msgpack'
    encoding = 'utf-8'

    def parse(self, stream, media_type=None, parser_context=None):
        try:
            return msgpack.load(stream,
                                use_list=True,
                                encoding=self.encoding,
                                object_hook=settings.MSGPACK_DECODER().default)
        except Exception as e:
            raise ParseError('MsgPack parse error - %s' % six.text_type(e))
