# Generated by Django 2.2.6 on 2019-11-15 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0045_auto_20191115_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospedajes_app.Property'),
        ),
    ]
