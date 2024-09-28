from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phoneNumber = models.CharField(max_length=100, null=True)
    intrest = models.CharField(max_length=100, null=True)
    ratings=models.BigIntegerField(default=0)
    views=models.BigIntegerField(default=0)
    uploads=models.BigIntegerField(default=0)
    gender = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
