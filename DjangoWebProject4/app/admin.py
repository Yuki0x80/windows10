from django.contrib import admin
from app.models import Check_list


class Check_listAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name',)
admin.site.register(Check_list, Check_listAdmin)
