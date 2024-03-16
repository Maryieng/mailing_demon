# Generated by Django 5.0.2 on 2024-03-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reporting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_log', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')),
                ('status', models.BooleanField(verbose_name='Статус попытки')),
                ('response', models.TextField(blank=True, null=True, verbose_name='Ответ сервера')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]