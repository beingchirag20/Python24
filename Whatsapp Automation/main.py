import pywhatkit

# Prompt the user to enter a phone number
rec_num = input("Enter receiver's number: ")

# Validate the input (optional, for ensuring proper format)
if not rec_num.startswith("+") or not rec_num[1:].replace(" ", "").isdigit():
    print("Invalid phone number format! Please enter in the format +<country_code> <number>")
else:
    # Prompt the user to enter a message
    message = input("Enter the message: ")

    # Set the time for sending the message (e.g., 2 minutes from now)
    from datetime import datetime, timedelta

    now = datetime.now()
    send_time = now + timedelta(minutes=2)
    scheduled_hour = send_time.hour
    scheduled_minute = send_time.minute

    # Send the message
    pywhatkit.sendwhatmsg(rec_num, message, scheduled_hour, scheduled_minute)
    print(f"Message scheduled to be sent at {scheduled_hour}:{scheduled_minute}")
