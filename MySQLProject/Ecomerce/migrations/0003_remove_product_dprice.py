# Generated by Django 4.0.1 on 2022-01-19 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomerce', '0002_product_dprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='dPrice',
        ),
    ]
