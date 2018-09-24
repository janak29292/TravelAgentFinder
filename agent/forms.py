from django import forms
from accounts.models import User, Client, Agent
from agent.models import EnqTourReply, EnqHotelReply, EnqTrainReply, EnqAirReply, EnqBusReply, EnqVisaReply, EnqCarReply, EnqInsrnceReply
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

class AgentForm(forms.ModelForm):
    class Meta():
        model = Agent
        fields =('company_name',)



#Reply forms

class EnqTourReplyForm(forms.ModelForm):
    class Meta():
        model = EnqTourReply
        fields = ('names_of_cities','budget','additional_information')

class EnqHotelReplyForm(forms.ModelForm):
    class Meta():
        model =EnqHotelReply
        fields = ('names_of_hotels','prices_of_hotels','location_of_hotels','additional_information')

class EnqTrainReplyForm(forms.ModelForm):
    class Meta():
        model = EnqTrainReply
        fields = ('names_of_trains','train_timings','days_of_running','fares','additional_information')

class EnqAirReplyForm(forms.ModelForm):
    class Meta():
        model = EnqAirReply
        fields = ('flight_names','dates_and_timings','fares','additional_information')

class EnqBusReplyForm(forms.ModelForm):
    class Meta():
        model = EnqBusReply
        fields = ('bus_timings','fares','additional_information')

class EnqVisaReplyForm(forms.ModelForm):
    class Meta():
        model = EnqVisaReply
        fields = ('charges','additional_information')

class EnqCarReplyForm(forms.ModelForm):
    class Meta():
        model = EnqCarReply
        fields = ('vehicles_available','charges','additional_information')

class EnqInsrnceReplyForm(forms.ModelForm):
    class Meta():
        model = EnqInsrnceReply
        fields = ('insurance_coverage','charges','additional_information')
