# Generated by Django 2.2.4 on 2020-03-31 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='text',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]