from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class InventoryFoodName(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventory_food_names')

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class InventoryFoodIN(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventory_foods_in')

    name = models.ForeignKey(InventoryFoodName, on_delete=models.CASCADE, related_name='inventory_foods_in')
    quantity = models.FloatField()

    price_per = models.FloatField()

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class InventoryFoodOUT(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventory_foods_out')

    name = models.ForeignKey(InventoryFoodIN, on_delete=models.CASCADE, related_name='inventory_foods_out')
    quantity = models.FloatField()

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def in_stock(self):
        if self.name.quantity >= self.quantity:
            return self.name.quantity - self.quantity
        return 0
