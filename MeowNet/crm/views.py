from django.shortcuts import render
from crm.models import Logs
from datetime import datetime

def Logger_decorator(func):
    def wrapper(req,*args, **kwargs):
        app = Logs.objects.create(
            text=f'Пользователь {req.user} Использовал API/Заходил по ссылке: {req.path}, в {datetime.now()}',
            who= req.user,
            when = datetime.today()
        )
        app.save()
        if (req.user.is_authenticated):
            pass
        return func(req, *args, **kwargs)
    return wrapper
