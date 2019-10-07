from rest_framework import viewsets
from app_conditions.serializers import ConditionSerializer, ConditionCASerializer
from app_conditions.models import Condition, ConditionCA


class ConditionViewSet(viewsets.ModelViewSet):
    serializer_class = ConditionSerializer
    queryset = Condition.objects.all()


class ConditionCAViewSet(viewsets.ModelViewSet):
    queryset = ConditionCA.objects.all()
    serializer_class = ConditionCASerializer
