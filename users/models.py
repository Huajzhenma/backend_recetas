from django.db import models

# Create your models here.
class User(models.Model):
    username  = models.CharField(max_length= 70)
    email = models.EmailField()
    password = models.TextField()
    gender = models.CharField(max_length=15)
    
    
    

    