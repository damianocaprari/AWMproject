from app_conditions.serializers import ConditionSerializer, ConditionCASerializer
from app_conditions.models import Condition, ConditionCA

from rest_framework import viewsets, permissions


class ConditionViewSet(viewsets.ModelViewSet):
    serializer_class = ConditionSerializer
    queryset = Condition.objects.all()
    permission_classes = (permissions.IsAdminUser,)  # todo da cambiare con il livello appropriato


class ConditionCAViewSet(viewsets.ModelViewSet):
    queryset = ConditionCA.objects.all()
    serializer_class = ConditionCASerializer
    permission_classes = (permissions.IsAdminUser,)  # todo da cambiare con il livello appropriato
