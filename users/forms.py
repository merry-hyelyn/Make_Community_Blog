from django import forms
from .models import User

class UserForm(forms.ModelForm):
    model = User
    feild = ['username', 'password','']