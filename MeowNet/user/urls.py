
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.auth ,name='authlogin'),
    path('profile',views.Profile ,name='profile'),
    path('sales',views.Sales),
    path('support',views.Support),
    path('manager-panel/',views.Admin ,name='managerpanel'),
    path('manager-panel/test',views.testing_room, name='test'),
    path('manager-panel/users',views.userinf , name='users-stat'),
    path('manager-panel/adres',views.find_adres,name='find_adres')
  
]
