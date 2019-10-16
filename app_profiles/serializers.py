from app_profiles.models import Profile, ProfileCA, UserCA
from django.contrib.auth.models import User
from rest_framework import serializers


class ProfileCASerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileCA
        fields = ['id', ] + ProfileCA.fields + ProfileCA.readonly_fields


class ProfileSerializer(serializers.ModelSerializer):
    custom_attributes = ProfileCASerializer(many=True)

    class Meta:
        model = Profile
        fields = ['id',] + Profile.fields + Profile.readonly_fields + ['custom_attributes',]


class UserCASerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCA
        fields = ['id', ] + UserCA.fields + UserCA.readonly_fields


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
    profile = ProfileSerializer()
    custom_attributes = UserCASerializer(many=True)

    # TODO riferimenti ai Models che hanno User come author/owner
    # spells = serializers.HyperlinkedRelatedField(view_name='api:spell-detail', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url',
                  'username', 'first_name', 'last_name', 'email',
                  'is_staff', 'is_superuser', 'is_active',
                  'date_joined', 'last_login',
                  'custom_attributes', 'profile',
                  # 'spells',
        ]


class UserSerializerForJWT(serializers.ModelSerializer):
    # profile = ProfileSerializer()
    # custom_attributes = UserCASerializer(many=True)

    # TODO riferimenti ai Models che hanno User come author/owner

    class Meta:
        model = User
        fields = ['id', 'username', 'email', # 'first_name', 'last_name',
                  'is_active', # 'is_staff', 'is_superuser',
                  # 'date_joined', 'last_login',
                  # 'custom_attributes', 'profile',
                  # 'spells',
        ]
