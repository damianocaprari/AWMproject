from django.contrib.auth.models import User
from rest_framework import permissions


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


class IsAnonPostUser(permissions.BasePermission):
    """permette di accettare richieste POST anche da utenti non autenticati
    per registrazione utenti"""
    def has_permission(self, request, view):
        print(view)
        if request.method == 'POST':
            return True
        return False
