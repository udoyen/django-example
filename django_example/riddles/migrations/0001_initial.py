# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Riddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riddle_text', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='riddle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riddles.Riddle'),
        ),
    ]
