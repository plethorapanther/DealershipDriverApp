from django.forms import ModelForm
from .models import Driver, TripEntry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create class for driver form
class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields =('address', 'email')

#create class for portfolio form
class TripEntryForm(ModelForm):
    class Meta:
        model = TripEntry
        fields =('driverName', 'date', 'driverAddress', 'vin', 'managerName', 'stockNum', 'codriver', 'milesDriven', 'description')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)