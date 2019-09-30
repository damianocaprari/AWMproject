from django.contrib import admin
from .models import Monster

class MonsterAdmin(admin.ModelAdmin):
    fields = Monster.fields
    # TODO finisci qui i campi

admin.site.register(Monster, MonsterAdmin)
