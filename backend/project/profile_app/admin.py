from django.contrib import admin
from profile_app.models import MainUserProfile, ApplicationMonthlyPayment
# Register your models here.

admin.site.register(MainUserProfile)
admin.site.register(ApplicationMonthlyPayment)
