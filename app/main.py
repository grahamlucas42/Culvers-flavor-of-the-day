# app/main.py
from fastapi import FastAPI
from app.culvers import get_flavors
from app.emailer import send_email

app = FastAPI()


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/send-emails")
def trigger_email():
    flavors = get_flavors()
    send_email(flavors)
    return {"message": f"Sent: {len(flavors)} flavors"}
