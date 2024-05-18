import psutil
import tkinter as tk
from tkinter import messagebox

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

def show_notification():
    messagebox.showwarning("Battery Low", f"{percent}% Battery remain!!")

# Create a root window (it will not be shown)
root = tk.Tk()
root.withdraw()  # Hide the root window

while True:
    if plugged!=True and percent < 30:
        show_notification()
        break