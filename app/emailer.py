import smtplib
import ssl
from jinja2 import Environment, FileSystemLoader
from email.mime.text import MIMEText
import os
# from dotenv import load_dotenv


def send_email(flavors):
    # load_dotenv()
    sender = os.getenv("EMAIL_USERNAME")
    reciever = os.getenv("RECIPIENT_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("email_template.html")

    html_output = template.render(flavors=flavors)

    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html_output)

    msg = MIMEText(html_output, "html", "utf-8")
    msg["Subject"] = "Culver's Flavor of the Day"
    msg["From"] = sender
    msg["To"] = reciever

    # Send securely
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
