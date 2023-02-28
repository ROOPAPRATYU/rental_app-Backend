from django.urls import path
from. views import sendnotification,schedule_sms,send_email,schedule_mail,verify_payment_token,set_status,schedule_status

urlpatterns = [

    path("sendsms/",sendnotification,name="sendnotification"),
    path("scheduletask/",schedule_sms,name="sheduletask"),
    path("schedulemail/",schedule_mail,name="emailschedule"),
    path("sendmail/",send_email,name="sendemail"),
    path("varify/<str:token>",verify_payment_token),
    path("setstatus/",set_status,name="changestatus"),
    path("schedulestatus/",schedule_status,name="schedule_status")]
  