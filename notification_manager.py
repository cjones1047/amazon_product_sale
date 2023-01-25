import os
import dotenv
import smtplib


class NotificationManager:

    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        dotenv.load_dotenv()
        self.sender_email = os.getenv("SENDER_EMAIL")
        self.sender_email_password = os.getenv("SENDER_EMAIL_PASSWORD")

    def create_email_body(self):
        pass

    def send_email(self, recipient_email, subject, body):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.sender_email, password=self.sender_email_password)
            connection.sendmail(from_addr=self.sender_email,
                                to_addrs=recipient_email,
                                msg=f"Subject:{subject}\n\n{body}")
