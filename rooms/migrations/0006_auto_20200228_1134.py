# Generated by Django 2.2.5 on 2020-02-28 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20200227_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='instant_blokc',
            new_name='instant_block',
        ),
    ]
