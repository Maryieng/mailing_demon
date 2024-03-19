from apscheduler.triggers.cron import CronTrigger
from django_apscheduler import util

from apscheduler.jobstores.base import ConflictingIdError
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from mailings.services import send_mailings


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)

def start() -> None:
    """ scheduler to run the program every 10 minutes """
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    if scheduler.get_job('send_mailings'):
        scheduler.remove_job('send_mailings')
    try:
        scheduler.add_job(send_mailings, 'interval', id='send_mailings', seconds=10)
        scheduler.add_job(
            delete_old_job_executions, trigger=CronTrigger(day_of_week="mon", hour="00", minute="00"),
            id="delete_old_job_executions", max_instances=1, replace_existing=True,)
        scheduler.start()
    except ConflictingIdError as e:
        print(f"Error adding job: {e}")
