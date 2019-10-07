from app_spells.models import Spell, SpellTag, SpellAdditionalInfo, SpellCA
from app_spells.serializers import SpellSerializer, SpellCASerializer, SpellTagSerializer, SpellAdditionalInfoSerializer
from rest_framework import viewsets


class SpellViewSet(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer


class SpellTagViewSet(viewsets.ModelViewSet):
    queryset = SpellTag.objects.all()
    serializer_class = SpellTagSerializer


class SpellAdditionalInfoViewSet(viewsets.ModelViewSet):
    queryset = SpellAdditionalInfo.objects.all()
    serializer_class = SpellAdditionalInfoSerializer


class SpellCAViewSet(viewsets.ModelViewSet):
    queryset = SpellCA.objects.all()
    serializer_class = SpellCASerializer
