from django.db import models

class Auser(models.Model):
    userid=models.CharField(max_length=20)
    password=models.CharField(max_length=30)

class Guser(models.Model):
    guser=models.ForeignKey(Auser,on_delete=models.CASCADE)    
    userid=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
