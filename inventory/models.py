from django.db import models

PRODUCT_TYPE = (
    ("2_WHEELER", "2 Wheeler"),
    ("4_WHEELER", "4 Wheeler"),
    ("OTHER", "Other"),
)

class InventoryModel(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length = 20,
        choices = PRODUCT_TYPE,
        default = '2_WHEELER'
    )
    available_quantity = models.SmallIntegerField(default=0)
    def __str__(self):
        return self.name
