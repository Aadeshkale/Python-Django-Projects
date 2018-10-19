from django.urls import path
from django.conf.urls import url
from formapp import views
urlpatterns = [
    url(r'^$',views.home),
    url(r'insert/',views.index),
    url(r'display/',views.dis),
    url(r'update/',views.upd),
    url(r'delete/',views.dele),
]
