from django.conf.urls import url
from cookiesapp import views 
urlpatterns = [
    url(r'^$',views.index),
    url(r'^create/',views.create),
    url(r'^delete/',views.delete),
    url(r'^count',views.count),
]
