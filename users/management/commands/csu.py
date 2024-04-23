from typing import Any

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args: Any, **kwargs: Any) -> None:
        """ creating a superuser """
        user = User.objects.create(
            email='kassionio.o@yandex.ru',
            first_name='Admin',
            last_name='Sky',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('12345')
        user.save()
