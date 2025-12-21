from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
def auth(req):
    
   return render(req,'autorization.html')

@login_required(login_url='authlogin')
def Profile(req,):

   return render(req,'Profile.html')

def Support(req):

   return render(req,'Support.html')

def Sales(req):
    
   return render(req,'Salesdepartment.html')
@login_required
def Admin(req):
   if (req.user.user_acces != 3):
      return redirect('')
   

   return render(req,'AdminPanel.html')