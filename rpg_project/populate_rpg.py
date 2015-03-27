import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rpg_project.settings')

import django
django.setup()

from rpg.models import Area, Monster, Item, Weapon, Armor, Location


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
    add_area('Beach','area_images/Beach.jpg','6','You are at the beach. Hope you brought your sunscreen.')
    add_area('Cave','area_images/Cave.jpg','5','You are in a cave! Filled with magic water... and bats.')
    add_area('Ruins','area_images/Ruins.jpg','9','Oh no everybody is dead.')
    add_monster('LaserCat','monster_images/cat.jpg','7','15','False','34','5', Area.objects.get(name='Cat Island'))
    add_monster('Spider-Dog','monster_images/SpiderDog.jpg','7','9','False','20','5', Area.objects.get(name='Cat Island'))
    add_monster('Dodo','monster_images/dodo.jpg','3','5','False','21','3', Area.objects.get(name='Mountains'))
    add_monster('Octopuslaphantasuarus','monster_images/Dinolephant.jpg','4','18','False','32','7', Area.objects.get(name='Mountains'))
    add_monster('Salad Fingers','monster_images/saladfingers.jpg','6','5','False','6','4', Area.objects.get(name='City'))
    add_monster('Puppet','monster_images/puppet.jpg','8','9','False','26','5',Area.objects.get(name='City'))
    add_monster('The Hero Glasgow Deserves','monster_images/PinkBatman.jpg','5','18','False','35','8',Area.objects.get(name='City'))
    add_monster('Charlie the Unicorn','monster_images/charlie.jpg','5','12','False','26','5', Area.objects.get(name='Closet'))
    add_monster('Monkey','monster_images/Monkey.jpg','4','6','False','6','5', Area.objects.get(name='Closet'))
    add_monster('Marcel the Shell with Shoes On','monster_images/marcel.jpg','10','25','False','50','6', Area.objects.get(name='Forest'))   
    add_monster('Ricky Wayne','monster_images/RickyWayne.jpg','10','31','False','50','14', Area.objects.get(name='Suburb'))
    add_monster('Honey Boo Boo','monster_images/Honeybooboo.jpg','7','30','False','25','9', Area.objects.get(name='Suburb'))
    add_monster('Slug','monster_images/slug.jpg','3','9','False','26','5', Area.objects.get(name='Tundra'))
    add_monster('Tele Tubby Roid','monster_images/Tubbyroids.jpg','7','20','False','30','15', Area.objects.get(name='Tundra'))    
    add_monster('Snowman','monster_images/Snowman.jpg','2','3','False','16','3', Area.objects.get(name='Cave'))
    add_monster('Emperor Kardashian Supremus','monster_images/Evil.jpg','9','40','False','40','15', Area.objects.get(name='Cave')
    add_monster('Kraken','monster_images/kraken.jpg','4','9','False','18','5',Area.objects.get(name='Beach'))
    add_monster('Crabulon','monster_images/Crab.jpg','8','25','False','20','4', Area.objects.get(name='Beach'))
    add_monster('Godzilla','monster_images/Godzilla.jpg','8','20','False','30','8',Area.objects.get(name='Ruins'))
    add_monster('Mc Precious','monster_images/Mcprecious.jpg','3','10','False','15','3',Area.objects.get(name='Ruins'))
    add_monster('Bruce Jenner','monster_images/Bruce.jpg','1','2','False','14','2', Area.objects.get(name='Desert'))
    add_monster('Nerd','monster_images/nerd.jpg','2','3','False','6','5', Area.objects.get(name='Desert'))
    add_monster('T rex','monster_images/Trex.jpg','6','20','False','25','13', Area.objects.get(name='Desert'))
    add_monster('Shark','monster_images/shark.jpg','2','15','False','32','6', Area.objects.get(name='Space'))
    add_monster('Snake','monster_images/Snake.jpg','8','6','False','24','5', Area.objects.get(name='Space'))
    add_monster('Emperor Fabulontious','monster_images/Fabulonto.jpg','8','22','False','24','9', Area.objects.get(name='Space'))    
    add_monster('Nannerpuss','monster_images/nannerpuss.jpg','6','9','False','20','4', Area.objects.get(name='Sea'))
    add_monster('Tha Alpha Goldfish','monster_images/Obesegoldfish.jpg','7','25','False','19','9', Area.objects.get(name='Sea'))
    add_item('Pizza','item_images/pizza.jpg','10')
    add_item('Tampon','item_images/tampon.jpg','3')
    add_item('Rock','item_images/rock.jpg','1')
    add_weapon('FoamSword','item_images/foam.jpg','2','4','14')
    add_weapon('Flamethrower','item_images/FlameThrower.jpg','9','25','38')
    add_weapon('Hammer','item_images/Hammer.jpg','3','9','19')
    add_weapon('Spork','item_images/spork.jpg','2','9','16')
    add_weapon('Pillow','item_images/Pillow.jpg','3','6','20')
    add_weapon('NunChucks','item_images/NunChucks.jpg','8','5','10')
    add_weapon('LightSaber','item_images/LightSaber.jpg','6','9','17')
    add_armor('armorofTesting','picofarmoroftest','3','10')
    add_location('Crestpine Village','area_images/crestpine.jpg','1','The sleepy little village of Crestpine.. what secrets does it hold?','0','0',True)
    add_location('Barbarica DC','area_images/barbarian.jpg','3','You can smell the stench emanating from the city for miles, the brutal capital of the Barbarians is not for the weak of scent. Legend says that their ruler has not bathed for millenna','45','32',True)    assign()
    add_location('Monkeytopia','area_images/Monkeycity.jpg','7','The City of the Monkeys, better known as Dinotopia by the resident dinosaur population','65','65',True)
def assign():
    for i in Monster.objects.all():
        i.items.add(Weapon.objects.get(name='Pillow'))
        i.items.add(Weapon.objects.get(name='NunChucks'))
        i.items.add(Weapon.objects.get(name='Hammer'))
        i.items.add(Weapon.objects.get(name='Flamethrower'))
        i.items.add(Weapon.objects.get(name='LightSaber'))
        i.items.add(Weapon.objects.get(name='Spork'))
        i.items.add(Weapon.objects.get(name='FoamSword'))

def add_area(name, picture, rarity, backstory):
    a = Area.objects.get_or_create(name=name, picture=picture, rarity=rarity, backstory=backstory)[0]
    return a

def add_location(name, picture, rarity, backstory, coordX, coordY, town):
    l = Location.objects.get_or_create(name=name, picture=picture, rarity=rarity, backstory=backstory, coordX=coordX, coordY=coordY, town=town)[0]
    return l

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
