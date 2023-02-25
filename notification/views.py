from .tasks import send_notification
from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask,CrontabSchedule
def sendnotification(request):
    send_notification.delay()
    return HttpResponse("sent whatsapp message ")
#to perform the periodic task
def schedule_sms(request):
    schedule,created=CrontabSchedule.objects.get_or_create(hour=22,minute=18,day_of_month=23)
    task=PeriodicTask.objects.create(crontab=schedule,name="schedule_message_whatsapp"+"2",task="notification.tasks.send_notification")
    return HttpResponse('done scheduled a task')

    

