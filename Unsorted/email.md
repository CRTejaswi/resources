    Copyright(c) 2019
    Author: Chaitanya Tejaswi(github.com / CRTejaswi)    License: MIT

# Email
> Personal notes.


<details>
<summary> Naive Email </summary>

> Naive email. Followed by Client & Server response.

``` py
#!/usr/bin/env python3
import smtplib


port = 1025
smtp_server = 'localhost'
sender_email = 'aeronfinium@gmail.com'
receiver_email = 'cartosdev@gmail.com'
message = input('Message:\n\t')
server = smtplib.SMTP(smtp_server, port)
server.set_debuglevel(True)
server.sendmail(sender_email, receiver_email, message)
```
```
$ py test.py
Message:
    Hello World! This is my first CLI email.

send: 'ehlo [192.168.99.1]\r\n'
reply: '250-Feynman\r\n'
reply: '250-8BITMIME\r\n'
reply: b'250 HELP\r\n'
reply: retcode (250); Msg: b'Feynman\n8BITMIME\nHELP'
send: 'mail FROM:<aeronfinium@gmail.com>\r\n'
reply: b'250 OK\r\n'
reply: retcode (250); Msg: b'OK'
send: 'rcpt TO:<cartosdev@gmail.com>\r\n'
reply: b'250 OK\r\n'
reply: retcode (250); Msg: b'OK'
send: 'data\r\n'
reply: b'354 End data with <CR><LF>.<CR><LF>\r\n'
reply: retcode (354); Msg: b'End data with <CR><LF>.<CR><LF>'
data: (354, b'End data with <CR><LF>.<CR><LF>')
send: b'Hello World! This is my first CLI email.\r\n.\r\n'
reply: b'250 OK\r\n'
reply: retcode (250); Msg: b'OK'
data: (250, b'OK')
```
```
$ python -m smtpd -c DebuggingServer -n localhost:1025
---------- MESSAGE FOLLOWS ----------
b'Hello World! This is my first CLI email.'
------------ END MESSAGE ------------
```

</details>

<details>
<summary> Basic Email (without attachment) </summary>

> CHANGES: Send plain-text without attachments.

``` py
#!/usr/bin/env python3
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
import sys

SMTP_SERVER = 'smtp.gmail.com'

def multilineText():
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    return contents

def email(sender='aeronfinium@gmail.com',
          receiver='cartosdev@gmail.com'):
    # Initializations
    port = 465
    smtp_server = SMTP_SERVER
    sender_email = sender
    receiver_email = receiver
    password = getpass()
    message = MIMEMultipart()
    # Create the message
    body = multilineText()
    message['Subject'] = body.pop(0)
    message['From'] = sender_email
    message['To'] = receiver_email
    body = '\n'.join(body)
    message.attach(MIMEText(body, 'plain'))
    # Deliver the message
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == '__main__':
    email(*sys.argv[1:])
```
</details>

<details>
<summary> Basic Email (with attachment) </summary>

> CHANGES: Send plain-text with an attachment.

``` py
#!/usr/bin/env python3
from getpass import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
import sys

SMTP_SERVER = 'smtp.gmail.com'


def multilineText():
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    return contents

def email(sender='aeronfinium@gmail.com',
          receiver='cartosdev@gmail.com',
          filename='test.pdf'):
    # Initializations
    port = 465
    smtp_server = SMTP_SERVER
    sender_email = sender
    receiver_email = receiver
    password = getpass()
    message = MIMEMultipart()
    # Create the message
    body = multilineText()
    message['Subject'] = body.pop(0)
    message['From'] = sender_email
    message['To'] = receiver_email
    body = '\n'.join(body)
    message.attach(MIMEText(body, 'plain'))
    # Deal with the attachment
    with open(filename, 'rb') as f:
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(f.read())
    encoders.encode_base64(attachment)
    attachment.add_header(
        'Content-Disposition',
        f'attachment; filename={filename}'
    )
    message.attach(attachment)
    # Deliver the message
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == '__main__':
    email(*sys.argv[1:])
# py .\temp.py aeronfinium@gmail.com omkarmudholkar201@gmail.com "B:\Anna McLuckie - Time Of Your Life.mp4"
```
</details>


### REFERENCES
- [Sending Emails With Python (RealPython)](https://realpython.com/python-send-email/) <br>
- [_Ch18: Email_, Automate The Boring Stuff (Sweigart)](file:///B:/CRTejaswi/Documents/Books/Tech/05%20-%20Computer%20Science%20Engineering/03%20-%20Languages/Python3/Python%20-%20Automate%20Boring%20Stuff%20(Sweigart).pdf#page=570) <br>
- [ezgmail (Sweigart)](https://github.com/asweigart/ezgmail) <br>