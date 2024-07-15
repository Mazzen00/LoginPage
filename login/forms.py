from django import forms
from .models import LoginModel

class LoginForm(forms.ModelForm):
  class Meta:
    model = LoginModel
    fields = ('email' , 'password')
