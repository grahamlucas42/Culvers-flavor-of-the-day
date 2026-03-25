# app/main.py
import os
from fastapi import FastAPI, Header, HTTPException
from app.culvers import get_flavors
from app.emailer import send_email
# from dotenv import load_dotenv

app = FastAPI()

# load_dotenv()
API_KEY = os.getenv("API_KEY")


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/send-emails")
def trigger_email(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    flavors = get_flavors()
    send_email(flavors)
    return {"message": f"Sent: {len(flavors)} flavors"}
