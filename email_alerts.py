from flask_mail import Mail, Message
from flask import Flask
from dotenv import load_dotenv  # Add this to load environment variables from a .env file if you use it
import os

# Load the .env file (only needed if you're using a .env file)
load_dotenv()

app = Flask(__name__)

# Using environment variables instead of hardcoding email credentials
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')  # Fetch from environment variable
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')  # Fetch from environment variable
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

def send_email_alert(file_path):
    with app.app_context():
        msg = Message('File Integrity Alert', sender=os.getenv('EMAIL_USER'), recipients=['recipient-email@gmail.com'])
        msg.body = f"File changed: {file_path}"
        mail.send(msg)
