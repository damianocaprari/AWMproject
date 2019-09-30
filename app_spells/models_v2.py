from app_characterclasses.models import CharacterClass
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

class Spell_SourceBook_Model

class Spell_Tag_Model(models.Model):
    tag = models.CharField(max_length=50, blank=True, null=True)

class Spell_AdditionalInfo_Model(models.Model):
    CONE = 'CONE'
    CUBE = 'CUBE'
    CYLINDER = 'CYLINDER'
    LINE = 'LINE'
    SPHERE = 'SPHERE'
    SQUARE = 'SQUARE'
    AOE_TYPE_CHOICES = (
      (CONE, 'Cone'),
      (CUBE, 'Cube'),
      (CYLINDER, 'Cylinder')
      (LINE, 'Line'),
      (SPHERE, 'Sphere'),
      (SQUARE, 'Square'),
    )

    STR = 'STR'
    CON = 'CON'
    DEX = 'DEX'
    INT = 'INT'
    WIS = 'WIS'
    CHA = 'CHA'
    SAVE_TYPE_CHOICES = (
      (STR, STR),
      (CON, CON),
      (DEX, DEX),
      (INT, INT),
      (WIS, WIS),
      (CHA, CHA),
    )

    avatar = models.ImageField(blank=True, null=True, upload_to='avatars')
    aoe_type = models.CharField(max_length=50, choices=AOE_TYPE_CHOICES, blank=True, null=True)
    aoe_size = models.PositiveSmallIntegerField(null=True, blank=True)
    part_of_weapon_attack = models.BooleanField(default=False)
    save_type = models.CharField(max_length=50, choices=SAVE_TYPE_CHOICES, blank=True, null=True)
    source_book             = models.CharField(max_length=5, choices=SOURCE_BOOK_CHOICES, null=True, blank=True)
    source_book_other       = models.CharField(max_length=50, null=True, blank=True)
    source_page_number      = models.PositiveSmallIntegerField(null=True, blank=True)
    spell_list              = models.ManyToManyField(CharacterClass, related_name='spells')
    tags = models.ManyToManyField(Spell_Tag_Model, related_name='spell_additional_info', blank=True, null=True)

class Spell_Model(models.Model):
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

    ACTION = 'ACTION'
    BONUS_ACTION = 'BONUS_ACTION'
    HOUR = 'HOUR'
    MINUTE = 'MINUTE'
    NO_ACTION = 'NO_ACTION'
    REACTION = 'REACTION'
    SPECIAL = 'SPECIAL'
    CASTING_TIME_UNIT_CHOICES = (
        (ACTION, 'Action'),
        (BONUS_ACTION, 'Bonus Action'),
        (HOUR, 'Hour'),
        (MINUTE, 'Minute'),
        (NO_ACTION, 'No Action'),
        (REACTION, 'Reaction'),
        (SPECIAL, 'Special'),
    )

    SELF = 'SELF'
    TOUCH = 'TOUCH'
    RANGED = 'RANGED'
    SIGHT = 'SIGHT'
    UNLIMITED = 'UNLIMITED'
    RANGE_TYPE_CHOICES = (
        (SELF, 'Self'),
        (TOUCH, 'Touch'),
        (RANGED, 'Ranged'),
        (SIGHT, 'Sight'),
        (UNLIMITED, 'Unlimited'),
    )

    CONCENTRATION = 'CONCENTRATION'
    INSTANTANEOUS = 'INSTANTANEOUS'
    SPECIAL = 'SPECIAL'
    TIME = 'TIME'
    UNTIL_DISPELLED = 'UNTIL_DISPELLED'
    UNTIL_DISPELLED_OR_TRIGGERED = 'UNTIL_DISPELLED_OR_TRIGGERED'
    DURATION_TYPE_CHOICES = (
        (CONCENTRATION, 'Concentration'),
        (INSTANTANEOUS, 'Instantaneous'),
        (SPECIAL, 'Special'),
        (TIME, 'Time'),
        (UNTIL_DISPELLED, 'Until Dispelled'),
        (UNTIL_DISPELLED_OR_TRIGGERED, 'Until Dispelled or Triggered'),
    )

    ROUND = 'ROUND'
    MINUTE = 'MINUTE'
    HOUR = 'HOUR'
    DAY = 'DAY'
    DURATION_UNIT_CHOICES = (
      (ROUND, 'Round'),
      (MINUTE, 'Minute'),
      (HOUR, 'Hour'),
      (DAY, 'Day'),
    )

    name = models.CharField(max_length=256, min_length=2)
    version = models.CharField(max_length=256, null=True, blank=True)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)
    school = models.CharField(max_length=256, min_length=2)
    casting_time_amount = models.PositiveSmallIntegerField()
    casting_time_unit = models.CharField(max_length=50, choices=CASTING_TIME_UNIT_CHOICES)
    casting_time_description = models.CharField(max_length=256, null=True, blank=True)
    component_verbal = models.BooleanField(default=False)
    component_somatic = models.BooleanField(default=False)
    component_material = models.BooleanField(default=False)
    component_material_description = models.CharField(max_length=1024, null=True, blank=True)
    range_type = models.CharField(max_length=50, choices=RANGE_TYPE_CHOICES)
    range_size = models.PositiveSmallIntegerField(null=True, blank=True)
    duration_type = models.CharField(max_length=50, choices=DURATION_TYPE_CHOICES)
    duration_amount = models.PositiveSmallIntegerField(null=True, blank=True)
    duration_unit = models.CharField(max_length=50, choices=DURATION_UNIT_CHOICES, null=True, blank=True)
    description = models.TextField(max_length=8192, min_length=2)
    ritual = models.BooleanField(default=False)
    higher_level = models.BooleanField(default=False)
    classes = models.ManyToManyField(CharacterClass, related_name='spells')

    author = models.ForeignKey('auth.User', related_name='spells', on_delete=models.SET_NULL, null=True)



    fields = [
        'owner',
        'name',
        'level',
        'school',
        'spell_list',
        'casting_time',
        'casting_time_other',
        'ritual',
        'range',
        'concentration',
        'duration',
        'duration_other',
        'component_verbal',
        'component_somatic',
        'component_material',
        'description',
        'source_book',
        'source_book_other',
        'source_page_number',
    ]

    def __str__(self):
        return '{} - {}'.format(self.level, self.name)

    # Validate the model as a whole
    def clean(self):
        if self.casting_time == 'OTHER':
            if self.casting_time_other is None:
                raise ValidationError(_('OTHER has been selected for Casting Time but no additional description has been provided.'))
        else:
            self.casting_time_other = None

        if self.duration == 'OTHER':
            if self.duration_other is None:
                raise ValidationError(_('OTHER has been selected for Duration but no additional description has been provided.'))
        else:
            self.duration_other = None

        if self.source_book == 'OTHER':
            if self.source_book_other is None:
                raise ValidationError(_('OTHER has been selected for Source Book but no additional description has been provided.'))
        else:
            self.source_book_other = None


    class Meta(object):
        ordering = ['level', 'name']
        unique_together = ('name', 'version')
