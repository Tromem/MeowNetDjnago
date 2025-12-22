from django.urls import path , include
from . import views
urlpatterns = [
    path('API-CREATE-WORKER/',views.create_user)
    
]