from django.db import models

# Create your models here.

class Condition(models.Model):
    name                = models.CharField(max_length=50, unique=True)
    description         = models.TextField(max_length=4000)
    source_page_number  = models.PositiveSmallIntegerField(null=True, blank=True)

    fields = [
        'name',
        'description',
        'source_page_number',
    ]

    def __str__(self):
        return '{}'.format(self.name)

    #per ordinare in base a nome??
    class Meta(object):
        ordering = ['name']