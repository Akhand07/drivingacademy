from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, ContactUs
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields="__all__"
class ContactusForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields=('name','email','yourQuery')

