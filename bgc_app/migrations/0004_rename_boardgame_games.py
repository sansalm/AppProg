# Generated by Django 3.2.9 on 2021-12-11 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgc_app', '0003_review_stars'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BoardGame',
            new_name='Games',
        ),
    ]
