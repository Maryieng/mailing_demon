from apscheduler.schedulers.background import BackgroundScheduler

from mailings.services import send_mailings


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailings, 'interval', minutes=10)
    scheduler.start()
