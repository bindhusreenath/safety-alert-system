# Safety Alert System 🚨

A real-time emergency alert system that sends SMS and phone calls with GPS location when a panic button is pressed.

## Architecture

Flutter Mobile App → FastAPI Backend → Twilio Alerts

## Features

* Panic button
* Sends emergency SMS
* Initiates emergency call
* GPS location sharing
* Background alert processing
* Retry mechanism
* Alert logging

## Tech Stack

Frontend:

* Flutter

Backend:

* FastAPI
* Python

Services:

* Twilio SMS & Voice API

Database:

* SQLite

## Project Structure

```
app/                     FastAPI backend
mobile/safety_alert_app  Flutter application
```

## Running Backend

```
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

## Running Mobile App

```
cd mobile/safety_alert_app
flutter pub get
flutter run
```

## API Endpoint

```
POST /trigger-alert
```

Example payload:

```
{
"user_name": "Bindhu",
"latitude": 17.3850,
"longitude": 78.4867,
"contacts": ["+91XXXXXXXXXX"]
}
```

## Future Improvements

* Live location tracking
* Shake detection panic trigger
* Push notifications
* Firebase integration
* Emergency contact management
