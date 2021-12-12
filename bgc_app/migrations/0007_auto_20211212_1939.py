# Generated by Django 3.2.9 on 2021-12-12 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bgc_app', '0006_games_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='ownerfield',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='details',
            name='stars',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='games',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
