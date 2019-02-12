from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    priority = models.IntegerField(null=True)

    def __str__(self):
        return self.email


class Product(models.Model):
    class Product(models.Model):
        User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        type = models.CharField(max_length=250)
        title = models.CharField(max_length=350)
        cpu = models.CharField(max_length=250)
        processor = models.CharField(max_length=250)
        ram = models.CharField(max_length=150)
        storage = models.CharField(max_length=150)
        color = models.CharField(max_length=150)
        battery = models.CharField(max_length=150)
        price = models.CharField(max_length=150)

        def __str__(self):
            return self.title
