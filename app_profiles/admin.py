from app_profiles.models import Profile, ProfileCA
from django.contrib import admin


# ---- INLINES ---- #
class ProfileCAInline(admin.TabularInline):
    model = ProfileCA
# ---- EO INLINES ---- #


# ---- MODEL-ADMINS ---- #
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'creation_time', 'last_modified')
    fields = (
        ('user', 'creation_time', 'last_modified',),
        ('avatar',),
    )
    readonly_fields = Profile.readonly_fields
    date_hierarchy = 'creation_time'
    inlines = [
        ProfileCAInline,
    ]
# ---- EO MODEL-ADMINS ---- #


# ---- REGISTERS ----#
admin.site.register(Profile, ProfileAdmin)
# ---- EO REGISTERS ---- #
