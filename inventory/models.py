# inventory/models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    # Method to calculate total value
    def total_value(self):
        return self.quantity * self.price
