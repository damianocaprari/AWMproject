from app_conditions.models import Condition, ConditionCA
from app_conditions.serializers import ConditionSerializer, ConditionCASerializer
from rest_framework import viewsets, permissions


class ConditionViewSet(viewsets.ModelViewSet):
    serializer_class = ConditionSerializer
    queryset = Condition.objects.all()
    permission_classes = (permissions.AllowAny,)  # todo da cambiare con il livello appropriato
    # TODO le permissions possono essere combinate usando & (and), | (or), ~ (not)
    # ad esempio: permission_classes = (permissions.IsAuthenticated & IsOwnUser | permissions.IsAdminUser,)


class ConditionCAViewSet(viewsets.ModelViewSet):
    queryset = ConditionCA.objects.all()
    serializer_class = ConditionCASerializer
    permission_classes = (permissions.IsAdminUser,)  # todo da cambiare con il livello appropriato
    # TODO le permissions possono essere combinate usando & (and), | (or), ~ (not)
    # ad esempio: permission_classes = (permissions.IsAuthenticated & IsOwnUser | permissions.IsAdminUser,)
