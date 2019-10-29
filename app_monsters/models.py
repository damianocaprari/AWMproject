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


    owner = models.ForeignKey('auth.User', related_name='monsters', on_delete=models.CASCADE)

    ac_notes = models.TextField(max_length=4000, null=True, blank=True)
    ac_value = models.PositiveSmallIntegerField()
    ability_cha = models.PositiveSmallIntegerField()
    ability_con = models.PositiveSmallIntegerField()
    ability_dex = models.PositiveSmallIntegerField()
    ability_int = models.PositiveSmallIntegerField()
    ability_str = models.PositiveSmallIntegerField()
    ability_wis = models.PositiveSmallIntegerField()
    #actions
    challenge_rating        =  models.CharField(max_length=256, choices=CHALLENGE_RATING_CHOICES)



    #condition_immunities
    #damage_immunities
    #damage_resistances
    #damage_vulnerabilities
    description             = models #str
    hp__notes = models.TextField(max_length=4000, null=True, blank=True)
    hp__value = models.PositiveSmallIntegerField()
    image_url               = models
    initiative_modifier     = models.SmallIntegerField()
    #languages
    #legendary_actions
    name                    = models.CharField(max_length=50, unique=True)
    #reactions
    #saves
    #senses
    #skills
    source                  = models.CharField(max_length=50, null=True, blank=True)
    #speeds
    #traits
    type                    = models.CharField(max_length=50, null=True, blank=True)


    fields = [
    ]

    #def __str__(self):
        #return '{} - {}'.format(self.level, self.name)

    # Validate the model as a whole
    #def clean(self):
        #if self.casting_time == 'OTHER':
            #if self.casting_time_other is None:
                #raise ValidationError(_('OTHER has been selected for Casting Time but no additional description has been provided.'))

    class Meta(object):
        pass
        #ordering = ['level', 'name']



class MonsterAction(models.Model):
    monster = models.ForeignKey(Monster, related_name='actions', on_delete=models.CASCADE())
    content = models.TextField(max_length=4000, null=True, blank=True)
    name    = models.CharField(max_length=50, null=True, blank=True)

class MonsterConditionImmunity(models.Model):
    monster = models.ForeignKey(Monster, related_name='condition_immunities', on_delete=models.CASCADE())
    condition_immunity = models.CharField(max_length=50, null=True, blank=True)

class MonsterDamageImmunity(models.Model):
    monster = models.ForeignKey(Monster, related_name='damage_immunities', on_delete=models.CASCADE())
    damage_immunity = models.CharField(max_length=50, null=True, blank=True)

class MonsterDamageResistance(models.Model):
    monster = models.ForeignKey(Monster, related_name='damage_resistances', on_delete=models.CASCADE())
    damage_resistance = models.CharField(max_length=50, null=True, blank=True)

class MonsterDamageVulnerability(models.Model):
    monster = models.ForeignKey(Monster, related_name='damage_vulnerabilities', on_delete=models.CASCADE())
    damage_vulnerability = models.CharField(max_length=50, null=True, blank=True)

class MonsterLanguage(models.Model):
    monster = models.ForeignKey(Monster, related_name='languages', on_delete=models.CASCADE())
    language = models.CharField(max_length=50, null=True, blank=True)

class MonsterLegendaryAction(models.Model):
    monster = models.ForeignKey(Monster, related_name='legendary_actions', on_delete=models.CASCADE())
    content = models.TextField(max_length=4000, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

class MonsterReaction(models.Model):
    monster = models.ForeignKey(Monster, related_name='reactions', on_delete=models.CASCADE())
    content = models.TextField(max_length=4000, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

class MonsterSave(models.Model):
    monster = models.ForeignKey(Monster, related_name='saves', on_delete=models.CASCADE())
    modifier = models.SmallIntegerField(null=True, blank=True)
    name     = models.CharField(max_length=50, null=True, blank=True)

class MonsterSense(models.Model):
    monster = models.ForeignKey(Monster, related_name='senses', on_delete=models.CASCADE())
    sense = models.CharField(max_length=50, null=True, blank=True)

class MonsterSkill(models.Model):
    monster = models.ForeignKey(Monster, related_name='skills', on_delete=models.CASCADE())
    modifier = models.SmallIntegerField(null=True, blank=True)
    name     = models.CharField(max_length=50, null=True, blank=True)

class MonsterSpeed(models.Model):
    monster = models.ForeignKey(Monster, related_name='speeds', on_delete=models.CASCADE())
    speed = models.CharField(max_length=50, null=True, blank=True)

class MonsterTrait(models.Model):
    monster = models.ForeignKey(Monster, related_name='traits', on_delete=models.CASCADE())
    content = models.TextField(max_length=4000, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

class MonsterCA(models.Model):
    owner = models.ForeignKey(Monster, related_name='custom_attributes', on_delete=models.CASCADE())
    name = models.CharField(max_length=256)
    value = models.CharField(max_length=1000)

##### -- FAI N_CLEAN CON MESSAGGI DI ERRORE

#AC	                                dict
#AC___Notes	                        str
#AC___Value	                        int

#Abilities	                        dict
#Abilities___Cha	                int
#Abilities___Con	                int
#Abilities___Dex	                int
#Abilities___Int	                int
#Abilities___Str	                int
#Abilities___Wis	                int

#Actions	                        list
#Actions___xxx	                    dict
#Actions___xxx___Content	        str
#Actions___xxx___Name	            str
#Actions___xxx___Usage	            str

#Challenge	                        str

#ConditionImmunities	            list
#ConditionImmunities___xxx	        str

#DamageImmunities	                list
#DamageImmunities___xxx	            str

#DamageResistances	                list
#DamageResistances___xxx	        str

#DamageVulnerabilities	            list
#DamageVulnerabilities___xxx	    str
#Description	                    str
#HP	                                dict
#HP___Notes	                        str
#HP___Value	                        int
#Id	                                str
#ImageURL	                        str
#InitiativeModifier	                int
#Languages	                        list
#Languages___xxx	                str
#LegendaryActions	                list
#LegendaryActions___xxx	            dict
#LegendaryActions___xxx___Content	str
#LegendaryActions___xxx___Name	    str
#LegendaryActions___xxx___Usage	    str
#Name	                            str
#Player	                            str
#Reactions	                        list
#Reactions___xxx	                dict
#Reactions___xxx___Content	        str
#Reactions___xxx___Name	            str
#Reactions___xxx___Usage	        str
#Saves	                            list
#Saves___xxx	                    dict
#Saves___xxx___Modifier	            int
#Saves___xxx___Name	                str
#Senses	                            list
#Senses___xxx	                    str
#Skills	                            list
#Skills___xxx	                    dict
#Skills___xxx___Modifier	        int
#Skills___xxx___Name	            str
#Source	                            str
#Speed	                            list
#Speed___xxx	                    str
#Traits	                            list
#Traits___xxx	                    dict
#Traits___xxx___Content	            str
#Traits___xxx___Name	            str
#Traits___xxx___Usage	            str
#Type	                            str
