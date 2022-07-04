from django.db import models

from inventory.models import InventoryModel
# Create your models here.

class SalesModel(models.Model):
    order_no = models.IntegerField(primary_key=True)
    customer = models.CharField(max_length=100)
    sku = models.ForeignKey(InventoryModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer
