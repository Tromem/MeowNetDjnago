from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login ,logout
from .models import UserModel

def auth(req):
    
   if req.POST:
      
      username = req.POST['username']
      password = req.POST['password']
      user = authenticate(req,username=username,password = password)
      
      if user is not None:
         login(req,user=user)
         return redirect('profile')  

   return render(req,'autorization.html')

@login_required(login_url='authlogin')
def Profile(req,):
   if req.user.is_superuser or req.user:
      return redirect('/user/admin')
   return render(req,'Profile.html')

def Support(req):

   return render(req,'Support.html')

def Sales(req):
    
   return render(req,'Salesdepartment.html')
@login_required
def Admin(req):
   
   if ( req.user.user_acces >= 4  ):
      
      Users = UserModel.objects.filter(user_acces=2)
      data = {'employers':Users}
      if(req.user.is_superuser == True ):
         return render(req,'AdminPanel.html',data)
      else:
         return redirect('main')
   

   return render(req,'AdminPanel.html',data)

@login_required
def testing_room(req):
   if ( req.user.user_acces != 5):
      if(req.user.is_superuser == True ):
         return render(req,'testing.html')

      return redirect('main')
   

   return render(req,'testing.html')