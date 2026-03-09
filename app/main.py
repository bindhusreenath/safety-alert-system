from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.alert import router as alert_router
from app.database import init_db

init_db()

app = FastAPI(title="Safety Alert Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(alert_router)