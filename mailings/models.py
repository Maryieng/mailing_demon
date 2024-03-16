from django.db import models

from clients.models import Clients
from letters.models import Message

NULLABLE = {'blank': True, 'null': True}


class Mailings(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]

    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'


    name = models.CharField(max_length=100, verbose_name='Имя рассылки', **NULLABLE)
    start_time = models.DateTimeField(verbose_name='Время начала рассылки')
    end_time = models.DateTimeField(verbose_name='Время окончания рассылки')
    frequency = models.CharField(max_length=15, choices=FREQUENCY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=15, default=CREATED, verbose_name='Статус рассылки')
    clients = models.ManyToManyField(Clients, verbose_name='Клиенты рассылки')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение", **NULLABLE)

    def __str__(self):
        return f"Рассылка: {self.name}, Периодичность: {self.frequency}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
