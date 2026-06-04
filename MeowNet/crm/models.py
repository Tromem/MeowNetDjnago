from django.db import models
from main.models import tarif
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Application_from_user(models.Model):
                   
    
    OPTION_1 = 'opt1'
    OPTION_2 = 'opt2'
    OPTION_3 = 'opt3'
    OPTION_4 = 'opt4'
    
    OPTION_1_status = 'opt1'
    OPTION_2_status = 'opt2'
    OPTION_3_status = 'opt3'
    OPTION_4_status = 'opt4'
    OPTION_5_status = 'opt5'
    
    
    MY_CHOICES_manager = [
        (OPTION_1, 'Техническая поддержка'),
        (OPTION_2, 'Монтажник'),
        (OPTION_3, 'Продажи'),
        (OPTION_4,'Менеджер')
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
    FromOrder = models.ForeignKey('user.UserModel', on_delete=models.SET_NULL, null=True, blank=True ,verbose_name="Модель от кого пришел")
    user = models.CharField(null=True, blank=True, max_length=50, verbose_name='Фио если нет модели')
    phone = models.CharField(null=True, blank=True, max_length=15, verbose_name="Номер если нет модели")
    adres = models.CharField(null=True, blank=True, max_length=100, verbose_name='Адрес без модели')
    order = models.ForeignKey('user.UserModel', on_delete=models.SET_NULL, verbose_name='Кому заказ принадлежит', related_name='applications' ,null=True, blank=True)
    first_owner_order = models.ForeignKey('user.UserModel', on_delete=models.SET_NULL, verbose_name='Кто первый взял заявку', related_name='first_applications' ,null=True, blank=True)
    tariffield = models.ForeignKey(tarif,on_delete=models.SET_NULL,verbose_name='Выбраный тариф',null=True,blank=True)
    type_manager_take = models.CharField(max_length=60,choices=MY_CHOICES_manager,default=OPTION_3)
    pasport = models.CharField(max_length=10,null=True, blank=True)
    Desired_date = models.DateTimeField(null=True, blank=True, verbose_name='Желаемая дата подключения')
    is_active = models.BooleanField(default=True)
    problem = models.ForeignKey('main.typeproblem',null=True,blank=True,on_delete=models.CASCADE)
    color = models.CharField(max_length=100 ,blank=True,null=True)
    
    
    
class city(models.Model):
    city_name = models.CharField(max_length=50)
   
    def __str__(self):
        return self.city_name
class adres(models.Model):
    name_adres = models.CharField(max_length=60)
    index = models.CharField(max_length=30)
    from_city = models.ForeignKey(city,  on_delete=models.CASCADE)
    def __str__(self):
        return self.name_adres

class Home(models.Model):
    
    fttx = 'fttx'
    PON = 'PON'
    Adsl = 'DSL'
    Not_have = 'None'

    Choises_tech_oport = [
        (fttx,'fttx'),
        (PON,'PON'),
        (Adsl,'Adsl'),
        (Not_have,'Нтхв')
    ]
   
    
    ports = models.IntegerField()
    number_home = models.CharField(max_length=5)
    tech_opportunity = models.CharField(choices=Choises_tech_oport,default=fttx)
    adres_name = models.ForeignKey(adres,on_delete=models.CASCADE)
    problem = models.ForeignKey('main.typeproblem',null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.number_home
    

class full_adres(models.Model):
    floor = models.IntegerField()
    Apartment = models.CharField(max_length=10)
    home = models.ForeignKey(Home,models.CASCADE)


@receiver(pre_save,sender=Home)
def check_tech(sender,instance, **kwargs):
    if instance.ports > 0:
        instance.Technical_feasibility = True
    else : instance.Technical_feasibility = False
        

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
    match instance.application_status:
        case 'opt1':
            instance.color = 'rgb(180, 180, 255)'
        case 'opt2':
            instance.color = 'rgba(255, 120, 120, 0.6)'
        case 'opt3':
            instance.color = 'rgb(245, 245, 245)'
        case 'opt4':
            instance.color = 'rgb(255, 237, 136)'
        case 'opt5':
            instance.color = 'rgba(120, 250, 130, 0.5)'
    if instance.application_status =='opt1' and not instance.order:
        instance.type_manager_take = 'opt2'

class Logs(models.Model):
    text = models.CharField(max_length=500)
    user_who = models.ForeignKey('user.UserModel',on_delete=models.SET_NULL, null=True ,blank=True,related_name='user_who')
    when = models.DateTimeField(auto_now_add=True)