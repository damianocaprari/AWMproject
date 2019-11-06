from app_characterclasses.models import CharacterClass
from app_characterclasses.serializers import CharacterClassSerializer
from rest_framework import permissions, viewsets
from app_api.permissions import ReadOnly


class CharacterClassViewSet(viewsets.ModelViewSet):
    queryset = CharacterClass.objects.all()
    serializer_class = CharacterClassSerializer
    permission_classes = (ReadOnly | permissions.IsAdminUser,)
