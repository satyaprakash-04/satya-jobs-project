from django.conf.urls import url
from sjobapp import views

urlpatterns = [
    url('$', views.jobhome),
    url('bljobs/', views.b_lurujobiinfo),
    url('bbsrjob/', views.bbsrjobinfo),
    url('hydjobs/', views.hydjobinfo),
    url('punejobs', views.punejobinfo),
]