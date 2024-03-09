import tkinter as tk
import time

class Stopwatch(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Stopwatch")    
        self.geometry("300x100")
        self.configure(bg="black")
        

        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

        self.display = tk.Label(self, text="00:00:00.000", font=("Roboto", 24))
        self.display.place(relx=0.5, rely=0.5, anchor="center")
        

        self.start_button = tk.Button(self, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=5)
        

        self.stop_button = tk.Button(self, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.RIGHT, padx=5)
        self.stop_button.config(state=tk.DISABLED)

        self.reset_button = tk.Button(self, text="Reset", command=self.reset)
        #self.reset_button.pack(side=tk.BOTTOM, padx=5)
        self.reset_button.pack(anchor='center')

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(side=tk.BOTTOM, padx=5)
        #self.quit_button.pack(anchor='center')

        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.milliseconds / 1000
            self.update()

            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop(self):
        if self.running:
            self.running = False
            self.after_cancel(self.update_id)
            self.stop_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.NORMAL)

    def reset(self):
        self.running = False
        self.stop()
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.display.config(text="00:00:00.000")

    def update(self):
        if self.running:
            self.milliseconds = int((time.time() - self.start_time) * 1000)
            self.seconds, milliseconds = divmod(self.milliseconds, 1000)
            self.minutes, self.seconds = divmod(self.seconds, 60)
            self.hours, self.minutes = divmod(self.minutes, 60)
            self.display.config(text="{:02d}:{:02d}:{:02d}.{:03d}".format(self.hours, self.minutes, self.seconds, milliseconds))
            #self.display.pack(anchor='center')
            self.update_id = self.after(1, self.update)

if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.mainloop()
