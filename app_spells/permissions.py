from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser, IsAuthenticated
from app_spells.models import Spell, SpellAdditionalInfo


class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return False


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            spell = Spell.objects.get(pk=view.kwargs['pk'])
            if spell.author == request.user:
                return True
        except:
            return False
        return False


class IsOwnerOrReadOnlyAdditionalInfo(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            spell_additional_info = SpellAdditionalInfo.objects.get(pk=view.kwargs['pk'])
            if spell_additional_info.spell is not None:
                    if spell_additional_info.spell.author == request.user:
                        return True
        except:
            return False
        return False


class IsPost(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False
