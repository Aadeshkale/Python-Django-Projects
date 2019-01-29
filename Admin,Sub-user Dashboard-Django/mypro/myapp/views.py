from django.urls import reverse
from django.shortcuts import render,redirect
from django.views import View
from myapp.forms import RegForm,LoginForm,UserForm
from myapp.models import Auser,Guser
from django.contrib import messages
from django.http import HttpResponseRedirect
class IndexView(View):
    # template_name = 'index.html'
    def get(self,request):
        return render(request,'index.html')

class MyFormView(View):
    def get(self,request):
        myform=RegForm()
        return render(request,'reg.html',{'myform':myform})
    def post(self,request):
        myform=RegForm(request.POST)
        if myform.is_valid():
            userid=request.POST['userid']
            password=request.POST['password']
            repassword=request.POST['repassword']
            if password != repassword:
                messages.warning(request,'Password is not match :(')
            elif Auser.objects.filter(userid=userid):
                messages.warning(request,'User is Already Registered :(')
            else:
                myform.save()
                messages.success(request,'User Created Successfully :)')
        else:
            messages.warning(request,'Data is Invalid :(')    
        return HttpResponseRedirect(request.path)
class LoginFormView(View):
    def get(self,request):
        myform=LoginForm()
        return render(request,'login.html',{'myform':myform})
    def post(self,request):
        myform=LoginForm(request.POST)
        if myform.is_valid():
            userid=request.POST['userid']
            password=request.POST['password']
            # if not Auser.objects.filter(userid=userid) or Guser.objects.filter(userid=userid):
            #     messages.warning(request,'User is Not Registered :(')
            if Auser.objects.filter(userid=userid,password=password):
                return redirect('./panel/{}'.format(userid))
            elif Guser.objects.filter(userid=userid,password=password):
                return redirect('./gpanel')
            else:
                messages.warning(request,'User is Not Registered :(')    
        else:
            messages.warning(request,'Data is Invalid :(')    
        return HttpResponseRedirect(request.path)

class PanelView(View):
    def get(self,request,name):
        myform=UserForm()
        ob=Auser.objects.get(userid=name)
        aid=ob.id
        data=Guser.objects.filter(guser_id=aid)
        return render(request,'panel.html',{'myform':myform,'adminuser':name,'data':data})

    def post(self,request,name):
        myform=UserForm(request.POST)
        userid=request.POST['userid']
        if myform.is_valid():
            if Guser.objects.filter(userid=userid):
                messages.warning(request,'User is already exists :(')
            else:
                ob=Auser.objects.get(userid=name)
                aid=ob.id
                userid=request.POST['userid']
                password=request.POST['password']
                Guser.objects.create(
                userid=userid,
                password=password,
                guser_id=aid
                )
                messages.success(request,'User Created Succesfully :)')     
        else:
            messages.success(request,'User is not created :)')
        return HttpResponseRedirect(request.path)

class GpanelView(View):
    def get(self,request):
        return render(request,'gpanel.html')