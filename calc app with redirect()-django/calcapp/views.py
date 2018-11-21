from django.shortcuts import render,redirect
from calcapp.forms import Cal
from django.http import HttpResponse
# Create your views here.
def index(request):
    myform=Cal()
    return render(request,'index.html',{'myform':myform})

def opration(request):
   global i
   global j
   x=int(request.GET['num1'])
   y=int(request.GET['num2'])
   btn=request.GET['but']
   i=x 
   j=y
   if btn =='add' :
       return redirect(add)
   if btn =='sub' :
       return redirect(sub)
   if btn =='mul' :
       return redirect(mul)
   if btn =='div' :
       return redirect(div)      

def add(request):
    z=i+j
    s='Addition is:',z
    return HttpResponse(s)

def sub(request):
    z=i-j
    s='Substarction is:',z
    return HttpResponse(s)
def mul(request):
    z=i*j
    s='Addition is:',z
    return HttpResponse(s)
def div(request):
    z=i//j
    s='division is:',z
    return HttpResponse(s)
