from django.conf.urls import url
from mailapp import views
urlpatterns=[
    url(r'^$',views.index),
]