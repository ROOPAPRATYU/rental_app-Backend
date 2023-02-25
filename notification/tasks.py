from celery import shared_task
from twilio.rest import Client
import datetime
from rental_application.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

from propertyManager.models import PropertyDetail
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
@shared_task(bind=True)
def send_notification(request):
    #collect ("email","rent_date","rent","phone_number") data from the propertydetails database table
    tenentdetails=PropertyDetail.objects.values_list("email","rent_date","rent","phone_number","tenant_name","property_name","bhk")
    for userinfo in tenentdetails:
        timing=datetime.datetime.today()
        message = client.messages.create(from_='whatsapp:+14155238886',body='Hi {} please pay your rent amount {} for property {}({}BHK) ,your rent on due please pay before {}/{}/{},if already paid please ignore it'.format(userinfo[4],userinfo[2],userinfo[5],userinfo[6],timing.day,timing.month,timing.year),to='whatsapp:+91{}'.format(userinfo[3]))
            
    return ('Great! Expect a message on whatsapp..')






    

