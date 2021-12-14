from tkinter  import *
import tkinter.font
from time import sleep
from pyfirmata import Arduino, util
from pyfirmata import INPUT, OUTPUT, PWM

arduinoPort = "/dev/ttyUSB0"
board = Arduino(arduinoPort)
sleep(2)

pin3 = board.get_pin("d:3:o")                           # LED Pin
motorPin = board.get_pin("d:5:p")				        # PWM pin connected to LED
motorEL = board.get_pin("d:8:o")                        # Motor Enable
motorZF = board.get_pin("d:6:o")                        # Motor Direction

win = Tk()
win.title("Motor Control")
myFont = tkinter.font.Font(family = "Helvetica", size =12, weight = "bold")

def ledToggle():
    if ledButton["text"] == "Turn Motor off":
        pin3.write(0)
        motorEL.write(0)
        ledButton["text"] = "Turn Motor ON"
    else:
        pin3.write(1)
        motorEL.write(1)
        ledButton["text"]= "Turn Motor off"
   
        
def close():
    win.destroy()

def speed(val):
    val = float(val)
    if val <0:
        val = abs(val) 
        motorZF.write(0)
        selection = "Backward = " + str(val)
    elif val >0:
        motorZF.write(1)
        selection = "Forward = " + str(val)
    else:
        selection = "Stop" 
    
    label.config(text = selection)    
    motorPin.write(val)
    sleep(0.01)


ledButton = Button(win, text="Turn Motor ON", font=myFont, command=ledToggle, bg="bisque2", height=1, width=24)
ledButton.grid(row=0,column=1)

var = DoubleVar()
speedScale = Scale(win, from_=-0.5, to=0.5, resolution = 0.05, variable = var, command = speed, orient=HORIZONTAL, length = 500, width = 50 )
speedScale.grid(row=1,column=1)

label = Label(win)
label.grid(row=2, column = 1)

exitButton = Button (win,text = "Exit", font = myFont, command = close, bg = "red", height = 1, width = 10)
exitButton.grid(row=10,column=1)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()
