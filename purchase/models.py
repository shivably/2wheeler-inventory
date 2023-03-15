from django.db import models

from supplier.models import SupplierModel
from inventory.models import InventoryModel
# Create your models here.

EXPENSE_TYPE = (
    ("DOCUMENT", "Document"),
    ("MECHANIC", "Mechanic"),
    ("SPARES", "Spares"), 
    ("OTHER", "Other"),
)

class NewStockModel(models.Model):
    order_no = models.IntegerField(primary_key=True)
    sku = models.ForeignKey(InventoryModel, on_delete=models.CASCADE)
    supplier = models.ForeignKey(SupplierModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    number = models.CharField(max_length=100)
    chassis_number = models.CharField(max_length=100)
    engine_number = models.CharField(max_length=100)
    purchase_price = models.IntegerField()
    sale_price = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    registration_date = models.DateField(default=None)
    manufacturing_date = models.DateField(default=None)
    sold = models.BooleanField(default=False)
    noc = models.BooleanField(default=False, null=True)
    noc_date = models.DateField(default=None, null=True)

    def __str__(self):
        return "{}({})".format(self.sku.name, self.number)
    

class ExpenseOnStock(models.Model):
    stock = models.ForeignKey(NewStockModel, on_delete=models.CASCADE)
    price = models.IntegerField()
    type = models.CharField(
        max_length = 20,
        choices = EXPENSE_TYPE,
        default = 'MECHANIC'
    )
    description = models.TextField(max_length=200) 