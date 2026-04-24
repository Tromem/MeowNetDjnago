from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login ,logout
from .models import UserModel
from main.models import typeproblem

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
   return render(req,'Profile.html')

def Support(req):

   return render(req,'Support.html')

def Sales(req):
    
   return render(req,'Salesdepartment.html')


@login_required
def Admin(req):
   Users = UserModel.objects.filter(user_acces__gt=0).order_by('-user_acces')
   data = {'employers':Users}
   if ( req.user.user_acces >= 4 or req.user.is_superuser == True):
      return render(req,'AdminPanel.html',data)
   else:
      return redirect('/')



@login_required
def testing_room(req):
   Users = UserModel.objects.all()
   data = {'employers':Users}
  
   if ( req.user.user_acces != 5):
      if(req.user.is_superuser == True ):
         
         return render(req,'testing.html',data)

      return redirect('main')
   

   return render(req,'testing.html',data)


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
      return render(req,'findadres.html')
   
   else:
      return redirect('/')