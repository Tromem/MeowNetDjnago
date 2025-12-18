from django.shortcuts import render

def auth(req):
    
   return render(req,'autorization.html')

def Profile(req,):

   return render(req,'Profile.html')

def Support(req):

   return render(req,'Support.html')

def Sales(req):
    
   return render(req,'Salesdepartment.html')

def Admin(req):
    return render(req,'AdminPanel.html')