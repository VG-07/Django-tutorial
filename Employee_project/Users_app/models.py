from django.db import models

# Create your models here.
class users_form(models.Model):
    user_name =models.CharField(max_length=100) 
    last_name =models.CharField(max_length=50)
    Email =models.EmailField(unique=True)