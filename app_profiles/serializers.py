from app_profiles.models import Profile, ProfileCA, UserCA
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class ProfileCASerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileCA
        fields = ['id', ] + ProfileCA.fields + ProfileCA.readonly_fields


class ProfileSerializer(serializers.ModelSerializer):
    custom_attributes = ProfileCASerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = Profile
        fields = ['id',] + Profile.fields + Profile.readonly_fields + ['custom_attributes',]


class UserCASerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCA
        fields = ['id', ] + UserCA.fields + UserCA.readonly_fields


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
    profile = ProfileSerializer(read_only=True, required=False, allow_null=True)
    custom_attributes = UserCASerializer(many=True, allow_null=True, required=False)

    # TODO riferimenti ai Models che hanno User come author/owner
    # spells = serializers.HyperlinkedRelatedField(view_name='api:spell-detail', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url',
                  'username', 'password', 'first_name', 'last_name', 'email',
                  #'is_staff', 'is_superuser', 'is_active',
                  'date_joined', #'last_login',
                  'custom_attributes', 'profile',
                  # 'spells',
        ]
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id', 'profile', 'date_joined',]

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        if validated_data.get('email') is not None:
            user.email = validated_data.get('email')
        if validated_data.get('first_name') is not None:
            user.first_name = validated_data.get('first_name')
        if validated_data.get('last_name') is not None:
            user.last_name = validated_data.get('last_name')
        user.save()

        profile = Profile.objects.create(user=user)
        profile.save()

        return user


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
