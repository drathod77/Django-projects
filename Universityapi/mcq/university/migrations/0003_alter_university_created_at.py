# Generated by Django 4.0.3 on 2022-03-10 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_rename_universitycontacts_universitycontacts2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='created_at',
            field=models.IntegerField(),
        ),
    ]
