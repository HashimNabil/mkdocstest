## Import tkinter library 
from tkinter  import *
import tkinter.font
from time import sleep

# open new Window
win = Tk()

# Set window Title 
win.title("Motor Control")  

# Set font format
myFont = tkinter.font.Font(family = "Helvetica", size =12, weight = "bold")  

# Button Function 
def ledToggle():
    if ledButton["text"] == "Turn Motor off":
        ledButton["text"] = "Turn Motor ON"
    else:
        ledButton["text"]= "Turn Motor off"

# Close Button Function          
def close():
    win.destroy()

# Slider Function 
def speed(val):
    val = float(val)
    if val <0:
        val = abs(val) 
        selection = "Backward = " + str(val)
    elif val >0:
        selection = "Forward = " + str(val)
    else:
        selection = "Stop" 
    
    label.config(text = selection)    
    sleep(0.01)

# Create Button 
ledButton = Button(win, text="Turn Motor ON", font=myFont, command=ledToggle, bg="bisque2", height=1, width=24)
ledButton.grid(row=0,column=1)

# Create Slider
var = DoubleVar()
speedScale = Scale(win, from_=-0.5, to=0.5, resolution = 0.05, variable = var, command = speed, orient=HORIZONTAL, length = 500, width = 50 )
speedScale.grid(row=1,column=1)

# Create Lable
label = Label(win)
label.grid(row=2, column = 1)

# Create Exit Button 
exitButton = Button (win,text = "Exit", font = myFont, command = close, bg = "red", height = 1, width = 10)
exitButton.grid(row=10,column=1)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()