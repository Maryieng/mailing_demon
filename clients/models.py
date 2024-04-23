from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Clients(models.Model):
    name = models.CharField(max_length=80, verbose_name='ФИО')
    client_email = models.EmailField(max_length=50, verbose_name='Контактный email')
    comment = models.TextField(max_length=300, verbose_name='Комментарий')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", **NULLABLE)

    def __str__(self) -> str:
        return f'{self.name} {self.client_email}'

    class Meta:
        verbose_name = ("Клиент")
        verbose_name_plural = ("Клиенты")
