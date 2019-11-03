from django.shortcuts import render
from .models import Monster

from app_monsters.models import Monster, MonsterCA
from app_monsters.serializers import MonsterSerializer, MonsterCASerializer
from rest_framework import viewsets, permissions


class MonsterViewSet(viewsets.ModelViewSet):
    serializer_class = MonsterSerializer
    queryset = Monster.objects.all()
    permission_classes = (permissions.AllowAny,)  # todo da cambiare con il livello appropriato
    # TODO le permissions possono essere combinate usando & (and), | (or), ~ (not)
    # ad esempio: permission_classes = (permissions.IsAuthenticated & IsOwnUser | permissions.IsAdminUser,)
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class MonsterCAViewSet(viewsets.ModelViewSet):
    queryset = MonsterCA.objects.all()
    serializer_class = MonsterCASerializer
    permission_classes = (permissions.IsAdminUser,)  # todo da cambiare con il livello appropriato
    # TODO le permissions possono essere combinate usando & (and), | (or), ~ (not)
    # ad esempio: permission_classes = (permissions.IsAuthenticated & IsOwnUser | permissions.IsAdminUser,)


#def index(request):
#    monsters = Monster.objects.all()
#    context = {
#        'monsters': monsters,
#    }
#    return render(request, 'app_monsters/list.html', context)
