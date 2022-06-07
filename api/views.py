from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User,Message
from twilio.rest import Client
from whatsapp_api import settings
from lorem_text import lorem
from random import choice
import os 
from dotenv import load_dotenv
load_dotenv(dotenv_path=f"{settings.BASE_DIR}/.env")
client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
@csrf_exempt
def whatsAppGet(request):
    try:
        if(request.META['REQUEST_METHOD']=="POST"):
            data=request.POST
            user_name=data['ProfileName']
            user_number=data['WaId']
            user_from=data['From']
            message=data['Body']
            user=User.objects.filter(number=user_number)
            if(not user):
                user=User(number=user_number,name=user_name)
                user.save()
            else:
                user=user[0]
            message_obj=Message(user=user,message=message)
            message_obj.save()
            response_message=generateResponse(message,user_name)
            client.messages.create(body=response_message,from_=f"whatsapp:{os.getenv('HOST_NUMBER')}",to=user_from)
            return JsonResponse({"status":True})
        return JsonResponse({"status":False})
    except Exception as e:
        print(e)
        return JsonResponse({"status":False})

def generateResponse(message:str,name:str):
    if(message.lower()=="hi"):
        return f"Hello {name}!"
    elif(message.lower()=="hello"):
        return f"Hi {name} Whats Up!"
    else:
        dummy_text=[lorem.sentence,lorem.paragraph]
        func=choice(dummy_text)
        return f"{name} ! {func()}"