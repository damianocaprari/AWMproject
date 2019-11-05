from app_characterclasses.models import CharacterClass
from app_characterclasses.serializers import CharacterClassSerializer
from rest_framework import permissions, viewsets


class CharacterClassViewSet(viewsets.ModelViewSet):

    queryset = CharacterClass.objects.all()
    serializer_class = CharacterClassSerializer
    permission_classes = (permissions.IsAdminUser,)
    # permission_classes = (permissions.AllowAny,)