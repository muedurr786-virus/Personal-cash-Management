from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *


# User Registration Form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserCreate
        fields = ["username", "email", "password1", "password2"]
        
        
class AuthForm(AuthenticationForm):
    class Meta:
        model = UserCreate
        fields = ["username", "password1"]


# Profile Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ["full_name", "occupation", "address", "image"]


# Add Cash Form
class AddCashForm(forms.ModelForm):
    class Meta:
        model = AddcashModel
        fields = ["amount", "source", "description"]


# Expend Cash Form
class ExpendForm(forms.ModelForm):
    class Meta:
        model = ExpaendModel
        fields = ["amount", "description"]
