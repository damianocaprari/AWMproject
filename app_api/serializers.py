from app_spells.models import Spell
from app_characterclasses.models import CharacterClass
from app_conditions.models import Condition

from django.contrib.auth.models import User
from rest_framework import serializers


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


class ConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condition
        fields = ("id", "name", "description", "source_page_number")
