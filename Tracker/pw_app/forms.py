from django import forms
from django.db import models
from django.forms import fields
from .models import Product, Warehouse, Shipment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "quantity" ]

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ["name", "location", "phone", "product"]

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ["products", "warehouses"]