from django.db import models

from inventory.models import InventoryModel
from purchase.models import NewStockModel
# Create your models here.

class CustomerModel(models.Model):
    customer = models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.customer


class SalesModel(models.Model):
    order_no = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    stock = models.ForeignKey(NewStockModel, on_delete=models.CASCADE, default=None)
    advance = models.IntegerField()
    deal_price = models.IntegerField()
    final_price = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    delivered = models.BooleanField(default=True)
    test_drive_taken = models.BooleanField(default=True)

    def __str__(self):
        return "{}({})".format(self.customer, self.stock)
