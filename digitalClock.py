from tkinter import *
import time

def clockk():
  current_time = time.strftime('%H:%M:%S')
  lbl.config(text = current_time)
  lbl.after(1000, clockk)

root = Tk()

lbl = Label(root, font =('Georgia pro', 35, 'bold italic'), background = 'crimson', foreground= 'black')
lbl.pack(anchor= 'center')


root.mainloop()
clockk()
