import os
import dotenv
import smtplib


class NotificationManager:

    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        dotenv.load_dotenv()
        self.sender_email = os.getenv("SENDER_EMAIL")
        self.sender_email_password = os.getenv("SENDER_EMAIL_PASSWORD")
        self.message = None

    def message_under_target(self, current_price, product_title, product_url, recipient_email):
        new_message = (f"Subject:Amazon Sale Alert\n\n"
                       "This product you've been watching:\n"
                       f"{product_title}\n\n"
                       f"Is now only {current_price}\n\n"
                       "Check it out at this link:\n"
                       f"{product_url}")
        self.message = new_message
        self.send_email(recipient_email=recipient_email)

    def message_over_target(self, current_price, product_title, product_url, lowest_price, recipient_email):
        new_message = (f"Subject:Amazon Sale Alert\n\n"
                       "This product you've been watching:\n"
                       f"{product_title}\n\n"
                       f"Is now selling for {current_price}\n\n"
                       f"The lowest price it's ever sold for is {lowest_price}\n\n"
                       "Check it out at this link:\n"
                       f"{product_url}")
        self.message = new_message
        self.send_email(recipient_email=recipient_email)

    def send_email(self, recipient_email):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.sender_email, password=self.sender_email_password)
            connection.sendmail(from_addr=self.sender_email,
                                to_addrs=recipient_email,
                                msg=self.message.encode("utf-8"))
