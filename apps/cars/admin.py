from django.contrib import admin
from apps.cars.models import Car,Category,Description

# Register your models here.
admin.site.register(Car)
admin.site.register(Category)
admin.site.register(Description)
