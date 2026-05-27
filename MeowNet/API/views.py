from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import hashlib 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from user.models import UserModel
from crm.models import Application_from_user ,tarif
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from user.models import UserModel
from main.models import tarif,TypeTarif
from django.core import serializers
from django.contrib.auth.decorators import login_required
from datetime import datetime
from main.models import typeproblem
from crm.models import *
from django.db.models import Q
from django.contrib.auth import logout
from django.utils.dateparse import parse_datetime
from django.shortcuts import redirect
from datetime import datetime
from crm.views import Logger_decorator
from user import password_generator
from user.models import ServerStatus

@csrf_exempt
@login_required
@Logger_decorator
def create_user(req):
   if req.user.is_superuser or req.user.user_acces == 5:
    if req.method == 'POST':
        data = json.loads(req.body)
        name = data.get('username')
        password = make_password(data.get('password'))
        user_last_name = data.get('user_last_name')
        id = data.get('id')
        user_acces = data.get('access')
        try:
           find_user = UserModel.objects.get(username=name)
           return JsonResponse({'error':f'Пользователь с именем {name} уже существует'})
        except:
         newuser = UserModel.objects.create(username = name,password=password,id_userlog = id,settings ='132' ,user_acces =user_acces,user_last_name=user_last_name)
         newuser.save()


        return JsonResponse({'name': name})
   return JsonResponse({'Response':'Доступ запрещен'})
    

@csrf_exempt
def auth(req):
    
   if req.POST:

      username = req.POST['username']
      password = req.POST['password']
      user = authenticate(req,username=username,password = password)
      
      if user is not None:
         data = {
            'usercheck':user.userhash
         }
         return JsonResponse(data)

   return JsonResponse("Error user not found or invalid password or login")

@csrf_exempt
@login_required
def get_user_by_id_username(req):
  if  req.user.user_acces >= 2:
      if req.method == "POST":
            data = json.loads(req.body)
            
            try:
               user = None
               username = data.get('username')
               print(data.get('id'))

               if username:
                  user = UserModel.objects.get(username=username)
               else :
                  userid = data.get('id')
                  user = UserModel.objects.get(id_userlog=userid)
               
               if user:
                  if req.user.user_acces < 4:
                     pasport = '**********'
                  else:
                     pasport = user.paper_data
                  if user.user_tarif:
                     tarif = user.user_tarif.Tarif_name
                  else:
                     tarif = "Тариф не найден"
                  response = {
                     'pasport':pasport,
                     'userlastname':user.user_last_name,
                     'address':user.address,
                     'balance':user.balance,
                     'username':user.username,
                     'usertarif':tarif,
                     'numberphone':user.numberphone,


                  }
                  
                  return  JsonResponse(response,status=200)
            except UserModel.DoesNotExist:
               return JsonResponse({
                  'status':'error',
                  'message':'Пользователь не найден!'},status=404)
          
   
@csrf_exempt
def getcards(req):
   
   if req.method == "GET":
      
      data = tarif.objects.all()
      raw_json_data = serializers.serialize('json',data)
      cooked_json_data = json.loads(raw_json_data)
      
      return JsonResponse(cooked_json_data,safe=False,  json_dumps_params={'ensure_ascii': False})

@csrf_exempt
@login_required
@Logger_decorator
def delete_user(req):
   if req.user.is_superuser or req.user.user_acces == 5:
      if req.method =='POST':
         jsonraw = json.loads(req.body)
         data = jsonraw.get('userid')
         username = jsonraw.get('username')
         print(jsonraw)
         
         try :
            User = UserModel.objects.get(id=data)
         except:
            User = UserModel.objects.get(username=username)
         if User:         
            User.delete()
         else:
            return JsonResponse({'error':"Пользователь не найден"})
         return JsonResponse({'response ':'Пользователь успешно удален!'})
   else:
      return JsonResponse({'response':'Доступ запрещен'})
   
@csrf_exempt
@login_required
@Logger_decorator
def swap_role(req):
   if req.user.is_superuser or req.user.user_acces == 5:
      jsonBody =json.loads(req.body)
      data_acces = jsonBody.get('acces_swap')
      data_user = jsonBody.get('userid')
      user = UserModel.objects.get(id=data_user)
      if user:
         
         user.user_acces = data_acces
         user.save()
         return JsonResponse({"Response":'Роль успешно изменена!'})
      else:
         return JsonResponse({'error':"Пользователь не найден"})
   else:
      return JsonResponse({"error":'Доступ запрещен!'})

@csrf_exempt
def post_aplication(req):
 if req.method == 'POST':
   
   jsonbody= json.loads(req.body)
   
   if req.user.is_authenticated:
         name = req.user.user_last_name
         phone = req.user.numberphone
         description = "Хочу заменить тариф!"
         adres = req.user.address
         opt = jsonbody.get('opt')
         tarif_field = jsonbody.get('tarif')
         problem = jsonbody.get('problem')
   else:
      name = jsonbody.get('name')
      phone = jsonbody.get('phone')
      description = jsonbody.get('description')
      adres = jsonbody.get('adres')
      opt = jsonbody.get('opt')
      problem = jsonbody.get('problem')
      tarif_field = jsonbody.get('tarif')
   
   if not (problem == None):
      try:
         get_type_problem = typeproblem.objects.get(id=problem)
      except typeproblem.DoesNotExist:
         return JsonResponse({'error':'Модель не найдена, ошибка!'})
   else:
      get_type_problem = None
   if tarif_field:
      try:
         get_tarif = tarif.objects.get(id=tarif_field)
      except tarif.DoesNotExist:
         return JsonResponse({"error":"Тариф не найден"})
   print(get_type_problem)
   if not req.user.is_authenticated:
      user = None 
   else: user = req.user
   
   new_app_without_user = Application_from_user.objects.create(
                                                  comment = description,
                                                  data_create = datetime.now(),
                                                  FromOrder = user,
                                                  user=name,
                                                  phone=phone,
                                                  adres=adres,
                                                  tariffield = get_tarif,
                                                  type_manager_take = opt,
                                                  problem = get_type_problem
                                                  
                                                  
                                                  )
   new_app_without_user.save()
   return JsonResponse({'conf':'Запрос получен'})
   
@csrf_exempt
@login_required
@Logger_decorator
def get_adres(req):
   if req.user.is_superuser or req.user.user_acces > 1:
      if req.method == 'POST':

         data = json.loads(req.body) 
         adres_ = data.get('adres')
         city_ = data.get('city')
         
         if city_ and adres_:
            get_adres_pos = adres.objects.filter(Q(name_adres__icontains=adres_), from_city=city_)
         else:
            get_adres_pos = adres.objects.none()
         
         
         return JsonResponse({'response':list(get_adres_pos.values())},safe=False)
   
@login_required
@csrf_exempt
def get_inf_api(req):
      if req.user.is_superuser or req.user.user_acces > 1:
         if req.method == 'POST':
            
            data = json.loads(req.body)
            citys = data.get('city')
            
            adress_name = data.get('adres')
            
            try:
               adress = adres.objects.get(name_adres=adress_name,from_city=citys)
            
            except adres.DoesNotExist:
               return JsonResponse({'error':'Адрес не найден'})
            
            house = data.get('house')
            try:
               find_house = Home.objects.get(number_home=house,adres_name=adress.id)
            
            except Home.DoesNotExist:
               return JsonResponse({"error":"Адрес не найден"})
            
           
            return JsonResponse({'response':serializers.serialize('json',[find_house]),'problem':find_house.problem}, safe=False, json_dumps_params={'ensure_ascii': False})
@login_required
@csrf_exempt 
@Logger_decorator        
def make_app(req):
   
   body = json.loads(req.body)
   description = body.get('description')
   name = body.get('name')
   phone = body.get('phone')
   adress = body.get('adres')
   get_city = city.objects.get(id=adress[0])
   full_adres =get_city.city_name + " " +adress[1:-1]
   OPTION = body.get('OPTION')
   connection_type_json = body.get('connection_type')
   try:
      conn_type = tarif.objects.get(id=connection_type_json)
   except tarif.DoesNotExist:
      return JsonResponse({'error':'Не найден тариф'}) 
   print(full_adres)
   new_app_without_user = Application_from_user.objects.create(application_status='opt3',
                                                  tariffield = conn_type ,
                                                  comment = description,
                                                  data_create = datetime.now(),
                                                  FromOrder = req.user,
                                                  user=name,
                                                  phone=phone,
                                                  adres=full_adres,
                                                  type_manager_take = OPTION,
                                                  
                                                  
                                                  
                                                  )
   new_app_without_user.save()
   return JsonResponse({'response':'Заявка создана!'})
   
@login_required
@csrf_exempt
@Logger_decorator
def change_name(req):
   if req.user.is_superuser or req.user.user_acces <= 4:
      body = req.body
      data = json.loads(body)
      NewLastName = data.get('newlastName')
      Login = data.get('login')
      try:
         find_user = UserModel.objects.get(id=Login)
         find_user.user_last_name = NewLastName
         find_user.save()
         return JsonResponse({'response':'Имя было успешно изменено!'})
      except UserModel.DoesNotExist:
         
         return JsonResponse({'error':'Пользователь не найден!'})
  
   else: JsonResponse({"error":'Ошибка доступа!'})

@login_required
@csrf_exempt
@Logger_decorator
def change_password(req):
   if req.user.is_superuser or req.user.user_acces <= 4:
      
      body = req.body
      print(body)
      data = json.loads(body)
      NewPassord = data.get('newpassword')
      login = data.get('login')
      
      CodedPassword = make_password(NewPassord)
      
      try:
         
         find_user = UserModel.objects.get(id=login)
         print(find_user)
         find_user.password = CodedPassword
         find_user.save()
         return JsonResponse({'response':'Пароль был успешно изменен!'})
      except UserModel.DoesNotExist:
         return JsonResponse({'error':'Пользователь не найден!'})
      

   
   else:return JsonResponse({"error":'Ошибка доступа!'})


@login_required
@csrf_exempt
def work_shift(req):
   
   user = req.user
   statuswork = user.in_work
   
   if statuswork == False:
      user.in_work = True
      user.save()

   else:

      check = check_user_app(req)
      print(check)
      if not check:
         return JsonResponse({'error':'У вас есть незакрытые заявки!'})
      else: 
         apps = Application_from_user.objects.filter(order = req.user)
         for i in apps:
            i.order = None
            i.save()
         user.in_work = False
         user.save()
         return JsonResponse({'status':'200'},status=200)
   return JsonResponse({'status':'200'},status=200)
@login_required
@csrf_exempt
def get_new_app(req):
   user = req.user 
   if check_user_app(req) == False:
      return JsonResponse({'error':'У вас есть незакрытые заявки!'})
   elif get_apps(req) == False:
      out_apps(req)
      return JsonResponse({"notfound":'Сейчас нет доступных заявок!'})
   else:
      out_apps(req)
      get_apps(req)
      user_new_apss = user.applications.all()
      serial_apps = serializers.serialize('json',user_new_apss)
      cooked = json.loads(serial_apps)
      print(cooked)
      return JsonResponse({'apps':cooked}, safe=False, json_dumps_params={'ensure_ascii': False})

def check_user_app(req):
   user = req.user
   user_app = user.applications.all()
   for i in user_app:
      if req.user.user_acces == 3 and i.application_status == 'opt1':
         return False
      if i.application_status == 'opt3':
         
         return False
   return True
# Модули доступа
# 5 - максимальный доступ к црм
# 4 - Менеджер по сотрудникам
# 3 - Технический работник по подключению 
# 2 -отдел технической поддержки
# 1 - отдел продаж 
# 0 - доступ запрещен
def get_apps(req):
   print(req.user.user_acces)
   if req.user.user_acces > 3:
      return False
   types_emp = {
      2:'opt1',
      3:'opt2',
      1:'opt3'
   }
   user_app_acces =types_emp[req.user.user_acces] 
   if req.user.user_acces == 3:
      none_applications = Application_from_user.objects.filter(Q(application_status='opt3')| Q(application_status='opt1'),order__isnull=True,type_manager_take=user_app_acces)
   else:
      none_applications = Application_from_user.objects.filter(order__isnull=True,application_status='opt3',type_manager_take=user_app_acces)
    
   if none_applications:
         if len(none_applications) >= 2:
            none_applications[0].order = req.user
            none_applications[1].order = req.user
            none_applications[0].first_owner_order == req.user
            none_applications[1].first_owner_order == req.user
            
            none_applications[0].save()
            none_applications[1].save()                    
         else:
            none_applications[0].order = req.user
            none_applications[0].first_owner_order == req.user
            none_applications[0].save()
   else: return False
         
   return True

def out_apps(req):
   user = req.user
   user_app = user.applications.all()
   if user_app:
      for i in user_app:
         i.order = None
         i.save()

def logout_view(req):
    logout(req) 
    return redirect('/') 
@csrf_exempt
def find_app(req):
   id_req  = json.loads(req.body).get('id')
   types_emp = {
      'opt1':2,
      'opt2':3,
      'opt3':1,
      'opt4':4
   }
  
   app = Application_from_user.objects.get(id=id_req)

   user_app_acces = types_emp[app.type_manager_take]
   if(not req.user.user_acces == user_app_acces and req.user.user_acces < 4 ):
      return JsonResponse({'error':'Заявка не по вашему уровню доступа!'})
   if (not app.order == None):
      return JsonResponse({'error':'Сейчас заявка принадлежит другому пользователю!'})
  
   response = model_to_dict(app)
   response['data_create'] = app.data_create
   response['pk'] = app.pk
   date_create = app.data_create
   tariff = tarif.objects.get(id = response['tariffield'])
   response['tariffield'] = tariff.Tarif_name
   print(response)
   app.order = req.user
   app.save()
   return JsonResponse({'app':response},safe=False, json_dumps_params={'ensure_ascii': False})

@login_required
def update_application(req,pk):
   try:
         pk_Key =str(pk)
         pk_Key = pk_Key.zfill(4)
         app = Application_from_user.objects.get(id=pk_Key)
   except Application_from_user.DoesNotExist:
         return JsonResponse({"error":"Заявка не найдена!"}) 
   types_emp = {
      2:'opt1',
      3:'opt2',
      1:'opt3',
      4:'opt4'
   }
   if (req.method == 'POST' 
       and types_emp[req.user.user_acces] == app.type_manager_take or req.user.user_acces >=4):
      
      data = json.loads(req.body)
      
      if req.user.user_acces < 3 and (data.get('application_status') == 'opt5'):
         return JsonResponse({'error':'Нет доступа на статус заявки!'})
         
      app.user = data.get('user', app.user)
      app.phone = data.get('phone', app.phone)
      app.application_status = data.get('application_status', app.application_status)
      

      if not data.get('date_create') == '':
         app.Desired_date = data.get('date_create', app.Desired_date)
     
      app.pasport = data.get('pasport', app.pasport)
      app.adres = data.get('adres', app.adres)
      app.comment = data.get('comment', app.comment)
      

      
      try:
         get_tarif = tarif.objects.filter(Tarif_name=data.get('tariffield')).first()        
         app.tariffield = get_tarif
      except tarif.DoesNotExist:
         return JsonResponse({'error':'Тариф не найден'})
      app.save()
      return JsonResponse({'status':'200'})

@login_required
@csrf_exempt
def make_new_user(req):
   if not req.user.user_acces >= 4:
      return JsonResponse({"error":'В доступе отказано'})

   idapp = json.loads(req.body).get('id')
   app = Application_from_user.objects.get(id=idapp)
   if app.FromOrder:
      user = app.FromOrder
      
      user.user_tarif = app.tariffield
      user.save()
      app.is_active = False
      app.save()
      return JsonResponse({'status':'Пользователь найден'})
   password = password_generator.password_generator()
   
   new_password=make_password(password)
   print(app.user)
   login = password_generator.login_generator(app.user)
   print(password)
   print(login)
   try:
      tariff = tarif.objects.get(Tarif_name=app.tariffield)
   except tarif.DoesNotExist:
      return JsonResponse({'error':'Тариф не найден'})
   try:
           find_user = UserModel.objects.get(username=login)
           return JsonResponse({'error':f'Пользователь с именем {login} уже существует'})
   except:
            app.is_active = False
            app.save()
            New_user = UserModel.objects.create(address=app.adres,                      
      password=new_password,username=login,
      paper_data=app.pasport,
      balance=0,Date_of_last_write_off=datetime.now(),
      user_tarif=tariff,
      numberphone=app.phone,user_last_name=app.user)
            New_user.save()
   return JsonResponse({'status':'200'})
   
   

@login_required   
def del_change_add_form(req):
   if req.user.user_acces >= 4:
      
      if req.method == 'POST':
         data =json.loads(req.body)
         
         nametarif = data.get('nametarif')
         price = data.get('price')
         price_to_connect = data.get('price_to_connect')
         discounts = data.get('discounts')
         time_to_end_discount = data.get('time_to_end_discount')
         Mounts_discount = data.get('Mounts_discount')
         speed = data.get('speed')
         tv_chanels = data.get('tv_chanels')
         typetarif = data.get('typetarif')

         dict_data = {
            'Tarif_name':nametarif,
            'price':price,
            'price_to_connect':price_to_connect,
            'discounts':discounts,
            'time_to_end_discount':time_to_end_discount,
            'Mounts_discount':Mounts_discount,
            'in_archive':False,
            'speed':speed,
            'typetarif':TypeTarif.objects.get(id=typetarif),
            'tv_chanels':tv_chanels,
         }
         new_tarif = tarif.objects.create(**dict_data)
         
         return JsonResponse({'status':200})
      
      elif req.method == 'PATCH':
         data = json.loads(req.body)
         id = data.get('change_tarif_id')
         try:
            tarif_s = tarif.objects.get(id=id)
            
            tarif_s.Tarif_name = data.get('nametarif',tarif_s.Tarif_name)
            tarif_s.price = data.get('price',tarif_s.price)
            tarif_s.price_to_connect = data.get('price_to_connect',tarif_s.price_to_connect)
            tarif_s.discounts = data.get('discounts',tarif_s.discounts)
            tarif_s.time_to_end_discount = data.get('time_to_end_discount',tarif_s.time_to_end_discount)
            tarif_s.Mounts_discount = data.get('Mounts_discount',tarif_s.Mounts_discount)
            tarif_s.speed = data.get('speed',tarif_s.speed)
            tarif_s.tv_chanels = data.get('tv_chanels',tarif_s.tv_chanels)
            tarif_s.typetarif = TypeTarif.objects.get(id=(data.get('typetarif',tarif_s.typetarif.id)))
            tarif_s.save()
            return JsonResponse({'status':200}) 
         except tarif.DoesNotExist:
            return JsonResponse({"error":'Тариф не найден'})
         
         
      
      elif req.method == 'DELETE':
         data = json.loads(req.body)
         id = data.get('tarif-id')
         print(id)
         type_work = data.get('typework')
         try:
            tarif_s = tarif.objects.get(id=id)
            print(type_work)
            if type_work == True:
               tarif_s.in_archive = True
               tarif_s.save()
               return JsonResponse({'status':200})
            else: 
               tarif_s.in_archive = False
               tarif_s.save()
               return JsonResponse({'status':200})
            
           
         except tarif.DoesNotExist:
            return JsonResponse({"error":'Тариф не найден'})

      
      else: return JsonResponse({'error':'Неизвестный метод запроса!'})
  
   else: return JsonResponse({'error':'В доступе отказано!'})

def server_status_update(req):
   if req.method == 'POST':
        
        try:
            data = json.loads(req.body)
            status_value = data.get('status')
            tech_inf = data.get('Tech_inf')
            for_who = data.get('for_who')
            time_to_end_str = data.get('time_to_end')
            
            # Проверка на обязательные поля
            if status_value is None or not tech_inf or not time_to_end_str:
                return JsonResponse({'error': 'Обязательные поля не заполнены'}, status=400)

            # Получаем или создаём объект ServerStatus
            server_status, created = ServerStatus.objects.get_or_create(for_who=for_who)

            server_status.status = status_value
            server_status.Tech_inf = tech_inf
            server_status.for_who = for_who if for_who else ''
            
            server_status.time_to_end = parse_datetime(time_to_end_str)
            print(server_status.status)
            server_status.save()

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

   return JsonResponse({'error': 'Метод не разрешен'}, status=405)
def server_status_reset_selected(req):
   if req.method == 'POST':
        try:
            data = json.loads(req.body)
            ids = data.get('ids', [])

            if not ids:
                return JsonResponse({'error': 'Нет выбранных отключений'}, status=400)

            # Фильтруем по id и сбрасываем поля
            server_statuses = ServerStatus.objects.filter(id__in=ids)
            if not server_statuses.exists():
                return JsonResponse({'error': 'Выбранные отключения не найдены'}, status=404)

            server_statuses.update(status=False, Tech_inf='', for_who='', time_to_end=None)

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

   return JsonResponse({'error': 'Метод не разрешен'}, status=405)
@login_required
@csrf_exempt
def new_app_from_user(req):
   data = json.loads(req.body)
   textproblem = data.get('text')
   if(req.user.user_tarif):
      tarif_field = req.user.user_tarif
   else:
      tarif_field =  None 
   data = {
      'comment': textproblem,
      'FromOrder':req.user,
      'adres':req.user.address,
      'phone':req.user.numberphone,
      'tariffield':tarif_field,
      'type_manager_take':'opt1',
      'pasport':req.user.paper_data,


   }
   try:
      techapp = Application_from_user.objects.create(**data)
   except Exception as ex:
      return JsonResponse({'error':str(ex)})
   return JsonResponse({'response':'Заявка была успешно отправлена, ожидайте звонка!'})
@login_required
@csrf_exempt
def add_balance(req):
   money = 1000
   req.user.balance = req.user.balance + money
   req.user.save()

   Logs.objects.create(text=f'Пользователь {req.user.username}, с id {req.user.id_userlog} пополнил баланс на сумму:{money} в {datetime.now()} по местному времени',
                       who=req.user
                       )
   return JsonResponse({'response':'Баланс был обновлен!'})
@login_required
@csrf_exempt
def add_app_from_worker(req):
   if req.user.user_acces > 0:
      
      data = json.loads(req.body)
      app = {}
      for key ,name in data.items():
         if key == 'tariffield' and not name =='nothing':
            
            tarif_take = tarif.objects.get(id=name)
            app[key]=tarif_take
            continue
         elif key =='problem' and not name =='nothing':
            
            problem_get = typeproblem.objects.get(id=name)
            app[key]= problem_get
            continue
         elif name == 'nothing':
            continue
         app[key] = name
      print(app)
        
      user_acces = req.user.user_acces
      opts = {
         2:'opt1',
         3:'opt2',
         1:'opt3',
         4:'opt4'
      }
      new_app =  Application_from_user.objects.create(**app,order=req.user,type_manager_take=opts[user_acces])
      
      return JsonResponse({'status':200})
   
def get_app_when_find(req):
   if req.user.user_acces > 1:
      user_data = req.GET.get('user')
      app_type =  req.GET.get('inftype')
      
      if int(user_data):
         try:
            user = UserModel.objects.get(id_userlog=user_data)
            return get_app(req,user,app_type)
            
         except UserModel.DoesNotExist:
            return JsonResponse({"error":"Пользователь не найден!"})
      else:
         try:
            user = UserModel.objects.get()
            return get_app(req,user,app_type)
         except UserModel.DoesNotExist:
            return JsonResponse({"error":"Пользователь не найден!"})
      
   else: return JsonResponse({"error":'В доступе отказано'})

def get_app(req,usermodel,type_manager):
   try:
      app = Application_from_user.objects.filter(FromOrder=usermodel,type_manager_take=type_manager)
      return JsonResponse({'applications':list(app.values())})

   except Application_from_user.DoesNotExist:
      return JsonResponse({'error':'У пользователя нет заявок'})
