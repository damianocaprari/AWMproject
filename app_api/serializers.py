from app_spells.models import Spell
from app_characterclasses.models import CharacterClass
from django.contrib.auth.models import User
from rest_framework import serializers


class SpellSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:spell-detail')
    owner = serializers.HyperlinkedRelatedField(view_name='api:user-detail',
                                                read_only=True)
    spell_list = serializers.HyperlinkedRelatedField(view_name='api:characterclass-detail',
                                                     many=True,
                                                     queryset=CharacterClass.objects.all())
    class Meta:
        model = Spell
        fields = ['id', 'url'] + Spell.fields


class CharacterClassSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:characterclass-detail')
    spells = serializers.HyperlinkedRelatedField(view_name='api:spell-detail',
                                                 many=True,
                                                 queryset=Spell.objects.all())
    class Meta:
        model = CharacterClass
        fields = ['id', 'url', 'spells'] + CharacterClass.fields


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
    spells = serializers.HyperlinkedRelatedField(view_name='api:spell-detail',
                                                 many=True,
                                                 read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'url', 'spells')
