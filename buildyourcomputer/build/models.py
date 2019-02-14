from django.db import models
from django.contrib.auth.models import AbstractUser, User


class CustomUser(AbstractUser):
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.email


class choice(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text
