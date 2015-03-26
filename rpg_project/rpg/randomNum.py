import random
from django.contrib.auth.models import User
from rpg.models import *


def isEvent(a):
    monsters = Monster.objects.filter(area=a)   
    for m in monsters:
        if m == whichMonster(a):
            return [True, m]
    return [False]

def Drop(m):
    drops = []
    for i in m.items.all():
       dropchance = m.rarity + 100/(i.rarity ** 2)
       if random.randint(1,100) <= dropchance:
           drops += [i]
    return drops
           

def whichArea():
    areas = Area.objects.all().count()
    return random.randint(1,areas)

def whichMonster(a):
    monsters = Monster.objects.filter(area=a)
    index = monsters.count()-1
    monster = monsters[random.randint(0,index)]
    monsterChance = monster.rarity * 10
    monsterRandomizer = random.randint(10,200)
    if monsterChance == monsterRandomizer:
        if monsterRandomizer == 100:
            return monster
    elif monsterChance == 90 and monsterRandomizer >= 90:
        return monster
    elif monsterChance == 80 and monsterRandomizer >= 80:
        return monster
    elif monsterChance == 70 and monsterRandomizer >= 70:
        return monster
    elif monsterChance == 60 and monsterRandomizer >= 60:
        return monster
    elif monsterChance == 50 and monsterRandomizer >= 50:
        return monster
    elif monsterChance == 40 and monsterRandomizer >= 40:
        return monster
    elif monsterChance == 30 and monsterRandomizer >= 30:
        return monster
    elif monsterChance == 20 and monsterRandomizer >= 20:
        return monster
    elif monsterChance == 10 and monsterRandomizer >= 10: # FIX THIS
        return monster

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
        
