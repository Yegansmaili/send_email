import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(receiver_email, subject, message):
    sender_email = "your email"
    sender_password = "your password"


    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Success")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    receiver_email = input("email:")
    subject = input("subject:")
    message = input("your message:")

    send_email(receiver_email, subject, message)
