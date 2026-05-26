from django.shortcuts import render , redirect
from .models import tarif
from crm.views import Status_site_decorator_for_who
@Status_site_decorator_for_who('User')
def main(req):
    
    Get_tarif = tarif.objects.filter(discounts=0)
    Get_action = tarif.objects.exclude(discounts=0)
    
    data = {
        'actions':Get_action,
        'tarif':Get_tarif
    }
    return render(req,template_name='index.html',context=data)


    