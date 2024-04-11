from django_apscheduler import util

from apscheduler.jobstores.base import ConflictingIdError
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

from mailings.services import send_mailings


@util.close_old_connections
def start() -> None:
    """ scheduler to run the program every 10 minutes """
    scheduler = BackgroundScheduler()
    if scheduler.get_job('send_mailings'):
        scheduler.remove_job('send_mailings')
    try:
        scheduler.add_job(send_mailings, 'interval', id='send_mailings', seconds=10)
        scheduler.start()
    except ConflictingIdError as e:
        print(f"Error adding job: {e}")
