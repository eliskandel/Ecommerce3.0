from django.db import models
from user.models import User

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100, null=False)
    description=models.TextField()
    price=models.FloatField(null=False, blank=False)
    seller=models.ForeignKey(User, on_delete=models.CASCADE)
    stock_quantity=models.IntegerField(default=0)
    rating= models.FloatField(default=5)
    def __str__(self) -> str:
        return self.name