from app_profiles.models import Profile, ProfileCA, UserCA
from app_profiles.permissions import IsOwnUser, IsAnonPostUser
from app_profiles.serializers import ProfileSerializer, ProfileCASerializer, UserSerializer, UserCASerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets, permissions, parsers, status


class ProfileViewSet(viewsets.ModelViewSet):
    #parser_classes = (JSONParser, MultiPartParser, FormParser,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated & IsOwnUser | IsAdminUser,)


class ProfileCAViewSet(viewsets.ModelViewSet):
    queryset = ProfileCA.objects.all()
    serializer_class = ProfileCASerializer
    permission_classes = (IsAdminUser,)


class UserViewSet(viewsets.ModelViewSet, viewsets.mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated & IsOwnUser | IsAnonPostUser | IsAdminUser,)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class UserCAViewSet(viewsets.ModelViewSet):
    queryset = UserCA.objects.all()
    serializer_class = UserCASerializer
    permission_classes = (IsAdminUser,)
