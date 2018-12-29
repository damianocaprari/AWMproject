from django.contrib import admin
from .models import Spell

class SpellAdmin(admin.ModelAdmin):
    fields = Spell.fields

admin.site.register(Spell, SpellAdmin)
