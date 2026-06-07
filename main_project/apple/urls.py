from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('building', views.building_form, name= "building"),
    path('login/', views.login_form, name= 'login'),
    path('success/', views.login_success, name= 'success'),
    path('logout/', views.logout_form, name= 'logout'),
    path('middleware/', views.mid, name= 'maddleware'),
]