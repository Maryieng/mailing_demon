from apscheduler.schedulers.background import BackgroundScheduler

from mailings.services import send_mailings


def start() -> None:
    """ scheduler to run the program every 10 minutes """
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailings, 'interval', minutes=10)
    scheduler.start()
