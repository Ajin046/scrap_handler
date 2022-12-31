from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class ScrapModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scrap_type = models.CharField(max_length=255)
    first_Name = models.CharField(max_length=255, null=True)
    last_Name = models.CharField(max_length=255, null=True)
    Email = models.CharField(max_length=255, null=True)
    Address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    Pin_code = models.CharField(max_length=255, null=True)
