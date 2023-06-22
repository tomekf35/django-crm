from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateInput, Textarea, TextInput
from .models import Record

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AddRecordForm(forms.ModelForm):
    birth_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Record
        fields = (
            'first_name', 
            'last_name', 
            'birth_date',
            'email', 
            'tel_number', 
            'address', 
            'zip_code',
            'state',
            'country',
        )