from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
#from .forms import DriverForm, TripEntryForm
from django.contrib import messages


# Create your views here.
def index(request):
# Render index.html
    return render( request, 'driver_app/index.html')
 
class DriverListView(generic.ListView):
    model = Driver

class DriverDetailView(generic.DetailView):
    model = Driver

class TripEntryListView(generic.ListView):
    model = TripEntry
    
class TripEntryDetailView(generic.DetailView):
    model = TripEntry
