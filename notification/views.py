from .tasks import send_notification,send_email_notification,change_status,send_mail_to_owner
from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask,CrontabSchedule
from propertyManager.models import PropertyDetail
from django.core.mail import send_mail
from rental_application.settings import EMAIL_HOST_USER
def sendnotification(request):
    send_notification.delay()
    return HttpResponse("sent whatsapp message ")
#to perform the periodic task
def schedule_sms(request):
    schedule,created=CrontabSchedule.objects.get_or_create(hour=12,minute=30,day_of_month=3)
    task=PeriodicTask.objects.create(crontab=schedule,name="schedule_message_whatsapp"+"4",task="notification.tasks.send_notification")
    return HttpResponse('done scheduled a task')

def send_email(request):
    send_email_notification.delay()
    return HttpResponse("sent email")

def schedule_mail(request):
    schedule,created=CrontabSchedule.objects.get_or_create(hour=00,minute=00,day_of_month=3)
    task=PeriodicTask.objects.create(crontab=schedule,name="schedule_email"+"1",task="notification.tasks.send_email_notification")
    return HttpResponse('done scheduled a task')

def verify_payment_token(request,token):
    try:
        obj=PropertyDetail.objects.get(rent_token=token)
        if obj.is_paid==False:
            obj.is_paid=True
            obj.save()
            send_mail_to_owner.delay(token=obj.rent_token)
            #send_email_to_owner.delay(token=obj.rent_token)
            return HttpResponse("Thank you for confirming your rent pay and sent email to owner with same confirmation")
        return HttpResponse("already verified with this user payment")
    except Exception as e:
        return HttpResponse("invalid token")

def set_status(request):
    change_status.delay()
    return HttpResponse("changed status for paid rent to not paid")

def schedule_status(request):
    schedule,created=CrontabSchedule.objects.get_or_create(hour=00,minute=00,day_of_month=1)
    task=PeriodicTask.objects.create(crontab=schedule,name="schedule_status"+"1",task="notification.tasks.change_status")
    return HttpResponse("done scheduled a task")