# Generated by Django 5.0.2 on 2024-03-16 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0002_reporting_mailings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporting',
            name='response',
        ),
    ]