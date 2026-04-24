from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import hashlib 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from user.models import UserModel
from crm.models import Application_from_user
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from user.models import UserModel
from main.models import tarif
from django.core import serializers
from django.contrib.auth.decorators import login_required
from datetime import datetime
from main.models import typeproblem

@csrf_exempt
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
                  return  JsonResponse(response)
            except UserModel.DoesNotExist:
               return JsonResponse({'error':'Модель не найдена!'})
          
   
@csrf_exempt
def getcards(req):
   
   if req.method == "GET":
      
      data = tarif.objects.all()
      raw_json_data = serializers.serialize('json',data)
      cooked_json_data = json.loads(raw_json_data)
      
      return JsonResponse(cooked_json_data,safe=False,  json_dumps_params={'ensure_ascii': False})

@csrf_exempt
@login_required
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
   
   name = jsonbody.get('name')
   phone = jsonbody.get('phone')
   description = jsonbody.get('description')
   adres = jsonbody.get('adres')
   opt =jsonbody.get('opt')
   problem = jsonbody.get('problem')
   if problem:
      try:
         get_type_problem = typeproblem.objects.get(id=problem)
      except typeproblem.DoesNotExist:
         return JsonResponse({'error':'Модель не найдена, ошибка!'})
   else:
      get_type_problem = None


   new_app_without_user = Application_from_user.objects.create(application_status='opt3',
                                                  comment = description,
                                                  data_create = datetime.now(),
                                                  FromOrder = req.user,
                                                  user=name,
                                                  phone=phone,
                                                  adres=adres,
                                                  tariffield = None,
                                                  type_manager_take = opt,
                                                  problem = get_type_problem
                                                  
                                                  )
   new_app_without_user.save()
   return JsonResponse({'conf':'Запрос получен'})
   

