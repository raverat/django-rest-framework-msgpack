import msgpack

from rest_framework import renderers

from rest_framework_msgpack.settings import settings


class MsgPackRenderer(renderers.BaseRenderer):

    media_type = 'application/msgpack'
    format = 'msgpack'
    render_style = 'binary'
    charset = None

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data is None:
            return ''
        return msgpack.packb(data, default=settings.MSGPACK_ENCODER().default)
