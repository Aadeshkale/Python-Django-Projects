from django.shortcuts import render
from formapp.models import Emp
from formapp.forms import EmpFrom ,Empupd ,EmpDel
from django.http import HttpResponse

# Create your views here.

def home(request):
        return render(request,'home.html')


def index(request):
    if request.method=='POST':
        myform=EmpFrom(request.POST)
        if myform.is_valid():
            myform.save()
            return HttpResponse('Data inserted Successfully ')
        else:    
            return HttpResponse('Data not inserted')
    else:
        myform=EmpFrom()
        return render(request,'index.html',{'myform':myform})    

def dis(request):
    data=Emp.obj.all()
    return render(request,'display.html',{'data':data})

def upd(request):
    if request.method=='POST':
        myform=Empupd(request.POST)
        ids=request.POST.get('ids','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        gender=request.POST.get('gender','')
        city=request.POST.get('city','')
        if myform.is_valid():
           try:
                if Emp.obj.get(eid=ids):
                   emp=Emp.obj.get(eid=ids)
                   emp.name=name
                   emp.email=email
                   emp.phone=phone
                   emp.gender=gender
                   emp.city=city
                   emp.save()
                   return HttpResponse('Data updated Successfully ')
           except Exception as e:
               return HttpResponse('Emp id is invalid')         
        else:    
            return HttpResponse('Data is invalid')
    else:
        myform=Empupd()
        return render(request,'update.html',{'myform':myform})

def dele(request):
    if request.method=='POST':
        myform=EmpDel(request.POST)
        ids=request.POST.get('ids','')
        if myform.is_valid():
           try:
                if Emp.obj.get(eid=ids):
                    emp=Emp.obj.get(eid=ids)
                    emp.delete()
                    return HttpResponse('Data Deleted Successfully ')
           except Exception as e:
               return HttpResponse('Emp id is invalid')         
        else:    
            return HttpResponse('Data is invalid')
    else:
        myform=EmpDel()
        return render(request,'delete.html',{'myform':myform})