# appliances/models.py
from django.db import models

class Appliance(models.Model):
    
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specification = models.TextField()
    def __str__(self):
           return f"{self.model} - {self.price}"

class Order(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    delivery_time_window = models.TimeField()