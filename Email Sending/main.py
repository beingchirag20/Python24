import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formatdate

# Email credentials
my_email = "#senders email"
password = "senders 2 step verification password"  
receiver = input("Enter recipient email: ")

# Email content
msg = MIMEMultipart()
msg['From'] = my_email
msg['To'] = receiver
msg['Subject'] = "Receipt"
msg['Date'] = formatdate(localtime=True)

#Create a text part
body_text = input("Enter your message (if none then just click on enter):")
body_part = MIMEText(body_text)
msg.attach(body_part)

# Path to the file
file_path = r"C:\Users\being\OneDrive\Desktop\Data Science\Python\Python Programs\Receipt send in email\receipt.pdf"

# Read the PDF or any other file 
with open(file_path, "rb") as attachment:
    part = MIMEApplication(attachment.read(), Name="receipt.pdf")

# Add header to the attachment
part['Content-Disposition'] = f'attachment; filename="{file_path}"'
msg.attach(part)

try:
    # SMTP setup
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_email, password)

    # Send email
    server.sendmail(my_email, receiver, msg.as_string())
    print("Email Sent Successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    try:
        server.quit()
    except NameError:
        pass  # Handle NameError gracefully if server was never defined
