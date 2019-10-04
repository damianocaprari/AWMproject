from rest_framework import serializers
from .models import  Condition


class ConditionSerializer(serializers.ModelSerializer):

  class Meta:
    model = Condition
    fields = ("id", "name", "description", "source_page_number")