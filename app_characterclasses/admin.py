from .models import CharacterClass
from app_spells.models import Spell
from django.contrib import admin


class SpellInline(admin.TabularInline):
    model = Spell.spell_list.through


class CharacterClassAdmin(admin.ModelAdmin):
    model = CharacterClass
    inlines = [SpellInline]


admin.site.register(CharacterClass, CharacterClassAdmin)