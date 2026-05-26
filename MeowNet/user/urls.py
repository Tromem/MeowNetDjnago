
from django.urls import path , include
from . import views

urlpatterns = [
    
    
    path('manager-panel/',views.Admin ,name='managerpanel'),
    path('manager-panel/settings/emp',views.settings_emp, name='emp'),
    path('manager-panel/users',views.userinf , name='users-stat'),
    path('manager-panel/adres',views.find_adres,name='find_adres'),
    path('agent-panel/',views.employer,name='epmloyer'),
    path('manager-panel/settings/tarifs',views.tarif_settings,name='TarifSettings'),
    path('manager-panel/settings/AllSettings',views.all_settings,name='Allsettings'),
    path('manager-panel/settings/base',views.base, name='base'),
    path('manager-panel/emp/apps',views.Emp_app.as_view(),name='Empapps'),
    path('agent-panel/phones',views.phonefind,name='phones')
   
    
  
]
