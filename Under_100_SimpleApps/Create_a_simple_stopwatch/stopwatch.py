import tkinter as tk
from datetime import datetime
import time

class Stopwatch(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Stopwatch")
        self.geometry("300x200")
        
        self.elapsed_time = 0
        self.running = False

        self.label = tk.Label(self, text="00:00:00.000", font=("Arial", 24))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self, text="Start", command=self.start_stop)
        self.start_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(self, text="Reset", command=self.reset)
        self.reset_button.pack(side="right", padx=10)

        self.update_time()

    def start_stop(self):
        self.running = not self.running
        if self.running:
            self.start_button.config(text="Stop")
            self.start_time = time.time() - self.elapsed_time
            self.update_time()
        else:
            self.start_button.config(text="Start")
            self.elapsed_time = time.time() - self.start_time

    def reset(self):
        self.running = False
        self.start_button.config(text="Start")
        self.elapsed_time = 0
        self.update_time()

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time

        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        milliseconds = int((self.elapsed_time % 1) * 1000)

        time_str = "{:02d}:{:02d}:{:02d}.{:03d}".format(hours, minutes, seconds, milliseconds)
        self.label.config(text=time_str)

        self.after(1, self.update_time)

if __name__ == "__main__":
    app = Stopwatch()
    app.mainloop()
