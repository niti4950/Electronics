# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-14 07:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.Category'),
        ),
    ]
