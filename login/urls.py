from django.urls import path 

from . import views

from django.contrib.auth import views as auth_views
 
urlpatterns = [
path('index/' , views.index),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),


]
