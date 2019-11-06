from app_monsters import permissions
from app_monsters.models import Monster, MonsterCA
from app_monsters.serializers import MonsterSerializer, MonsterCASerializer
from rest_framework import viewsets


class MonsterViewSet(viewsets.ModelViewSet):
    serializer_class = MonsterSerializer
    queryset = Monster.objects.all()
    permission_classes = (permissions.IsAuthenticated & permissions.IsPost | permissions.IsOwnerOrReadOnly | permissions.IsAdminUser,)


    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class MonsterCAViewSet(viewsets.ModelViewSet):
    queryset = MonsterCA.objects.all()
    serializer_class = MonsterCASerializer
    permission_classes = (permissions.IsAdminUser,)


