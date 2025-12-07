from django.db import models

class tarif(models.Model):
    
    Tarif_name = models.CharField(max_length=100)
    price = models.IntegerField() # В рублях 
    price_to_connect = models.IntegerField() # В рублях
    discounts = models.IntegerField() #В процентах
    time_to_end_discount = models.DateField()# Когда тариф выключается
    Mounts_discount = models.IntegerField() # Сколько дней длится акция
    in_archive = models.BooleanField() # Нахождение в архиве 
