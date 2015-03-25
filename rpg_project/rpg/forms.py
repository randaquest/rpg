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
        widgets = {'level': forms.HiddenInput(), 'maxHP': forms.HiddenInput(), 'currentHP': forms.HiddenInput(),
                   'strength': forms.HiddenInput(), 'intelligence': forms.HiddenInput(), 'experience': forms.HiddenInput(), 'coordX': forms.HiddenInput(),
                   'coordY': forms.HiddenInput(),'inBattle': forms.HiddenInput(),'battle': forms.HiddenInput(),
                   'areaID': forms.HiddenInput(), 'skillpoints': forms.HiddenInput()}
#@admin required
class MonsterForm(forms.ModelForm):
    class Meta:
        model = Monster
        fields = ('name','picture','rarity','maxHP','boss','baseXP','area')

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
        fields = ('name','picture','rarity', 'backstory')
