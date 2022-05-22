from django.contrib import admin
from .models import Product, Warehouse, Shipment

# Register your models here.

admin.site.register([Product, Warehouse, Shipment])
