from app_profiles.models import Profile, ProfileCA, UserCA
from app_profiles.permissions import IsOwnUser, IsAnonPostUser
from app_profiles.serializers import ProfileSerializer, ProfileCASerializer, UserSerializer, UserCASerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated & IsOwnUser | permissions.IsAdminUser,)


class ProfileCAViewSet(viewsets.ModelViewSet):
    queryset = ProfileCA.objects.all()
    serializer_class = ProfileCASerializer
    permission_classes = (permissions.IsAdminUser,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated & IsOwnUser | IsAnonPostUser | permissions.IsAdminUser,)


class UserCAViewSet(viewsets.ModelViewSet):
    queryset = UserCA.objects.all()
    serializer_class = UserCASerializer
    permission_classes = (permissions.IsAdminUser,)
