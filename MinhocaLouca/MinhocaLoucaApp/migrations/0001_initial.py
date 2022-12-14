# Generated by Django 4.1.3 on 2022-11-20 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('nickname', models.CharField(help_text='Entre com o nickname', max_length=20, primary_key=True, serialize=False)),
                ('email', models.EmailField(help_text='Informe o Email', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(choices=[('E', 'EASY'), ('M', 'NORMAL'), ('H', 'HARD')], max_length=1)),
                ('nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MinhocaLoucaApp.player')),
            ],
        ),
    ]
