# Generated by Django 4.0.3 on 2022-03-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0003_ratting_genre_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratting',
            name='genre_ids',
        ),
        migrations.AlterField(
            model_name='ratting',
            name='backdrop_path',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ratting',
            name='poster_path',
            field=models.CharField(max_length=255),
        ),
    ]