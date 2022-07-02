from django.db import models

from supplier.models import SupplierModel
# Create your models here.

class NewStockModel(models.Model):
    order_no = models.IntegerField(primary_key=True)
    sku = models.CharField(max_length=100)
    supplier = models.ForeignKey(SupplierModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sku