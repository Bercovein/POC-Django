# Generated by Django 2.2.6 on 2019-11-07 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospedajes_app', '0017_auto_20191107_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Features',
            },
        ),
    ]
