import smtplib
from email.mime.text import MIMEText

SENDER_EMAIL = "tumharaemail@gmail.com"
APP_PASSWORD = "xxxx xxxx xxxx xxxx"   # Gmail App Password
RECEIVER_EMAIL = "receiveremail@gmail.com"

msg = MIMEText("🎯 New Exam Alert!\nSSC ka naya notice aaya hai.")
msg["Subject"] = "Exam Alert Test"
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SENDER_EMAIL, APP_PASSWORD)
server.send_message(msg)
server.quit()

print("✅ Email sent successfully")