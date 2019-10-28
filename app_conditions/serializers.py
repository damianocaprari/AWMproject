from app_conditions.models import Condition, ConditionCA
from rest_framework import serializers


class ConditionCASerializer(serializers.ModelSerializer):

    class Meta:
        model = ConditionCA
        fields = ['id', ] + ConditionCA.fields + ConditionCA.readonly_fields


class ConditionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:condition-detail')
    custom_attributes = ConditionCASerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = Condition
        fields = ['id', 'url',] + Condition.fields + Condition.readonly_fields + ['custom_attributes',]
