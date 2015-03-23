import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rpg_project.settings')

import django
django.setup()

from rpg.models import Area, Monster, Item


def populate():
    add_area('tutorial island','pictureofisland','0','A place for newbies 1')
    add_area('tutorial island2','pictureofisland','0','A place for newbies 2')
    add_area('tutorial island3','pictureofisland','0','A place for newbies 3')
    add_area('tutorial island4','pictureofisland','0','A place for newbies 4')
    add_monster('newb1','picofnewb','0','10','False','10', Area.objects.get(name='tutorial island'))
    add_monster('newb2','picofnewb','0','10','False','10', Area.objects.get(name='tutorial island2'))
    add_monster('newb3','picofnewb','0','10','False','10', Area.objects.get(name='tutorial island3'))
    add_monster('newb4','picofnewb','0','10','False','10', Area.objects.get(name='tutorial island4'))

def add_area(name, picture, rarity, backstory):
    p = Area.objects.get_or_create(name=name, picture=picture, rarity=rarity, backstory=backstory)[0]
    return p

def add_monster(name, picture, rarity, maxHP, boss, baseXP, area):
    c = Monster.objects.get_or_create(name=name, picture=picture, rarity=rarity, maxHP=maxHP, boss=boss, baseXP=baseXP, area=area)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rpg population script..."
    populate()
