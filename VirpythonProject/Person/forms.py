from django import forms

from .models import Person, Registration


class CustomerForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Enter your Name")
    age = forms.IntegerField(min_value=18, label="Enter your age")
    check = forms.BooleanField(required=False, label="Do you want to join us")
    category = forms.ChoiceField(choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Administrator', 'Administrator')])

class PersonComplainForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'body']



class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='Enter your first name')
    last_name = forms.CharField(label='Enter your last name')
    email = forms.EmailField(label='Enter your email')
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registration
        fields = ['firstname', 'lastname', 'email', 'password']



