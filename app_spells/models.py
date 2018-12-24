from django.db import models
from rest_framework import serializers
from app_classes.models import CharacterClass

class Spell(models.Model):
    '''
    Remember to reflect changes in the admin.py file
    '''

    CASTING_TIME_CHOICES = (
        ('1_ACTION', '1 Action'),
        ('1_BONUS', '1 Bonus Action'),
        ('1_REACTION', '1 Reaction'),
        ('1_MINUTE', '1 Minute'),
        ('10_MINUTES', '10 Minutes'),
        ('1_HOUR', '1 Hour'),
        ('8_HOURS', '8 Hours'),
        ('12_HOURS', '12 Hours'),
        ('24_HOURS', '24 Hours'),
    )
    DURATION_CHOICES = (
        ('INSTANTANEOUS', 'Instantaneous'),
        ('1_ROUND', '1 Round'),
        ('1_MINUTE', '1 Minute'),
        ('10_MINUTES', '10 Minutes'),
        ('1_HOUR', '1 Hour'),
        ('2_HOURS', '2 Hour'),
        ('8_HOURS', '8 Hours'),
        ('24_HOURS', '24 Hours'),
        ('7_DAYS', '7 Days'),
        ('10_DAYS', '10 Days'),
        ('30_DAYS', '30 Days'),
        ('UNTIL_DISPELLED', 'Until Dispelled'),
        ('OTHER', 'Other'),
    )
    LEVEL_CHOICES = (
        (0, 'Cantrip'),
        (1, '1st'),
        (2, '2nd'),
        (3, '3rd'),
        (4, '4th'),
        (5, '5th'),
        (6, '6th'),
        (7, '7th'),
        (8, '8th'),
        (9, '9th'),
    )
    SCHOOL_CHOICES = (
        ('ABJ', 'Abjuration'),
        ('CON', 'Conjuration'),
        ('DIV', 'Divination'),
        ('ENC', 'Enchantment'),
        ('EVO', 'Evocation'),
        ('ILL', 'Illusion'),
        ('NEC', 'Necromancy'),
        ('TRA', 'Transmutation'),
    )
    SOURCE_BOOK_CHOICES = (
        ('PHB', 'Player\'s Handbook'),
        ('EE', 'Elemental Evil Player\'s Companion'),
        ('SCAG', 'Sword Coast Adventurer\'s Guide'),
        ('XGE', 'Xanathar\'s Guide to Everything'),
    )

    casting_time            = models.CharField(max_length=10, choices=CASTING_TIME_CHOICES)
    component_material      = models.CharField(max_length=100, null=True, blank=True)
    component_material_cost = models.PositiveIntegerField(default=0)
    component_verbal        = models.BooleanField()
    component_somatic       = models.BooleanField()
    concentration           = models.BooleanField()
    description             = models.TextField(max_length=2000)
    duration                = models.CharField(max_length=15, choices=DURATION_CHOICES)
    level                   = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)
    name                    = models.CharField(max_length=50)
    range                   = models.PositiveSmallIntegerField(verbose_name='range (ft)', null=True)
    ritual                  = models.BooleanField()
    school                  = models.CharField(max_length=4, choices=SCHOOL_CHOICES)
    source_book             = models.CharField(max_length=4, choices=SOURCE_BOOK_CHOICES, null=True, blank=True)
    source_page_number      = models.PositiveSmallIntegerField(null=True, blank=True)
    spell_list              = models.ManyToManyField(CharacterClass)

    def __str__(self):
        return '{} - {}'.format(self.level, self.name)

    class Meta:
        ordering = ['level', 'name']
