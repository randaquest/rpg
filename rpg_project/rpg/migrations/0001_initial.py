# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemID', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('picture', models.ImageField(upload_to=b'item_images', blank=True)),
                ('rarity', models.IntegerField(default=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('item_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rpg.Item')),
                ('defence', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=('rpg.item',),
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('monsterID', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('picture', models.ImageField(upload_to=b'monster_images', blank=True)),
                ('rarity', models.IntegerField(default=50)),
                ('difficulty', models.IntegerField(default=1)),
                ('boss', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usable',
            fields=[
                ('item_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rpg.Item')),
                ('effect', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=('rpg.item',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('level', models.IntegerField(default=1)),
                ('maxHP', models.IntegerField(default=100)),
                ('currentHP', models.IntegerField(default=100)),
                ('strength', models.IntegerField(default=10)),
                ('dexterity', models.IntegerField(default=10)),
                ('intelligence', models.IntegerField(default=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('item_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='rpg.Item')),
                ('minD', models.IntegerField(default=1)),
                ('maxD', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=('rpg.item',),
        ),
        migrations.AddField(
            model_name='inventory',
            name='itemID',
            field=models.ForeignKey(to='rpg.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inventory',
            name='userID',
            field=models.ForeignKey(to='rpg.UserProfile'),
            preserve_default=True,
        ),
    ]
