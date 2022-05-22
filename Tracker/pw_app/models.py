from django.db import models

class Product(models.Model):
    name= models.CharField(max_length=64)
    description = models.CharField(max_length= 256)
    price = models.IntegerField()
    quantity = models.IntegerField()


    def __str__(self):
        return f"{self.name}"

class Warehouse(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=256)
    phone = models.CharField(max_length=12)
    product = models.ManyToManyField(Product, through='Shipment')


    def __str__(self):
        return f"{self.name}"

class Shipment(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, )
    warehouses = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True,)
