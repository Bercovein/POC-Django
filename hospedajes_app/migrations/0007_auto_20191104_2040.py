# Generated by Django 2.2.6 on 2019-11-04 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0006_auto_20191104_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='fk_city',
            new_name='city',
        ),
    ]
