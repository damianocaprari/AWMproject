from django.contrib import admin
from .models import Spell
from .models_v2 import SpellModel, SpellAdditionalInfoModel, SpellCAModel, SpellTagModel


class SpellAdmin(admin.ModelAdmin):
    fields = Spell.fields


admin.site.register(Spell, SpellAdmin)


#######################################################################################################################


class SpellAdditionalInfoInline(admin.StackedInline):
    filter_horizontal = ['tags']
    fields = (
        ('avatar', 'tags',),
        ('aoe_type', 'aoe_size',),
        ('part_of_weapon_attack', 'save_type',),
    )
    model = SpellAdditionalInfoModel


class SpellCAInline(admin.TabularInline):
    model = SpellCAModel


class SpellAdmin2(admin.ModelAdmin):
    #fields = Spell_Model.fields
    """
    fieldsets = (
      (None, {
        'fields' : (
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
      }),
      ('Additional Info', {
        'classes': ('collapse',),
        'fields': (
          ('spell_additional_info__avatar', 'spell_additional_info__last_modified',),
          ('spell_additional_info__aoe_type', 'spell_additional_info__aoe_size',),
          ('spell_additional_info__save_type',),
          ('spell_additional_info__part_of_weapon_attack',),
          ('spell_additional_info__tags',),
        )
      }),
    )
    """
    list_display = ('level', 'name', 'author', 'creation_time', 'last_modified')
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
    readonly_fields = SpellModel.readonly_fields
    date_hierarchy = 'creation_time'
    inlines = [
        SpellAdditionalInfoInline,
        SpellCAInline
    ]


admin.site.register(SpellModel, SpellAdmin2)


class SpellTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'creation_time', 'last_modified')
    fields = (
        ('creation_time', 'last_modified',),
        ('tag',),
    )
    readonly_fields = SpellModel.readonly_fields


admin.site.register(SpellTagModel, SpellTagAdmin)
