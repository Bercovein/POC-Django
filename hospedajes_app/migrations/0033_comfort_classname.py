# Generated by Django 2.2.6 on 2019-11-08 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0032_auto_20191108_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='comfort',
            name='className',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
