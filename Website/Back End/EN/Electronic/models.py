from django.db import models
from django.contrib.auth.models import AbstractUser, User


class CustomUser(AbstractUser):
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.email


class Product(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.CharField(max_length=250)
    title = models.CharField(max_length=350)
    CPU = models.CharField(max_length=250)
    GPU = models.CharField(max_length=250)
    logo = models.CharField(max_length=1000)
    ram = models.CharField(max_length=150)
    storage = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    battery = models.CharField(max_length=150)
    price = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Favorite(models.Model):
    customUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
