from django.db import models



class TypeTarif(models.Model):
    typetarif = models.CharField(max_length=80)

class tarif( models.Model):
    
    

    Tarif_name = models.CharField(max_length=100)
    price = models.IntegerField() # В рублях 
    price_to_connect = models.IntegerField() # В рублях
    discounts = models.IntegerField(null=True) #В процентах
    time_to_end_discount = models.DateField(null=True )# Когда тариф выключается
    Mounts_discount = models.IntegerField(null=True) # Сколько дней длится акция
    in_archive = models.BooleanField(null=True) # Нахождение в архиве 
    speed = models.IntegerField() #Скорость в мб 
    typetarif = models.ForeignKey(TypeTarif,on_delete=models.CASCADE)
    tv_chanels = models.IntegerField()



    
