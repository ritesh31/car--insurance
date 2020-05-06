from django.urls import (re_path)
from rest_framework.routers import SimpleRouter
from .views.customer_view import (CustomerView)


router = SimpleRouter()
# router.register('customer', CustomerView, basename='customer')

urlpatterns = [
    re_path(r'^customer/(?P<id>\w+)$', CustomerView.as_view(), name='customer_details'),
    re_path('customer/', CustomerView.as_view(), name='customer')
] + router.urls
