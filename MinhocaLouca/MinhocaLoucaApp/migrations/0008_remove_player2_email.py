# Generated by Django 4.1.2 on 2022-11-27 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MinhocaLoucaApp', '0007_player2_normalscore2_hardscore2_easyscore2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player2',
            name='email',
        ),
    ]
