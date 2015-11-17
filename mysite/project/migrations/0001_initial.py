# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('Con_id', models.AutoField(serialize=False, primary_key=True)),
                ('Con_name', models.CharField(max_length=100)),
                ('Con_email', models.EmailField(max_length=70, unique=True, null=True, blank=True)),
                ('Con_phone', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('Sup_id', models.AutoField(serialize=False, primary_key=True)),
                ('Sup_name', models.CharField(max_length=100)),
                ('Sup_email', models.EmailField(max_length=70, unique=True, null=True, blank=True)),
                ('Sup_phone_india', models.IntegerField(default=0, null=True)),
                ('Sup_phone_usa', models.IntegerField(default=0, null=True)),
                ('Sup_DOJ', models.DateField()),
            ],
        ),
    ]
