from django.db import models



class TypeTarif(models.Model):
    typetarif = models.CharField(max_length=80)
    def __str__(self):
        return self.typetarif

class tarif( models.Model):

    Tarif_name = models.CharField(max_length=100)
    price = models.IntegerField() # В рублях 
    price_to_connect = models.IntegerField() # В рублях
    discounts = models.IntegerField(null=True, blank=True) #В процентах
    time_to_end_discount = models.DateField(null=True , blank=True)# Когда тариф выключается
    Mounts_discount = models.IntegerField(null=True, blank=True) # Сколько дней длится акция
    in_archive = models.BooleanField(null=True, blank=True,default=False) # Нахождение в архиве 
    speed = models.IntegerField() #Скорость в мб 
    typetarif = models.ForeignKey(TypeTarif,on_delete=models.CASCADE)
    tv_chanels = models.IntegerField()

    def __str__(self):
        return self.Tarif_name


class typeproblem(models.Model):
    
    OPTION_1 = 'opt1'
    OPTION_2 = 'opt2'
    OPTION_3 = 'opt3'
    MY_CHOICES = [
        (OPTION_1, 'Сложные тех. неполадки'),
        (OPTION_2, 'Средние тех. неполадки'),
        (OPTION_3, 'Легкие тех. неполадки'),
    ]

    name_problem = models.CharField(max_length=500)
    difficulity = models.CharField(choices=MY_CHOICES,max_length=60,default=OPTION_1)
    def __str__(self):
        return self.name_problem
    