from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=20)
    business_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
