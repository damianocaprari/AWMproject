from app_profiles.models import Profile, ProfileCA, UserCA
from app_profiles.serializers import ProfileSerializer, ProfileCASerializer, UserSerializer, UserCASerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAdminUser,)  # todo da cambiare con il livello appropriato


class ProfileCAViewSet(viewsets.ModelViewSet):
    queryset = ProfileCA.objects.all()
    serializer_class = ProfileCASerializer
    permission_classes = (permissions.IsAdminUser,)  # todo da cambiare con il livello appropriato


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)  # todo da cambiare con il livello appropriato


class UserCAViewSet(viewsets.ModelViewSet):
    queryset = UserCA.objects.all()
    serializer_class = UserCASerializer
    permission_classes = (permissions.IsAdminUser,)  # todo da cambiare con il livello appropriato
