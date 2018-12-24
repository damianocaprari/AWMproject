from django.contrib import admin
from .models import CharacterClass

class CharacterClassAdmin(admin.ModelAdmin):
    fields = [
        'name',
    ]

admin.site.register(CharacterClass, CharacterClassAdmin)