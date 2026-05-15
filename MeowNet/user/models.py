from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import pre_save
from django.dispatch import receiver
from random import randint
import hashlib
from django.db import models
from django.utils import timezone
from datetime import timedelta

class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return super().get_by_natural_key(username=username)
    def create_user(self,username,password=None,**extra_fields):
        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password, **extra_fields):
        # Создание суперпользователя
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class Emlpoyers:
    employer = models.CharField(max_length=50)
    access = models.IntegerField()

class UserModel(AbstractBaseUser, PermissionsMixin):
    
    id_userlog = models.CharField(max_length=12, unique=True, verbose_name='ID')
    username = models.CharField(max_length=150, unique=True, verbose_name='Логин')
    settings = models.CharField(max_length=70  ,verbose_name='Настройки',blank=True,null=True)# Настройки ввиде символов которые будет считывать js
    user_last_name = models.CharField(max_length=150 ,verbose_name="ФИО",null=True)
    address = models.CharField(max_length=300 ,verbose_name='Адрес подключения')
    paper_data = models.CharField(max_length=10 ,verbose_name='Паспортные данные')
    cout_applications = models.IntegerField(null=True ,blank=True, verbose_name='Все выполненые заявки')
    cout_applications_in_work = models.IntegerField(null=True ,blank=True ,verbose_name='Все заявки в работе')
    in_work = models.BooleanField(null=True ,blank=True ,verbose_name="Состояние смены",default=False) 
    start_of_shift = models.DateTimeField(null=True ,blank=True, verbose_name="Начало смены") # Начало смены
    end_of_shift = models.DateTimeField(null=True ,blank=True) #Конец смены
    works_day = models.IntegerField(null=True ,blank=True)  #Рабочие дни в месяц
    work_hours = models.IntegerField(null=True ,blank=True) #секунды в часы  
    user_acces = models.IntegerField(null=True ,blank=True,default=0)
    userhash = models.CharField(max_length=128 ,unique=True)
    numberphone = models.CharField(max_length=13)
    balance = models.IntegerField(default=0)
    user_tarif = models.ForeignKey("main.tarif", models.SET_NULL,null=True,blank=True)
    user_tarif_active = models.BooleanField(default = True, blank=False)
    user_tarif_balance = models.BooleanField(default= True, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    Date_of_last_write_off = models.DateField(null=True,blank=True)
    Date_of_new_write_off = models.DateField(null=True,blank=True)
    appartaments = models.CharField( max_length=5 ,blank=True,null=True)


    USERNAME_FIELD = 'username'
    objects = UserManager()
    def save(self,*args, **kwargs):
        if self.Date_of_last_write_off:
            self.Date_of_new_write_off = self.Date_of_last_write_off + timedelta(days=30)
        super().save(*args, **kwargs)
        if self.user_tarif  and self.user_tarif_balance == True:
            self.user_tarif_active == True
            super().save(*args, **kwargs) 

            
            

@receiver(pre_save,sender=UserModel)
def makeId(sender, instance, **kwargs):
    if not instance.id_userlog:
        while True:
            new_id = str(randint(12345678999, 999999999999))
            if not sender.objects.filter(id_userlog=new_id).exists():
                instance.id_userlog = new_id
                break
@receiver(pre_save,sender=UserModel)
def make_hash(sender,instance, **kwargs):
    if not instance.userhash:
        rawdata = instance.username + instance.password
        userhash = hashlib.sha256(bytes(rawdata,'UTF-8')).hexdigest()
        instance.userhash = userhash

 

        