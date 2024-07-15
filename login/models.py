from django.db import models

# Create your models here.
   
class LoginModel(models.Model):
      email = models.EmailField(max_length=100 , default = 'user' , null = True)
      password = models.CharField(max_length=50)
      
    
      def __str__(self):
        return self.email


