from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os

load_dotenv()

# mail_username = os.getenv('MAIL_USERNAME')
# mail_password = os.getenv('MAIL_PASSWORD')
# mail_sender = os.getenv('MAIL_DEFAULT_SENDER')
# print(f"MAIL_USERNAME: {mail_username}")
# print(f"MAIL_PASSWORD: {mail_password}")
# print(f"MAIL_DEFAULT_SENDER: {mail_sender}")

def create_app():
    load_dotenv()

    portfolio = Flask(__name__)
    portfolio.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    portfolio.config['MAIL_SERVER'] = 'smtp.gmail.com'
    portfolio.config['MAIL_PORT'] = 587
    portfolio.config['MAIL_USE_TLS'] = True
    portfolio.config['MAIL_USE_SSL'] = False
    portfolio.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    portfolio.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    portfolio.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

    mail = Mail(portfolio)

    portfolio.extensions['mail'] = mail

    from .en_views import en_views
    from .it_views import it_views

    portfolio.register_blueprint(en_views, url_prefix='/en/')
    portfolio.register_blueprint(it_views, url_prefix='/it/')
    
    return portfolio

