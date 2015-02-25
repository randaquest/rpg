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

@admin required
class MonsterForm(forms.ModelForm):
    areas = Area.objects.all().values('name')
    areaID = forms.ChoiceField(choices=areas)
    class Meta:
        model = Monster
        fields = ('name','picture','rarity','difficulty','baseXP','areaID')

@admin required
class ItemForm(forms.ModelForm):
    monsters = Monster.objects.all().values('name')
    monsterID = forms.ChoiceField(choices=monsters)
    class Meta:
        model = Monster
        fields = ('name','picture','rarity','difficulty','baseXP','areaID')
