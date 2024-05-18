import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(from_address, to_address, subject, body, smtp_server, smtp_port, login, password):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection

        # Log in to the email account
        server.login(login, password)

        # Send the email
        server.send_message(msg)
        print(f"Email sent successfully to {to_address}")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        # Close the connection to the SMTP server
        server.quit()

if __name__ == "__main__":
    from_address = "your_email@gmail.com"
    to_address = "recipient_email@example.com"
    subject = "Test Email"
    body = "This is a test email sent from a Python script."
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    login = "your_email@gmail.com"
    password = "your_email_password"  # Use an app-specific password if you have two-factor authentication enabled

    send_email(from_address, to_address, subject, body, smtp_server, smtp_port, login, password)
