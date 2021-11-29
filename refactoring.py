import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Email:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"

    def send_message(self, recipients, subject, message, numbers):
        send_email_message = MIMEMultipart()
        send_email_message['From'] = self.login
        send_email_message['To'] = ', '.join(recipients)
        send_email_message['Subject'] = subject
        send_email_message.attach(MIMEText(message))
        send_mail = smtplib.SMTP(self.GMAIL_SMTP, numbers)
        send_mail.ehlo()
        send_mail.starttls()
        send_mail.ehlo()
        send_mail.login(self.login, self.password)
        res = send_mail.send_message(self.login, send_email_message.as_string())
        send_mail.quit()
        return res

    def receive(self, mailbox, header=None):
        receive_mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        receive_mail.login(self.login, self.password)
        receive_mail.list()
        receive_mail.select(mailbox)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = receive_mail.uid('search', header, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = receive_mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        receive_mail.logout()
        return email_message


if __name__ == '__main__':
    email = Email('login@gmail.ru', 'qwerty')
    print(email.send_message(['vasya@email.com', 'petya@email.com'], 'Subject', 'Message', '587'))
    print(email.receive('inbox'))
