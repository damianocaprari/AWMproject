from app_characterclasses.models import CharacterClass
from app_characterclasses.serializers import CharacterClassSerializer
from rest_framework import permissions, viewsets


class CharacterClassViewSet(viewsets.ModelViewSet):

    queryset = CharacterClass.objects.all()
    serializer_class = CharacterClassSerializer
    permission_classes = (permissions.AllowAny,)  # todo da cambiare con il livello appropriato
    # TODO le permissions possono essere combinate usando & (and), | (or), ~ (not)
    # ad esempio: permission_classes = (permissions.IsAuthenticated & IsOwnUser | permissions.IsAdminUser,)
