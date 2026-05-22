from django.urls import path
from . import views

urlpatterns= [
    path('', views.buy, name= 'buy'),
    path('bk/', views.bk, name= 'bk'),
    path('ng/', views.ng, name= 'ng'),
    path('payment/', views.payment_method, name= 'payment'),
    path('rp/', views.recent_product, name= 'rp')
]