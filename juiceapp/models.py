from django.db import models

# Create your models here.
class Juice(models.Model):
    name = models.CharField(max_length=128, unique=True)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name

# class Client(models.Model):
#     name = models.CharField(max_length=128, unique=True)
#     email = models.EmailField()

class Sale(models.Model):
    # client = models.ForeignKey(Client)
    juice = models.ForeignKey(Juice)
    date = models.DateField(auto_now=True)

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale)
    juice = models.ForeignKey(Juice)
    quantity = models.IntegerField(default=1)
