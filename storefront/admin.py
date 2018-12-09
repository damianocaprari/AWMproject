from django.contrib import admin
from .models import Character

class CharacterAdmin(admin.ModelAdmin):
    fields = ['name', 'creation_date']

admin.site.register(Character, CharacterAdmin)