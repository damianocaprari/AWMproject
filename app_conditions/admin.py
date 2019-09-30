from django.contrib import admin
from .models import Condition

# Register your models here.
class ConditionAdmin(admin.ModelAdmin):
    fields = Condition.fields

admin.site.register(Condition, ConditionAdmin)
