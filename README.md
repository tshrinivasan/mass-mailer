Mass Mailer using Gmail
=====


### Requirements
1. Install these dependencies.<br>
  `$ sudo apt-get install python python-dev`
  
2. You need to have an account in Gmail.

### How to use this script:
1. First make sure that, whether you have changed/set your gmail user name and it's password in "mail.py" at line number 10 and 11.

2. In "body" file, you put the content of the mail that you want to send.

3. In "to_mails" file,add the list of email address you want to send the email given that there is **only one email address per line**

4. In "mail.py"  at line 45, make sure you provide the *SUBJECT* string

5. (Optional) If there are any attachments, specify the file names in line 46. and make sure the attachments are in same folder as the *mail.py* file.


### Running the program:
`$ python mail.py`


### Note: 
**Only 500 mails can be sent via gmail per day**

http://support.google.com/a/bin/answer.py?hl=en&answer=166852

http://google.wikia.com/wiki/Gmail_sending_limit
