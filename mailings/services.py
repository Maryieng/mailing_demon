import smtplib
from smtplib import SMTPException

from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail

from mailings.models import Mailings
from reporting.models import Reporting


# def send_mailings(mailing):
#     now = timezone.localtime(timezone.now())
#     mailing_list = Mailings.objects.all()
#     for mailing in mailing_list:
#         if mailing.start_time <= now <= mailing.end_time:
#             for message in mailing.messages.all():
#                 for client in mailing.clients.all():
#                     try:
#                         result = send_mail(
#                             subject=message.title,
#                             message=message.text,
#                             from_email=settings.EMAIL_HOST_USER,
#                             recipient_list=[client.email],
#                             fail_silently=False
#                         )
#                         log = Reporting.objects.create(
#                             time=mailing.start_time,
#                             status=result,
#                             server_response='OK',
#                             mailing_list=mailing,
#                             client=client
#                         )
#                         log.save()
#                         return log
#                     except SMTPException as error:
#                         log = Reporting.objects.create(
#                             time=mailing.start_time,
#                             status=False,
#                             server_response=error,
#                             mailing_list=mailing,
#                             client=client
#                         )
#                         log.save()
#                     return log
#         else:
#             mailing.status = Mailings.COMPLETED
#             mailing.save()


def send_mailings(subject, message, email_list, mailings):
    try:
        server_response = send_mail(subject=subject,
                                    message=message,
                                    from_email=settings.EMAIL_HOST_USER,
                                    recipient_list=email_list,
                                    fail_silently=False
                                    )
        Reporting.objects.create(status=server_response, mailings=mailings)
    except smtplib.SMTPException as e:
        Reporting.objects.create(status=False, mailings=mailings)

