from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=45)
    age  = models.IntegerField()
    gender = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    aadhar = models.IntegerField()
    #address = models.CharField(max_length=90)
    vaccinename = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    zone = models.IntegerField()
    dose = models.IntegerField()
    time = models.DateTimeField()
    
