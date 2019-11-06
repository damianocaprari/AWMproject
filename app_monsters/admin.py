from django.contrib import admin
from app_monsters.models import Monster, MonsterCA


class MonsterCAInline(admin.TabularInline):
    model = MonsterCA


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
        MonsterCAInline,
    ]

admin.site.register(Monster, MonsterAdmin)
