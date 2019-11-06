from app_monsters.models import Monster, MonsterCA
from rest_framework import serializers


class MonsterCASerializer(serializers.ModelSerializer):
    class Meta:
        model = MonsterCA
        fields = ['id', ] + MonsterCA.fields + MonsterCA.readonly_fields


class MonsterSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:monster-detail')
    author = serializers.HyperlinkedRelatedField(view_name='api:user-detail', read_only=True, default=serializers.CurrentUserDefault())
    custom_attributes = MonsterCASerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = Monster
        fields = ['id', 'url'] + Monster.fields + Monster.readonly_fields + ['custom_attributes']

    def create(self, validated_data):
        user = self.context['request'].user
        monster = Monster.objects.create(**validated_data)
        monster.author = user
        monster.save()
        return monster
