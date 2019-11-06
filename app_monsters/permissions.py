from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser, IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from app_monsters.models import Monster


class IsOwnerOrReadOnly(permissions.BasePermission):
    """permette l'accesso alla risorsa solo se l'utente della richiesta è l'owner della risorsa"""
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            monster = Monster.objects.get(pk=view.kwargs['pk'])
            print(monster)
            if monster.author == request.user:
                return True
        except:
            return False
        return False


class IsPost(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False


# -------------------------


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsOwnUser(permissions.BasePermission):
    """permette l'accesso alla risorsa solo se l'utente della richiesta è l'owner della risorsa"""
    def has_permission(self, request, view):
        try:
            user = User.objects.get(pk=view.kwargs['pk'])
            if request.user == user:
                return True
        except:
            return False
        return False
