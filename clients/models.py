from django.db import models

class Clients(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    client_email = models.EmailField(max_length=50, verbose_name='Контактный email')
    comment = models.TextField(max_length=300, verbose_name='Комментарий')


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = ("Клиент")
        verbose_name_plural = ("Клиенты")
