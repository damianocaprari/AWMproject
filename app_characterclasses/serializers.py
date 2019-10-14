from app_characterclasses.models import CharacterClass
from app_spells.models import Spell

from rest_framework import serializers


class CharacterClassSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='api:characterclass-detail')
  spells = serializers.HyperlinkedRelatedField(view_name='api:spell-detail', many=True,
                                               queryset=Spell.objects.all())

  class Meta:
    model = CharacterClass
    fields = ['id', 'url', 'spells'] + CharacterClass.fields
