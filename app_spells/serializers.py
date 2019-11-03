from app_spells.models import Spell, SpellTag, SpellAdditionalInfo, SpellCA
from app_characterclasses.models import CharacterClass
from rest_framework import serializers


class SpellCASerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='api:spellca-detail')

    class Meta:
        model = SpellCA
        fields = ['id',] + SpellCA.fields + SpellCA.readonly_fields


class SpellTagSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:spelltag-detail')

    class Meta:
        model = SpellTag
        fields = ['id', 'url'] + SpellTag.fields + SpellTag.readonly_fields


class SpellAdditionalInfoSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='api:spelladditionalinfo-detail')
    #spell = serializers.PrimaryKeyRelatedField(queryset=Spell.objects.all())
    tags = SpellTagSerializer(many=True)

    class Meta:
        model = SpellAdditionalInfo
        fields = ['id', ] + SpellAdditionalInfo.fields + SpellAdditionalInfo.readonly_fields + ['tags',]



class SpellSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:spell-detail')
    author = serializers.HyperlinkedRelatedField(view_name='api:user-detail', read_only=True, default=serializers.CurrentUserDefault())

    classes = serializers.PrimaryKeyRelatedField(many=True, queryset=CharacterClass.objects.all())
    spell_additional_info = SpellAdditionalInfoSerializer(allow_null=True, required=False)
    custom_attributes = SpellCASerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = Spell
        fields = ['id', 'url'] + Spell.fields + Spell.readonly_fields + ['custom_attributes', 'spell_additional_info',]

    def create(self, validated_data):

        print("\n\n\",\n", validated_data)

        spell_additional_info_validated_data = validated_data.pop('spell_additional_info')

        classes_validated_data = validated_data.pop('classes')


        user = self.context['request'].user
        print("\n\n\n", user, "\n\n\n\n")

        spell  = Spell.objects.create(**validated_data)

        #spell.save()

        print("POST SAVE")
        print("class valid data", classes_validated_data)
        for id in classes_validated_data:
            print("id", id)
            #clazz = CharacterClass.objects.get(pk=id)
            #print("clazz", clazz)
            #spell.classes.add(clazz)

        spell.classes.add(*classes_validated_data)

        #clazzes = CharacterClass.objects.filter(pk__in=classes_validated_data)
        #print("POST CLAZZES")
        #print(clazzes)
        #spell.classes.add(*clazzes)
        print("POST ADD")
        #print("ciao")

        spell_additional_info_set_serializer = self.fields['spell_additional_info']
        if spell_additional_info_validated_data is not None:
            spell_additional_info_validated_data['owner'] = spell
            spell_additional_info = spell_additional_info_set_serializer.create(spell_additional_info_validated_data)

        spell.author = user
        spell.save()
        return spell

        '''
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
        custom_attributes_validated_data = validated_data.pop('custom_attributes')
        
        user = self.context['request'].user
        print("\n\n\n", user, "\n\n\n\n")

        monster = Monster.objects.create(**validated_data)
        monster.author = user

        actions_set_serializer = self.fields['actions']
        for each in actions_validated_data:
            each['owner'] = monster
        actions = actions_set_serializer.create(actions_validated_data)

        speeds_set_serializer = self.fields['speeds']
        for each in speeds_validated_data:
            each['owner'] = monster
        speeds = speeds_set_serializer.create(speeds_validated_data)
        '''





"""{"name":"asdasdefeesv","version":null,"level":1,"school":"Divination","casting_time_amount":2,"casting_time_unit":"ACTION","casting_time_description":null,"component_verbal":"false","component_somatic":"false","component_material":"true","component_material_description":null,"range_type":"TOUCH","range_distance":null,"duration_type":"INSTANTANEOUS","duration_amount":0,"duration_unit":null,"description":"dcwefwegregregrwe","ritual":"true","higher_level":"true","classes":["http://127.0.0.1:8000/api/characterclasses/3/","http://127.0.0.1:8000/api/characterclasses/4/"],"spell_additional_info":null}"""