import imaplib
import getpass

M = imaplib.IMAP4_SSL("imap.gmail.com")
email_main = getpass.getpass("enter email: ",)
password = getpass.getpass("enter password: ")

M.login(email_main, password=password)
# print(M.list())
M.select('inbox')
typ, data = M.search(None, 'SUBJECT "YENAPODA RASCALA"' )
# data is just a list of email ids
email_id = data[0]
# once we have the email ids we need to fetch them, '(RFC822)' is a protocol for fetching
result, email_id = M.fetch(email_id, '(RFC822)')
raw_e = email_id[0][1]
raw_str = raw_e.decode('utf-8')

import email

email_msg = email.message_from_string(raw_str)

for part in email_msg.walk():
    if part.get_content_type()== 'text/html':
        body = part.get_payload(decode=True)
        print(body)

