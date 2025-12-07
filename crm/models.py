from django.db import models
from user.models import UserModel


class Application_from_user(models.Model):
    status_choises  = ((1,'Заявка заведена'),
                       (2,"Неуспешно"),
                       (3,"Новая заявка"),
                       (4,"Доработка"),
                       (5,"Юридическая заявка"))

    application_status = models.Choices(choices=status_choises,
                              default = 5)
    comment = models.TextField()
    data_create = models.DateTimeField( auto_now_add=False)
    user= models.OneToOneField(UserModel ,on_delete=models.CASCADE,null=True)


