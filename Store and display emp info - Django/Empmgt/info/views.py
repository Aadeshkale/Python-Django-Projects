from __future__  import unicode_literals 
from django.shortcuts import render
from django.http import HttpResponse 
from .models import Emp
# Create your views here.
def index(request):
    response=HttpResponse()   # creating http response
    response.write("<html><body>")
    response.write("<h1>Employees:</h1><hr>")
    res=Emp.objects.all()     # retriving all emp info from database
    response.write("<ul>")
    for e in res:
       response.write("<li><a href='info/%d/'>%s</a></li>"%(e.eid,e.name))   # forming link for details  
    response.write("</ul>")
    response.write("</body></html>")
    return response             # returning httpresponse

def details(request,eid):
    response=HttpResponse()    # creating http response
    e=Emp.objects.get(eid=eid) # retriving perticular record
    response.write("<html><body>")
    response.write("<h1>Employee Details of %s:</h1>"%(e.name))
    response.write("<hr>")
    response.write("<h2>Name: %s</h2>"%(e.name))
    response.write("<h2>Email: %s</h2>"%(e.email))
    response.write("<h2>Location: %s</h2>"%(e.loc))
    response.write("<h2>Salary: %s</h2>"%(e.sal))
    response.write("<hr>")
   
    return response

