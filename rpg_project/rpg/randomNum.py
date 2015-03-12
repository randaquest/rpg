from Maths import random
from rpg import models

def isEvent:
    if random.randint(1,3) == 3:
        return True

def isDrop:
    if random.randint(1,10) == 10:
        return True
    return False

def whichArea:
    areas = length(Area.objects.all())
    return random.randint(1,areas)

def whichMonster:
    monsters = length(Monsters.objects.all())
    return random.randint(1,monsters)

def damage:
    strength = request.user.strength
    damage = random.randint(0.5*strength, strength)
    critical = random.randint(1,20)
    if critical = 20:
        damage = 2*damage
    return damage
        
