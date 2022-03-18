# Generated by Django 4.0.3 on 2022-03-16 18:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='albums',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None),
        ),
    ]
