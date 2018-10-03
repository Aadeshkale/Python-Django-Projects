from django.db import models

# Create your models here.
class Emp(models.Model):
    eid=models.AutoField(primary_key=True)   # overidding existing id field
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    loc=models.CharField(max_length=20)
    sal=models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        db_table='empinfo'                   # overiding existing database table name  
        ordering=['-sal']                    # sorting data based on salary in admin site in decending order
        indexes=[
            models.Index(fields=['name'])    # creating indexing on name field
        ] 

