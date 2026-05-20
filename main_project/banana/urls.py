from django.urls import path
from . import views

urlpatterns= [
    path('', views.contract, name= 'contract'),
    path('time/', views.time, name= 'time'),
]