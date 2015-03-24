import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rpg_project.settings')

import django
django.setup()

from rpg.models import Area, Monster, Item, Weapon, Armor


def populate():
    add_area('Cat Island','/static/img/Scenario1/catisland.jpg','7','Meow meow, meow mew meow meow meow. Meow meow mew mew meow meow. Meow meow meow! Meowwwww!!!!')
    add_area('Mountains','/static/img/Scenario2/mountains.jpg','3','Candy mountain candy mountain fill me with sweet sugary goodness. Here is mountains.')
    add_area('City','/static/img/Scenario3/city.jpg','6','You are now in a city! With all the people hustling around, make sure you do not get run over by the taxis!')
    add_area('Closet','/static/img/Scenario4/closet.jpg','5','This is your closet. The rug is soft beneath your feet. There are about 87 suits for you to pick from.')
    add_area('Forest','/static/img/Scenario5/trees.jpg','4','You are in a forest. There are lots of tall trees and greenery. And animals. Yes.')
    add_area('Space','/static/img/Scenario6/space.jpg','10','Space.')
    add_area('Desert','/static/img/Scenario7/desert.jpg','6','Is this a mirage?! No, it is a desert. There is water over the hill... just kidding. Hope you brought your own.')
    add_area('Suburb','/static/img/Scenario8/suburb.jpg','1','This is boring. Get out as soon as you can. Suburbia.')
    add_area('Sea','/static/img/Scenario9/sea.jpg','4','Blub blub blub blub blub blub. You are in an ocean. Hope you can swim!')
    add_area('Tundra','/static/img/Scenario10/ice.jpg','7','This is an arctic tundra. The cold wind whips over your bald head. You turn to the left, turn to the right, snow. That is all.')
    add_monster('LaserCat','/static/img/Scenario1/cat.jpg','7','20','False','17', Area.objects.get(name='Cat Island'))
    add_monster('Dodo','/static/img/Scenario2/dodo.jpg','3','10','False','11', Area.objects.get(name='Mountains'))
    add_monster('Salad Fingers','/static/img/Scenario3/saladfingers.jpg','6','5','False','3', Area.objects.get(name='City'))
    add_monster('Charlie the Unicorn','/static/img/Scenario4/charlie.jpg','5','16','False','13', Area.objects.get(name='Closet'))
    add_monster('Marcel the Shell with Shoes On','/static/img/Scenario5/marcel.jpg','10','35','False','25', Area.objects.get(name='Forest'))
    add_monster('Shark','/static/img/Scenario6/shark.jpg','2','18','False','16', Area.objects.get(name='Space'))
    add_monster('Nerd','/static/img/Scenario7/nerd.jpg','1','3','False','3', Area.objects.get(name='Desert'))
    add_monster('Ricky Wayne','/static/img/Scenario8/RickyWayne.jpg','10','38','False','30', Area.objects.get(name='Suburb'))
    add_monster('Nannerpuss','/static/img/Scenario9/nannerpuss.jpg','6','9','False','10', Area.objects.get(name='Sea'))
    add_monster('Slug','/static/img/Scenario10/slug.jpg','7','14','False','13', Area.objects.get(name='Tundra'))
    add_item('Pizza','/static/img/Scenario1/pizza.jpg')
    add_item('Tampon','/static/img/Scenario6/tampon.jpg')
    add_item('Rock','/static/img/Scenario8/rock.jpg')
    add_weapon('Foam Sword','/static/img/Scenario2/foam.jpg','3','8')
    add_weapon('Flamethrower','/static/img/Scenario3/FlameThrower.jpg','6','14')
    add_weapon('Hammer','/static/img/Scenario4/Hammer.jpg','2','4')
    add_weapon('Spork','/static/img/Scenario5/spork.jpg','9','16')
    add_weapon('Pillow','/static/img/Scenario7/Pillow.jpg','18','20')
    add_weapon('Nun Chucks','/static/img/Scenario9/NunChucks.jpg','5','10')
    add_weapon('Light Saber','/static/img/Scenario10/LightSaber.jpg','9','17')
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
