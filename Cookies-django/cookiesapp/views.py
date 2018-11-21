from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')

def create(request):
    if  request.COOKIES.get('color'):
        msg="Cookie is already exists "
        return render(request,'created.html',{'msg':msg})
    else:
        msg="Favriote Color is red - cookie is created"
        response = render(request,'created.html',{'msg':msg})
        response.set_cookie('color','red')
        return response

def count(request):
    if request.COOKIES.get('visit'):
       cnt=int(request.COOKIES.get('visit'))
       cnt=cnt+1
       msg="Your {} Time visiting this site....".format(cnt)
       response= render(request,'created.html',{'msg':msg})
       response.set_cookie('visit',str(cnt))
       return response 
    else:
        msg="Your First Time visiting this site...."
        response=render(request,'created.html',{'msg':msg})
        response.set_cookie('visit','1')
        return response


def delete(request):
    if request.COOKIES.get('color'):
        response=render(request,'created.html',{'msg':'Cookie deleted successfully'})
        response.delete_cookie('color')
        return response
    else:
        msg="Cookie Does not exists "
        return render(request,'created.html',{'msg':msg})          