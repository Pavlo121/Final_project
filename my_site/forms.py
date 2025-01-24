from django import forms
from .models import UserProfile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone', 'email', 'password']


