# Generated by Django 4.1.2 on 2022-11-22 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MinhocaLoucaApp', '0003_alter_score_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='difficulty',
            field=models.CharField(choices=[('E', 'EASY'), ('M', 'NORMAL'), ('H', 'HARD')], max_length=1),
        ),
    ]
