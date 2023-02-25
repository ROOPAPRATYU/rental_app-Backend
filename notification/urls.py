from django.urls import path
from. views import sendnotification,schedule_sms

urlpatterns = [
    
    path("sendsms/",sendnotification,name="sendnotification"),
    path("scheduletask/",schedule_sms,name="sheduletask")]
  