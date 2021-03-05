#!/usr/bin/python3

from email.message import EmailMessage
import getpass, mimetype, os, smtplib

def get_mime(attachment_path):
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    return (mime_type, mime_subtype)

def create_message_obj(sender, recipient, subject, body, attachment_path):
    message = EmailMessage()

    # create message header
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject

    # create message body
    message.set_content(body)

    # add attachment
    with open(attachment_path, 'rb') as f:
        mimetype = get_mime(attachment_path)
        message.add_attachement(
            f.read(),
            maintype=mimetype[0],
            subtype=mimetype[1],
            filename=os.path.basename(attachment_path)
        )
    return message

def main():
    sender = ''
    recipient = ''
    subject = ''
    body = ''''''
    attachment_path = ''

    # create message
    message = create_message_obj(sender, recipient, subject, body, attachment_path)

    # initialize SMTP connection and send the message
    try:
        mail_server = smtplib.SMTP_SSL('smtp.example.com')
        mail_server.set_debuglevel(1)
        mail_pass = getpass.getpass('Please enter the mail password: ')
        mail_server.login(sender, mail_pass)
        mail_server.send_message(message)
        mail_server.quit()
    except:
        print("Can't seem to send email, please check the internet connection or the provided credential")

if __name__ == '__main__':
    main()
   