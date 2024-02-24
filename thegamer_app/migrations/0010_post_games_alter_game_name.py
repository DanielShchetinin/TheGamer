# Generated by Django 5.0.2 on 2024-02-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thegamer_app', '0009_alter_game_release_date_alter_game_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='games',
            field=models.ManyToManyField(through='thegamer_app.GamePost', to='thegamer_app.game'),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
