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
from django.contrib import messages
from user.models import ServerStatus
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from django.core.paginator import Paginator
import math
from django.db import IntegrityError
from .password_generator import login_generator
from django.contrib.auth.hashers import make_password
# Модули доступа
# 5 - максимальный доступ к црм
# 4 - Менеджер по сотрудникам
# 3 - Технический работник по подключению 
# 2 -отдел технической поддержки
# 1 - отдел продаж 
# 0 - доступ запрещен



def auth(request):
    # Если уже авторизован
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST.get('username')
        user_last_name = request.POST.get('userlastname')
        password = request.POST.get('password')

        # Авторизация по username
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, "Неверный логин или пароль")
                return render(request, 'autorization.html')

        # Регистрация по фамилии
        elif user_last_name and password:
            user_login = login_generator(user_last_name)
            data = {
                'username': user_login,
                'password': make_password(password),
                'user_last_name': user_last_name,
                'paper_data': 'Отсуствуют',
                'address': 'Не указан',
                'balance': 0,
                'numberphone':request.POST.get('phone')
            }
            try:
                # Создаем нового пользователя
                new_user = UserModel.objects.create(**data)
                # Авторизация нового пользователя
                auth_user = authenticate(request, username=user_login, password=password)
                if auth_user:
                    login(request, auth_user)
                    return redirect('profile')
                else:
                    messages.error(request, "Не удалось авторизовать нового пользователя")
                    return render(request, 'autorization.html')
            except IntegrityError:
                messages.error(request, "Пользователь с таким логином уже существует")
                return render(request, 'autorization.html')

        else:
            messages.error(request, "Введите все необходимые данные")
            return render(request, 'autorization.html')

    # GET-запрос — просто отображаем страницу авторизации
    return render(request, 'autorization.html')

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
def phonefind(req):
   if req.user.user_acces > 0:
      try:
         apps_phone = Application_from_user.objects.filter(phone__icontains=req.GET.get('phone'))
         data = {'apps':apps_phone}
      
         return render(req,'phoneinf.html',data)
      except:
         return render(req,'phoneinf.html')
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
@csrf_exempt
def userinf(req):
   if req.method == 'POST':
      id = json.loads(req.body).get('user_id')
      try:
         user = UserModel.objects.get(id_userlog=id)
      except UserModel.DoesNotExist:
         return JsonResponse({'error':'Пользоватлеь не найден'})
      try:
         Logs_obj = Logs.objects.filter(user_who=user)
      except Logs.DoesNotExist:
         return JsonResponse({'error':'Логов не обнаруженно'})
      
      return JsonResponse({'Logs':list(Logs_obj.values())})
   
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

@login_required  
def employer(req):
      user = req.user
      applications = user.applications.all()
      AppEmp = Application_from_user.objects.filter(order=None,application_status='opt5',is_active=True)
      AppEmp_len_page = math.ceil(len(AppEmp)/2)
      if req.GET.get('page'):
         page = req.GET.get('page')
      else: page = 1
      pages = Paginator(AppEmp,2)
      get_page = pages.get_page(page)
      tarifs = tarif.objects.all()
      data = {
         'app':applications,
         'AdmApp':get_page,
         'tarifs':tarifs,
         'pages':range(AppEmp_len_page),
         'problem':typeproblem.objects.all()
      }
      return render(req,'workerPanel.html',data)

@login_required
def tarif_settings(req):
   if req.user.user_acces < 4:
      return redirect('/')
   else:
      data = {
      'type':TypeTarif.objects.all(),
      'tarif':tarif.objects.all()
           }
   
      return render(req,'tarif_settings.html',data)
@login_required
def all_settings(req):
   Status = ServerStatus.objects.all()
   data = {'server_status':Status}
   return render(req,'allsettings.html',data)
@login_required
def services(req):
   return render(req,'servieces.html')
@login_required
def base(req):
   html = 'baseinf.html'
   
   if req.user.user_acces >= 4:
      user =req.GET.get('user')
      
      users_models = UserModel.objects.filter(user_acces__gt=0)
      if user:
         user_obj = UserModel.objects.get(username=user)
         Logger = Logs.objects.filter(user_who=user_obj)
         paginator = Paginator(Logger,10)
         pages = math.ceil(len(Logger)/10)
         page_number = req.GET.get('page')
         page = paginator.get_page(page_number)
         
         data = {'logs':page,'num_pages':range(pages),'users':users_models,'user_selected':user}
         
         return render(req,html,data)
      
      
      Logger = Logs.objects.all().order_by('-when')
      
      pages = math.ceil(len(Logger)/10)
      
      paginator = Paginator(Logger,10)
      
      page_number = req.GET.get('page')
      
      page = paginator.get_page(page_number)
      
      data = {'logs':page,'num_pages':range(pages),'users':users_models}
      return render(req,html ,data)
   



   else: return redirect('profile') 
@login_required 
def profileSettings(req):
   return render(req,'settingsprofile.html')


class Emp_app(LoginRequiredMixin,TemplateView):
   
   
   template_name = 'checkAppEmp.html'
   
   def get(self ,req):
      if req.user.user_acces >=3:
         apps = Application_from_user.objects.filter(order__isnull=False)
         users = UserModel.objects.filter(user_acces__gt=0)
         data = {'all_aps':apps,'users':users}
         return render(req,template_name=self.template_name,context=data)
      else : return redirect('profile')
   def post(self,req):
      if req.method == 'POST':
         data = json.loads(req.body)
         id= data.get('id')
         try:
            app = Application_from_user.objects.get(id=id)
            if app.order == None:
               return JsonResponse({'error':'У заявки нет владельца!'})
            else: 
               app.order = None
               app.save()
               return JsonResponse({'resp':'Заявка отозвана'})
         except Application_from_user.DoesNotExist:
            return JsonResponse({'error':'Упс, не смогли найти заявку!'})

        