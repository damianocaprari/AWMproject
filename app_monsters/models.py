from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Monster(models.Model):
    CHALLENGE_RATING_CHOICES = (
      ('0', '0'),
      ('1/8', '1/8'),
      ('1/4', '1/4'),
      ('1/2', '1/2'),
      ('1', '1'),
      ('2', '2'),
      ('3', '3'),
      ('4', '4'),
      ('5', '5'),
      ('6', '6'),
      ('7', '7'),
      ('8', '8'),
      ('9', '9'),
      ('10', '10'),
      ('11', '11'),
      ('12', '12'),
      ('13', '13'),
      ('14', '14'),
      ('15', '15'),
      ('16', '16'),
      ('17', '17'),
      ('18', '18'),
      ('19', '19'),
      ('20', '20'),
    )

    ALIGNMENT_CHOICES = (
      ('Lawful Good', 'Lawful Good'),
      ('Neutral Good', 'Neutral Good'),
      ('Chaotic Good', 'Chaotic Good'),
      ('Lawful Neutral', 'Lawful Neutral'),
      ('True Neutral', 'True Neutral'),
      ('Chaotic Neutral', 'Chaotic Neutral'),
      ('Lawful Evil', 'Lawful Evil'),
      ('Neutral Evil', 'Neutral Evil'),
      ('Chaotic Evil', 'Chaotic Evil'),
    )

    HIT_DICE_CHOICES = (
      ('1d3', '1d3'),
      ('1d4', '1d4'),
      ('1d6', '1d6'),
      ('1d8', '1d8'),
      ('1d10', '1d10'),
      ('1d12', '1d12'),
    )

    SIZE_CHOICES = (
      ('Fine', 'Fine'),
      ('Diminutive', 'Diminutive'),
      ('Small', 'Tiny'),
      ('Medium', 'Medium'),
      ('Large', 'Large'),
      ('Huge', 'Huge'),
      ('Gargantuan', 'Gargantuan'),
      ('Colossal', 'Colossal'),
    )

    # owner = models.ForeignKey('auth.User', related_name='monsters', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', related_name='monsters', on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    version = models.CharField(max_length=256, null=True, blank=True)

    name = models.CharField(max_length=256, unique=True)
    size = models.CharField(max_length=256, choices=SIZE_CHOICES)
    type = models.CharField(max_length=256, null=True, blank=True)
    subtype = models.CharField(max_length=256, null=True, blank=True)
    alignment = models.CharField(max_length=256, choices=ALIGNMENT_CHOICES)
    armor_class = models.PositiveSmallIntegerField()
    armor_class_notes = models.CharField(max_length=256, null=True, blank=True)
    hit_point = models.PositiveSmallIntegerField()
    hit_dice = models.CharField(max_length=256, choices=HIT_DICE_CHOICES)
    # ## hp__notes = models.TextField(max_length=4000, null=True, blank=True)
    # speeds
    ability_str = models.PositiveSmallIntegerField()
    ability_dex = models.PositiveSmallIntegerField()
    ability_con = models.PositiveSmallIntegerField()
    ability_int = models.PositiveSmallIntegerField()
    ability_wis = models.PositiveSmallIntegerField()
    # ## ability_cha = models.PositiveSmallIntegerField()
    # saves
    # skills
    # damage_vulnerabilities
    # damage_resistances
    # condition_immunities
    # damage_immunities
    # senses
    # languages
    challenge_rating = models.CharField(max_length=256, choices=CHALLENGE_RATING_CHOICES)
    # special_abilities
    # actions
    # legendary_actions

    # ------------------ per ora NIENTE
    # description             = models #str
    # image_url               = models
    # initiative_modifier     = models.SmallIntegerField()
    # reactions
    # source                  = models.CharField(max_length=50, null=True, blank=True)
    # traits

    fields = [
      'author',
      'name',
      'version',
      'size',
      'type',
      'subtype',
      'alignment',
      'armor_class',
      'armor_class_notes',
      'hit_point',
      'hit_dice',
      # ## hp__notes = models.TextField(max_length=4000, null=True, blank=True)
      # speeds
      'ability_str',
      'ability_dex',
      'ability_con',
      'ability_int',
      'ability_wis',
      # ## ability_cha = models.PositiveSmallIntegerField()
      # saves
      # skills
      # damage_vulnerabilities
      # damage_resistances
      # condition_immunities
      # damage_immunities
      # senses
      # languages
      'challenge_rating',
      # special_abilities
      # actions
      # legendary_actions
    ]

    readonly_fields = [
      'creation_time',
      'last_modified',
    ]

    def __str__(self):
      return self.name

    class Meta(object):
      ordering = ['challenge_rating', 'name']
      unique_together = ('name', 'version')

    # Validate the model as a whole
    """
    def clean(self):
      if self.casting_time == 'OTHER':
        if self.casting_time_other is None:
          raise ValidationError(_('OTHER has been selected for Casting Time but no additional description has been provided.'))
    """


class MonsterAction(models.Model):
  monster = models.ForeignKey(Monster, related_name='actions', on_delete=models.CASCADE)
  desc = models.TextField(max_length=4000, null=True, blank=True)
  name = models.CharField(max_length=256, null=True, blank=True)
  attack_bonus = models.SmallIntegerField(default=0)
  damage_dice = models.CharField(max_length=256, null=True, blank=True)
  damage_bonus = models.SmallIntegerField(null=True, blank=True)

  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

  readonly_fields = [
    'creation_time',
    'last_modified',
  ]

  fields = [
    'monster',
    'name',
    'desc',
    'attack_bonus',
    'damage_dice',
    'damage_bonus',
  ]


class MonsterConditionImmunity(models.Model):
  monster = models.ForeignKey(Monster, related_name='condition_immunities', on_delete=models.CASCADE)
  condition_immunity = models.CharField(max_length=256, null=True, blank=True)

  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  readonly_fields = [
    'creation_time',
    'last_modified',
  ]

  fields = [
    'monster',
    'condition_immunity',
  ]


class MonsterDamageImmunity(models.Model):
  monster = models.ForeignKey(Monster, related_name='damage_immunities', on_delete=models.CASCADE)
  damage_immunity = models.CharField(max_length=256, null=True, blank=True)
  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  readonly_fields = [
    'creation_time',
    'last_modified',
  ]
  fields = [
    'monster',
    'damage_immunity',
  ]


class MonsterDamageResistance(models.Model):
  monster = models.ForeignKey(Monster, related_name='damage_resistances', on_delete=models.CASCADE)
  damage_resistance = models.CharField(max_length=256, null=True, blank=True)
  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  readonly_fields = [
    'creation_time',
    'last_modified',
  ]
  fields = [
    'monster',
    'damage_resistance',
  ]


class MonsterDamageVulnerability(models.Model):
  monster = models.ForeignKey(Monster, related_name='damage_vulnerabilities', on_delete=models.CASCADE)
  damage_vulnerability = models.CharField(max_length=256, null=True, blank=True)
  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  readonly_fields = [
    'creation_time',
    'last_modified',
  ]
  fields = [
    'monster',
    'damage_vulnerability',
  ]


class MonsterLanguage(models.Model):
  monster = models.ForeignKey(Monster, related_name='languages', on_delete=models.CASCADE)
  language = models.CharField(max_length=256, null=True, blank=True)
  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  readonly_fields = [
    'creation_time',
    'last_modified',
  ]
  fields = [
    'monster',
    'language',
  ]


class MonsterLegendaryAction(models.Model):
  monster = models.ForeignKey(Monster, related_name='legendary_actions', on_delete=models.CASCADE)
  attack_bonus = models.SmallIntegerField(default=0)
  content = models.TextField(max_length=4000, null=True, blank=True)
  name = models.CharField(max_length=256, null=True, blank=True)
  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  readonly_fields = [
    'creation_time',
    'last_modified',
  ]
  fields = [
    'monster',
    'attack_bonus',
    'content',
    'name',
  ]


class MonsterReaction(models.Model):
  monster = models.ForeignKey(Monster, related_name='reactions', on_delete=models.CASCADE)
  content = models.TextField(max_length=4000, null=True, blank=True)
  name = models.CharField(max_length=50, null=True, blank=True)
  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  readonly_fields = [
    'creation_time',
    'last_modified',
  ]


class MonsterSave(models.Model):
  monster = models.ForeignKey(Monster, related_name='saves', on_delete=models.CASCADE)
  modifier = models.SmallIntegerField(null=True, blank=True)
  name = models.CharField(max_length=256, null=True, blank=True)
  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  readonly_fields = [
    'creation_time',
    'last_modified',
  ]

  fields = [
    'monster',
    'modifier',
    'name'
  ]


class MonsterSense(models.Model):
  monster = models.ForeignKey(Monster, related_name='senses', on_delete=models.CASCADE)
  sense = models.CharField(max_length=256, null=True, blank=True)
  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  readonly_fields = [
    'creation_time',
    'last_modified',
  ]


class MonsterSkill(models.Model):
  SKILLS_CHOICES = (
    ('Athletics', 'Athletics'),
    ('Acrobatics', 'Acrobatics'),
    ('Sleight of Hand', 'Sleight of Hand'),
    ('Stealth', 'Stealth'),
    ('Arcana', 'Arcana'),
    ('History', 'History'),
    ('Investigation', 'Investigation'),
    ('Nature', 'Nature'),
    ('Religion', 'Religion'),
    ('Animal Handling', 'Animal Handling'),
    ('Insight', 'Insight'),
    ('Medicine', 'Medicine'),
    ('Perception', 'Perception'),
    ('Survival', 'Survival'),
    ('Deception', 'Deception'),
    ('Intimidation', 'Intimidation'),
    ('Performance', 'Performance'),
    ('Persuasion', 'Persuasion'),
  )
  monster = models.ForeignKey(Monster, related_name='skills', on_delete=models.CASCADE)
  modifier = models.SmallIntegerField(null=True, blank=True)
  name = models.CharField(max_length=256, null=True, blank=True, choices=SKILLS_CHOICES)
  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  readonly_fields = [
    'creation_time',
    'last_modified',
  ]

  fields = [
    'monster',
    'modifier',
    'name'
  ]


class MonsterSpeed(models.Model):
  monster = models.ForeignKey(Monster, related_name='speeds', on_delete=models.CASCADE)
  speed = models.CharField(max_length=256, null=True, blank=True)
  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

  readonly_fields = [
    'creation_time',
    'last_modified',
  ]

  fields = [
    'monster',
    'speed',
  ]


class MonsterTrait(models.Model):
  monster = models.ForeignKey(Monster, related_name='traits', on_delete=models.CASCADE)
  content = models.TextField(max_length=4000, null=True, blank=True)
  name = models.CharField(max_length=50, null=True, blank=True)
  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  readonly_fields = [
    'creation_time',
    'last_modified',
  ]


fields = [
  'monster',
  'name',
  'content',

]



class MonsterCA(models.Model):
  owner = models.ForeignKey(Monster, related_name='custom_attributes', on_delete=models.CASCADE)
  name = models.CharField(max_length=256)
  value = models.CharField(max_length=1000)
  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  readonly_fields = [
    'creation_time',
    'last_modified',
  ]

  fields = [
    'owner',
    'name',
    'vaule'
  ]


class MonsterSpecialAbilities(models.Model):
  monster = models.ForeignKey(Monster, related_name='special_abilities', on_delete=models.CASCADE)
  desc = models.TextField(max_length=4000, null=True, blank=True)
  name = models.CharField(max_length=256, null=True, blank=True)
  attack_bonus = models.SmallIntegerField(default=0)
  creation_time = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  readonly_fields = [
    'creation_time',
    'last_modified',
  ]

##### -- FAI N_CLEAN CON MESSAGGI DI ERRORE

# AC	                                dict
# AC___Notes	                        str
# AC___Value	                        int

# Abilities	                        dict
# Abilities___Cha	                int
# Abilities___Con	                int
# Abilities___Dex	                int
# Abilities___Int	                int
# Abilities___Str	                int
# Abilities___Wis	                int

# Actions	                        list
# Actions___xxx	                    dict
# Actions___xxx___Content	        str
# Actions___xxx___Name	            str
# Actions___xxx___Usage	            str

# Challenge	                        str

# ConditionImmunities	            list
# ConditionImmunities___xxx	        str

# DamageImmunities	                list
# DamageImmunities___xxx	            str

# DamageResistances	                list
# DamageResistances___xxx	        str

# DamageVulnerabilities	            list
# DamageVulnerabilities___xxx	    str
# Description	                    str
# HP	                                dict
# HP___Notes	                        str
# HP___Value	                        int
# Id	                                str
# ImageURL	                        str
# InitiativeModifier	                int
# Languages	                        list
# Languages___xxx	                str
# LegendaryActions	                list
# LegendaryActions___xxx	            dict
# LegendaryActions___xxx___Content	str
# LegendaryActions___xxx___Name	    str
# LegendaryActions___xxx___Usage	    str
# Name	                            str
# Player	                            str
# Reactions	                        list
# Reactions___xxx	                dict
# Reactions___xxx___Content	        str
# Reactions___xxx___Name	            str
# Reactions___xxx___Usage	        str
# Saves	                            list
# Saves___xxx	                    dict
# Saves___xxx___Modifier	            int
# Saves___xxx___Name	                str
# Senses	                            list
# Senses___xxx	                    str
# Skills	                            list
# Skills___xxx	                    dict
# Skills___xxx___Modifier	        int
# Skills___xxx___Name	            str
# Source	                            str
# Speed	                            list
# Speed___xxx	                    str
# Traits	                            list
# Traits___xxx	                    dict
# Traits___xxx___Content	            str
# Traits___xxx___Name	            str
# Traits___xxx___Usage	            str
# Type	                            str
