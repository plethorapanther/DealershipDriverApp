from django.db import models

# Create your models here.

class TripEntry(models.Model):


    driverName = models.CharField("Driver Name", max_length=200)
    date = models.CharField("Date", max_length=200)
    driverAddress = models.CharField("Driver Address", max_length=200)
    vin = models.CharField("VIN #", max_length=17)
    managerName = models.CharField("Manager Name", max_length=200)
    stockNum = models.CharField("Stock Number", max_length=200)
    codriver = models.CharField("Codriver", max_length=200. blank - True)
    milesDriven = models.CharField("Miles Driven", max_length=200)
    description = models.TextField(blank = True)

