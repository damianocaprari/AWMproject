from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser, IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from app_spells.models import Spell


class IsReadOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method in SAFE_METHODS:
      return True
    return False


class IsOwnerOrReadOnly(permissions.BasePermission):
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


class IsPost(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method == 'POST':
      return True
    return False
