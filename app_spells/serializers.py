from app_spells.models import Spell, SpellTag, SpellAdditionalInfo, SpellCA
from app_characterclasses.models import CharacterClass
from rest_framework import serializers


class SpellCASerializer(serializers.ModelSerializer):

    class Meta:
        model = SpellCA
        fields = ['id',] + SpellCA.fields + SpellCA.readonly_fields


class SpellTagSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:spelltag-detail')

    class Meta:
        model = SpellTag
        fields = ['id', 'url'] + SpellTag.fields + SpellTag.readonly_fields


class SpellAdditionalInfoSerializer(serializers.ModelSerializer):
    tags = SpellTagSerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = SpellAdditionalInfo
        fields = ['id', ] + SpellAdditionalInfo.fields + SpellAdditionalInfo.readonly_fields + ['tags',]
        read_only_fields = ['id', 'spell', 'tags',]


class SpellSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:spell-detail')
    author = serializers.HyperlinkedRelatedField(view_name='api:user-detail', read_only=True, default=serializers.CurrentUserDefault())

    classes = serializers.PrimaryKeyRelatedField(many=True, queryset=CharacterClass.objects.all())
    spell_additional_info = SpellAdditionalInfoSerializer(allow_null=True, required=False)
    custom_attributes = SpellCASerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = Spell
        fields = ['id', 'url'] + Spell.fields + Spell.readonly_fields + ['custom_attributes', 'spell_additional_info',]

    def update(self, instance, validated_data):
        spell_additional_info_validated_data = validated_data.pop('spell_additional_info', None)
        classes_validated_data = validated_data.pop('classes', None)
        instance.classes.add(*classes_validated_data)

        if spell_additional_info_validated_data is not None:
            spell_additional_info = SpellAdditionalInfo.objects.get(spell=instance)
            spell_additional_info.avatar = spell_additional_info_validated_data['avatar']
            spell_additional_info.aoe_type = spell_additional_info_validated_data['aoe_type']
            spell_additional_info.aoe_size = spell_additional_info_validated_data['aoe_size']
            #spell_additional_info.part_of_weapon_attack = spell_additional_info_validated_data['part_of_weapon_attack']
            spell_additional_info.save_type = spell_additional_info_validated_data['save_type']
            spell_additional_info.save()

        return super().update(instance, validated_data)
        # return instance


    def create(self, validated_data):
        spell_additional_info_validated_data = validated_data.pop('spell_additional_info')
        classes_validated_data = validated_data.pop('classes')

        user = self.context['request'].user
        spell = Spell.objects.create(**validated_data)
        spell.classes.add(*classes_validated_data)

        spell.author = user
        spell.save()

        spell_additional_info_set_serializer = self.fields['spell_additional_info']
        if spell_additional_info_validated_data is not None:
            spell_additional_info_validated_data['spell'] = spell
            spell_additional_info = spell_additional_info_set_serializer.create(spell_additional_info_validated_data)

        spell_additional_info.save()  # qui non sono sicuro che funzioni senza problemi
        # puoi provare a creare una spell direttamente dall'API, e controllare che 1) non crashi, 2) il campo spell_additional_info non sia "null"

        return spell
