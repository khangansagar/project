# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20151117_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='support_status',
            name='status',
            field=models.CharField(default=b'Training', max_length=100, choices=[(b'training', b'Training'), (b'active', b'Active'), (b'less active', b'Less Active'), (b'independent', b'Independent'), (b'terminated', b'Terminated'), (b'completed', b'Completed')]),
        ),
    ]
