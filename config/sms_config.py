import vonage
from decouple import config


client = vonage.Client(key=config("SMS_API_KEY"), secret=config("SMS_SECRET_KEY"))
sms = vonage.Sms(client)

