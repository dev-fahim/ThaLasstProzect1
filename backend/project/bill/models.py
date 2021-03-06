from django.db import models
from menu.models import Menu
from profile_app.models import MainUserProfile
# Create your models here.


class Bill(models.Model):
    user = models.ForeignKey(MainUserProfile, on_delete=models.CASCADE, related_name="bills")

    code = models.PositiveIntegerField()

    discount = models.FloatField()

    def __str__(self):
        return self.user


class BillData(models.Model):
    user = models.ForeignKey(MainUserProfile, on_delete=models.CASCADE, related_name="bill_data")

    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name="bill_data")

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="bills")

    quantity = models.FloatField()

    discount = models.FloatField()

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
