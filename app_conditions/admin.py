from app_conditions.models import Condition, ConditionCA
from django.contrib import admin


# ---- INLINES ---- #
class ConditionCAInline(admin.TabularInline):
    model = ConditionCA
# ---- EO INLINES ---- #


# ---- MODEL-ADMINS ---- #
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_time', 'last_modified')
    fields = (
        ('name', 'creation_time', 'last_modified',),
        ('description',),
    )
    readonly_fields = Condition.readonly_fields
    date_hierarchy = 'creation_time'
    inlines = [
        ConditionCAInline,
    ]
# ---- EO MODEL-ADMINS ---- #


# ---- REGISTERS ----#
admin.site.register(Condition, ConditionAdmin)
# ---- EO REGISTERS ---- #
