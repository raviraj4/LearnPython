import smtplib
import getpass

smtp_ob = smtplib.SMTP('smtp.gmail.com', 587)
# password = getpass.getpass("enter your password: ")
smtp_ob.ehlo()
smtp_ob.starttls()
email = getpass.getpass("email: ")
password = getpass.getpass("password: ")
smtp_ob.login(email, password=password)

from_address = email
to_address = input("to:")
subject = input("Subject: ")
message = input("Message: ")
msg = "Subject: "+subject+"\n"+message

smtp_ob.sendmail(from_addr=from_address,to_addrs=to_address, msg=msg)
print("message sent!")
    
# password = getpass.getpass("enter password: ")