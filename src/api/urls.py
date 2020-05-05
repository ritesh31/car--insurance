"""
API urls.
"""

from django.urls import (path, include,)

urlpatterns = [
    path('v1.0/', include(('api.v1_0.router', 'api'), namespace='1.0')),
]