from django.shortcuts import render
from mailapp.forms import Send 
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import Settings
from django.core import mail
# Create your views here.
def index(request):
    if request.method=='POST':
        myform=Send(request.POST)
        if myform.is_valid():
            name=request.POST.get('name','')
            subject=request.POST.get('subject','')
            comment=request.POST.get('comment','')
            mail.send_mail(subject,comment,name,['ur destination email address here '],fail_silently=False)
            messages.info(request,'Email Sent Sucessfully')
        else:
            messages.warning(request,'Data is Invalid , Email is not sent')    
        
        return HttpResponseRedirect(request.path_info)    
    else:
        myform=Send()
        return render(request,'index.html',{'myform':myform})    