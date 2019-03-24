from django.urls import path
from AppTwo import views


urlpatterns=[

 path('register/',views.register,name='RegisterForm'),

 ]
