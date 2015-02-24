from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    level = models.IntegerField(default=1)
    maxHP = models.IntegerField(default=100)
    currentHP = models.IntegerField(default=100)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    
    def __unicode__(self):
        return self.user.username
    

class Monster(models.Model):
    monsterID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='monster_images', blank=True)
    rarity = models.IntegerField(default=50)
    difficulty = models.IntegerField(default=1)
    boss = models.BooleanField(default=False)

    def __unicode__(self):
                return self.name

class Item(models.Model): # Abstract class defining common attributes of all items
    itemID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='item_images', blank=True)
    rarity = models.IntegerField(default=50)

    def __unicode__(self):
        return self.name

class Weapon(Item):
    minD = models.IntegerField(default=1)
    maxD = models.IntegerField(default=1)

class Armor(Item):
    defence = models.IntegerField(default=1)

class Usable(Item):
    effect = models.IntegerField(default=0)

class Inventory(models.Model):
    userID = models.ForeignKey(UserProfile)
    itemID = models.ForeignKey(Item)
    
