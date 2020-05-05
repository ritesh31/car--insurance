from django.contrib import admin
from django.conf import settings
from django.urls import (path, re_path, include)
from django.views.static import serve

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]

if not settings.DEBUG:
    urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), ]