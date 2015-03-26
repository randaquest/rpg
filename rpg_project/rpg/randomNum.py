import random
from django.contrib.auth.models import User
from rpg.models import *


def isEvent(a):
    monsters = Monster.objects.filter(area=a)   
    for m in monsters:
        monsterchance = 100/(m.rarity + 2)
        if random.randint(1,100) <= monsterchance:
            return [True, m]
    return [False]

def Drop(m):
    drops = []
    for i in m.items.all():
       dropchance = m.rarity + 100/(i.rarity+1)
       if random.randint(1,100) <= dropchance:
           drops += [i]
    return drops
           

def whichArea(u):
    areas = Area.objects.all()
    while 1 == 1:
        for a in areas:
            chance = a.rarity +2
            if a == u.areaID and chance > 1:
                chance -= 1
            areachance = 100/chance
            if random.randint(1,100) <= areachance:
                return a

def damage(u):
    hitchance = 78 + (u.dexterity / 5)
    if random.randint(0,100) >= hitchance:
        miss = True
    else:
        miss = False
    critchance = u.dexterity / 2
    strength = u.strength
    if u.weapon is not None:
        minD = u.weapon.minD
        maxD = u.weapon.maxD
    else:
        minD = 2
        maxD = 12
    based = random.randint(minD,maxD)
    damage = based * 1+(strength/100)
    critical = random.randint(1,20)
    if random.randint(0,50) <= critchance:
        damage = 2*damage
        crit = True
    else:
        crit = False
    return [miss, crit, damage]

def monsterDamage(m, u):
    damage = random.randint(int(0.2*m.strength), m.strength) + int(0.25*u.level)
    return damage
        
