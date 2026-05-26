
from django.urls import path , include
from user.views import Profile ,auth,services,profileSettings

from . import views
urlpatterns = [
    path('',views.main,name='main'),
    path('profile',Profile ,name='profile'),
    path('user/auth/',auth ,name='authlogin'),
    path('profile/services',services,name="services"),
    path('profile/settings',profileSettings,name='settingsuser'),
    
    
]
