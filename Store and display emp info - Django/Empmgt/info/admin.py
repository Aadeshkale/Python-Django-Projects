from django.contrib import admin
from .models import Emp
class AdminEmp(admin.ModelAdmin):
    list_display=['eid','name','email','sal','loc']

admin.site.register(Emp) # Register your models here.