# Generated by Django 5.0.2 on 2024-04-11 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('set_is_active', 'Активация пользователя')], 'verbose_name': 'Пользователь',
                     'verbose_name_plural': 'Пользователи'},
        ),
    ]
