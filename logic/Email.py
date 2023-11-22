import smtplib, ssl
from email.parser import BytesParser, Parser
from email.policy import default
import os

class Email:
    @staticmethod
    def Send(subject: str, message: str, toaddrs: str) -> None:
        # Check if SMTP is configured
        if os.environ['SMTPPort'] != 0 or os.environ['SMTPPort'] is not None:
            # Initialise SMTP session
            with smtplib.SMTP_SSL(os.environ['SMTPServer'], int(os.environ['SMTPPort']), context=ssl.create_default_context()) as server:
                # Set the headers of the email
                headers = Parser(policy=default).parsestr(
                f"From: {os.environ['SMTPFrom']}\n"
                f"To: {toaddrs}\n"
                f"Subject: {subject}\n"
                "\n"
                f"This is a no-reply email, replies to this email will not be received!\n\n{message}\n")

                # Login into SMTP server and send the email
                server.login(os.environ['SMTPUsername'], os.environ['SMTPPassword'])
                server.send_message(headers)
                server.quit()
        else:
            print("SMTP is not configured! Email is below:")
            print(f"To: {toaddrs}\n" +f"Subject: {subject}\n" +"\n" +f"{message}\n")