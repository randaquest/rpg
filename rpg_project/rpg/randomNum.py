import random
from django.contrib.auth.models import User
from rpg.models import *


def isEvent():
    if random.randint(1,3) == 3:
        return True

def isDrop():
    if random.randint(1,10) == 10:
        return True
    return False

def whichArea():
    areas = Area.objects.all().count()
    return random.randint(1,areas)

def whichMonster(a):
    monsters = Monster.objects.filter(area=a)
    index = monsters.count()-1
    monster = monsters[random.randint(0,index)]
    return monster

def damage(u):
    strength = u.strength
    damage = random.randint(1, strength)
    critical = random.randint(1,20)
    if critical == 20:
        damage = 2*damage
    return damage

def monsterDamage():
    return 2
        
