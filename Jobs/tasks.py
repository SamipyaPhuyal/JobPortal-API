from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email(app_id):
    subject='Job Application'
    message='You have been selected for the job'
    return send_mail(subject,message,settings.DEFAULT_FROM_EMAIL,[app_id])