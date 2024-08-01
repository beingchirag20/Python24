import pywhatkit
from random import randint
import time

def send_opt():
    # Send an option to the user
    rec_num = input("Enter receiver's number: ")
    if not rec_num.startswith("+") or not rec_num[1:].replace(" ", "").isdigit():
     print("Invalid phone number format! Please enter in the format +<country_code> <number>")
    else:
       otp = randint(1000, 2000)
       message = f"Your OTP is: {otp}"
    
    try:
       time.sleep(5)
       pywhatkit.sendwhatmsg_instantly(rec_num, message, True, 10)
       print("OTP sent successfully!")
    except Exception as e:
       print("Error occurred: ", str(e))

    time.sleep(30)

    resend = input("Resend OTP?(Yes/No):")
    if resend.lower() == "yes":
       new_otp = randint(1000, 2000)
       new_message = f"Your new OTP is: {new_otp}"
       pywhatkit.sendwhatmsg_instantly(rec_num, new_message, True, 10)
       print("OTP sent successfully!")
    else:
       print("Exiting...")

send_opt()
