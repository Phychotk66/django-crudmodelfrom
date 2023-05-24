from django.db import models

# Create your models here.
class Vser (models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=25)
    password = models.CharField( max_length=8)
    massages = models.CharField(max_length=500)
    

