from django.db import models
from django.contrib.auth.models import User

class Juice(models.Model):
    name = models.CharField(max_length=128, unique=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Sale(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    is_completed = models.BooleanField(default=False)

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    juice = models.ForeignKey(Juice, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
