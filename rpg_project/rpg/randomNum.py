import random
from django.contrib.auth.models import User
from rpg.models import *


def isEvent(a, u):
    monsters = Monster.objects.filter(area=a)   
    for m in monsters:
        monsterchance = 100/(m.rarity + 2)
        monstrength = m.maxHP + m.strength
        ustrength = 0.5*(u.maxHP + u.strength)
        if monstrength > ustrength:
            monsterchance = 0
        if random.randint(1,100) <= monsterchance:
            return [True, m]
    return [False]

def Drop(m):
    drops = []
    x = 2
    for i in m.items.all():
       dropchance = 100/(i.rarity+x)
       if random.randint(1,100) < dropchance:
           drops += [i]
           x += 1
    return drops

def flee():
    if random.randint(1,2) == 2:
        return True
    return False

def gold(m):
    basegold = m.rarity + m.baseXP
    return random.randint(1,10)*basegold
           

def whichArea(u):
    l = Location.objects.filter(coordX=u.coordX, coordY=u.coordY) #All locations with coords the same as our users
    if l.count() > 0:
        loc = Location.objects.get(coordX=u.coordX, coordY=u.coordY) #Since the query is non-empty, must have a result to get
        return Area.objects.get(areaID=loc.areaID) #return the result as an area object
    areas = Area.objects.all()
    nonlocations = []
    for a in areas:
        if Location.objects.filter(areaID=a.areaID).count() == 0: #Inheritance was meaning you could stumble onto static locations
            nonlocations += [a]                                   # This seperates the areas from static locations
    while 1 == 1:
        for a in nonlocations:
            chance = a.rarity +2
            if a == u.areaID and chance > 1:
                chance -= 1
            areachance = 100/chance
            if random.randint(1,100) <= areachance:
                return a

def damage(u):
    hitchance = 78 + (u.dexterity / 5) #78 means 80% hitchance at 10 dex and 98% at 100 dex
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
        
