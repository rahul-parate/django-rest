from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Profile(User):

	phone = models.CharField(max_length=100)
	address = models.CharField(max_length=300)
	name = models.CharField(max_length=200)
