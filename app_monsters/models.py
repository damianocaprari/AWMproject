from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Monster__action(models.Model):
    monster = models.ForeignKey(Monster, related_name='actions')
    content = models.TextField(max_length=4000, null=True, blank=True)
    name    = models.CharField(max_length=50, null=True, blank=True)

class Monster__condition_immunity(models.Model):
    monster = models.ForeignKey(Monster, related_name='condition_immunities')
    condition_immunity = models.CharField(max_length=50, null=True, blank=True)

class Monster__damage_immunity(models.Model):
    monster = models.ForeignKey(Monster, related_name='damage_immunities')
    damage_immunity = models.CharField(max_length=50, null=True, blank=True)

class Monster__damage_resistance(models.Model):
    monster = models.ForeignKey(Monster, related_name='damage_resistances')
    damage_resistance = models.CharField(max_length=50, null=True, blank=True)

class Monster__damage_vulnerability(models.Model):
    monster = models.ForeignKey(Monster, related_name='damage_vulnerabilities')
    damage_vulnerability = models.CharField(max_length=50, null=True, blank=True)

class Monster__language(models.Model):
    monster = models.ForeignKey(Monster, related_name='languages')
    language = models.CharField(max_length=50, null=True, blank=True)

class Monster__legendary_action(models.Model):
    monster = models.ForeignKey(Monster, related_name='legendary_actions')
    content = models.TextField(max_length=4000, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

class Monster__reaction(models.Model):
    monster = models.ForeignKey(Monster, related_name='reactions')
    content = models.TextField(max_length=4000, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

class Monster__save(models.Model):
    monster = models.ForeignKey(Monster, related_name='saves')
    modifier = models.SmallIntegerField(null=True, blank=True)
    name     = models.CharField(max_length=50, null=True, blank=True)

class Monster__sense(models.Model):
    monster = models.ForeignKey(Monster, related_name='senses')
    sense = models.CharField(max_length=50, null=True, blank=True)

class Monster__skill(models.Model):
    monster = models.ForeignKey(Monster, related_name='skills')
    modifier = models.SmallIntegerField(null=True, blank=True)
    name     = models.CharField(max_length=50, null=True, blank=True)

class Monster__speed(models.Model):
    monster = models.ForeignKey(Monster, related_name='speeds')
    speed = models.CharField(max_length=50, null=True, blank=True)

class Monster__trait(models.Model):
    monster = models.ForeignKey(Monster, related_name='traits')
    content = models.TextField(max_length=4000, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

class Monster_av(models.Model):
    monster = models.ForeignKey(Monster, related_name='monster_av')
    name = models.CharField(max_length=256)
    value = models.CharField(max_length=1000)


class Monster(models.Model):
    owner = models.ForeignKey('auth.User', related_name='monsters', on_delete=models.CASCADE)

    ac__notes = models.TextField(max_length=4000, null=True, blank=True)
    ac__value = models.PositiveSmallIntegerField()
    ability_cha = models.PositiveSmallIntegerField()
    ability_con = models.PositiveSmallIntegerField()
    ability_dex = models.PositiveSmallIntegerField()
    ability_int = models.PositiveSmallIntegerField()
    ability_str = models.PositiveSmallIntegerField()
    ability_wis = models.PositiveSmallIntegerField()
    #actions
    challenge               = models.CharField(max_length=5, null=True, blank=True)
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
