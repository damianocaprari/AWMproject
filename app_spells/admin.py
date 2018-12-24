from django.contrib import admin
from .models import Spell

class SpellAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'level',
        'spell_list',
        'school',
        'ritual',
        'casting_time',
        'duration',
        'range',
        'component_verbal',
        'component_somatic',
        'component_material',
        'component_material_cost',
        'concentration',
        'description',
        'source_book',
        'source_page_number',
    ]

admin.site.register(Spell, SpellAdmin)