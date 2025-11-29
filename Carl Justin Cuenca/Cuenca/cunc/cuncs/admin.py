from django.contrib import admin
from. models import dataClassas , clientData, Skill, Projects

# Register your models here.

@admin.register(dataClassas)
class DataClassAdmin(admin.ModelAdmin):
    list_display = ('name','school','hobbies')
    search_fields = ('name',)

@admin.register(clientData)
class ClientDataAdmin(admin.ModelAdmin):
    list_display = ('nameData','accountData')
    search_fields = ('nameData',)

admin.site.register(Skill)
admin.site.register(Projects)