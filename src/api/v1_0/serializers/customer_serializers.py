from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from customer.models import Customer

class CustomerCreateSerializer(serializers.ModelSerializer):
  """
  Create customer
  """
  class Meta:
      model = Customer
      fields = ('id', 'name', 'mobile_number', 'email', 'car_company', 'car_fuel', 'car_year')

  def create(self, validated_data):
      customer = Customer(
        name=validated_data['name'],
        mobile_number=validated_data['mobile_number'],
        email=validated_data['email'],
        car_company=validated_data['car_company'],
        car_fuel=validated_data['car_fuel'],
        car_year=validated_data['car_year']
      )
      customer.save()
      return customer
      