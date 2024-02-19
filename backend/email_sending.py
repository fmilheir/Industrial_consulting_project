from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = ''
app.config['MAIL_SERVER'] = ''
app.config['MAIL_USE_TLS'] = ''
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
mail = Mail(app)


def send_verification_email(user_email, verification_code):
    msg = Message('Verify Your Account',
                  sender='your-email@example.com',
                  recipients=[user_email])
    msg.body = f'Your verification code is: {verification_code}'
    mail.send(msg)