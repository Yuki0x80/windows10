# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name=b'coment', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='page',
            field=models.IntegerField(default=0, verbose_name=b'Page', blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=255, verbose_name=b'Company', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'BookName'),
        ),
        migrations.AddField(
            model_name='impression',
            name='book',
            field=models.ForeignKey(related_name='impressions', verbose_name=b'Book', to='app.Book'),
        ),
    ]
