from django.shortcuts import render
from app_spells.models import Spell, SpellTag, SpellAdditionalInfo, SpellCA
from app_spells.serializers import SpellSerializer, SpellCASerializer, SpellTagSerializer, SpellAdditionalInfoSerializer
from rest_framework import generics, permissions, viewsets


class SpellView(viewsets.ModelViewSet):
    queryset = Spell.objects.all()
    serializer_class = SpellSerializer


class SpellTagView(viewsets.ModelViewSet):
    queryset = SpellTag.objects.all()
    serializer_class = SpellTagSerializer


class SpellAdditionalInfoView(viewsets.ModelViewSet):
    queryset = SpellAdditionalInfo.objects.all()
    serializer_class = SpellAdditionalInfoSerializer


class SpellCAView(viewsets.ModelViewSet):
    queryset = SpellCA.objects.all()
    serializer_class = SpellCASerializer
