# Generated by Django 2.2.5 on 2020-03-19 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_auto_20200310_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='instant_book',
            field=models.CharField(choices=[('IsisAble', 'Availiable'), ('IsisAble', 'Disable')], max_length=20),
        ),
    ]
