
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import hashlib 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from user.models import UserModel
from django.contrib.auth.hashers import make_password


@csrf_exempt
def create_user(req):

    if req.method == 'POST':
        data = json.loads(req.body)
        name = data.get('username')
        password = make_password(data.get('password'))
        id = data.get('id')
        user_acces = data.get('access')
        print(user_acces)
        rawdata=  name + password
        

        newuser = UserModel.objects.create(username = name,password=password,id_userlog = id,settings ='132',userhash=userhash ,user_acces =user_acces)
        newuser.save()

        return JsonResponse({'name': name})