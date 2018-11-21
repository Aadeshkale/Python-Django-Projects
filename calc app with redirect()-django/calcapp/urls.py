from django.conf.urls import url
from calcapp import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^opration/',views.opration),
    url(r'^add',views.add),
    url(r'^sub',views.sub),
    url(r'^mul',views.mul),
    url(r'^div',views.div),
]
 