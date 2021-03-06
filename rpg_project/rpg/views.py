from django.shortcuts import render
from rpg.models import *
from django.http import HttpResponseRedirect, HttpResponse
from rpg.forms import UserForm, UserProfileForm, MonsterForm, AreaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import exceptions
from rpg import randomNum


def game(request):
    try:
        u = request.user.userprofile
    except exceptions.ObjectDoesNotExist:
        return HttpResponseRedirect('/rpg/register')
    if u.inBattle:
        return battle(request)
    try:
        a = u.areaID
        if a is not None:
            area = a
        else:
            area = randomNum.whichArea(u)
    except exceptions.ObjectDoesNotExist:
        area = randomNum.whichArea(u)

        
    
    if request.method == 'POST':
        MonstersInArea = Monster.objects.filter(area=area).count()
        if MonstersInArea > 0:
            monsterEncounter = randomNum.isEvent(a,u)
            if monsterEncounter[0]:
                m = monsterEncounter[1]
                u.inBattle = True
                u.battle = Battle.objects.create(monster = m, mHP = m.maxHP)
                u.save()
                return battle(request)
        if 'n' in request.POST:
            u.coordY += 1
            area = randomNum.whichArea(u)
        elif 'e' in request.POST:
            u.coordX += 1
            area = randomNum.whichArea(u)
        elif 's' in request.POST:
            u.coordY -= 1
            area = randomNum.whichArea(u)
        elif 'w' in request.POST:
            u.coordX -= 1
            area = randomNum.whichArea(u)
        #For now not actually using the coordinates

    u.areaID = area
    u.save()
    l = Location.objects.filter(areaID=area.areaID)
    if l.count() > 0:
        loc = Location.objects.get(areaID=area.areaID)
        if loc.town:
            return town(request)
    hp = u.currentHP*100 / u.maxHP
    mana = u.currentMana*100 / u.maxMana
    exp = u.experience
    contextDict = { 'char' : u,'area' : area, 'hp' : hp, 'mana' : mana, 'exp' : exp}
    return render(request, 'rpg/game.html', contextDict)

def battle(request):
    try:
        u = request.user.userprofile
    except exceptions.ObjectDoesNotExist:
        return HttpResponseRedirect('/rpg/register')

    if u.inBattle:
        m = u.battle.monster
        action = False
        victory = False
        escape = False
        damage = [False, False, 0]
        mdamage = 0
        drops = []
        actionable = True
        gld = randomNum.gold(m)
        dropped = False
        attempt = False
        if request.method == 'POST':
            if 'continue' in request.POST:
                u.inBattle = False
                return game(request)
            if 'attack' in request.POST:
                action = True
                mdamage = randomNum.monsterDamage(m,u)
                u.currentHP -= mdamage
                damage = randomNum.damage(u)
                if damage[0] == False:
                    u.battle.mHP -= damage[2]
                if u.battle.mHP < 0:
                    u.battle.mHP = 0
            elif 'flee' in request.POST:
                attempt = True
                if randomNum.flee():
                    escape = True;
                else:
                    mdamage = randomNum.monsterDamage(m,u)
                    u.currentHP -= mdamage
                    escape = False;
            #elif 'spell' etc.
            if u.currentHP <= 0:
                u.currentHP = 0
                u.inBattle = False
                return death(request)
            elif u.battle.mHP <= 0:
                u.gold += gld
                u.experience += m.baseXP
                if u.experience > 100:
                    u.experience -= 100
                    u.level += 1
                    u.skillpoints += 3
                drops = randomNum.Drop(m)
                if drops != []:
                    dropped = True
                    for i in drops:
                        u.inventory.add(i)
                u.save()
                victory = True;
            u.battle.save()
            u.save()
        if victory or escape:
            actionable = False
        hp = u.currentHP*100 / u.maxHP
        mana = u.currentMana*100 / u.maxMana
        exp = u.experience
        monhp = u.battle.mHP*100 / m.maxHP
        contextDict = { 'char' : u, 'area' : u.areaID, 'monster' : m, 'victory' : victory, 'action' : action, 'mhp' : u.battle.mHP,
                        'damage' : damage[2], 'crit' : damage[1], 'miss' : damage[0],  'mdamage' : mdamage, 'hp' : hp, 'monhp' : monhp,
                        'exp' : exp, 'mana' : mana, 'drops' : drops, 'dropped' : dropped, 'gold' : gld, 'escape' : escape, 'actionable' : actionable,
                        'attempt' : attempt}
            
        return render(request, 'rpg/battle.html', contextDict)
    else:
        return game(request)


def town(request):
    u = request.user.userprofile
    a = u.areaID
    rested = False

    if request.method == 'POST':
        if 'rest' in request.POST:
            rested = True
            u.currentHP = u.maxHP
            u.currentMana = u.maxMana
            u.gold -= 10
            u.save()
        if 'shop' in request.POST:
            return HttpResponseRedirect('/rpg/shop')
        if 'highscores' in request.POST:
            return highscores(request)
        #if 'quests' in request.POST:
            #quests
    hp = u.currentHP*100 / u.maxHP
    mana = u.currentMana*100 / u.maxMana
    exp = u.experience
    contextDict = {'area' : a, 'char' : u, 'rested' : rested, 'hp' : hp, 'mana' : mana, 'exp' : exp}

    return render(request, 'rpg/town.html', contextDict)

def highscores(request):
    u = request.user.userprofile
    a = u.areaID
    rankings = UserProfile.objects.order_by('-level', '-experience')[:10]
    hp = u.currentHP*100 / u.maxHP
    mana = u.currentMana*100 / u.maxMana
    exp = u.experience
    contextDict = {'char' : u, 'area' : a, 'ranks' : rankings, 'hp' : hp, 'mana' : mana, 'exp' : exp}
    return render(request, 'rpg/highscores.html', contextDict)

def shop(request):
    u = request.user.userprofile
    check = Location.objects.filter(coordX=u.coordX, coordY=u.coordY).count()
    if check == 0:
        return HttpResponseRedirect('/rpg/game')
    a = u.areaID
    lvl = u.level/10
    purchased = False
    weaps = Weapon.objects.filter(rarity__lte=(3+lvl))
    armor = Armor.objects.filter(rarity__lte=(3+lvl))
    items = Item.objects.all()
    
    if request.method == 'POST':
        for i in items:
            if i.name in request.POST:
                if u.gold >= i.rarity*1000:
                    u.inventory.add(i)
                    u.gold -= i.rarity*1000
                    u.save()
                    purchased = True

    hp = u.currentHP*100 / u.maxHP
    mana = u.currentMana*100 / u.maxMana
    exp = u.experience
    contextDict = { 'char' : u, 'area' : a, 'weaps' : weaps, 'armor' : armor, 'p' : purchased, 'hp' : hp, 'mana' : mana, 'exp' : exp }

    return render(request, 'rpg/shop.html', contextDict)
            
    


def inventory(request):
    u = request.user.userprofile
    items = u.inventory.all()
    weapons = []
    armor = []
    reitems = []
    for i in items:
        if Weapon.objects.get(itemID = i.itemID):
            weapons += [Weapon.objects.get(itemID = i.itemID)]
        elif Armor.objects.get(itemID = i.itemID):
            armor += [Armor.objects.get(itemID = i.itemID)]
        else:
            reitems += [i]
    if request.method == 'POST':
        for i in weapons:
            if i.name in request.POST:
                u.weapon = i
                u.save()
        for i in armor:
            if i.name in request.POST:
                u.armor = i
                u.save()
    hp = u.currentHP*100 / u.maxHP
    mana = u.currentMana*100 / u.maxMana
    exp = u.experience
    contextDict = { 'char' : u, 'items' : reitems, 'weapons' : weapons, 'armor' : armor, 'hp' : hp, 'exp' : exp, 'mana' : mana, 'area' : u.areaID }
    return render(request, 'rpg/inventory.html', contextDict)

def status(request):
    u = request.user.userprofile
    if u.skillpoints > 0:
        leveled = True
    else: leveled = False

    if request.method == 'POST':
            if 'health' in request.POST:
                if leveled:
                    u.maxHP += 10
                    u.currentHP += 10
                    u.skillpoints -= 1
            if 'mana' in request.POST:
                if leveled:
                    u.maxMana += 10
                    u.currentMana += 10
                    u.skillpoints -= 1
            if 'strength' in request.POST:
                if leveled:
                    u.strength += 1
                    u.skillpoints -= 1
            if 'dexterity'  in request.POST:
                if leveled:
                    u.dexterity += 1
                    u.skillpoints -= 1
            if 'intelligence'  in request.POST:
                if leveled:
                    u.intelligence += 1
                    u.skillpoints -= 1
            if u.skillpoints <= 0:
                        leveled = False
            u.save()
    hp = u.currentHP*100 / u.maxHP
    mana = u.currentMana*100 / u.maxMana
    exp = u.experience
    contextDict = { 'char' : u, 'leveled' : leveled, 'hp' : hp, 'exp' : exp, 'mana' : mana, 'area' : u.areaID }
    return render(request, 'rpg/status.html', contextDict)
                    
    


    

def death(request):
    try:
        u = request.user.userprofile
    except exceptions.ObjectDoesNotExist:
        return redirect(register)
    u.maxHP = 100
    u.currentHP = 100
    u.strength = 10
    u.intelligence = 10
    u.dexterity = 10
    u.experience = 0
    u.skillpoints = 0
    u.level = 1
    u.coordX = 0
    u.coordY = 0
    u.gold = 0
    u.save()
    contextDict = {'char' : u, 'area' : u.areaID}
    return render(request, 'rpg/death.html', contextDict)
    


def index(request):

    return render(request, 'rpg/index.html')

def intro(request):
    return render(request, 'rpg/intro.html')

def create_monster(request):
    created = False

    if request.method == 'POST':
        monster_form = MonsterForm(data=request.POST)

        if monster_form.is_valid():
            monster = monster_form.save()
            if 'picture' in request.FILES:
                monster.picture = request.FILES['picture']
            monster.save()

            
            created = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print monster_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        monster_form = MonsterForm()

    # Render the template depending on the context.
    return render(request,
            'rpg/create_monster.html',
            {'monster_form': monster_form, 'created': created} )


def create_area(request):
    created = False

    if request.method == 'POST':
        area_form = AreaForm(data=request.POST)

        if area_form.is_valid():
            area = area_form.save()
            if 'picture' in request.FILES:
                area.picture = request.FILES['picture']
            area.save()

            
            created = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print area_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.

                # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
    else:
        area_form = AreaForm()

    # Render the template depending on the context.
    return render(request,
            'rpg/create_area.html',
            {'area_form': area_form, 'created': created} )

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'rpg/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
            if user:
                # Is the account active? It could have been disabled.
                if user.is_active:
                    # If the account is valid and active, we can log the user in.
                    # We'll send the user back to the homepage.
                    login(request, user)
                    return HttpResponseRedirect('/rpg/index')
                else:
                    # An inactive account was used - no logging in!
                    return HttpResponse("Your RPG account is disabled.")
            else:
                # Bad pw was provided. So we can't log the user in.
                print "Incorrect password: {0}, {1}".format(username, password)
                return HttpResponse("Incorrect password.")
        else:
                # Bad un was provided. So we can't log the user in.
                print "Incorrect username: {0}, {1}".format(username, password)
                return HttpResponse("Incorrect username.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'rpg/login.html', {})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/rpg/index')

def intro(request):
    return render(request, 'rpg/intro.html', {})

