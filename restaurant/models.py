from django.db import models
from datetime import datetime


# Create your models here.

class Booking(models.Model) :
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(default=6)
    booking_date = models.DateTimeField(default= datetime.now)

    def __str__(self):
        return self.Name


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)

    def __str__(self):
        return self.title
    
