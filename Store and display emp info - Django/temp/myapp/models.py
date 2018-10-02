from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    loc=models.CharField(max_length=20)
    sal=models.IntegerField()
    
    def __str__(self):
        return self.name
    class Meta:
        ordering=['sal']


    
