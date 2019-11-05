from app_spells.models import Spell, SpellTag, SpellAdditionalInfo, SpellCA
from app_spells.serializers import SpellSerializer, SpellCASerializer, SpellTagSerializer, SpellAdditionalInfoSerializer
from rest_framework import viewsets

from app_spells import permissions


class SpellViewSet(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer
    permission_classes = (permissions.IsAuthenticated & permissions.IsPost | permissions.IsOwnerOrReadOnly | permissions.IsAdminUser,)
    # permission_classes = (permissions.AllowAny,)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class SpellTagViewSet(viewsets.ModelViewSet):
    queryset = SpellTag.objects.all()
    serializer_class = SpellTagSerializer
    permission_classes = (permissions.IsReadOnly | permissions.IsAdminUser,)
    # permission_classes = (permissions.AllowAny,)


class SpellAdditionalInfoViewSet(viewsets.ModelViewSet):
    queryset = SpellAdditionalInfo.objects.all()
    serializer_class = SpellAdditionalInfoSerializer
    permission_classes = (permissions.IsAuthenticated & permissions.IsPost | permissions.IsOwnerOrReadOnly | permissions.IsAdminUser,)
    # permission_classes = (permissions.AllowAny,)


class SpellCAViewSet(viewsets.ModelViewSet):
    queryset = SpellCA.objects.all()
    serializer_class = SpellCASerializer
    permission_classes = (permissions.AllowAny,)
