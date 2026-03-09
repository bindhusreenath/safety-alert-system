from fastapi import APIRouter, BackgroundTasks
from typing import List
from pydantic import BaseModel
from app.services.sms_service import send_sms
from app.services.call_service import make_call
from app.database import save_alert

router = APIRouter()


class AlertRequest(BaseModel):
    user_name: str
    latitude: float
    longitude: float
    contacts: List[str]


import time

def process_alert(payload: AlertRequest):

    print("🚨 BACKGROUND TASK STARTED")

    location_link = f"https://maps.google.com/?q={payload.latitude},{payload.longitude}"

    sms_body = (
        f"EMERGENCY ALERT\n"
        f"{payload.user_name} needs help.\n"
        f"Location: {location_link}"
    )

    for number in payload.contacts[:3]:

        sms_success = False
        call_success = False

        # SMS Retry (3 attempts)
        for attempt in range(3):
            try:
                print(f"📩 Attempt {attempt+1}: Sending SMS to {number}")
                send_sms(number, sms_body)
                sms_success = True
                break
            except Exception as e:
                print("SMS failed:", e)
                time.sleep(2)

        # Call Retry (2 attempts)
        for attempt in range(2):
            try:
                print(f"📞 Attempt {attempt+1}: Calling {number}")
                make_call(number)
                call_success = True
                break
            except Exception as e:
                print("Call failed:", e)
                time.sleep(2)

        print("RESULT:", number, sms_success, call_success)


@router.post("/trigger-alert")
def trigger_alert(payload: AlertRequest, background_tasks: BackgroundTasks):
    """Core emergency trigger endpoint"""

    background_tasks.add_task(process_alert, payload)

    return {
        "status": "alert_triggered",
        "message": "Emergency alerts are being sent"
    }