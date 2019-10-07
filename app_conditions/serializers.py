from rest_framework import serializers
from app_conditions.models import  Condition, ConditionCA


class ConditionCASerializer(serializers.ModelSerializer):

    class Meta:
        model = ConditionCA
        fields = ['id', ] + ConditionCA.fields + ConditionCA.readonly_fields


class ConditionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:condition-detail')
    custom_attributes = ConditionCASerializer(many=True)

    class Meta:
        model = Condition
        fields = ['id', 'url',] + Condition.fields + Condition.readonly_fields + ['custom_attributes',]
