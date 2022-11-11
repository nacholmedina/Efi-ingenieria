from django.conf.urls import include
from django.contrib.auth.models import User
from django.urls import path, re_path

from carrera import views

urlpatterns = [
    path('carreras/', views.CarreraList.as_view()),
    path('carreras/(id>\d+)', views.CarreraDetail.as_view()),
]