# Generated by Django 4.0.3 on 2022-03-16 18:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists_api', '0002_artist_albums'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='albums',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None), blank=True, null=True, size=None),
        ),
    ]
