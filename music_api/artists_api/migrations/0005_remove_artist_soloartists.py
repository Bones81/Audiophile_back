# Generated by Django 4.0.3 on 2022-03-17 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists_api', '0004_remove_artist_albums'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='soloArtists',
        ),
    ]