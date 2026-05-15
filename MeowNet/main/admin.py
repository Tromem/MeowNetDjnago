from django.contrib import admin
from .models import *
from main.models import typeproblem
from crm.models import Logs
admin.site.register(TypeTarif)
admin.site.register(typeproblem)
admin.site.register(Logs)