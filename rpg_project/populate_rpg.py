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
    add_item('item of testing','picofitemoftest')
    add_weapon('sword of testing','picofswordoftest','3','6')
    add_armor('armor of testing','picofarmoroftest','10')

def add_area(name, picture, rarity, backstory):
    a = Area.objects.get_or_create(name=name, picture=picture, rarity=rarity, backstory=backstory)[0]
    return a

def add_item(name, picture):
    i = Item.objects.get_or_create(name=name, picture=picture)[0]
    return i

def add_weapon(name, picture, minD, maxD):
    w = Weapon.objects.get_or_create(name=name, picture=picture, minD=minD, maxD=maxD)[0]
    return w

def add_armor(name, picture, defence):
    ar = Armor.objects.get_or_create(name=name, picture=picture, defence=defence)[0]
    return ar

def add_monster(name, picture, rarity, maxHP, boss, baseXP, area):
    m = Monster.objects.get_or_create(name=name, picture=picture, rarity=rarity, maxHP=maxHP, boss=boss, baseXP=baseXP, area=area)[0]
    return m

# Start execution here!
if __name__ == '__main__':
    print "Starting Rpg population script..."
    populate()
