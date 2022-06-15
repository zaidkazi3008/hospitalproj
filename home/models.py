from datetime import date, datetime
from django.db import models


# Create your models here.
class Form(models.Model):

    name = models.CharField(max_length=122 ,default='')
    phone = models.CharField(max_length=12 ,default='')
    age = models.CharField(max_length=122 ,default='')
    gender = models.CharField(max_length=100 ,default='')
    address = models.CharField(max_length=122 ,default='' )
    pain= models.TextField(max_length=122 ,default='')
    bleeding= models.TextField(max_length=122 ,default='')
    burning= models.TextField(max_length=122 ,default='')
    itching= models.TextField(max_length=122 ,default='')
    constipation= models.TextField(max_length=122 ,default='')
    prolepse= models.TextField(max_length=122 ,default='')
    anus= models.TextField(max_length=122 ,default='')
    othercom= models.TextField(max_length=122 ,default='')  
    otherhis= models.CharField(max_length=200 ,default='')
    digitalex=models.CharField(max_length=200 ,default='')
    pathological=models.CharField(max_length=122 ,default='')
    anesthesia=models.CharField(max_length=200 ,default='')
    diagnosis=models.CharField(max_length=200 ,default='')
    estimate=models.CharField(max_length=122 ,default='')

    


    def __str__(self):
        return self.name
