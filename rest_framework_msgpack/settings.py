from django.conf import settings as pj_settings

from rest_framework.settings import APISettings


USER_SETTINGS = getattr(pj_settings, 'REST_FRAMEWORK_MSGPACK', {})

DEFAULTS = {
    'MSGPACK_DECODER': 'rest_framework_msgpack.decoders.MsgPackDecoder',
    'MSGPACK_ENCODER': 'rest_framework_msgpack.encoders.MsgPackEncoder'
}

IMPORT_SETTINGS = (
    'MSGPACK_DECODER',
    'MSGPACK_ENCODER'
)

settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_SETTINGS)
