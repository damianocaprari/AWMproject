from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User
from app_monsters.models import Monster


class IsOwnerOrReadOnly(permissions.BasePermission):
  """permette l'accesso alla risorsa solo se l'utente della richiesta è l'owner della risorsa"""
  print("Sono dentro che provo")

  def has_permission(self, request, view):
      user = Monster.objects.get(pk=view.kwargs['id'])
      print(user)
      try:
          if request.user == user:
              print("USER", user)
              return True
      except:
          return request.method in SAFE_METHODS
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

  # solo per modificare gli object singoli.. non qui
  """
  def has_object_permission(self, request, view, obj):
    print(request.method)
    if 'PUT' == request.method:
      print(obj)
      if obj.id == request.user.id:
        print("qui ritornerei TRUE")  # return True
    print("qui ritornerei FALSE")  # return False
    return True
  """


# IsAuthenticatedOrReadOnly in view
"""
class IsAnonPostUser(permissions.BasePermission):
    #permette di accettare richieste POST anche da utenti non autenticati
    #per registrazione utenti
    def has_permission(self, request, view):
        print(view)
        if request.method == 'POST':
            return True
        return False
"""
