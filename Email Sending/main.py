import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formatdate

# Email credentials
my_email = "beingchirag6@gmail.com"
password = "iwwp bvdp uvby nxxs"  
receiver = input("Enter recipient email: ")

# Email content
msg = MIMEMultipart()
msg['From'] = my_email
msg['To'] = receiver
msg['Subject'] = "Receipt"

# Path to the PDF file
pdf_path = r"C:\Users\being\OneDrive\Desktop\Data Science\Python\Python Programs\Receipt send in email\receipt.pdf"

# Read the PDF file
with open(pdf_path, "rb") as attachment:
    part = MIMEApplication(attachment.read(), Name="receipt.pdf")

# Add header to the attachment
part['Content-Disposition'] = f'attachment; filename="{pdf_path}"'
msg.attach(part)

try:
    # SMTP setup
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_email, password)

    # Send email
    server.sendmail(my_email, receiver, msg.as_string())
    print("Email Sent!")

except Exception as e:
    print(f"Error: {e}")

finally:
    try:
        server.quit()
    except NameError:
        pass  # Handle NameError gracefully if server was never defined
