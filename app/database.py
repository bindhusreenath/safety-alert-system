import sqlite3

def init_db():
    conn = sqlite3.connect("alerts.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        latitude REAL,
        longitude REAL,
        contact TEXT,
        sms_status TEXT,
        call_status TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_alert(user_name, lat, lon, contact, sms_status, call_status):
    conn = sqlite3.connect("alerts.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO alerts (user_name, latitude, longitude, contact, sms_status, call_status)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (user_name, lat, lon, contact, sms_status, call_status))

    conn.commit()
    conn.close()