from django.db import models


class Clients(models.Model):
    name = models.CharField(max_length=80, verbose_name='ФИО')
    client_email = models.EmailField(max_length=50, verbose_name='Контактный email')
    comment = models.TextField(max_length=300, verbose_name='Комментарий')

    def __str__(self) -> str:
        return f'{self.name} {self.client_email}'

    class Meta:
        verbose_name = ("Клиент")
        verbose_name_plural = ("Клиенты")
