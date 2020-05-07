from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, )
from .manager import UserManager

class Agent(AbstractBaseUser):
    
    email = models.EmailField(max_length=255, unique=True, null=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.