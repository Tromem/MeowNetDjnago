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
    path('API-MAKE-APP-FROM-SELLER/',views.make_app),
    path('API-Change-Name/',views.change_name),
    path('API-Change-Password-worker/',views.change_password),
    path('API-Change-work-shift/',views.work_shift),
    path('API-GET-NEW-APP/',views.get_new_app),
    path('API-LOGOUT/',views.logout_view,name='logout'),
    path('API-FIND-APP/',views.find_app),
    path('API-UPDATE-APLICATION/<int:pk>/',views.update_application),
    path('API-MakeUser/',views.make_new_user),
    path('API-TARIF-WORKER/',views.del_change_add_form),
    path('server-status/update/',views.server_status_update),
    path('server-status/reset-selected/',views.server_status_reset_selected),
    path('API-NEW-SUP-APP/',views.new_app_from_user),
    path('Add-balance/',views.add_balance),
    path('Add-app-worker/',views.add_app_from_worker),
    path('get-app-for-user/',views.get_app_when_find)
   
]