from django.db import models
from main.models import tarif
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Application_from_user(models.Model):
                    # ((1,'Заявка заведена'),
                    #    (2,"Неуспешно"),
                    #    (3,"Новая заявка"),
                    #    (4,"Доработка"),
                    #    (5,"Юридическая заявка"))
    id = models.CharField(primary_key=True,
                          max_length=6,
                          editable=False)
    application_status = models.IntegerField()
    comment = models.TextField( null=True, blank=True)
    data_create = models.DateTimeField(auto_now_add=False, auto_now=True ,verbose_name="Когда создали заявку")
    FromOrder = models.OneToOneField('user.UserModel', on_delete=models.CASCADE, null=True, blank=True ,verbose_name="Модель от кого пришел")
    user = models.CharField(null=True, blank=True, max_length=50, verbose_name='Фио если нет модели')
    phone = models.CharField(null=True, blank=True, max_length=15, verbose_name="Номер если нет модели")
    adres = models.CharField(null=True, blank=True, max_length=100, verbose_name='Адрес без модели')
    order = models.ForeignKey('user.UserModel', on_delete=models.CASCADE, verbose_name='Кому заказ принадлежит', related_name='applications' ,null=True, blank=True)
    tariffield = models.ForeignKey(tarif,on_delete=models.CASCADE,verbose_name='Выбраный тариф',null=True,blank=True)

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