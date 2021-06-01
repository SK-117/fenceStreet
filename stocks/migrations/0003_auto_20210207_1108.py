# Generated by Django 3.1.4 on 2021-02-07 11:08

import django.core.validators
from django.db import migrations
import stocks.models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20210207_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='symbol',
            field=stocks.models.SymbolField(max_length=5, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$')]),
        ),
    ]
