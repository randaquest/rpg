from django import forms
from django.contrib.auth.models import User
from rpg.models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

#@admin required
class MonsterForm(forms.ModelForm):
    #Needs a way to add multiple items.
    areas = Area.objects.all().values('name')
    areaID = forms.ChoiceField(choices=areas)
    class Meta:
        model = Monster
        fields = ('name','picture','rarity','difficulty','baseXP','areaID')

#@admin required
#class ItemForm(forms.ModelForm):
    #Need a way to define type - Weap, Armor or usable
   # class Meta:
       # model = Item
        #fields = ('name','picture','rarity','difficulty','baseXP')

#@admin required
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('name','picture','rarity')
