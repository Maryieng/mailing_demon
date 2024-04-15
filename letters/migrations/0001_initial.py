# Generated by Django 5.0.2 on 2024-03-31 12:53
from typing import List, Any

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: List[Any] = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter_subject', models.CharField(max_length=250, verbose_name='Тема письма')),
                ('body_letter', models.TextField(max_length=500, verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
    ]
