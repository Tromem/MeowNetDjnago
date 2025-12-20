from django.db import models
from django.contrib.auth.models import AbstractBaseUser


    




#  доделать юзера
class UserModel(AbstractBaseUser):
    
    UserRole = models.IntegerField()
    number_user_id = models.PositiveIntegerField(primary_key=True)
    settings = models.CharField(max_length=70)
    user_last_name = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    paper_data = models.CharField(max_length=10)
    cout_applications = models.IntegerField(null=True)
    cout_applications_in_work = models.IntegerField(null=True)
    in_work = models.BooleanField(null=True) 
    start_of_shift = models.DateTimeField(null=True) # Начало смены
    end_of_shift = models.DateTimeField(null=True) #Конец смены
    works_day = models.IntegerField(null=True)  #Рабочие дни в месяц
    work_hours = models.IntegerField(null=True) #секунды в часы  
    user_acces = models.IntegerField(default=0)



