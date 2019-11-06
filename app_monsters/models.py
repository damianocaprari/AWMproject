from django.db import models


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
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Huge', 'Huge'),
        ('Gargantuan', 'Gargantuan'),
        ('Colossal', 'Colossal'),
    )

    author = models.ForeignKey('auth.User', related_name='monsters', on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    version = models.CharField(max_length=256, null=True, blank=True)

    name = models.CharField(max_length=256, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='avatars/monsters')
    size = models.CharField(max_length=256, choices=SIZE_CHOICES)
    type = models.CharField(max_length=256)
    subtype = models.CharField(max_length=256, null=True, blank=True)
    alignment = models.CharField(max_length=256, choices=ALIGNMENT_CHOICES)
    armor_class = models.PositiveSmallIntegerField()
    armor_class_notes = models.CharField(max_length=256, null=True, blank=True)
    hit_point = models.PositiveSmallIntegerField()
    hit_dice = models.CharField(max_length=256, choices=HIT_DICE_CHOICES)
    ability_str = models.PositiveSmallIntegerField()
    ability_dex = models.PositiveSmallIntegerField()
    ability_con = models.PositiveSmallIntegerField()
    ability_int = models.PositiveSmallIntegerField()
    ability_wis = models.PositiveSmallIntegerField()
    ability_cha = models.PositiveSmallIntegerField()

    challenge_rating = models.CharField(max_length=256, choices=CHALLENGE_RATING_CHOICES)

    # --------------
    traits = models.CharField(max_length=8192, null=True, blank=True)
    speeds = models.CharField(max_length=256, null=True, blank=True)
    saves = models.CharField(max_length=256, null=True, blank=True)
    skills = models.CharField(max_length=256, null=True, blank=True)

    damage_vulnerabilities = models.CharField(max_length=256, null=True, blank=True)
    damage_resistances = models.CharField(max_length=256, null=True, blank=True)
    condition_immunities = models.CharField(max_length=256, null=True, blank=True)
    damage_immunities = models.CharField(max_length=256, null=True, blank=True)

    senses = models.CharField(max_length=256, null=True, blank=True)
    languages = models.CharField(max_length=256, null=True, blank=True)
    special_abilities = models.CharField(max_length=8192, null=True, blank=True)
    actions = models.CharField(max_length=8192, null=True, blank=True)
    legendary_actions = models.CharField(max_length=8192, null=True, blank=True)

    fields = [
        'author',
        'name',
        'image',
        'version',
        'size',

        'type',
        'subtype',
        'alignment',
        'armor_class',
        'armor_class_notes',

        'hit_point',
        'hit_dice',
        'ability_str',
        'ability_dex',
        'ability_con',
        'ability_int',
        'ability_wis',
        'ability_cha',
        'challenge_rating',

        'traits',
        'speeds',
        'saves',
        'skills',
        'damage_vulnerabilities',
        'damage_resistances',
        'condition_immunities',
        'damage_immunities',
        'senses',
        'languages',
        'special_abilities',
        'actions',
        'legendary_actions',
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


class MonsterCA(models.Model):
    owner = models.ForeignKey(Monster, related_name='custom_attributes', on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=2048)
    value = models.CharField(max_length=8192)

    readonly_fields = [
        'creation_time',
        'last_modified',
    ]

    fields = [
        'owner',
        'name',
        'value',
    ]
