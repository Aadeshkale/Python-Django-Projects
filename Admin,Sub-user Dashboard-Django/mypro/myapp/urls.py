from django.urls import path,re_path
from myapp.views import IndexView,MyFormView,LoginFormView,PanelView,GpanelView
urlpatterns = [
    re_path(r'^$',IndexView.as_view(),name="index"),
    re_path(r'register',MyFormView.as_view()),
    re_path(r'login',LoginFormView.as_view()),
    re_path(r'panel/(?P<name>\w+)/',PanelView.as_view()),
    re_path(r'gpanel',GpanelView.as_view()),
]
 