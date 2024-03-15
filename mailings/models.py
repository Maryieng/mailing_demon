from django.db import models

from clients.models import Clients

NULLABLE = {'blank': True, 'null': True}


class Mailings(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]
    name = models.CharField(max_length=100, verbose_name='Имя рассылки', **NULLABLE)
    start_time = models.DateTimeField(verbose_name='Время начала рассылки')
    end_time = models.DateTimeField(verbose_name='Время окончания рассылки')
    frequency = models.CharField(max_length=15, choices=FREQUENCY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, verbose_name='Статус рассылки')
    clients = models.ManyToManyField(Clients, verbose_name='Клиенты рассылки')

    def __str__(self):
        return f"Рассылка: {self.name}, Время: {self.start_time} | {self.end_time}, Статус: {self.status}, Периодичность: {self.frequency}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class Message(models.Model):
    letter_subject = models.CharField(max_length=250, verbose_name='Тема письма')
    body_letter = models.TextField(max_length=500, verbose_name='Тело письма')

    def __str__(self):
        return f"Тема письма: {self.letter_subject}"

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"
