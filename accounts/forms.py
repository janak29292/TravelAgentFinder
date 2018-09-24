from django import forms
from accounts.models import User, Client, Agent
from datetime import datetime

# class ChangePassword(forms.ModelForm):
#     old_password = forms.CharField(widget=forms.PasswordInput())
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())
#     class Meta():
#         model = User
#         email = {
#             'required': True
#         }
#         fields = ('password',)
#
#     def clean(self):
#         cleaned_data = super(ChangePassword, self).clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#
#         if password != confirm_password:
#             raise forms.ValidationError(
#                 "password and confirm_password does not match"
#                 )

class ChangeName(forms.ModelForm):
    class Meta():
        model=Client
        fields=('first_name','last_name')

class ChangeEmail(forms.ModelForm):
    class Meta():
        model=User
        fields=('email',)

class ChangePhone(forms.ModelForm):
    class Meta():
        model=Client
        fields=('phone',)

class ChangeDateofBirth(forms.ModelForm):
    date_of_birth=forms.DateField(widget=forms.SelectDateWidget(years = range(datetime.today().year, 1930, -1)))
    class Meta():
        model=Client
        fields=('date_of_birth',)

class ChangeAddress(forms.ModelForm):
    class Meta():
        model=Client
        fields=('address',)

class ChangeOccupation(forms.ModelForm):
    class Meta():
        model=Client
        fields=('occupation',)

class ChangeCompany(forms.ModelForm):
    class Meta():
        model=Agent
        fields=('company_name',)
