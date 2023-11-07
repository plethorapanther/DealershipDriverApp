from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import DriverForm, TripEntryForm
from django.contrib import messages


# Create your views here.
def index(request):
# Render index.html
    return render( request, 'driver_app/index.html')
 
class DriverListView(generic.ListView):
    model = Driver

class DriverDetailView(generic.DetailView):
    model = Driver

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(DriverDetailView, self).get_context_data(**kwargs)
        #get the portfolio's id
        id = int(self.kwargs.get('pk'))
        #get all projects associated with portfolio
        entries = TripEntry.objects.filter(driver_id = self.get_object().id)

        # Create any data and add it to the context
        context['driver_trip_entries'] = entries
        return context

class TripEntryListView(generic.ListView):
    model = TripEntry

class TripEntryDetailView(generic.DetailView):
    model = TripEntry


def createTripEntry(request, driver_id):
    form = TripEntryForm()
    driver = Driver.objects.get(pk=driver_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        trip_data = request.POST.copy()
        trip_data['driver_id'] = driver_id
        
        form = TripEntryForm(trip_data)
        if form.is_valid():
            # Save the form without committing to the database
            trip = form.save(commit=False)
            # Set the portfolio relationship
            trip.driver = driver
            trip.save()

            # Redirect back to the portfolio detail page
            return redirect('driver-detail', driver_id)

    context = {'form': form}
    return render(request, 'driver_app/trip_entry_form.html', context)

def updateTripEntry(request, driver_id, pk):
    
    driver = Driver.objects.get(pk=driver_id)
    project = TripEntry.objects.get(id=pk)
    form = TripEntryForm(instance = project)

    if request.method == 'POST':
        # Create a new dictionary with form data and driver_id
        trip_data = request.POST.copy()
        trip_data['driver_id'] = driver_id
        
        form = TripEntryForm(trip_data, instance = project)
        if form.is_valid():
            # Save the form without committing to the database
            trip = form.save(commit=False)
            # Set the portfolio relationship
            trip.driver = driver
            trip.save()

            # Redirect back to the portfolio detail page
            return redirect('driver-detail', driver_id)
        
    context = {'form': form}
    return render(request, 'driver_app/trip_entry_form.html', context)

def deleteTripEntry(request, driver_id, pk):
    driver = Driver.objects.get(id=driver_id)
    trip = TripEntry.objects.get(id=pk)
    if request.method == "POST":
        trip.delete()
        return redirect('/')
    context = {'trip': trip,
    'driver': driver}
    return render(request, 'portfolio_app/delete_project.html', context)