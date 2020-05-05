from django.db import models
from django.core.validators import MaxValueValidator

class Customer(models.Model):
    """
    Customer model
    """
    TATA = 'tata'
    MARUTI='maruti'
    MAHINDRA='mahindra'
    BMW='bmw'
    MERCEDES='mercedes'
    CAR_COMPANY_CHOICES = (
        (TATA, 'Tata'),
        (MARUTI, 'Maruti'),
        (MAHINDRA, 'Mahindra'),
        (BMW, 'BMW'),
        # (MERCEDES, 'Mercedes')
    )

    PETROL='petrol'
    DIESEL='diesel'
    NATURAL_GAS='natural_gas'
    HYDROGEN='hydrogen'
    CAR_FUEL_CHOICES = (
        (PETROL, 'Petrol'),
        (DIESEL, 'Diesel'),
        (NATURAL_GAS, 'Natural Gas'),
        (HYDROGEN, 'Hydrogen')
    )

    name = models.CharField(max_length=32)
    mobile_number = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    car_company = models.CharField(max_length=20, choices=CAR_COMPANY_CHOICES)
    car_fuel = models.CharField(max_length=20, choices=CAR_FUEL_CHOICES)
    car_year = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])