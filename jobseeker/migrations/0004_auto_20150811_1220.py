# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0003_auto_20150811_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='etat_civil',
            field=models.CharField(max_length=22, choices=[(b'Celibataire', b'Celibataire'), (b'Marie', b'Marie')]),
        ),
    ]
