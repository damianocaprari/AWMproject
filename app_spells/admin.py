from django.contrib import admin
from app_spells.models import Spell, SpellAdditionalInfo, SpellCA, SpellTag


# ---- INLINES ---- #
class SpellAdditionalInfoInline(admin.StackedInline):
    filter_horizontal = ['tags']
    fields = (
        ('avatar', 'tags',),
        ('aoe_type', 'aoe_size',),
        ('part_of_weapon_attack', 'save_type',),
    )
    model = SpellAdditionalInfo


class SpellCAInline(admin.TabularInline):
    model = SpellCA
# ---- EO INLINES ---- #


# ---- MODEL-ADMINS ---- #
class SpellAdmin(admin.ModelAdmin):
    list_display = ('level', 'name', 'author', 'creation_time', 'last_modified')
    list_display_links = ('name',)
    fields = (
        ('author', 'creation_time', 'last_modified',),
        ('name', 'version',),
        ('level', 'school',),
        ('casting_time_amount', 'casting_time_unit', 'casting_time_description',),
        ('component_verbal', 'component_somatic', 'component_material', 'component_material_description',),
        ('range_type', 'range_distance',),
        ('duration_type', 'duration_amount', 'duration_unit',),
        ('description',),
        ('ritual', 'higher_level',),
        ('classes',),
    )
    filter_horizontal = ['classes']
    readonly_fields = Spell.readonly_fields
    date_hierarchy = 'creation_time'
    inlines = [
        SpellAdditionalInfoInline,
        SpellCAInline
    ]


class SpellTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'creation_time', 'last_modified')
    fields = (
      ('creation_time', 'last_modified',),
      ('tag',),
    )
    readonly_fields = Spell.readonly_fields
# ---- EO MODEL-ADMINS ---- #


# ---- REGISTERS ----#
admin.site.register(Spell, SpellAdmin)
admin.site.register(SpellTag, SpellTagAdmin)
# ---- EO REGISTERS ---- #
