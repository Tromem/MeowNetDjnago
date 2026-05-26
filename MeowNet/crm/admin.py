from django.contrib import admin
from API.models import *
from crm.models import *
from user.models import *
from main.models import *
# Register your models here.
admin.site.register(Application_from_user)
admin.site.register(UserModel)
admin.site.register(tarif)
admin.site.register(Home)
admin.site.register(adres)
admin.site.register(city)
admin.site.register(ServerStatus)