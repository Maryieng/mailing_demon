import smtplib
from datetime import datetime, timedelta

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from mailings.models import Mailings
from reporting.models import Reporting


# def send_mailings(subject, message, email_list, mailings):
def send_mailings():
    current_time = timezone.localtime(timezone.now())
    mailings = Mailings.objects.all().exclude(status=Mailings.COMPLETED)
    for mailing in mailings:
        try:
            if mailing.end_time < current_time:
                mailing.status = Mailings.COMPLETED
                mailing.save()
                continue
            if mailing.start_time <= current_time < mailing.end_time:
                email_list = [client.client_email for client in mailing.clients.all()]
                server_response = send_mail(
                    subject=mailing.message.letter_subject,
                    message=mailing.message.body_letter,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=email_list,
                    fail_silently=False
                )
                Reporting.objects.create(status=server_response, mailings=mailing)
                if mailing.frequency == 'daily':
                    next_mailing_time = current_time + timedelta(days=1)
                elif mailing.frequency == 'weekly':
                    next_mailing_time = current_time + timedelta(weeks=1)
                elif mailing.frequency == 'monthly':
                    next_mailing_time = current_time + relativedelta(months=1)

                mailing.status = Mailings.STARTED
                mailing.start_time = next_mailing_time
                mailing.save()
        # elif current_datetime < mailing.end_time:
        # else:
        #     mailing.status = Mailings.COMPLETED
        #     mailing.save()

        except smtplib.SMTPException as e:
            Reporting.objects.create(status=False, mailings=mailings)
    # try:
    #     server_response = send_mail(subject=subject,
    #                                 message=message,
    #                                 from_email=settings.EMAIL_HOST_USER,
    #                                 recipient_list=email_list,
    #                                 fail_silently=False
    #                                 )
    #     Reporting.objects.create(status=server_response, mailings=mailings)
    # except smtplib.SMTPException as e:
    #     Reporting.objects.create(status=False, mailings=mailings)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailings, 'interval', days=1)
    scheduler.start()
