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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="warehouse", blank=True)

    def __str__(self):
        return f"{self.name}"

class Shipment(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )

    product = models.ManyToManyField(Product)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    warehouse = models.ManyToManyField(Warehouse)