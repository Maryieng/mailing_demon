from django.core.management import BaseCommand

from mailings.start_scheduler import start


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options) -> None:
        """ function to run the scheduler from the terminal """
        start()
