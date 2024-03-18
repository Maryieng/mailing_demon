# Generated by Django 5.0.2 on 2024-03-12 16:23
from typing import Any

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: list[Any] = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('client_email', models.EmailField(max_length=50, verbose_name='Контактный email')),
                ('comment', models.TextField(max_length=300, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
