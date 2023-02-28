from celery import shared_task
from twilio.rest import Client
import datetime
from rental_application.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from django.core.mail import send_mail
from rental_application.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from user_profile.models import OwnerProfile



from propertyManager.models import PropertyDetail
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
@shared_task(bind=True)
def send_notification(request):
    #collect ("email","rent_date","rent","phone_number") data from the propertydetails database table
    tenentdetails=PropertyDetail.objects.values_list("email","rent_date","rent","phone_number","tenant_name","property_name","bhk")
    for userinfo in tenentdetails:
        timing=datetime.datetime.today()
        message = client.messages.create(from_='whatsapp:+14155238886',body='Hi {} please pay your rent amount {} for property {}({}BHK) ,your rent on due please pay before {}/{}/{},if already paid please ignore it'.format(userinfo[4],userinfo[2],userinfo[5],userinfo[6],timing.day,timing.month,timing.year),to='whatsapp:+91{}'.format(8880869502))
            
    return ('Great! Expect a message on whatsapp..')

@shared_task(bind=True)
def send_email_notification(request):
    owner=OwnerProfile.objects.values_list("first_name")
    owner1=OwnerProfile.objects.values_list("last_name")
    tenentdetails=PropertyDetail.objects.values_list("email","rent_date","rent","phone_number","tenant_name","property_name","bhk","is_paid","rent_token","is_tenant_active")
    for userinfo in tenentdetails:
        timing=datetime.datetime.today()
        month=timing.month
        year=timing.year
        if userinfo[0] is not None and userinfo[7]==False and userinfo[9]==True:
            #curent_site=get_current_site(request)
            subject = "Property {} Rent Remeinder".format(userinfo[5])
            msg=render_to_string("duenotification.html",{
                "tenant_name":userinfo[4],
                "property_name":userinfo[5],
                "bhk":userinfo[6],
                "rent_amount":userinfo[2],
                "living":userinfo[1],
                "rent_token":userinfo[8],
                "month":month,
                "year":year,
                "owner_name":owner[0],
                "owner":owner1[0]

                #"domain":curent_site
            })
            to =  userinfo[0] 
            send_mail(subject,msg,EMAIL_HOST_USER, [to])
    return ("great expect a message on ur email")
   
@shared_task(bind=True)
def change_status(request):
    tenentdetails=PropertyDetail.objects.values_list("is_tenant_active","is_paid")
    try:
        obj=PropertyDetail.objects.get(is_paid=True)
        for userinfo in tenentdetails:
            if userinfo[0]==True and userinfo[1]==True:
                obj.is_paid=False
                obj.save()
        return ("changed the status for is_paid rent")
    except:
        return ("no change in status")

 


    

