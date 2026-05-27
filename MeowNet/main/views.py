from django.shortcuts import render , redirect
from .models import tarif
from crm.views import Status_site_decorator_for_who
@Status_site_decorator_for_who('User')
def main(req):
    data_type = req.GET.get('tariftype')
    
    Get_tarif = tarif.objects.filter(discounts=0)
    Get_action = tarif.objects.exclude(discounts=0)
    Get_tv = tarif.objects.filter(tv_chanels__gt=40,speed__lte=50)
    Get_pack = tarif.objects.filter(tv_chanels__gt=40,speed__gte=100)
    Get_ethernet = tarif.objects.filter(speed__gte=100,tv_chanels__lt=40)
    
    if data_type == 'tv':
        data = {'tarif':Get_tv}
    elif data_type == 'ethernet':
        data = {'tarif':Get_ethernet} 
    elif data_type == 'packs':
        data = {'tarif':Get_pack}  
    else:
        data = {
            'actions':Get_action,
            'tarif':Get_tarif,
            
        }
    return render(req,template_name='index.html',context=data)


    