#!/usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import glob

# Config Text File
gmail_user = "sender gmail"
gmail_pwd = "password"

def mail(to,subject,text,attachment_folder):
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    
    msg.attach(MIMEText(text))
    cwd = os.path.join(os.getcwd(),attachment_folder,"*")

    for attach in glob.glob(cwd):
        part = MIMEBase('application','octet-stream')
        part.set_payload(open(attach, 'rb').read())
        encoders.encode_base64(part)
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
    
attachment_folder = "attachments"
body=""
f1=open('body','r')
for  bodylines in f1.readlines():
	body+=bodylines 
f1.close()

subject = "different subject"
f=open('to_mails','r')
for to_mail_id in f.readlines():
    to_mail_id=to_mail_id.strip()
    mail(to_mail_id,
    subject,
    body,
    attachment_folder)
    print ("mail sent to :"+to_mail_id)
f.close()
print ("\nmail sent successfully to all\n")