import tkinter as tk
from tkinter import ttk
from datetime import datetime
import psutil
import time

#This function gets battery status & percentage
def get_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    charging = battery.power_plugged
    status = "Charging" if charging else "Discharging"
    return percent, status

def update_info():
    current_date = datetime.now().strftime("%Y-%m-%D  %H-%M=%S")
    time_label.config(text = f"Date-Time :{current_date}")  

    battery_status, battery_percent = get_battery()
    battery_label.config(text=f"Battery: ({battery_status})% {battery_percent}")

    root.after(1000, update_info)

# GUI Window setup
root = tk.Tk()
root.title("Battery and Date/Time Info")
root.geometry("300x190")  # Window size
root.resizable(False, False)

# Title Label
title_label = ttk.Label(root, text="System Monitor", font=("Helvetica", 14, "bold"))
title_label.pack(pady=10)

# Time Label
time_label = ttk.Label(root, text="", font=("Helvetica", 12))
time_label.pack(pady=5)

# Battery Label
battery_label = ttk.Label(root, text="", font=("Helvetica", 12))
battery_label.pack(pady=8)

# Update the information for the first time
update_info()

# Start the main loop
root.mainloop()
