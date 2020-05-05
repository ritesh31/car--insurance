from django.urls import (path)
from rest_framework.routers import SimpleRouter
from .views.customer_view import (CustomerView)


router = SimpleRouter()
# router.register('customer', CustomerView, basename='customer')

urlpatterns = [
    path('customer/', CustomerView.as_view(), name='customer')
] + router.urls
