from app_conditions.models import Condition, ConditionCA
from app_conditions.serializers import ConditionSerializer, ConditionCASerializer
from rest_framework import viewsets

from app_api import permissions


class ConditionViewSet(viewsets.ModelViewSet):
    serializer_class = ConditionSerializer
    queryset = Condition.objects.all()
    # permission_classes = (permissions.AllowAny,)
    permission_classes = (permissions.ReadOnly | permissions.IsAdminUser,)


class ConditionCAViewSet(viewsets.ModelViewSet):
    queryset = ConditionCA.objects.all()
    serializer_class = ConditionCASerializer
    permission_classes = (permissions.IsAdminUser,)