from django.contrib import admin
from core import models

admin.site.register(models.Item)
admin.site.register(models.CustomUser)