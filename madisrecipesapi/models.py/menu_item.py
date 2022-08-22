from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    price = models.DecimalField(max_length=7, decimal_places=2)
    food_type = models.CharField(max_length=55)
