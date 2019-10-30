from app_monsters.models import Monster, MonsterAction, MonsterCA, MonsterConditionImmunity, MonsterDamageImmunity, MonsterDamageResistance, MonsterDamageVulnerability, MonsterLanguage, MonsterLegendaryAction, MonsterReaction, MonsterSave, MonsterSense, MonsterSkill, MonsterSpecialAbilities, MonsterSpeed, MonsterTrait
# from app_characterclasses.models import CharacterClass
from rest_framework import serializers


class MonsterSpeedSerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterSpeed
    fields = ['id', ] + MonsterSpeed.fields + MonsterSpeed.readonly_fields


class MonsterSaveSerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterSave
    fields = ['id', ] + MonsterSave.fields + MonsterSave.readonly_fields


class MonsterSkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterSkill
    fields = ['id', ] + MonsterSkill.fields + MonsterSkill.readonly_fields


class MonsterDamageVulnerabilitySerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterDamageVulnerability
    fields = ['id', ] + MonsterDamageVulnerability.fields + MonsterDamageVulnerability.readonly_fields


class MonsterDamageResistanceSerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterDamageResistance
    fields = ['id', ] + MonsterDamageResistance.fields + MonsterDamageResistance.readonly_fields


class MonsterConditionImmunitySerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterConditionImmunity
    fields = ['id', ] + MonsterConditionImmunity.fields + MonsterConditionImmunity.readonly_fields




"""
MonsterCA, \
MonsterConditionImmunity,\
MonsterDamageImmunity,\
MonsterDamageResistance,\
MonsterDamageVulnerability,\
MonsterLanguage,\
MonsterLegendaryAction,\
MonsterReaction,\
MonsterSave,\
MonsterSense,\
MonsterSkill,\
MonsterSpecialAbilities,\
MonsterSpeed,\
MonsterTrait
"""


class MonsterCASerializer(serializers.ModelSerializer):
  # url = serializers.HyperlinkedIdentityField(view_name='api:spellca-detail')
  class Meta:
    model = MonsterCA
    fields = ['id', ] + MonsterCA.fields + MonsterCA.readonly_fields


class MonsterSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:monster-detail')
    author = serializers.HyperlinkedRelatedField(view_name='api:user-detail', read_only=True)
    #classes = serializers.HyperlinkedRelatedField(view_name='api:characterclass-detail', many=True, queryset=CharacterClass.objects.all())

    #spell_additional_info = SpellAdditionalInfoSerializer()
    #custom_attributes = SpellCASerializer(many=True, allow_null=True, required=False)
    monster_speed = MonsterSpeedSerializer()
    monster_save = MonsterSaveSerializer()
    monster_skill = MonsterSkillSerializer()
    monster_damage_vulnerability = MonsterDamageVulnerabilitySerializer()
    monster_damage_resistance = MonsterDamageResistanceSerializer()
    monster_condition_immunity = MonsterConditionImmunitySerializer()


    class Meta:
        model = Monster
        fields = ['id', 'url'] + Monster.fields + Monster.readonly_fields + ['monster_speed', 'monster_save','monster_skill','monster_damage_vulnerability','monster_damage_resistance','monster_condition_immunity']
