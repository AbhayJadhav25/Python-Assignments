import smtplib
from email.message import EmailMessage
def send_mail(sender , app_password , receiver , subject , body):

  msg = EmailMessage()

  msg["from"] = sender
  msg["To"] = receiver
  msg["Subject"] = subject

  msg.set_content(body )

  smtp = smtplib.SMTP_SSL("smtp.gmail.com" ,465)

  smtp.login(sender , app_password)
  smtp.send_message(msg)

  smtp.quit()

def main():

  sender_mail = "denverkjohn@gmail.com"
  app_password = "affz esaw igoy ufnx"
  receiver_email = ["jaggujagg06@gmail.com" , "mayurghodke111@gmail.com"]
  subject = "Test Gmail From Python Script"

  body = """Jay Ganesh 
  This is test email sent using Marvellous Python
  Regards , 
  Abhay Jadhav
  """
  send_mail(sender_mail , app_password , receiver_email , subject , body)

  print("Gmail sent Successfully.")

if __name__ == "__main__":
  main()
