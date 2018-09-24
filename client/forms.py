from django import forms
from accounts.models import User, Client
from client.models import (EnqTour, EnqHotel, EnqTrain, EnqAir, EnqBus, EnqVisa, EnqCar, EnqInsrnce,
                            EnqTourArchiv, EnqHotelArchiv, EnqTrainArchiv, EnqAirArchiv, EnqBusArchiv, EnqVisaArchiv, EnqCarArchiv, EnqInsrnceArchiv)
from datetime import datetime

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        email = {
            'required': True
        }
        fields = ('username','email','password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
                )

class ClientForm(forms.ModelForm):
    date_of_birth=forms.DateField(widget=forms.SelectDateWidget(years = range(datetime.today().year, 1930, -1)))
    class Meta():
        model = Client
        fields = ('first_name','last_name','phone','address','occupation','date_of_birth')


#Enquiry Forms

class EnqTourForm(forms.ModelForm):
    tour_start_date=forms.DateField(widget=forms.SelectDateWidget())
    tour_end_date=forms.DateField(widget=forms.SelectDateWidget())
    class Meta():
        model = EnqTour
        fields = ('country','cities_to_travel','tour_start_date','tour_end_date','maximum_price','minimum_price','number_of_adults','number_of_children','number_of_infants','additional_information')

class EnqHotelForm(forms.ModelForm):
    stay_from=forms.DateField(widget=forms.SelectDateWidget())
    stay_upto=forms.DateField(widget=forms.SelectDateWidget())
    class Meta():
        model = EnqHotel
        fields = ('location','stay_from','stay_upto','number_of_adults','number_of_children','number_of_infants','maximum_price','minimum_price','number_of_rooms_required','additional_information')

class EnqTrainForm(forms.ModelForm):
    date_of_travel=forms.DateField(widget=forms.SelectDateWidget())
    class Meta():
        model = EnqTrain
        fields = ('tour_type','travel_start_location','destination','date_of_travel','number_of_adults','number_of_children','number_of_infants','catagory','additional_information')

class EnqAirForm(forms.ModelForm):
    date_of_travel=forms.DateField(widget=forms.SelectDateWidget())
    class Meta():
        model = EnqAir
        fields = ('tour_type','travel_start_location','destination','date_of_travel','number_of_adults','number_of_children','number_of_infants','catagory','additional_information')

class EnqBusForm(forms.ModelForm):
    date_of_travel=forms.DateField(widget=forms.SelectDateWidget())
    class Meta():
        model = EnqBus
        fields = ('tour_type','travel_start_location','destination','date_of_travel','number_of_adults','number_of_children','number_of_infants','catagory','additional_information')

class EnqVisaForm(forms.ModelForm):
    class Meta():
        model = EnqVisa
        fields = ('service','additional_information')

class EnqCarForm(forms.ModelForm):
    book_from=forms.DateField(widget=forms.SelectDateWidget())
    book_upto=forms.DateField(widget=forms.SelectDateWidget())
    class Meta():
        model = EnqCar
        fields = ('tour_type','type_of_vehicle','book_from','book_upto','travel_start_location','destination','number_of_vehicles_required','additional_information')

class EnqInsrnceForm(forms.ModelForm):
    class Meta():
        model = EnqInsrnce
        fields = ('country','type_of_insurance','number_of_people','ages_of_people','travel_start_location','destination','additional_information')

class TourRating(forms.ModelForm):
    class Meta():
        model = EnqTourArchiv
        fields = ('rating',)

class HotelRating(forms.ModelForm):
    class Meta():
        model = EnqHotelArchiv
        fields = ('rating',)

class TrainRating(forms.ModelForm):
    class Meta():
        model = EnqTrainArchiv
        fields = ('rating',)

class AirRating(forms.ModelForm):
    class Meta():
        model = EnqAirArchiv
        fields = ('rating',)

class BusRating(forms.ModelForm):
    class Meta():
        model = EnqBusArchiv
        fields = ('rating',)

class VisaRating(forms.ModelForm):
    class Meta():
        model = EnqVisaArchiv
        fields = ('rating',)

class CarRating(forms.ModelForm):
    class Meta():
        model = EnqCarArchiv
        fields = ('rating',)

class InsrnceRating(forms.ModelForm):
    class Meta():
        model = EnqInsrnceArchiv
        fields = ('rating',)
