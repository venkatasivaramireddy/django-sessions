from django.db import models

class CollegeModel(models.Model):
    name = models.CharField(max_length=30)
    phono = models.IntegerField()
    email = models.EmailField(max_length=40,unique=True)
    password = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='images')
    idno = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=30)

