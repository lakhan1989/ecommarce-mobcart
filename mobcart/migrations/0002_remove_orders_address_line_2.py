# Generated by Django 4.1.3 on 2022-11-19 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobcart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address_line_2',
        ),
    ]
