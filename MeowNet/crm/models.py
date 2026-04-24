from django.db import models
from main.models import tarif
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Application_from_user(models.Model):
                   
    
    OPTION_1 = 'opt1'
    OPTION_2 = 'opt2'
    OPTION_3 = 'opt3'
    
    OPTION_1_status = 'opt1'
    OPTION_2_status = 'opt2'
    OPTION_3_status = 'opt3'
    OPTION_4_status = 'opt4'
    OPTION_5_status = 'opt5'
    
    
    MY_CHOICES_manager = [
        (OPTION_1, 'Техническая поддержка'),
        (OPTION_2, 'Монтажник'),
        (OPTION_3, 'Продажи'),
    ]

    MY_CHOICES_status = [
        (OPTION_1_status,'Заявка заведена'),
        (OPTION_2_status,"Неуспешно"),
        (OPTION_3_status,"Новая заявка"),
        (OPTION_4_status,"Доработка"),
        (OPTION_5_status,"Юридическая заявка")
    ]
    
    
    id = models.CharField(primary_key=True,
                          max_length=6,
                          editable=False)
    application_status = models.CharField(choices=MY_CHOICES_status,max_length=50,default=OPTION_3_status)
    comment = models.TextField( null=True, blank=True)
    data_create = models.DateTimeField(auto_now_add=False, auto_now=True ,verbose_name="Когда создали заявку")
    FromOrder = models.ForeignKey('user.UserModel', on_delete=models.CASCADE, null=True, blank=True ,verbose_name="Модель от кого пришел")
    user = models.CharField(null=True, blank=True, max_length=50, verbose_name='Фио если нет модели')
    phone = models.CharField(null=True, blank=True, max_length=15, verbose_name="Номер если нет модели")
    adres = models.CharField(null=True, blank=True, max_length=100, verbose_name='Адрес без модели')
    order = models.OneToOneField('user.UserModel', on_delete=models.CASCADE, verbose_name='Кому заказ принадлежит', related_name='applications' ,null=True, blank=True)
    tariffield = models.ForeignKey(tarif,on_delete=models.CASCADE,verbose_name='Выбраный тариф',null=True,blank=True)
    type_manager_take = models.CharField(max_length=60,choices=MY_CHOICES_manager,default=OPTION_3)
    problem = models.ForeignKey('main.typeproblem',null=True,blank=True,on_delete=models.CASCADE)


@receiver(pre_save,sender=Application_from_user)
def makeId(sender,instance, **kwargs):
    if not instance.id:
        last_id_obj = sender.objects.order_by('-id').first()
        if last_id_obj:
            last_id_obj = int(last_id_obj.id)
        else:
            last_id_obj = 0
        new_id_int = last_id_obj + 1
        instance.id = str(new_id_int).zfill(4)