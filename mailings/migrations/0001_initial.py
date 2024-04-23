# Generated by Django 5.0.2 on 2024-03-31 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('letters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя рассылки')),
                ('start_time', models.DateTimeField(verbose_name='Время начала рассылки')),
                ('end_time', models.DateTimeField(verbose_name='Время окончания рассылки')),
                ('frequency', models.CharField(choices=[('daily', 'Раз в день'), ('weekly', 'Раз в неделю'),
                                                        ('monthly', 'Раз в месяц')], max_length=15,
                                               verbose_name='Периодичность')),
                ('status', models.CharField(default='Создана', max_length=15, verbose_name='Статус рассылки')),
                ('clients', models.ManyToManyField(to='clients.clients', verbose_name='Клиенты рассылки')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                              to='letters.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
    ]
