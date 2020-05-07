from django.urls import (re_path)
from rest_framework.routers import SimpleRouter
from .views.customer_view import (CustomerView)
from .views.agent_view import (AgentView, AgentLoginView)

router = SimpleRouter()
# router.register('customer', CustomerView, basename='customer')

urlpatterns = [
    re_path(r'^customer/(?P<id>\w+)$', CustomerView.as_view(), name='customer_details'),
    re_path('customer/', CustomerView.as_view(), name='customer'),
    re_path('agent/', AgentView.as_view(), name='agent_create'),
    re_path('login/', AgentLoginView.as_view(), name='agent_login')
] + router.urls
