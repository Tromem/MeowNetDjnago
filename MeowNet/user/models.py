from django.db import models
from django.contrib.auth.models import AbstractBaseUser


    




#  доделать юзера
class UserModel(AbstractBaseUser):
    
    id = models.CharField(primary_key=True, verbose_name='Айди',max_length=12)
    username = models.CharField(max_length=150, unique=True ,verbose_name='Логин')
    settings = models.CharField(max_length=70  ,verbose_name='Настройки')# Настройки ввиде символов которые будет считывать js
    user_last_name = models.CharField(max_length=150 ,verbose_name="ФИО")
    address = models.CharField(max_length=300 ,verbose_name='Адрес подключения')
    paper_data = models.CharField(max_length=10 ,verbose_name='Паспортные данные')
    cout_applications = models.IntegerField(null=True ,blank=True, verbose_name='Все выполненые заявки')
    cout_applications_in_work = models.IntegerField(null=True ,blank=True ,verbose_name='Все заявки в работе')
    in_work = models.BooleanField(null=True ,blank=True ,verbose_name="Состояние смены") 
    start_of_shift = models.DateTimeField(null=True ,blank=True, verbose_name="Начало смены") # Начало смены
    end_of_shift = models.DateTimeField(null=True ,blank=True) #Конец смены
    works_day = models.IntegerField(null=True ,blank=True)  #Рабочие дни в месяц
    work_hours = models.IntegerField(null=True ,blank=True) #секунды в часы  
    user_acces = models.IntegerField(null=True ,blank=True)
    userhash = models.CharField(max_length=128 ,unique=True)
    numberphone = models.CharField(max_length=13)
    balance = models.IntegerField(default=0)
    user_tarif = models.ForeignKey("main.tarif", models.CASCADE)

    USERNAME_FIELD = 'username'


