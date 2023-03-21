from django.contrib import admin

from .models import SettingMain


@admin.register(SettingMain)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'activate']
