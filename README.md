# django-rest-framework-msgpack

[![Build Status](https://travis-ci.org/raverat/django-rest-framework-msgpack.svg?branch=master)](https://travis-ci.org/raverat/django-rest-framework-msgpack)
[![codecov](https://codecov.io/gh/raverat/django-rest-framework-msgpack/branch/master/graph/badge.svg)](https://codecov.io/gh/raverat/django-rest-framework-msgpack)

# Requirements

* Python (2.7)
* Django (1.8, 1.9, 1.10, 1.11)
* Django Rest Framework (3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8)

# Installation

Add `'rest_framework_msgpack.renderers.MsgPackRenderer'` to `'DEFAULT_RENDERER_CLASSES'` in django-rest-framework configuration.

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        ...,
        'rest_framework_msgpack.renderers.MsgPackRenderer',
    )
}
```

Or use it directly in your views

```python
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_msgpack.renderers import MsgPackRenderer


class UserCountView(APIView):
    """
    A view that returns the count of active users in msgpack
    """
    renderer_classes = (MsgPackRenderer,)
    
    def get(self, request, format=None):
        user_count = User.objects.filter(active=True).count()
        content = {'user_count': user_count}
        return Response(content)
```

Add `'rest_framework_msgpack.parsers.MsgPackParser'` to `'DEFAULT_PARSER_CLASSES'` in django-rest-framework configuration.

```python
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        ...,
        'rest_framework_msgpack.parsers.MsgPackParser',
    )
}
```

Or use it directly in your views

```python
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_msgpack.parsers import MsgPackParser

class ExampleView(APIView):
    """
    A view that can accept POST requests with msgpack content.
    """
    parser_classes = (MsgPackParser,)
    
    def post(self, request, format=None):
        return Response({'received data': request.data})
```
