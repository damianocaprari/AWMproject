from django.db import models


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    avatar = models.ImageField(blank=True, null=True, upload_to='avatars/profile')

    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    fields = [
        'user',
        'avatar',
    ]
    readonly_fields = [
        'creation_time',
        'last_modified',
    ]

    def __str__(self):
        return self.user.__str__()

    class Meta(object):
        pass


class ProfileCA(models.Model):
    owner = models.ForeignKey(Profile, related_name='custom_attributes', on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=2048)
    value = models.CharField(max_length=8192)

    fields = [
        'owner',
        'name',
        'value',
    ]
    readonly_fields = [
        'creation_time',
        'last_modified',
    ]


class UserCA(models.Model):
    owner = models.ForeignKey('auth.User', related_name='custom_attributes', on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=2048)
    value = models.CharField(max_length=8192)

    fields = [
        'owner',
        'name',
        'value',
    ]
    readonly_fields = [
        'creation_time',
        'last_modified',
    ]
