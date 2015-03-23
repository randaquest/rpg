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
        return redirect(register)
    if u.inBattle:
        return battle(request)
    try:
        a = u.areaID
        area = Area.objects.get(areaID)
    except exceptions.ObjectDoesNotExist:
        for ar in Area.objects.filter(areaID=randomNum.whichArea()):
            area = ar

        
    
    if request.method == 'POST':
        if 'n' in request.POST:
            u.coordY += 1
        elif 'e' in request.POST:
            u.coordX += 1
        elif 's' in request.POST:
            u.coordY -= 1
        elif 'w' in request.POST:
            u.coordX -= 1
        #For now not actually using the coordinates
        for ar in Area.objects.filter(areaID=randomNum.whichArea()):
            area = ar
        request.user.areaID = area
        if randomNum.isEvent():
            m = randomNum.whichMonster(area)
            u.inBattle = True
            u.battle = Battle.objects.create(monster = m, mHP = m.maxHP)
            u.save()
            return battle(request)

    request.user.areaID = area
    u.save()
        



    contextDict = { 'char' : u,'area' : area }
    return render(request, 'rpg/game.html', contextDict)

def battle(request):
    try:
        u = request.user.userprofile
    except exceptions.ObjectDoesNotExist:
        return redirect(reigster)

    action = False
    victory = False
    damage = 0
    mdamage = 0
    if u.inBattle:
        m = u.battle.monster
        if request.method == 'POST':
            if 'continue' in request.POST:
                u.inBattle = False
                u.experience += m.baseXP
                if u.experience > 100:
                    u.experience -= 100
                    u.level += 1
                u.save()
                return game(request)
            if 'attack' in request.POST:
                action = True
                mdamage = randomNum.monsterDamage()
                u.currentHP -= mdamage
                damage = randomNum.damage(u)
                u.battle.mHP -= damage
                #elif 'spell' etc.
                if u.currentHP <= 0:
                    u.inBattle = False
                    return death(request)
                elif u.battle.mHP <= 0:
                  #if isDrop():
                      #ItemTables.objects.get_or_create(itemID, u)
                    victory = True;
            u.battle.save()
            u.save()
        hp = str(u.currentHP*100 / u.maxHP)+'%'
        contextDict = { 'char' : u, 'monster' : m, 'victory' : victory, 'action' : action, 'mhp' : u.battle.mHP, 'damage' : damage, 'mdamage' : mdamage, 'hp' : hp }
            
        return render(request, 'rpg/battle.html', contextDict)
    else:
        return game(request)

def death(request):
    try:
        u = request.user.userprofile
    except exceptions.ObjectDoesNotExist:
        return redirect(reigster)
    u.maxHP = 100
    u.strength = 10
    u.intelligence = 10
    u.dexterity = 10
    u.experience = 0
    u.level = 1
    return render('You feel the world slipping away as you fall to the ground breathless... Hazy you awake, with nothing but a sliver of life')
    


def index(request):

    return render(request, 'rpg/index.html')

def create_monster(request):
    created = False

    if request.method == 'POST':
        monster_form = MonsterForm(data=request.POST)

        if monster_form.is_valid():
            monster = monster_form.save()
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
            area.save()

            
            created = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print area_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
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
                    return HttpResponseRedirect('/rpg/')
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
    return HttpResponseRedirect('/rpg/')
