from django.contrib import admin
from .models import Spell
from .models_v2 import Spell_Model

class SpellAdmin(admin.ModelAdmin):
    fields = Spell.fields

admin.site.register(Spell, SpellAdmin)


class SpellAdmin2(admin.ModelAdmin):
    fields = Spell_Model.fields
    readonly_fields = Spell_Model.readonly_fields

admin.site.register(Spell_Model, SpellAdmin2)
