# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_project_support_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project_Support_Status',
            new_name='Support_Status',
        ),
    ]
