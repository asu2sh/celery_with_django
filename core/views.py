from django.shortcuts import HttpResponse
from .tasks import test_func

from send_mail_app.tasks import send_mail_func

from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json


def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Emails Sent!")


def schedule_mail(request):
    hour = 11
    minute = 0
    at = '' + hour + ':' + minute
    schedule, created = CrontabSchedule.objects.get_or_create(hour=hour, minute=minute)
    task = PeriodicTask.objects.create(
        crontab = schedule,
        task = 'send_mail_app.tasks.send_mail_func',
        name = f'schedule_mail_task_{at}',
        args = json.dumps((1, 2)),
    )
    return HttpResponse("Email Scheduled!")