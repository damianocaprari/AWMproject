from app_monsters.models import Monster, MonsterAction, MonsterCA, MonsterConditionImmunity, MonsterDamageImmunity, \
  MonsterDamageResistance, MonsterDamageVulnerability, MonsterLanguage, MonsterLegendaryAction, MonsterReaction, \
  MonsterSave, MonsterSense, MonsterSkill, MonsterSpecialAbilities, MonsterSpeed, MonsterTrait
# from app_characterclasses.models import CharacterClass
from rest_framework import serializers


class MonsterActionSerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterAction
    fields = ['id', ] + MonsterAction.fields + MonsterAction.readonly_fields

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


class MonsterDamageImmunitySerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterDamageImmunity
    fields = ['id', ] + MonsterDamageImmunity.fields + MonsterDamageImmunity.readonly_fields


class MonsterLanguageSerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterLanguage
    fields = ['id', ] + MonsterLanguage.fields + MonsterLanguage.readonly_fields


class MonsterReactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterReaction
    fields = ['id', ] + MonsterReaction.fields + MonsterReaction.readonly_fields


class MonsterSenseSerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterSense
    fields = ['id', ] + MonsterSense.fields + MonsterSense.readonly_fields


class MonsterSpecialAbilitiesSerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterSpecialAbilities
    fields = ['id', ] + MonsterSpecialAbilities.fields + MonsterSpecialAbilities.readonly_fields


class MonsterTraitSerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterTrait
    fields = ['id', ] + MonsterTrait.fields + MonsterTrait.readonly_fields


class MonsterLegendaryActionSerializer(serializers.ModelSerializer):
  class Meta:
    model = MonsterLegendaryAction
    fields = ['id', ] + MonsterLegendaryAction.fields + MonsterLegendaryAction.readonly_fields


class MonsterCASerializer(serializers.ModelSerializer):
  # url = serializers.HyperlinkedIdentityField(view_name='api:spellca-detail')
  class Meta:
    model = MonsterCA
    fields = ['id', ] + MonsterCA.fields + MonsterCA.readonly_fields


class MonsterSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='api:monster-detail')
  author = serializers.HyperlinkedRelatedField(view_name='api:user-detail', read_only=True)
  # classes = serializers.HyperlinkedRelatedField(view_name='api:characterclass-detail', many=True, queryset=CharacterClass.objects.all())

  # spell_additional_info = SpellAdditionalInfoSerializer()
  # custom_attributes = SpellCASerializer(many=True, allow_null=True, required=False)
  speeds = MonsterSpeedSerializer(many=True)
  saves = MonsterSaveSerializer(many=True)
  skills = MonsterSkillSerializer(many=True)
  damage_vulnerabilities = MonsterDamageVulnerabilitySerializer(many=True)
  damage_resistances = MonsterDamageResistanceSerializer(many=True)
  condition_immunities = MonsterConditionImmunitySerializer(many=True)
  damage_immunities = MonsterDamageImmunitySerializer(many=True)
  languages = MonsterLanguageSerializer(many=True)
  reactions = MonsterReactionSerializer(many=True)
  senses = MonsterSenseSerializer(many=True)
  special_abilities = MonsterSpecialAbilitiesSerializer(many=True)
  traits = MonsterTraitSerializer(many=True)
  actions = MonsterActionSerializer(many=True)
  legendary_actions = MonsterLegendaryActionSerializer(many=True)

  custom_attributes = MonsterCASerializer(many=True, allow_null=True, required=False)

  class Meta:
    model = Monster
    fields = ['id', 'url'] + Monster.fields + Monster.readonly_fields + ['speeds', 'saves', 'skills',
                                                                         'damage_vulnerabilities', 'damage_resistances',
                                                                         'condition_immunities', 'damage_immunities',
                                                                         'languages', 'reactions', 'senses',
                                                                         'special_abilities',
                                                                         'traits', 'actions', 'legendary_actions',
                                                                         'custom_attributes']

  def create(self, validated_data):
    monster = Monster.object.create()  # (name = validate_data['name'], etc per ogni elemento

    # QUESTI SOTTO LI FAI PER QUELLI NON OBBLIGATORI
    '''
    if validated_data.get('email') is not None:
      user.email = validated_data.get('email')
    if validated_data.get('first_name') is not None:
      user.first_name = validated_data.get('first_name')
    if validated_data.get('last_name') is not None:
      user.last_name = validated_data.get('last_name')
    '''
    user = self.context['request'].user
    monster.author = user  # cosi carico id di user che l'ha creato

    user.save()
