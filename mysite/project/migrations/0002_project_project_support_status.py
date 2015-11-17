# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('Proj_id', models.AutoField(serialize=False, primary_key=True)),
                ('client', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('technology', models.CharField(max_length=100)),
                ('Sup_init_date', models.DateField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('consultant', models.ForeignKey(to='project.Consultant')),
                ('support', models.ForeignKey(to='project.Support')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Support_Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project', models.ForeignKey(to='project.Project')),
            ],
        ),
    ]
