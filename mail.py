#!/usr/bin/python
# ref : http://kutuma.blogspot.com/2007/08/sending-emails-via-gmail-with-python.html
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "username@gmail.com"
gmail_pwd = "password"

def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()


body=""
f1=open('body','r')
for  bodylines in f1.readlines():
	body+=bodylines 
f1.close()

subject = "SUBJECT TEXT GOES HERE"
attachment = "shrini.jpg"

f=open('to_mails','r')
for to_mail_id in f.readlines():
   to_mail_id=to_mail_id.strip()
   mail(to_mail_id,
   subject,
   body,
   attachment)
   print "mail sent to :"+to_mail_id
f.close()
print "\nmail sent successfully to all\n"
