from django.db import models

class Emp(models.Model):
    eid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField(max_length=10)
    gender=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    obj=models.Manager()
    class Meta:
        db_table='emp'
        ordering=['email']
    