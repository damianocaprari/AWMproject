from app_spells.models import Spell, SpellTag, SpellAdditionalInfo, SpellCA
from app_characterclasses.models import CharacterClass
from rest_framework import serializers


class SpellCASerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:spellca-detail')  # TODO forse spellca ??

    class Meta:
        model = SpellCA
        fields = ['id', 'url'] + SpellCA.fields + SpellCA.readonly_fields


class SpellTagSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:spelltag-detail')  # TODO forse spelltag ??

    class Meta:
        model = SpellTag
        fields = ['id', 'url'] + SpellTag.fields + SpellTag.readonly_fields


class SpellAdditionalInfoSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:spelladditionalinfo-detail')  # TODO forse spelladditionalinfo ??
    spell = serializers.HyperlinkedIdentityField(view_name='api:spell-detail')
    tags = SpellTagSerializer(many=True)

    class Meta:
        model = SpellAdditionalInfo
        fields = ['id', 'url'] + SpellAdditionalInfo.fields + SpellAdditionalInfo.readonly_fields + ['tags',]


class SpellSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:spell-detail')
    author = serializers.HyperlinkedRelatedField(view_name='api:user-detail', read_only=True)
    classes = serializers.HyperlinkedRelatedField(view_name='api:characterclass-detail', many=True,
                                                  queryset=CharacterClass.objects.all())
    spell_additional_info = SpellAdditionalInfoSerializer()
    custom_attributes = SpellCASerializer(many=True)

    class Meta:
        model = Spell
        fields = ['id', 'url'] + Spell.fields + Spell.readonly_fields + ['custom_attributes', 'spell_additional_info',]
