from django.shortcuts import render
from .models import tarif


def main(req):
    
    Get_tarif = tarif.objects.filter(discounts=0)
    Get_action = tarif.objects.exclude(discounts=0)
    
    data = {
        'actions':Get_action,
        'tarif':Get_tarif
    }
    return render(req,template_name='index.html',context=data)