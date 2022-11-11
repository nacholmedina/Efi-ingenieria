from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from registro import views

urlpatterns = [
    path('registro/', views.RegistroList.as_view()),
    path('registro/(<id>\d+)', views.RegistroDetail.as_view()),
]