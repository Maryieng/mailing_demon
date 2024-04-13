from django.db import models

from users.models import User


NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    letter_subject = models.CharField(max_length=250, verbose_name='Тема письма')
    body_letter = models.TextField(max_length=500, verbose_name='Тело письма')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", **NULLABLE)

    def __str__(self) -> str:
        return f"{self.letter_subject}"

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"
