from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from app.config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER


def make_call(to_number):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        response = VoiceResponse()
        response.say(
            "Emergency alert. The person using this safety system may need help. Please check your phone for location details.",
            voice="alice"
        )

        call = client.calls.create(
            twiml=str(response),
            to=to_number,
            from_=TWILIO_PHONE_NUMBER
        )

        print("Call initiated:", call.sid)
        return call.sid

    except Exception as e:
        print("Call failed:", e)