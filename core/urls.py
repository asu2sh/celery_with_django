from django.urls import path
from .views import test, send_mail_to_all, schedule_mail

urlpatterns = [
    path('', test, name='test'),
    path('send_mail', send_mail_to_all, name='sendmail'),
    path('schedule_mail', schedule_mail, name='schedulemail'),
]