from django.contrib.auth.models import User
from django import forms

class UserRegistration(forms.ModelForm):
    password=forms.CharField(max_length=15, required=True,\
        widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password',)

