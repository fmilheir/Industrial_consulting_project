import smtplib 




def send_verification_email(user_email, verification_token, mail, app):
    with app.app_context():
        try:
            server = smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
            server.ehlo()  # Optional, can improve deliverability
            server.starttls()  # For secure connections
            server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])  

            message = f"Subject: Verify Your Account\n\nYour verification code is: {verification_token}" 
            server.sendmail(app.config['MAIL_USERNAME'], user_email, message)
            print('Email sent successfully') 
        except Exception as e:
            print(f'Failed to send verification email: {e}')
        finally:
            server.quit() 