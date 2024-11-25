from flask import Blueprint, render_template, request, current_app
from flask_mail import Message
import time

en_views = Blueprint('en_views', __name__)

@en_views.route('/')
def english_home():
    return render_template('en/home.html')

@en_views.route('/contact', methods=['POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(
            subject="Someone wants to HIRE MEEE",
            recipients=["G.Certo@proton.me"],
            body=f"{name} got interested by my portfolio, his infos: \nName: {name},\nEmail: {email},\nMessage: {message} ",
            sender=current_app.config['MAIL_USERNAME']
        )

        try:
            mail = current_app.extensions['mail']
            mail.send(msg)
            return render_template('en/success.html', message="Message sent successfully!", redirect='You will be redirected automatically in:')
        except Exception as e:
            return render_template('en/success.html', message=f'Failed to send the message. Error: {str(e)}', redirect='You will be reidrected automatically in:')
    
