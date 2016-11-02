# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161029_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('category', models.CharField(max_length=255, verbose_name=b'Category', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='impression',
            name='book',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Impression',
        ),
    ]
