# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    role_choices = [('Admin', 'Admin'), ('User', 'User')]
    role = forms.ChoiceField(choices=role_choices, required=True, help_text='Select the user role.')
    
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('role',)