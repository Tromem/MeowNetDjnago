from django.urls import path , include
from . import views
urlpatterns = [
    path('API-CREATE-WORKER/',views.create_user),
    path('API-GET-CARDS/', views.getcards),
    path('API-DELETE-WORKER/',views.delete_user),
    path('API-SWAP-ROLE/',views.swap_role),
    path('API-GET-USER/',views.get_user_by_id_username),
    path('API-POST-Application/',views.post_aplication),
    path('API-GET-ADRES/',views.get_adres),
    path('API-GET-TECH-INF/',views.get_inf_api),
    path('API-MAKE-APP-FROM-SELLER/',views.make_app)
   
]