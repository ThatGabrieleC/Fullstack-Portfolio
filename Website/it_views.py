from flask import Blueprint, render_template, request, current_app
from flask_mail import Message

it_views = Blueprint('it_views', __name__)

@it_views.route('/')
def italian_home():
    return render_template('it/home.html')

@it_views.route('/contact', methods=['POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(
            subject="Qualcuno vuole ASSUMERMIIIII",
            recipients=["elgabbuz@gmail.com"],
            body=f"{name} è stato catturato dal mio portafoglio, his infos:\nName: {name},\nEmail: {email},\n Message: {message}",
            sender=current_app.config['MAIL_USERNAME']
        )

        try:
            mail = current_app.extensions['mail']
            mail.send(msg)
            return render_template('it/success.html', message="Messaggio inviato con successo", redirect="Sarai reindirizzato automaticamente in:")
        except Exception as e:
            return render_template('it/success.html', message=f"C'è stato un errore nell'invio del messaggio. Errore: {str(e)}", render="Sarai reindirizzato automaticamente in:")