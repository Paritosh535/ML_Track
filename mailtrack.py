import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendmail(subject,sender_email, reveiver_email, body):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = reveiver_email
    try:
        text = f"""{body}"""
        part1 = MIMEText(text, "plain")
        message.attach(part1)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, cfg.SENDER_MAIL_PASSWORD)
            server.sendmail(
                cfg.SENDER_MAIL_ID, reveiver_email, message.as_string()
            )
        print("Mail Send..")
    except:
        print("Error..")
        
        
