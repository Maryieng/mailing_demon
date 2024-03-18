from django.apps import AppConfig


class MailingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailings'

    def ready(self) -> None:
        """ Starts the scheduler along with the server """
        from . import start_scheduler
        start_scheduler.start()
