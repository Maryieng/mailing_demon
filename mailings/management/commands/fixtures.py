import os
from typing import Any

from django.core.management import BaseCommand, call_command


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> None:
        """ writes data for each application to files """
        os.environ["PYTHONIOENCODING"] = "utf-8"
        call_command("dumpdata", "blog", "-o", "fixtures/blog_data.json")
        call_command("dumpdata", "clients", "-o", "fixtures/clients_data.json")
        call_command("dumpdata", "letters", "-o", "fixtures/letters_data.json")
        call_command("dumpdata", "mailings", "-o", "fixtures/mailings_data.json")
        call_command("dumpdata", "reporting", "-o", "fixtures/reporting_data.json")
        call_command("dumpdata", "users", "-o", "fixtures/users_data.json")
        call_command("dumpdata", "auth.group", "-o", "fixtures/groups_data.json")
