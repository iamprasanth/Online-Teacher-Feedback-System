# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fusioncharts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='India',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('State', models.CharField(max_length=50)),
                ('Code', models.CharField(max_length=50)),
                ('Population', models.CharField(max_length=50)),
            ],
        ),
    ]
