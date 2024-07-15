from django.shortcuts import render 

# from rest_framework.views import APIView
# from rest_framework.response import Response
 

# from django.template import loader
# from django.http import HttpResponse

from .models import LoginModel
from .forms import LoginForm

# Create your views here.

def index(request):
  
  if request.method == 'POST':

    form = LoginForm(request.POST)

    if form.is_valid():

      form.save()

  return render(request , 'login/index.html' , {'form' : LoginForm()})

from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

class MyPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
