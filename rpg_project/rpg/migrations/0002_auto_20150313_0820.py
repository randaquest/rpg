# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('areaID', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('picture', models.ImageField(upload_to=b'area_images', blank=True)),
                ('rarity', models.IntegerField(default=1)),
                ('backstory', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DropTables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rarity', models.IntegerField(default=0)),
                ('itemID', models.ForeignKey(to='rpg.Item')),
                ('monsterID', models.ForeignKey(to='rpg.Monster')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemTables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(default=0)),
                ('itemID', models.ForeignKey(to='rpg.Item')),
                ('userID', models.ForeignKey(to='rpg.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='itemID',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='userID',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
        migrations.RemoveField(
            model_name='item',
            name='rarity',
        ),
        migrations.AddField(
            model_name='monster',
            name='areaID',
            field=models.ForeignKey(default=1, to='rpg.Area'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monster',
            name='baseXP',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='areaID',
            field=models.ForeignKey(default=1, to='rpg.Area'),
            preserve_default=False,
        ),
    ]
