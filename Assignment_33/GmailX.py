import smtplib
from email.message import EmailMessage
import mimetypes
def send_mail(sender , app_password , receiver , subject , body , filename):
  fobj = open(filename , "rb")
  data = fobj.read()

  msg = EmailMessage()

  msg["from"] = sender
  msg["To"] = receiver
  msg["Subject"] = subject

  
  msg.set_content(body )
  
  mime_type, _ = mimetypes.guess_type(filename)
  if mime_type is None:
      mime_type = "application/octet-stream"

  main_type, sub_type = mime_type.split('/')

  msg.add_attachment(data, maintype=main_type, subtype=sub_type,filename=filename)

  smtp = smtplib.SMTP_SSL("smtp.gmail.com" ,465)

  smtp.login(sender , app_password)

  smtp.send_message(msg)
  fobj.close()
  smtp.quit()

def main():

  sender_mail = "denverkjohn@gmail.com"
  app_password = "oioq vxpe oira odfb"
  receiver_email = ["jaggujagg06@gmail.com" , "mayurghodke111@gmail.com","abhay.bhosale7007@gmail.com"]
  subject = "Test Gmail From Python Script"

  body = """Jay Ganesh 
  This is test email sent using Marvellous Python
  Regards , 
  Abhay Jadhav
  """
  send_mail(sender_mail , app_password , receiver_email , subject , body , "a.txt")

  print("Gmail sent Successfully.")

if __name__ == "__main__":
  main()
