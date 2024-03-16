from django.db import models

from mailings.models import Mailings

NULLABLE = {'blank': True, 'null': True}

class Reporting(models.Model):
    time_log = models.DateTimeField(verbose_name='Дата и время последней попытки', auto_now_add=True)
    status = models.BooleanField(verbose_name='Статус попытки')
    response = models.TextField(verbose_name='Ответ сервера', **NULLABLE)
    mailings = models.ForeignKey(Mailings, on_delete=models.CASCADE, verbose_name='Рассылка', **NULLABLE)

    def __str__(self):
        return f"{self.time_log}, {self.status},{self.response}"

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
