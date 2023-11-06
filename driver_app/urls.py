from django.urls import path
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
#create path to list of all drivers
path('drivers/', views.DriverListView.as_view(), name= 'drivers'),
#create path to a single driver
path('driver/<int:pk>/', views.DriverDetailView.as_view(), name='driver-detail'),
#create path to list of all projects
path('trip_entries/', views.TripEntryListView.as_view(), name= 'trip_entries'),
#create path to a single project
path('trip_entry/<int:pk>/', views.TripEntryDetailView.as_view(), name='trip_entry-detail'),
]
