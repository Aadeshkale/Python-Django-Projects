from django.contrib import admin
from .models import Emp

class AdminEmp(admin.ModelAdmin):
    list_display=['id','name','email','loc','sal']



# Register your models here.
admin.site.register(Emp,AdminEmp)

