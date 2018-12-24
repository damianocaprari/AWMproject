from django.db import models

class CharacterClass(models.Model):
    name = models.CharField(max_length=50)
    #TBC

    def __str__(self):
        return '' + self.name