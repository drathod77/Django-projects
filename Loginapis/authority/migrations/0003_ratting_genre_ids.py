# Generated by Django 4.0.3 on 2022-03-03 06:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0002_ratting'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratting',
            name='genre_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=1, size=None),
            preserve_default=False,
        ),
    ]
