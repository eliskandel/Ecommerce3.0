from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    caterogy=models.CharField(max_length=20, default="buyer")
    def __str__(self) -> str:
        return self.username
    