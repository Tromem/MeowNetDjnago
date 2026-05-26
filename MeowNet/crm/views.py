from django.shortcuts import render
from crm.models import Logs
from datetime import datetime
from user.models import ServerStatus 

def Logger_decorator(func):
    def wrapper(req,*args, **kwargs):
        app = Logs.objects.create(
            text=f'Пользователь {req.user} Использовал API/Заходил по ссылке: {req.path}, в {datetime.now()}',
            user_who= req.user,
            when = datetime.today()
        )
        app.save()
        if (req.user.is_authenticated):
            pass
        return func(req, *args, **kwargs)
    return wrapper

def Status_site_decorator_for_who(Type_user:str):
    def Status_site_decorator(func):
        def warpper(req,*args, **kwargs):
            status = ServerStatus.objects.filter(for_who = Type_user, status = True)
            if len(status)> 0:
                
                if status[0].time_to_end < datetime.now():
                    status[0].delete()
                data = {'inf':status[0]}
                return render(req,'ErrorPage.html',data)
            return func(req,*args, **kwargs)
        return warpper
    return Status_site_decorator
