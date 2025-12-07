from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Worker(models.Model):
    
    settings = models.CharField(max_length=70)
    cout_applications = models.IntegerField()
    cout_applications_in_work = models.IntegerField()
    in_work = models.BooleanField() 
    start_of_shift = models.DateTimeField() # Начало смены
    end_of_shift = models.DateTimeField() #Конец смены
    works_day = models.IntegerField()  #Рабочие дни в месяц
    work_hours = models.IntegerField() #секунды в часы  




#  доделать юзера
class UserModel(AbstractBaseUser):
    
    ROLE_CHOICES = (
        (1,'Admin'),
        (2,'User'),
        (3,'Tech_support'),
        (4,'Seller')
    )
    
    
    UserRole = models.Choices(choices=ROLE_CHOICES,
                              default = 4)
    number_user_id = models.PositiveIntegerField(primary_key=True)
    user_access  = models.OneToOneField(Worker , 
                                        on_delete=models.CASCADE,
                                        null=True)
    
    user_last_name = models.CharField(max_length=150)
    
    address = models.CharField(max_length=300)
    paper_data = models.CharField(max_length=10)



