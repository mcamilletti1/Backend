# Generated by Django 4.2.3 on 2023-07-22 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disabilityscene', '0003_alter_movie_disabilities_alter_movie_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='accuracy_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='casting_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='character_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='originality_score',
            field=models.FloatField(),
        ),
    ]
