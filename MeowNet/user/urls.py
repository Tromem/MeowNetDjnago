
from django.urls import path , include
from . import views

urlpatterns = [
    path('auth',views.auth ,name='authlogin'),
    path('auth/profile',views.Profile),
    path('auth/Sales',views.Sales),
    path('auth/Support',views.Support),
    path('auth/Admin',views.Admin),
]
