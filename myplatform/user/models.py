from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone_number = models.IntegerField()
