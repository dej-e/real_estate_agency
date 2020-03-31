# Generated by Django 2.2.4 on 2020-03-31 17:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20200331_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL),
        ),
    ]
