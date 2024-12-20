import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Post:
    def __init__(self, login, password, host_SMTP="smtp.gmail.com", host_IMAP="imap.gmail.com", port=587):
        self.login = login
        self.password = password
        self.host_SMTP = host_SMTP
        self.host_IMAP = host_IMAP
        self.port = port

    def send_message(self, recipients, subject, text):
        # send message
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = ', '.join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(text))

        connection = smtplib.SMTP(self.host_SMTP, self.port)
        # identify ourselves to smtp gmail client
        connection.ehlo()
        # secure our email with tls encryption
        connection.starttls()
        # re-identify ourselves as an encrypted connection
        connection.ehlo()

        connection.login(self.login, self.password)
        connection.sendmail(message['From'], message['To'], message.as_string())

        connection.quit()
        # send end

    def receive_message(self, header=None):
        # receive
        mail = imaplib.IMAP4_SSL(self.host_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("INBOX")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        email_message = email.message_from_string(data[0][1])
        mail.logout()
        return email_message


if __name__ == '__main__':
    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message_text = 'Message'
    header = None

    client1 = Post(login, password)
    client1.send_message(recipients, subject, message_text)
    client1.receive_message(header)
