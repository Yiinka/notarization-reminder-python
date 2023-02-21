from ..config.sms_config import sms


def send_sms():
    response_data = sms.send_message(
        {
            "from": "Abram",
            "to": "2349028883120",
            "text": "What colour is the sky?",
        }
    )

    if response_data["messages"][0]["status"] == "0":
        return True
    else:
        return False
