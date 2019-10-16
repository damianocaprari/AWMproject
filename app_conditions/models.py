from django.db import models


class Condition(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(max_length=8192)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    fields = [
        'name',
        'description',
    ]
    readonly_fields = [
        'creation_time',
        'last_modified',
    ]

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ['name']


class ConditionCA(models.Model):
    owner = models.ForeignKey(Condition, related_name='custom_attributes', on_delete=models.CASCADE)
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
