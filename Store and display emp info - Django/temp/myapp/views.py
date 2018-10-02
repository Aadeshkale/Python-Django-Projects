from __future__  import unicode_literals   # to make use of brawoser
from django.shortcuts import render
from django.http import HttpResponse       # to handling http  request from brawoser 
from .models import Emp

def index(request):
    response=HttpResponse()
    response.write("<html><body>\n")
    response.write("<h1>Employee Details:-</<h1>")
    response.write("<hr>")
    elist=Emp.objects.all()

    for e in elist:
        response.write("<a href='myapp/info/%d/'><li>%s</li></a>"%(e.id,e.name))
    response.write("<br></body></html>")
    return response

def details(request,eid="0"):
    response=HttpResponse()
    response.write("<html><body>\n")
    try:
        e=Emp.objects.get(id=eid)
        response.write("<h1>Details of Employee %s</h1>"%(e.name))
        response.write("<h1>Name: %s</h1>"%(e.name))
        response.write("<h1>Email: %s</h1>"%(e.email))
        response.write("<h1>Location: %s</h1>"%(e.loc))
        response.write("<h1>Salary: %s</h1>"%(e.sal))
    except Exception as e:
        response.write("<h1>Employee is not found :(</h1>")  
    response.write("</body></html>")
    return response  
        
        



