# Generated by Django 2.2.6 on 2019-11-06 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0011_auto_20191106_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentaldate',
            name='fk_booking',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hospedajes_app.Booking'),
        ),
    ]
