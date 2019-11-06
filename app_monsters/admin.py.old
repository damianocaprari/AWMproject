from django.contrib import admin
#from .models import Monster
from app_monsters.models import Monster, MonsterCA
# OLD IMPORT MonsterSpeed, MonsterSave, MonsterSkill, MonsterDamageVulnerability, MonsterDamageResistance, MonsterLegendaryAction,MonsterTrait,MonsterSpecialAbilities,MonsterSense,MonsterReaction,MonsterLanguage,MonsterDamageImmunity,MonsterConditionImmunity,MonsterAction


class MonsterCAInline(admin.TabularInline):
    model = MonsterCA

"""
class MonsterSpeedInline(admin.StackedInline):
    extra = 0
    model = MonsterSpeed


class MonsterSaveInline(admin.StackedInline):
    extra = 0
    model = MonsterSave


class MonsterSkillInLine(admin.StackedInline):
    extra = 0
    model = MonsterSkill


class MonsterDamageVulnerabilityInLine(admin.StackedInline):
    extra = 0
    model = MonsterDamageVulnerability


class MonsterDamageResistanceInLine(admin.StackedInline):
    extra = 0
    model = MonsterDamageResistance


class MonsterConditionImmunityInLine(admin.StackedInline):
    extra = 0
    model = MonsterConditionImmunity


class MonsterDamageImmunityInLine(admin.StackedInline):
    extra = 0
    model = MonsterDamageImmunity


class MonsterSenseInLine(admin.StackedInline):
    extra = 0
    model = MonsterSense


class MonsterLanguageInLine(admin.StackedInline):
    extra = 0
    model = MonsterLanguage


class MonsterSpecialAbilitiesInLine(admin.StackedInline):
    extra = 0
    model = MonsterSpecialAbilities


class MonsterActionInLine(admin.StackedInline):
    extra = 0
    model = MonsterAction


class MonsterLegendaryActionInLine(admin.StackedInline):
    extra = 0
    model = MonsterLegendaryAction


class MonsterTraitInLine(admin.StackedInline):
    extra = 0
    model = MonsterTrait


class MonsterReactionInLine(admin.StackedInline):
    extra = 0
    model = MonsterReaction
"""

class MonsterAdmin(admin.ModelAdmin):
    list_display = ('name', 'challenge_rating', 'author', 'creation_time', 'last_modified')
    list_display_links = ('name',)
    fields = (
        ('author', 'creation_time', 'last_modified',),
        ('name', 'version','image'),
        ('size', 'type', 'subtype', 'alignment'),
        ('armor_class', 'armor_class_notes'),
        ('hit_point', 'hit_dice', 'speeds'),
        ('ability_str', 'ability_dex', 'ability_con'),
        ('ability_int','ability_wis','ability_cha'),
        ('challenge_rating', 'saves'),
        ('traits'),
        ('skills', 'languages'),
        ('damage_vulnerabilities','damage_resistances'),
        ('condition_immunities','damage_immunities'),
        ('actions'),
        ('senses'),
        ('special_abilities'),
        ('legendary_actions'),
    )

    readonly_fields = Monster.readonly_fields
    date_hierarchy = 'creation_time'

    inlines = [
        #MonsterSpeedInline,
        #MonsterSaveInline,
        ##MonsterSkillInLine,
        #MonsterDamageVulnerabilityInLine,
        #MonsterDamageResistanceInLine,
        #MonsterConditionImmunityInLine,
        #MonsterDamageImmunityInLine,
        #MonsterSenseInLine,
        #MonsterLanguageInLine,
        #MonsterSpecialAbilitiesInLine,
        #MonsterActionInLine,
        #MonsterTraitInLine,
        #MonsterReactionInLine,
        #MonsterLegendaryActionInLine,
        MonsterCAInline,
    ]

    # fields = Monster.fields
    # TODO finisci qui i campi

admin.site.register(Monster, MonsterAdmin)
