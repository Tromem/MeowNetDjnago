
from django.urls import path , include
from . import views

urlpatterns = [
    path('auth',views.auth ,name='authlogin'),
    path('auth/profile',views.Profile ,name='profile'),
    path('sales',views.Sales),
    path('support',views.Support),
    path('admin',views.Admin),
    path('admin/test',views.testing_room, name='test')
]
