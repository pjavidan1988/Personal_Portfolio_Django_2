from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.
from home.models import Setting
from home_en.models import Setting_en


class Setting_enAdmin(admin.ModelAdmin):
    list_display = ['name', 'update_at', 'status']





admin.site.register(Setting_en, Setting_enAdmin)
