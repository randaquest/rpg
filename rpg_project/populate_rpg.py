import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rpg_project.settings')

import django
django.setup()

from rpg.models import Area, Monster, Item


def populate():
    add_area('tutorial island','pictureofisland','0','A place for newbies')
    add_area('tutorial island2','pictureofisland','0','A place for newbies')
    add_area('tutorial island3','pictureofisland','0','A place for newbies')
    add_area('tutorial island4','pictureofisland','0','A place for newbies')

def add_area(name, picture, rarity, backstory):
    p = Area.objects.get_or_create(name=name, picture=picture, rarity=rarity, backstory=backstory)[0]
    return p

def add_monster(name, picture, rarity, difficulty, boss, baseXP, areaID):
    c = Monster.objects.get_or_create(name=name, picture=picture, rarity=rarity, difficulty=difficulty, boss=boss, baseXP=baseXP, areaID=areaID)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rpg population script..."
    populate()
