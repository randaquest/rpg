import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rpg_project.settings')

import django
django.setup()

from rpg.models import Area, Monster, Item, Weapon, Armor


def populate():
    add_area('Cat Island','area_images/catisland.jpg','7','Meow meow, meow mew meow meow meow. Meow meow mew mew meow meow. Meow meow meow! Meowwwww!!!!')
    add_area('Mountains','area_images/mountains.jpg','3','Candy mountain candy mountain fill me with sweet sugary goodness. Here is mountains.')
    add_area('City','area_images/city.jpg','6','You are now in a city! With all the people hustling around, make sure you do not get run over by the taxis!')
    add_area('Closet','area_images/closet.jpg','5','This is your closet. The rug is soft beneath your feet. There are about 87 suits for you to pick from.')
    add_area('Forest','area_images/trees.jpg','4','You are in a forest. There are lots of tall trees and greenery. And animals. Yes.')
    add_area('Space','area_images/space.jpg','10','Space.')
    add_area('Desert','area_images/desert.jpg','6','Is this a mirage?! No, it is a desert. There is water over the hill... just kidding. Hope you brought your own.')
    add_area('Suburb','area_images/suburb.jpg','1','This is boring. Get out as soon as you can. Suburbia.')
    add_area('Sea','area_images/sea.jpg','4','Blub blub blub blub blub blub. You are in an ocean. Hope you can swim!')
    add_area('Tundra','area_images/ice.jpg','7','This is an arctic tundra. The cold wind whips over your bald head. You turn to the left, turn to the right, snow. That is all.')
    add_monster('LaserCat','monster_images/cat.jpg','7','20','False','17','20', Area.objects.get(name='Cat Island'))
    add_monster('Dodo','monster_images/Scenario2/dodo.jpg','3','10','False','11','7', Area.objects.get(name='Mountains'))
    add_monster('Salad Fingers','monster_images/Scenario3/saladfingers.jpg','6','5','False','3','8', Area.objects.get(name='City'))
    add_monster('Charlie the Unicorn','monster_images/Scenario4/charlie.jpg','5','16','False','13','10', Area.objects.get(name='Closet'))
    add_monster('Marcel the Shell with Shoes On','monster_images/Scenario5/marcel.jpg','10','35','False','25','18', Area.objects.get(name='Forest'))
    add_monster('Shark','monster_images/Scenario6/shark.jpg','2','18','False','16','18', Area.objects.get(name='Space'))
    add_monster('Nerd','monster_images/Scenario7/nerd.jpg','1','3','False','3','5', Area.objects.get(name='Desert'))
    add_monster('Ricky Wayne','monster_images/Scenario8/RickyWayne.jpg','10','38','False','30','25', Area.objects.get(name='Suburb'))
    add_monster('Nannerpuss','monster_images/Scenario9/nannerpuss.jpg','6','9','False','10','8', Area.objects.get(name='Sea'))
    add_monster('Slug','monster_images/Scenario10/slug.jpg','7','14','False','13','15', Area.objects.get(name='Tundra'))
    add_item('Pizza','item_images/pizza.jpg','10')
    add_item('Tampon','monster_images/Scenario6/tampon.jpg','1')
    add_item('Rock','monster_images/Scenario8/rock.jpg','1')
    add_weapon('Foam Sword','item_images/foam.jpg','1','3','8')
    add_weapon('Flamethrower','monster_images/Scenario3/FlameThrower.jpg','1','6','14')
    add_weapon('Hammer','monster_images/Scenario4/Hammer.jpg','1','2','4')
    add_weapon('Spork','monster_images/Scenario5/spork.jpg','1','9','16')
    add_weapon('Pillow','monster_images/Scenario7/Pillow.jpg','1','18','20')
    add_weapon('Nun Chucks','monster_images/Scenario9/NunChucks.jpg','1','5','10')
    add_weapon('Light Saber','monster_images/Scenario10/LightSaber.jpg','1','9','17')
    add_armor('armor of testing','picofarmoroftest','1','10')
    assign()

def assign():
    for i in Monster.objects.all():
        i.items.add(Weapon.objects.get(name='Pillow'))

def add_area(name, picture, rarity, backstory):
    a = Area.objects.get_or_create(name=name, picture=picture, rarity=rarity, backstory=backstory)[0]
    return a

def add_item(name, picture, rarity):
    i = Item.objects.get_or_create(name=name, picture=picture)[0]
    return i

def add_weapon(name, picture, rarity, minD, maxD):
    w = Weapon.objects.get_or_create(name=name, picture=picture, minD=minD, maxD=maxD, equippable=True)[0]
    return w

def add_armor(name, picture, rarity, defence):
    ar = Armor.objects.get_or_create(name=name, picture=picture, defence=defence, equippable=True)[0]
    return ar

def add_monster(name, picture, rarity, maxHP, boss, baseXP,strength, area):
    m = Monster.objects.get_or_create(name=name, picture=picture, rarity=rarity, maxHP=maxHP, boss=boss, baseXP=baseXP, strength=strength, area=area)[0]
    return m

# Start execution here!
if __name__ == '__main__':
    print "Starting Rpg population script..."
    populate()
