# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('ph_number', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('skill_1', models.CharField(max_length=50)),
                ('skill_2', models.CharField(max_length=50)),
                ('skill_3', models.CharField(max_length=50)),
                ('skill_4', models.CharField(max_length=50)),
                ('Profile_pic', models.CharField(max_length=1000)),
                ('gender', models.CharField(max_length=15)),
                ('hire', models.CharField(max_length=20)),
            ],
        ),
    ]
