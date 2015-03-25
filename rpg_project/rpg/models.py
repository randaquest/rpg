from django.db import models
from django.contrib.auth.models import User

class Area(models.Model):
     areaID = models.AutoField(primary_key=True)
     name = models.CharField(max_length=128)
     picture = models.ImageField(upload_to='area_images', blank=True)
     rarity = models.IntegerField(default=1)
     backstory = models.CharField(max_length=128)

     def __unicode__(self):
                return self.name

class Item(models.Model): # Abstract class defining common attributes of all items
    itemID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='item_images', blank=True)
    rarity = models.IntegerField(default=1)
    equippable = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
     
class Weapon(Item):
    minD = models.IntegerField(default=1)
    maxD = models.IntegerField(default=1)

class Armor(Item):
    defence = models.IntegerField(default=1)

class Usable(Item):
    effect = models.IntegerField(default=0)

class Monster(models.Model):
    monsterID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='monster_images', blank=True)
    rarity = models.IntegerField(default=50)
    maxHP = models.IntegerField(default=10)
    boss = models.BooleanField(default=False)
    baseXP = models.IntegerField(default=10)
    strength = models.IntegerField(default=10)
    items = models.ManyToManyField(Item, blank=True, null=True)
    area = models.ForeignKey(Area, default=0)

    def __unicode__(self):
                return self.name

class Battle(models.Model):
    battleID = models.AutoField(primary_key=True)
    monster = models.ForeignKey(Monster, default=0)
    mHP = models.IntegerField(default=10)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    level = models.IntegerField(default=1, blank=False)
    weapon = models.ForeignKey(Weapon, related_name="wielder+", null=True)
    armor  = models.ForeignKey(Armor, related_name="wearer+", null=True)
    maxHP = models.IntegerField(default=100, blank=False)
    currentHP = models.IntegerField(default=100, blank=False)
    maxMana = models.IntegerField(default=100, blank=False)
    currentMana = models.IntegerField(default=100, blank=False)
    strength = models.IntegerField(default=10, blank=False)
    skillpoints = models.IntegerField(default=0, blank=False)
    dexterity = models.IntegerField(default=10, blank=False)
    intelligence = models.IntegerField(default=10, blank=False)
    experience = models.IntegerField(default=0, blank=False)
    coordX = models.IntegerField(default=0, blank=False)
    coordY = models.IntegerField(default=0, blank=False)
    inBattle = models.BooleanField(default=False, blank=False)
    battle = models.ForeignKey(Battle, blank=True, null=True)
    inventory = models.ManyToManyField(Item, blank=True, null=True)
    areaID = models.ForeignKey(Area, blank=True, null=True)
    
    def __unicode__(self):
        return self.user.username
    
    
