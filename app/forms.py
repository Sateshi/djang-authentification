from django import forms
from .models import Member

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ('username', 'password', 'email')