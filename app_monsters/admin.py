from django.contrib import admin
#from .models import Monster
from app_monsters.models import Monster


class MonsterAdmin(admin.ModelAdmin):
    list_display = ('name', 'challenge_rating', 'author', 'creation_time', 'last_modified')
    list_display_links = ('name',)
    fields = (
        ('author', 'creation_time', 'last_modified',),
        ('name', 'version',),
        ('size', 'type', 'subtype', 'alignment'),
        ('armor_class', 'armor_class_notes'),
        ('hit_point', 'hit_dice'),
        ('ability_str', 'ability_dex', 'ability_con'),
        ('ability_int','ability_wis'),
        ('challenge_rating')



    )

    readonly_fields = Monster.readonly_fields
    date_hierarchy = 'creation_time'

    # fields = Monster.fields
    # TODO finisci qui i campi

admin.site.register(Monster, MonsterAdmin)
