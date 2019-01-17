from django.db import models


class CharacterClass(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)

    fields = [
        'name',
    ]

    class Meta:
        ordering = ['name']
