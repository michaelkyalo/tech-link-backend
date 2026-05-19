from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
class EmailService:

    @staticmethod
    def send_email(to_email, subject, message):
        import os
        

        email = Mail(
            from_email="noreply@agrilink.com",
            to_emails=to_email,
            subject=subject,
            html_content=message
        )

        try:
            sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
            response = sg.send(email)
            return response.status_code

        except Exception as error:
            print(error)
            return None