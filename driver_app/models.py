# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.
class Driver(models.Model):
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField("Name", max_length=200)
    address = models.CharField("Address", max_length=200)
    email = models.CharField("Email Address", max_length=200)

        #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('driver-detail', args=[str(self.id)])
    
class TripEntry(models.Model):

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, default = None)

    driverName = models.CharField("Driver Name", max_length=200)
    date = models.CharField("Date", max_length=200)
    driverAddress = models.CharField("Driver Address", max_length=200)
    vin = models.CharField("VIN #", max_length=17)
    managerName = models.CharField("Manager Name", max_length=200)
    stockNum = models.CharField("Stock Number", max_length=200)
    codriver = models.CharField("Codriver", max_length=200, blank = True)
    milesDriven = models.CharField("Miles Driven", max_length=200)
    description = models.TextField(blank = True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, default = None)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.driverName

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('tripentry-detail', args=[str(self.id)])


class Event(models.Model):
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
 
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

 
    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))
 
    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending time must come after starting time')
 

