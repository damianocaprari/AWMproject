from app_characterclasses.models import CharacterClass
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


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

    ABJURATION = 'Abjuration'
    CONJURATION = 'Conjuration'
    DIVINATION = 'Divination'
    ENCHANTMENT = 'Enchantment'
    EVOCATION = 'Evocation'
    ILLUSION = 'Illusion'
    NECROMANCY = 'Necromancy'
    TRANSMUTATION = 'Transmutation'
    SCHOOL_CHOICES = (
        (ABJURATION, 'Abjuration'),
        (CONJURATION, 'Conjuration'),
        (DIVINATION, 'Divination'),
        (ENCHANTMENT, 'Enchantment'),
        (EVOCATION, 'Evocation'),
        (ILLUSION, 'Illusion'),
        (NECROMANCY, 'Necromancy'),
        (TRANSMUTATION, 'Transmutation'),
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

    author = models.ForeignKey('auth.User', related_name='spells_v2', on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=256)
    version = models.CharField(max_length=256, null=True, blank=True)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)
    school = models.CharField(max_length=256, choices=SCHOOL_CHOICES)
    casting_time_amount = models.PositiveSmallIntegerField()
    casting_time_unit = models.CharField(max_length=50, choices=CASTING_TIME_UNIT_CHOICES)
    casting_time_description = models.CharField(max_length=256, null=True, blank=True)
    component_verbal = models.BooleanField(default=False)
    component_somatic = models.BooleanField(default=False)
    component_material = models.BooleanField(default=False)
    component_material_description = models.CharField(max_length=1024, null=True, blank=True)
    range_type = models.CharField(max_length=50, choices=RANGE_TYPE_CHOICES)
    range_distance = models.PositiveSmallIntegerField(null=True, blank=True)
    duration_type = models.CharField(max_length=50, choices=DURATION_TYPE_CHOICES)
    duration_amount = models.PositiveSmallIntegerField(null=True, blank=True)
    duration_unit = models.CharField(max_length=50, choices=DURATION_UNIT_CHOICES, null=True, blank=True)
    description = models.TextField(max_length=8192)
    ritual = models.BooleanField(default=False)
    higher_level = models.BooleanField(default=False)
    classes = models.ManyToManyField(CharacterClass, related_name='spells_v2')

    fields = [
        'author',
        'name',
        'version',
        'level',
        'school',
        'casting_time_amount',
        'casting_time_unit',
        'casting_time_description',
        'component_verbal',
        'component_somatic',
        'component_material',
        'component_material_description',
        'range_type',
        'range_distance',
        'duration_type',
        'duration_amount',
        'duration_unit',
        'description',
        'ritual',
        'higher_level',
        'classes',
    ]
    readonly_fields = [
      'creation_time',
      'last_modified',
    ]

    def __str__(self):
        return '{} - {}'.format(self.level, self.name)

    # Validate the model as a whole
    def clean(self):
        if self.casting_time_unit == self.REACTION:
            if self.casting_time_description is None:
                raise ValidationError(_('casting_time_description is required when casting_time_unit is set to Reaction.'))

        if self.component_material == True:
            if self.component_material_description is None:
                raise ValidationError(_('component_material_description is required when component_material is set to True.'))

        if self.range_type == self.RANGED:
            if self.range_distance is None:
                raise ValidationError(_('range_distance is required when range_type is set to Ranged.'))

        if self.duration_type == self.CONCENTRATION \
        or self.duration_type == self.SPECIAL \
        or self.duration_type == self.TIME:
            if self.duration_amount is None:
                raise ValidationError(_('duration_amount is required when duration_type is set to Concentration, Special or Time.'))
            if self.duration_unit is None:
                raise ValidationError(_('duration_unit is required when duration_type is set to Concentration, Special or Time.'))

    class Meta(object):
        ordering = ['level', 'name']
        unique_together = ('name', 'version')


class Spell_CA(models.Model):
    spell = models.ForeignKey(Spell_Model, related_name='custom_attributes', on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=1024)
    value = models.TextField(max_length=8192)

    fields = [
      'spell',
      'name',
      'value',
    ]
    readonly_fields = [
      'creation_time',
      'last_modified',
    ]


class Spell_Tag_Model(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    tag = models.CharField(max_length=256)

    fields = [
      'tag',
    ]
    readonly_fields = [
      'creation_time',
      'last_modified',
    ]


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
      (CYLINDER, 'Cylinder'),
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

    spell = models.OneToOneField(Spell_Model, related_name='spell_additional_info', on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    avatar = models.ImageField(blank=True, null=True, upload_to='avatars')
    aoe_type = models.CharField(max_length=50, choices=AOE_TYPE_CHOICES, blank=True, null=True)
    aoe_size = models.PositiveSmallIntegerField(null=True, blank=True)
    part_of_weapon_attack = models.BooleanField(default=False)
    save_type = models.CharField(max_length=50, choices=SAVE_TYPE_CHOICES, blank=True, null=True)
    tags = models.ManyToManyField(Spell_Tag_Model, related_name='spell_additional_info')

    fields = [
        'spell',
        'avatar',
        'aoe_type',
        'aoe_size',
        'part_of_weapon_attack',
        'save_type',
        'tags',
    ]
    readonly_fields = [
      'creation_time',
      'last_modified',
    ]

    # Validate the model as a whole
    def clean(self):
        if self.aoe_size is not None:
            if self.aoe_type is None:
                raise ValidationError(_('aoe_type is required when aoe_size is set.'))
