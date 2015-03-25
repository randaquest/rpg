import random
from django.contrib.auth.models import User
from rpg.models import *


def isEvent():
    if random.randint(1,3) == 3:
        return True

def Drop(m):
    drops = []
##    if m.items.all().count() > 1:
    for i in m.items.all():
       dropchance = m.rarity + 100/(i.rarity ** 2)
       if random.randint(1,100) <= dropchance:
           drops += [i]
##    else:
##        i = Item.objects.get(m.items.all())
##        dropchance = m.rarity + 100/(i.rarity ** 2)
##        if random.randint(1,100) <= dropchance:
##               drops += i
    return drops
           

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

def monsterDamage(m, u):
    damage = random.randint(int(0.2*m.strength), m.strength) + int(0.25*u.level)
    return damage
        
