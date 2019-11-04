from app_monsters.models import Monster, MonsterCA
"""
MonsterAction, MonsterCA, MonsterConditionImmunity, MonsterDamageImmunity, \
  MonsterDamageResistance, MonsterDamageVulnerability, MonsterLanguage, MonsterLegendaryAction, MonsterReaction, \
  MonsterSave, MonsterSense, MonsterSkill, MonsterSpecialAbilities, MonsterSpeed, MonsterTrait
"""
# from app_characterclasses.models import CharacterClass
from rest_framework import serializers

"""
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
"""



class MonsterCASerializer(serializers.ModelSerializer):
  # url = serializers.HyperlinkedIdentityField(view_name='api:spellca-detail')
  class Meta:
    model = MonsterCA
    fields = ['id', ] + MonsterCA.fields + MonsterCA.readonly_fields


class MonsterSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='api:monster-detail')
  author = serializers.HyperlinkedRelatedField(view_name='api:user-detail', read_only=True, default=serializers.CurrentUserDefault())
  # classes = serializers.HyperlinkedRelatedField(view_name='api:characterclass-detail', many=True, queryset=CharacterClass.objects.all())

  # custom_attributes = SpellCASerializer(many=True, allow_null=True, required=False)
  """
  speeds = MonsterSpeedSerializer(many=True, allow_null=True, required=False)
  saves = MonsterSaveSerializer(many=True, allow_null=True, required=False)
  skills = MonsterSkillSerializer(many=True, allow_null=True, required=False)
  damage_vulnerabilities = MonsterDamageVulnerabilitySerializer(many=True, allow_null=True, required=False)
  damage_resistances = MonsterDamageResistanceSerializer(many=True, allow_null=True, required=False)
  condition_immunities = MonsterConditionImmunitySerializer(many=True, allow_null=True, required=False)
  damage_immunities = MonsterDamageImmunitySerializer(many=True, allow_null=True, required=False)
  languages = MonsterLanguageSerializer(many=True, allow_null=True, required=False)
  reactions = MonsterReactionSerializer(many=True, allow_null=True, required=False)
  senses = MonsterSenseSerializer(many=True, allow_null=True, required=False)
  special_abilities = MonsterSpecialAbilitiesSerializer(many=True, allow_null=True, required=False)
  traits = MonsterTraitSerializer(many=True, allow_null=True, required=False)
  actions = MonsterActionSerializer(many=True, allow_null=True, required=False)
  legendary_actions = MonsterLegendaryActionSerializer(many=True, allow_null=True, required=False)
  """

  custom_attributes = MonsterCASerializer(many=True, allow_null=True, required=False)

  class Meta:
    model = Monster
    fields = ['id', 'url'] + Monster.fields + Monster.readonly_fields + ['custom_attributes']
    """'speeds', 'saves', 'skills',
    'damage_vulnerabilities', 'damage_resistances',
     'condition_immunities', 'damage_immunities',
     'languages', 'reactions', 'senses',
     'special_abilities',
     'traits', 'actions', 'legendary_actions',
     """

  def create(self, validated_data):
    """
    actions_validated_data = validated_data.pop('actions')
    saves_validated_data = validated_data.pop('saves')
    skills_validated_data = validated_data.pop('skills')
    speeds_validated_data = validated_data.pop('speeds')
    damage_resistances_validated_data = validated_data.pop('damage_resistances')
    damage_vulnerabilities_validated_data = validated_data.pop('damage_vulnerabilities')
    damage_immunities_validated_data = validated_data.pop('damage_immunities')
    condition_immunities_validated_data = validated_data.pop('condition_immunities')
    languages_validated_data = validated_data.pop('languages')
    reactions_validated_data = validated_data.pop('reactions')
    senses_validated_data = validated_data.pop('senses')
    special_abilities_validated_data = validated_data.pop('special_abilities')
    traits_validated_data = validated_data.pop('traits')
    legendary_actions_validated_data = validated_data.pop('legendary_actions')
    """
    custom_attributes_validated_data = validated_data.pop('custom_attributes')

    user = self.context['request'].user
    print("\n\n\n", user,"\n\n\n\n")

    monster = Monster.objects.create(**validated_data)
    monster.author = user

    """
    actions_set_serializer = self.fields['actions']
    for each in actions_validated_data:
      each['owner'] = monster
    actions = actions_set_serializer.create(actions_validated_data)


    speeds_set_serializer = self.fields['speeds']
    for each in speeds_validated_data:
      each['owner'] = monster
    speeds = speeds_set_serializer.create(speeds_validated_data)

    saves_set_serializer = self.fields['saves']
    for each in saves_validated_data:
      each['owner'] = monster
    saves = saves_set_serializer.create(saves_validated_data)

    skills_set_serializer = self.fields['skills']
    for each in skills_validated_data:
      each['owner'] = monster
    skills = skills_set_serializer.create(skills_validated_data)

    damage_vulnerabilities_set_serializer = self.fields['damage_vulnerabilities']
    for each in damage_vulnerabilities_validated_data:
      each['owner'] = monster
    damage_vulnerabilities = damage_vulnerabilities_set_serializer.create(damage_vulnerabilities_validated_data)

    damage_resistances_set_serializer = self.fields['damage_resistances']
    for each in damage_resistances_validated_data:
      each['owner'] = monster
    damage_resistances = damage_resistances_set_serializer.create(damage_resistances_validated_data)

    condition_immunities_set_serializer = self.fields['condition_immunities']
    for each in condition_immunities_validated_data:
      each['owner'] = monster
    condition_immunities = condition_immunities_set_serializer.create(condition_immunities_validated_data)

    damage_immunities_set_serializer = self.fields['damage_immunities']
    for each in damage_immunities_validated_data:
      each['owner'] = monster
    damage_immunities = damage_immunities_set_serializer.create(damage_immunities_validated_data)

    languages_set_serializer = self.fields['languages']
    for each in languages_validated_data:
      each['owner'] = monster
    languages = languages_set_serializer.create(languages_validated_data)

    reactions_set_serializer = self.fields['reactions']
    for each in reactions_validated_data:
      each['owner'] = monster
    reactions = reactions_set_serializer.create(reactions_validated_data)

    senses_set_serializer = self.fields['senses']
    for each in senses_validated_data:
      each['owner'] = monster
    senses = senses_set_serializer.create(senses_validated_data)

    special_abilities_set_serializer = self.fields['special_abilities']
    for each in special_abilities_validated_data:
      each['owner'] = monster
    special_abilities = special_abilities_set_serializer.create(special_abilities_validated_data)

    traits_set_serializer = self.fields['traits']
    for each in traits_validated_data:
      each['owner'] = monster
    traits = traits_set_serializer.create(traits_validated_data)

    legendary_actions_set_serializer = self.fields['legendary_actions']
    for each in legendary_actions_validated_data:
      each['owner'] = monster
    legendary_actions = legendary_actions_set_serializer.create(legendary_actions_validated_data)
    """

    custom_attributes_set_serializer = self.fields['custom_attributes']
    for each in custom_attributes_validated_data:
      each['owner'] = monster
    custom_attributes = custom_attributes_set_serializer.create(custom_attributes_validated_data)

    monster.save()
    return monster


"""
  def create(self, validated_data):
    monster = Monster.objects.create()  # (name = validate_data['name'], etc per ogni elemento

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

    monster.name = validated_data.get['name']
    monster.armor_class = validated_data.get['armor_class']
    monster.name = validated_data.get['name']
    monster.name = validated_data.get['name']
    monster.name = validated_data.get['name']
    monster.name = validated_data.get['name']
    monster.name = validated_data.get['name']
    monster.name = validated_data.get['name']
    monster.name = validated_data.get['name']

    #fai per opzionali

    user.save()
"""