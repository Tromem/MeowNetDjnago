from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate , login ,logout
from django.views.decorators.csrf import csrf_exempt
from .models import UserModel
from crm.models import Application_from_user
from main.models import typeproblem
from crm.models import city, adres ,Home 
from main.models import tarif
import datetime  
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from main.models import TypeTarif ,tarif 
from django.views.decorators.csrf import csrf_exempt
from crm.views import Logger_decorator 
from crm.models import Logs

# Модули доступа
# 5 - максимальный доступ к црм
# 4 - Менеджер по сотрудникам
# 3 - Технический работник по подключению 
# 2 -отдел технической поддержки
# 1 - отдел продаж 
# 0 - доступ запрещен



def auth(req):
   if req.user.is_authenticated:
     return redirect('profile')
   
   if req.POST:

      username = req.POST['username']
      password = req.POST['password']
      user = authenticate(req,username=username,password = password)
      
      if user is not None:
         login(req,user=user)
         return redirect('profile')  

   return render(req,'autorization.html')

@login_required(login_url='authlogin')
def Profile(req):
   if req.user.is_superuser or req.user.user_acces >=4:
      return redirect('managerpanel')
   elif req.user.user_acces > 0 and req.user.user_acces < 4:
      return redirect('epmloyer')

   if not req.user.Date_of_new_write_off == None:
      if req.user.Date_of_new_write_off >= datetime.date.today():    
         user = req.user
         if user.balance >= user.user_tarif.price:
            user.balance = user.balance - user.user_tarif.price
            user.user_tarif_balance = True
            user.save()
         else:
            user.user_tarif_balance = False
            user.save()
      
   return render(req,'Profile.html')



@login_required
def Admin(req):
   Users = UserModel.objects.filter(user_acces__gt=0).order_by('-user_acces')
   data = {'employers':Users}
   if ( req.user.user_acces >= 4 or req.user.is_superuser == True):
      return render(req,'AdminPanel.html',data)
   else:
      return redirect('/')



@login_required
def settings_emp(req):
   Users = UserModel.objects.all()
   data = {'employers':Users}
  
   if ( req.user.user_acces == 5 or req.user.is_superuser):
      if(req.user.is_superuser == True ):
         
         return render(req,'empsettings.html',data)

      return redirect('main')
   

   return render(req,'empsettings.html',data)


@login_required
def userinf(req):
   if ( req.user.user_acces >= 2 or req.user.is_superuser ):
      problems = {'typeproblem': typeproblem.objects.all}
      return render(req,'userinfAdm.html',problems)
   else:
      return redirect('/')



@login_required
def find_adres(req):
   if ( req.user.user_acces >= 2 or req.user.is_superuser ):
      cities = city.objects.all()
      homes = Home.objects.all()
      adress = adres.objects.all()
      typeInternet = tarif.objects.all()
      data = {
         'city':cities,
         "home":homes,
         'adres':adress,
         'tarif':typeInternet
      }
      
      return render(req,'findadres.html',data)
   
   else:
      return redirect('/')
   
def employer(req):
      user = req.user
      applications = user.applications.all()
      AppEmp = Application_from_user.objects.filter(order=None,application_status='opt5',is_active=True)
      data = {
         'app':applications,
         'AdmApp':AppEmp
      }
      return render(req,'workerPanel.html',data)

@login_required
def tarif_settings(req):
   data = {
      'type':TypeTarif.objects.all(),
      'tarif':tarif.objects.all()
           }
   
   return render(req,'tarif_settings.html',data)
@login_required
def all_settings(req):
   
   return render(req,'allsettings.html')
@login_required
def services(req):
   return render(req,'servieces.html')
@login_required
def base(req):
   if req.user.user_acces >= 4:
      Logger = Logs.objects.all()
      data = {'logs':Logger}
      return render(req,'baseinf.html',data)
   else: return redirect('profile') 
   
  