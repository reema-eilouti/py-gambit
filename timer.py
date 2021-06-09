from tkinter import *
import time

class Timer():
    
    def __init__(self):
        self.root = None
        self.frame = None
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.timer_label = None

    def clock(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
        if self.minute == 60:
            self.hour += 1
            self.minute =0
        self.timer_label.config(text=str(self.hour) + ":" + str(self.minute) + ":" + str(self.second))
        self.timer_label.after(1000,self.clock)

    def main(self):
        # self.root = Tk()
        # self.root.geometry('200x50')
        self.frame = Frame(self.root)
        self.frame.grid(row=5, column=0, sticky="nswe")
        self.timer_label = Label(self.frame,text="", height=0,font=15)
        self.timer_label.pack(pady=20)
        self.clock()
        # self.root.mainloop()

if __name__ == "__main__":
    timer = Timer()
    timer.main()