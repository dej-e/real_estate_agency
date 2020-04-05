# Generated by Django 2.2.4 on 2019-08-29 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='construction_year',
            field=models.IntegerField(
                blank=True, db_index=True,
                null=True, verbose_name='Год постройки здания'
            ),
        ),
        migrations.AlterField(
            model_name='flat', name='living_area',
            field=models.IntegerField(
                blank=True, db_index=True,
                null=True, verbose_name='количество жилых кв.метров'
            ),
        ),
    ]
