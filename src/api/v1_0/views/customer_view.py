from rest_framework.generics import (ListCreateAPIView)
from customer.models import Customer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.v1_0.serializers.customer_serializers import CustomerCreateSerializer

class CustomerView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateSerializer

    def get_queryset(self):
        if 'id' in self.kwargs:
            queryset = Customer.objects.filter(id=self.kwargs['id'])
            return queryset
        else:
            queryset = Customer.objects.all()
            return queryset