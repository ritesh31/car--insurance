from rest_framework.generics import (CreateAPIView, ListAPIView)
from customer.models import Customer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.v1_0.serializers.customer_serializers import CustomerCreateSerializer

class CustomerView(CreateAPIView, ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)