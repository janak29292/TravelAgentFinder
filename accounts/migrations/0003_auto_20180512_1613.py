# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-12 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180512_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='payment_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Payment'),
        ),
    ]
